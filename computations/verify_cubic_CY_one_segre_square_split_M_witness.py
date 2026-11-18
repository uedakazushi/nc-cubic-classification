"""Exact centre-rank witness using the stable relations in the M quadric quotient."""
import json
from itertools import product
from pathlib import Path

from flint import fmpq, fmpq_mpoly_ctx
import sympy as s

from cubic_flint_rational_function import RationalFunction, RationalFunctionField, VARIABLES
from cubic_sparse_hilbert import SparseGradedAlgebra
from verify_cubic_CY_one_segre_cross import PivotAlgebra
from verify_cubic_CY_one_segre_double_split_quadratics import fraction_factors, quadratic_quotient
from verify_cubic_CY_one_segre_square_split_M import lower_m

p, u, w = VARIABLES


def convert_columns(columns, field):
    return [{divmod(i, 4): field.from_sympy(value) for i, value in enumerate(column) if value}
            for column in columns]


def normalized_factors(witness):
    context = fmpq_mpoly_ctx.get(("z", "t", "x"))
    z, t, x = context.gens()
    k = (x*x-1)/64
    # Include the translate of the already excluded boundary x*x+t=0.
    units = (x*(x*x-1)*(t*t-1)*(x*x-t*t)*(x**4-t*t)
             *(z*(x+t)**2-t*(x*x+1)-2*x)*(z*(x-t)**2-t*(x*x+1)+2*x))

    def transform(factor):
        terms = s.Poly(s.sympify(factor.replace("^", "**")), p, u, w, domain=s.QQ).terms()
        min_k = min(2*j-n for (_, j, n), _ in terms)
        min_minus = min(j-n for (_, j, n), _ in terms)
        min_plus = min(n-j for (_, j, n), _ in terms)
        # p=x/4, w=(1+t)/(k(1-t)), u=k^2(1-t)(z+1)/(1+t).
        value = context.constant(0)
        for (i, j, n), coefficient in terms:
            value += (fmpq(int(coefficient.p), int(coefficient.q))*(x/4)**i
                      *k**(2*j-n-min_k)*(1-t)**(j-n-min_minus)
                      *(1+t)**(n-j-min_plus)*(z+1)**j)
        while not (common := value.gcd(units)).is_constant():
            value //= common
        return value/value.leading_coefficient()

    all_factors = sorted({value for key, values in witness.items() if key.endswith("_factors")
                          for value in values})
    normalized = {str(poly): poly for value in all_factors
                  if not (poly := transform(value)).is_constant()}
    assert len(normalized) == 13
    return tuple(normalized.values())


def symmetry_translates(normalized):
    context = fmpq_mpoly_ctx.get(("z", "t", "x"))
    translates = []
    for sign_x, sign_tz in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
        support = {}
        for f in normalized:
            moved = context.from_dict({(i, j, h): co*sign_x**h*sign_tz**(i+j)
                                       for (i, j, h), co in f.to_dict().items()})
            monic = moved/moved.leading_coefficient()
            support[str(monic)] = monic
        translates.append(support)
    return translates


def normalized_support(witness):
    normalized = normalized_factors(witness)
    translates = symmetry_translates(normalized)
    common = set.intersection(*(set(support) for support in translates))
    context = fmpq_mpoly_ctx.get(("z", "t", "x"))
    z, t, _ = context.gens()
    assert common == {str(t), str(z*t-1)}
    return {"normalized_irreducible_factors": len(normalized),
            "common_factors": sorted(common)}


