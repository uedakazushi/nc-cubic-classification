"""Exact FDC3 cubic-centre witness, regularity factors and eight chart translates."""
import argparse
from collections import Counter
from functools import cache
from itertools import product
import json
from pathlib import Path

import sympy as s
from flint import fmpq

from cubic_flint_rational_function import RationalFunction, RationalFunctionField
from cubic_sparse_hilbert import SparseGradedAlgebra
from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_double_split_FDC import (
    e, fdc_coefficients, four_cross_both_outer, m, p, product_plane_change, ratio,
)
from verify_cubic_CY_one_segre_double_split_isolated import marked
from verify_cubic_CY_one_segre_double_split_TD import fraction

SYMBOLS = s.symbols("P M L E")
DIRECTORY = Path(__file__).parent
FIELD = RationalFunctionField(SYMBOLS)
CONTEXT = FIELD.context


def scalar(field, value, denominator=1):
    return field.from_sympy(s.Rational(value, denominator))


def normalized_parameters(field, values):
    P, M, L, E = values
    one = field.one
    p, m = P/scalar(field, 4), M/scalar(field, 4)
    s0, t0 = (p+m)/scalar(field, 2), (p-m)/scalar(field, 2)
    h, k = (one-P*P)/scalar(field, 64), (one-M*M)/scalar(field, 64)
    ratio = scalar(field, 64)*p*k*L-m
    e = k*k*E/s0
    return p, m, ratio, e, s0, t0, h, k


def add(row, position, coefficient, field):
    value = row.get(position, field.zero)+coefficient
    if value:
        row[position] = value
    else:
        row.pop(position, None)


class MarkowitzAlgebra(SparseGradedAlgebra):
    """Reduce with sparse row and column pivots, retaining the individual scalars."""

    def echelon(self, rows):
        active = [dict(row) for row in rows if row]
        pivots = {}
        self.selected = []
        while active:
            counts = Counter(column for row in active for column in row)

            def score(position):
                i, j = position
                coefficient = active[i][j]
                unit = coefficient.n.is_constant() and coefficient.d.is_constant()
                return (not unit, (len(active[i])-1)*(counts[j]-1),
                        coefficient.n.degrees()[-1]+coefficient.d.degrees()[-1],
                        len(coefficient.n)+len(coefficient.d), i, j)

            i, j = min(((i, j) for i, row in enumerate(active) for j in row), key=score)
            row = active.pop(i)
            pivot = row[j]
            self.selected.append(pivot)
            pivots[j] = {key: co/pivot for key, co in row.items()}
            for other in active:
                if j in other:
                    self.addto(other, pivots[j], -other[j])
            active = [row for row in active if row]
            print("pivot", len(pivots), "remaining rows", len(active), flush=True)
        return pivots

    def reduce(self, row, pivots):
        for column, pivot in pivots.items():
            if column in row:
                self.addto(row, pivot, -row[column])
        return row


def affine_columns(base, permutation, specialization):
    P, M, L = [base.from_sympy(value.subs(specialization, simultaneous=True))
               for value in SYMBOLS[:3]]
    transform = product_plane_change(SYMBOLS[0]/4, SYMBOLS[1]/4)
    tensor = s.kronecker_product(transform, transform).subs(specialization, simultaneous=True)
    transform = [[base.from_sympy(tensor[i, j]) for j in range(16)] for i in range(16)]
    coordinates = s.symbols("F0:15")
    relation = marked({**dict(enumerate(coordinates)), 10: 1, 11: 1},
                      s.Rational(1, 8), linear_columns=True)
    constant = relation.subs(dict.fromkeys(coordinates, 0))
    slopes = {i: relation.diff(c) for i, c in enumerate(coordinates) if i not in (10, 11)}
    linear_source = [[(base.from_sympy(constant[i, j]),
                       [(k, base.from_sympy(value[i, j])) for k, value in slopes.items() if value[i, j]])
                      for i in range(16)] for j in range(6)]

    def source_at(value):
        p, m, ratio, e, *_ = normalized_parameters(base, (P, M, L, value))
        data, _, _, _ = fdc_coefficients(p, m, ratio, e,
                                         lambda a, b=1: scalar(base, a, b))
        columns = []
        for column in linear_source:
            original = [sum((data[k]*co for k, co in terms), constant) for constant, terms in column]
            transformed = [sum((a*b for a, b in zip(row, original, strict=True) if a and b), base.zero)
                           for row in transform]
            columns.append(transformed)
        one = base.one
        mixed = (P*P-one)*(M*M-one)*L*L+scalar(base, 2)*P*M*L+one
        columns.append([L*L, mixed, base.zero, base.zero, base.zero, one]+[base.zero]*10)
        return columns

    rows = [4*i+j for i in permutation for j in permutation]

    def permuted_source(value):
        return [[column[i] for i in rows] for column in source_at(value)]

    fixed = permuted_source(base.zero)
    slopes = [[a-b for a, b in zip(at_one, at_zero, strict=True)]
              for at_one, at_zero in zip(permuted_source(base.one), fixed, strict=True)]
    return fixed, slopes


def rank_witness(permutation=(0, 1, 2, 3), parameters=SYMBOLS, specialization=None):
    base = RationalFunctionField(parameters[:-1])
    field = RationalFunctionField(parameters)
    fixed, slopes = affine_columns(base, permutation, specialization or {})
    helper = SparseGradedAlgebra(base, 4, [], [0]*4)
    derivative_rows = [{j: column[i] for j, column in enumerate(slopes) if column[i]}
                       for i in range(16)]
    derivative_pivots = helper.echelon(derivative_rows)
    assert set(derivative_pivots) == {0, 5}
    right_changes = [helper.reduce({i: base.one}, derivative_pivots) for i in range(7)]
    stable = []
    for j in range(7):
        if j in derivative_pivots:
            continue
        vector = [change.get(j, base.zero) for change in right_changes]
        column = [sum((fixed[i][k]*vector[i] for i in range(7) if vector[i]), base.zero)
                  for k in range(16)]
        assert all(not sum((slopes[i][k]*vector[i] for i in range(7) if vector[i]), base.zero)
                   for k in range(16))
        stable.append({divmod(i, 4): co for i, co in enumerate(column) if co})
    algebra = SparseGradedAlgebra(base, 4, stable, [0]*4)
    algebra.build(4)
    if not specialization:
        assert [len(algebra.basis[n]) for n in (2, 3, 4)] == [11, 26, 57]
    assert len(algebra.basis[2]) == 11

    def lift_poly(poly):
        return field.context.from_dict({(*exponents, 0): c for exponents, c in poly.to_dict().items()})

    def lift(value):
        return RationalFunction(lift_poly(value.n), lift_poly(value.d))

    @cache
    def word(letters):
        if len(letters) == 1:
            return {letters[0]: base.one}
        row = {}
        for i, coefficient in word(letters[:-1]).items():
            for j, value in algebra.right[len(letters)][i, letters[-1]].items():
                add(row, j, coefficient*value, base)
        return row

    @cache
    def full_word(letters):
        return {index: lift(value) for index, value in word(letters).items()}

    variation = field.from_sympy(parameters[-1])
    engine = MarkowitzAlgebra(field, 4, [], [0]*4)
    quotient = {}
    for degree in (3, 4):
        rows = []
        for index in sorted(derivative_pivots):
            columns = ([{divmod(i, 4): value for i, value in enumerate(part[index]) if value}
                        for part in (fixed, slopes)])
            for surrounding in product(range(4), repeat=degree-2):
                for left in range(degree-1):
                    images = []
                    for relation in columns:
                        row = {}
                        for monomial, coefficient in relation.items():
                            letters = surrounding[:left]+monomial+surrounding[left:]
                            for key, value in word(letters).items():
                                add(row, key, coefficient*value, base)
                        images.append(row)
                    rows.append({key: lift(images[0].get(key, base.zero))
                                 +variation*lift(images[1].get(key, base.zero))
                                 for key in images[0].keys() | images[1].keys()})
        print("degree", degree, "affine insertion rows", len(rows), flush=True)
        pivots = engine.echelon(rows)
        free = [index for index in range(len(algebra.basis[degree])) if index not in pivots]
        assert len(free) == (degree+1)**2
        quotient[degree] = pivots, free

    pivots, free = quotient[4]
    positions = {index: j for j, index in enumerate(free)}
    commutators = [{} for _ in range(4*len(free))]
    for column, index in enumerate(quotient[3][1]):
        cubic = algebra.basis[3][index]
        for generator in range(4):
            row = full_word(cubic+(generator,)).copy()
            for key, value in full_word((generator,)+cubic).items():
                add(row, key, -value, field)
            for key, value in engine.reduce(row, pivots).items():
                commutators[25*generator+positions[key]][column] = value
    assert len(engine.echelon(commutators)) == 16
    chosen = [poly for value in engine.selected for poly in (value.n, value.d)]
    denominators = [lift_poly(co.d) for degree in (2, 3, 4)
                    for row in algebra.right[degree].values() for co in row.values()]
    denominators.extend(lift_poly(co.d) for column in fixed+slopes for co in column)
    denominators.extend(lift_poly(co.d) for row in right_changes for co in row.values())
    denominators.extend(co.d for pivots, _ in quotient.values()
                        for row in pivots.values() for co in row.values())
    print("PASS central rank 16 and full cubic/quartic quotient dimensions", flush=True)
    return denominators, chosen


def associate(polynomial):
    return polynomial/polynomial.leading_coefficient()