def main():
    source = quadratic_quotient(lower_m()).applyfunc(s.cancel)
    independent = source.subs(u, 0)
    derivative = source.diff(u).applyfunc(s.cancel)
    assert (source-independent-u*derivative).applyfunc(s.cancel) == s.zeros(16, 7)
    derivative_rref, moving = derivative.rref()
    assert moving == (0, 5)
    stable = []
    coefficient_changes = []
    for column in range(source.cols):
        if column in moving:
            continue
        coordinates = s.eye(source.cols)[:, column]
        for index, pivot_column in enumerate(moving):
            coordinates[pivot_column] = -derivative_rref[index, column]
            coefficient_changes.append(coordinates[pivot_column])
        relation = (source*coordinates).applyfunc(s.cancel)
        assert not relation.has(u)
        stable.append(relation)

    base = RationalFunctionField((p, w))
    algebra = SparseGradedAlgebra(base, 4, convert_columns(stable, base), [0]*4)
    algebra.build(4)
    assert [len(algebra.basis[n]) for n in (2, 3, 4)] == [11, 26, 57]
    field = RationalFunctionField((p, u, w))

    def lift(value):
        def polynomial(poly):
            return field.context.from_dict({(i, 0, j): co for (i, j), co in poly.to_dict().items()})

        return RationalFunction(polynomial(value.n), polynomial(value.d))

    rights = {n: {key: {i: lift(co) for i, co in row.items()}
                  for key, row in algebra.right[n].items()} for n in (2, 3, 4)}

    def add(row, key, coefficient):
        value = row.get(key, field.zero)+coefficient
        if value:
            row[key] = value
        else:
            row.pop(key, None)

    def word(letters):
        state = {letters[0]: field.one}
        for n, letter in enumerate(letters[1:], start=2):
            result = {}
            for coordinate, coefficient in state.items():
                for key, value in rights[n][coordinate, letter].items():
                    add(result, key, coefficient*value)
            state = result
        return state

    engine = PivotAlgebra(field, 4, [], [0]*4)
    engine.pivot_product = field.one
    moving_columns = convert_columns([source[:, i] for i in moving], field)
    quotient = {}
    for n in (3, 4):
        rows = []
        for relation in moving_columns:
            for words in product(range(4), repeat=n-2):
                for left in range(n-1):
                    row = {}
                    for monomial, coefficient in relation.items():
                        for key, value in word(words[:left]+monomial+words[left:]).items():
                            add(row, key, coefficient*value)
                    rows.append(row)
        pivots = engine.echelon(rows)
        free = [i for i in range(len(algebra.basis[n])) if i not in pivots]
        assert len(free) == (n+1)**2
        quotient[n] = (pivots, free)
        print("degree", n, "moving relation rows", len(rows), "quotient dimension", len(free), flush=True)

    projection_product = engine.pivot_product
    pivots, free = quotient[4]
    positions = {index: j for j, index in enumerate(free)}
    commutators = [{} for _ in range(100)]
    for j, i in enumerate(quotient[3][1]):
        cubic = algebra.basis[3][i]
        for gen in range(4):
            row = word(cubic+(gen,))
            for key, value in word((gen,)+cubic).items():
                add(row, key, -value)
            for key, value in engine.reduce(row, pivots).items():
                commutators[25*gen+positions[key]][j] = value
    engine.pivot_product = field.one
    assert len(engine.echelon(commutators)) == 16

    denominators = {str(co.d): co.d for n in (2, 3, 4)
                    for row in rights[n].values() for co in row.values()}
    for entry in (*independent, *derivative, *coefficient_changes):
        co = field.from_sympy(entry)
        denominators[str(co.d)] = co.d
    for pivots, _ in quotient.values():
        for row in pivots.values():
            denominators.update({str(co.d): co.d for co in row.values()})
    minor = engine.pivot_product
    result = {
        "centre_rank": 16,
        "minor_numerator_factors": fraction_factors([minor.n]),
        "minor_denominator_factors": fraction_factors([minor.d]),
        "projection_denominator_factors": fraction_factors(denominators.values()),
        "projection_pivot_factors": fraction_factors([projection_product.n, projection_product.d]),
    }
    result["normalized_support"] = normalized_support(result)
    output = Path(__file__).with_name("cubic_CY_one_segre_square_split_M_open_certificate.json")
    output.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS M stable relation witness and exact cubic-centre rank 16", flush=True)


if __name__ == "__main__":
    main()