def regularity_factors():
    P, M, L, E = CONTEXT.gens()
    regular = P*(P*P-1)*(M*M-1)*(P*P-M*M)*L*E*(P*(1-M*M)*L-M)*(P-M*(1-P*P)*L)
    for sign in (-1, 1):
        upper = (P-sign)*(M+sign)*(1+(1-M*M)*L*E)+(1-M*M)*(E-1)
        regular *= (upper*upper+2*(1-M*M)*upper
                    -(P-M)*(M+sign)**2*(2*sign*(E-1)+P+M))
    return [associate(p) for p, _ in regular.factor()[1]]


def factor_support(polynomials, units):
    support = {}
    data = {str(poly): poly for poly in polynomials if not poly.is_constant()}
    for key in sorted(data, key=len):
        remaining = data[key]
        for factor in (*units, *support.values()):
            if remaining.is_constant():
                break
            while not (common := remaining.gcd(factor)).is_constant():
                remaining //= common
        for factor, _ in remaining.factor()[1]:
            monic = associate(factor)
            support[str(monic)] = monic
    return support


def coefficient_symmetry(state, generator):
    s0, t0, h, k, (x0, x1, x2, x3, x4, x5, x6, x7, x8) = state
    if generator == "P":
        return s0, -t0, k, h, (-x4/(h*h), -x7/(h*k), -x8/(k*k), -k*x3/h, -k*k*x0,
                               s0-x5, -h*x6/k, -h*k*x1, -h*h*x2)
    if generator == "Q":
        return -s0, t0, k, h, (-x2, -x1, -x0, -x6, -x8, -t0-x5, -x3, -x7, -x4)
    assert generator == "S"
    return t0, s0, h, k, (-x0, -x3/h, -x4/(h*h), -h*x1, -h*h*x2, -x5, -x7/h, -h*x6, -x8)


def pull(polynomial, values, field=FIELD):
    powers = [[field.one] for _ in values]
    for i, highest in enumerate(polynomial.degrees()):
        for _ in range(int(highest)):
            powers[i].append(powers[i][-1]*values[i])
    result = field.zero
    for exponents, coefficient in polynomial.to_dict().items():
        term = scalar(field, int(coefficient.p), int(coefficient.q))
        for i, exponent in enumerate(exponents):
            term *= powers[i][int(exponent)]
        result += term
    return result


def symmetry_supports(first, units):
    values = tuple(map(FIELD.from_sympy, SYMBOLS))
    p, m, ratio, e, s0, t0, h, k = normalized_parameters(FIELD, values)
    original, _, _, _ = fdc_coefficients(p, m, ratio, e,
                                         lambda a, b=1: scalar(FIELD, a, b))
    base = s0, t0, h, k, original[:9]
    results = {}
    for a, b, c in product((0, 1), repeat=3):
        letters = "S"*c+"Q"*b+"P"*a
        state = base
        for letter in letters:
            state = coefficient_symmetry(state, letter)
        s1, t1, _, k1, coordinates = state
        p1, m1 = s1+t1, s1-t1
        e1 = coordinates[8]+k1*k1/s1
        A = s1*coordinates[6]-k1
        d1 = p1*k1*A/s1-m1*e1
        moved = (scalar(FIELD, 4)*p1, scalar(FIELD, 4)*m1,
                 A/(scalar(FIELD, 64)*s1*e1), s1*e1/(k1*k1))
        if not letters:
            assert all(not (new-old) for new, old in zip(moved, values, strict=True))
        # Add the complement of the transformed p,e,d chart to the support.
        pulled = [p1.n, e1.n, d1.n]+[pull(poly, moved).n for poly in first]
        results[letters] = factor_support(pulled, units)
    return results


def check_shared_hypersurfaces(common, units):
    Q = s.Rational
    samples = [(2, 3, Q(-1, 4), 1), (2, 3, Q(-1, 6), 1), (2, 3, Q(-5, 28), 1),
               (2, 3, Q(-7, 30), 1), (2, 7, Q(1, 12), 1)]
    source = four_cross_both_outer()[0]
    checked = {}
    for P, M, L, E in samples:
        values = tuple(fmpq(int(Q(v).p), int(Q(v).q)) for v in (P, M, L, E))
        assert all(unit(*values) for unit in units)
        hypersurface, = [str(factor) for factor in common if not factor(*values)]
        p0, m0 = Q(P, 4), Q(M, 4)
        s0, k0 = (p0+m0)/2, Q(1-M*M, 64)
        ratio0, e0 = 64*p0*k0*L-m0, k0*k0*E/s0
        relations = source.subs({p: p0, m: m0, ratio: ratio0, e: e0}, simultaneous=True)
        _, rank = centre_calculation(relations, (0, 1, 2, 3), s.QQ, s.QQ.from_sympy)
        assert rank == 20
        checked[hypersurface] = {"coordinates": [str(v) for v in (P,M,L,E)], "rank": rank}
    assert len(checked) == len(common)
    print("PASS original rank 20 on a point of every shared hypersurface", flush=True)
    return checked


def check_discriminants():
    P, M, L, E = SYMBOLS
    field = RationalFunctionField((P, M, E))
    roots = [-1/((P-1)*(M+1)), -1/((P+1)*(M-1))]
    units = regularity_factors()

    def local_factors(root, order):
        denominators, pivots = rank_witness(order, field.variables, {L: root})
        parameters = tuple(field.from_sympy(value) for value in (P, M, root, E))
        regular = [pull(unit, parameters, field).n for unit in units]
        regular.append(field.from_sympy(s.denom(root)).n)
        return sorted(factor_support(denominators+pivots, regular))

    direct = local_factors(roots[0], (0, 1, 2, 3))
    assert not direct
    standard = local_factors(roots[1], (0, 1, 2, 3))
    alternate = local_factors(roots[1], (3, 2, 0, 1))
    expected = (M*M*P-M*P*P+M*P-1, M-P-1)
    names = [str(associate(field.from_sympy(value).n)) for value in expected]
    assert standard == names[:1] and alternate == names[1:]

    R1, R2 = P*(1-M*M)*L-M, P-M*(1-P*P)*L
    swap_L = R2/((1-P*P)*R1)
    assert s.cancel(swap_L.subs(L, roots[1])-roots[0].subs(M, -M)) == 0
    minimal = s.Poly(2*P*P+2*P-1, P, domain=s.QQ)
    assert minimal.is_irreducible
    number = s.QQ.algebraic_field((minimal, s.CRootOf(minimal, 0)))

    def convert(value):
        numerator, denominator = fraction(value)
        components = [number.new(s.Poly(part, P, domain=s.QQ).rem(minimal).rep.to_list())
                      for part in (numerator, denominator)]
        return components[0]/components[1]

    assert s.rem(expected[0].subs(M,P+1), minimal.as_expr(), P) == 0
    coordinates = (P, P+1, -2, -2*P)
    values = tuple(FIELD.from_sympy(value) for value in coordinates)
    for unit in units:
        value = pull(unit, values)
        assert convert(s.sympify(str(value.n).replace("^","**"), locals={"P":P}))
    p0, m0 = P/4, (P+1)/4
    s0, k0 = (p0+m0)/2, (1-(P+1)**2)/64
    source = four_cross_both_outer()[0]
    image = source.subs({p: p0, m: m0, ratio: -128*p0*k0-m0, e: -2*P*k0*k0/s0},
                        simultaneous=True)
    _, rank = centre_calculation(image, (0, 1, 2, 3), number, convert)
    assert rank == 20
    data = {"first_discriminant_factors": direct, "second_witness_factors": [standard, alternate],
            "exceptional_base_polynomial": str(minimal.as_expr()),
            "exceptional_centre_rank": rank}
    (DIRECTORY / "cubic_CY_one_segre_double_split_FDC_discriminant_certificate.json").write_text(
        json.dumps(data, indent=2)+"\n"
    )
    print("PASS both FDC3 discriminant hypersurfaces", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    flag = parser.add_mutually_exclusive_group()
    flag.add_argument("--alternate", action="store_true")
    flag.add_argument("--discriminants", action="store_true")
    arguments = parser.parse_args()
    if arguments.discriminants:
        return check_discriminants()
    alternate = arguments.alternate
    order = (3, 2, 0, 1) if alternate else (0, 1, 2, 3)
    denominators, pivots = rank_witness(order)
    units = regularity_factors()
    first = factor_support(denominators+pivots, units)
    assert len(first) == (8 if alternate else 10)
    moves = symmetry_supports(first.values(), units)
    common = set.intersection(*(set(group) for group in moves.values()))
    assert len(common) == (2 if alternate else 5)
    data = {
        "centre_rank": 16,
        "regularity_units": sorted(map(str, units)),
        "factors": sorted(first),
        "symmetry_supports": {name: sorted(support) for name, support in moves.items()},
        "common_factors": sorted(common),
    }
    if alternate:
        primary = json.loads((DIRECTORY / "cubic_CY_one_segre_double_split_FDC_witness_certificate.json").read_text())
        assert common <= set(primary["common_factors"])
    else:
        data["shared_hypersurface_samples"] = check_shared_hypersurfaces([first[key] for key in common], units)
    tag = "alternate" if alternate else "witness"
    (DIRECTORY / f"cubic_CY_one_segre_double_split_FDC_{tag}_certificate.json").write_text(
        json.dumps(data, indent=2)+"\n"
    )
    print("PASS FDC3 witness", len(first), "factors and", len(common), "shared factors", flush=True)


if __name__ == "__main__":
    main()
