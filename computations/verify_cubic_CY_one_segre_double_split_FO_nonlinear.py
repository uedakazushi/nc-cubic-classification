"""Exclude the remaining nonlinear FO cubic-centre locus."""
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import VARIABLES
from verify_cubic_CY_one_segre_double_split_FO_linear import (
    quadratic_field,
    quadratic_rank_support,
)
from verify_cubic_CY_one_segre_double_split_quadratics import (
    four_cross_one_outer,
)

x, d = s.symbols("x d")
c, u, w = VARIABLES
y = x*x
UNITS = [x, y-1, c-2, d+2, c+d, c, d, c+2, d-2, c-d,
         c*x-2, c*x+2, d*x-2, d*x+2]
PARAMETERS = {c: x/4, u: -4*x*(c+d)/(y-1), w: -(c-2)/(4*x*(c+d))}
TRANSLATES = [{}, {x: -x}, {c: -d, d: -c}, {x: -x, c: -d, d: -c}]
F = [
    (-c**3-2*c*d)*y-2*c*c+2*c*d+4*c+8,
    (-2*c*d+d**3)*y+2*c*d-2*d*d-4*d+8,
    (c**3-4*c*c+2*c*d)*y+2*c*c-2*c*d-4*c+8,
    (2*c*d-d**3-4*d*d)*y-2*c*d+2*d*d+4*d+8,
]
DIRECTORY = Path(__file__).parent


def numerator(value):
    return s.cancel(value).as_numer_denom()[0]


def monic(value, variables):
    return s.Poly(value, *variables, domain=s.QQ).monic().as_expr()


def factors(value, variables):
    return {monic(factor, variables) for factor, power in s.factor_list(value, *variables)[1]}


def witness(name):
    path = DIRECTORY / f"cubic_CY_one_segre_double_split_{name}_open_certificate.json"
    data = json.loads(path.read_text())
    support = (data["minor_numerator_factors"]+data["minor_denominator_factors"]
               + data["projection_denominator_factors"])
    return [numerator(s.sympify(part.replace("^", "**")).subs(PARAMETERS, simultaneous=True))
            for part in sorted(set(support))]


def original_witnesses():
    variables = (c, d, x)
    units = set.union(*(factors(f, variables) for f in UNITS))
    for name, indices in [("FO1", (1, 3)), ("FO1_linear_columns", (0, 2))]:
        support = set.union(*(factors(f, variables) for f in witness(name))) - units
        expected = {monic(F[i], variables) for i in indices}
        assert support == expected, (name, support, expected)
    involution = TRANSLATES[2]
    for i, j in [(0, 1), (2, 3)]:
        assert monic(F[i].subs(involution, simultaneous=True), variables) == monic(F[j], variables)


def curves():
    first = (c*c+2*c+4)*y+2*c
    second = (c*c-2*c-4)*y+2*c
    third = c*(c-4)*y+4
    mixed = -(c**3*y-4*c*c*y+2*c*c-4*c+8)/(2*c*(y-1))
    mixed_numerator = numerator(F[1].subs(d, mixed))
    mixed_curve, = factors(mixed_numerator, (c, x)) - {c-2, c*x-2, c*x+2}
    assert s.degree(mixed_curve, c) == s.degree(mixed_curve, x) == 6
    assert s.expand(F[2].subs(d, mixed).cancel()) == 0

    # Treat the three remaining pairs by their linear dependence on y.
    Y = s.Symbol("Y")
    f = [term.subs(y, Y) for term in F]
    res01 = s.resultant(f[0], f[1], Y)
    res23 = s.resultant(f[2], f[3], Y)
    assert s.cancel(res01/((c-d)**2*(c+d)*(c*d+4))) in (-2, 2)
    assert s.cancel(res23/((c-d)*(c+d)*(c*d-4)*(c-d-4))) in (-2, 2)
    assert s.cancel(F[0].subs(d, -4/c)/first) == 2-c
    assert s.cancel(F[2].subs(d, 4/c)/second) == c-2
    assert s.cancel(F[2].subs(d, c-4)/third) == c+2
    return [
        ("cd=-4", first, -4/c),
        ("cd=4", second, 4/c),
        ("d=c-4", third, c-4),
        ("mixed", mixed_curve, mixed),
    ]


def rank_witnesses():
    for name in ("FO1_quotient", "FO1_quotient_alternate"):
        forms = witness(name)
        for variables in TRANSLATES:
            yield [f.subs(variables, simultaneous=True) for f in forms]


def projection(equation, graph, supports):
    first_basis = s.groebner([equation], c, x, domain=s.QQ, order="grevlex")
    units = set.union(*(factors(numerator(f.subs(d, graph)), (c, x)) for f in UNITS))
    projected = []
    for support in supports:
        remaining = set.union(*(factors(numerator(f.subs(d, graph)), (c, x)) for f in support))
        remainders = [first_basis.reduce(f)[1] for f in remaining-units]
        if 0 in remainders:
            continue
        applicable = set()
        for value in set(remainders):
            norm = s.resultant(equation, value, x)
            assert norm
            applicable.update(factors(norm, (c,)))
        projected.append(applicable)
    return projected


def direct_product_curve(equation, graph):
    field = quadratic_field(x, s.Poly(equation, x))
    source = four_cross_one_outer()[0]
    source = source.subs(PARAMETERS, simultaneous=True).subs(d, graph).applyfunc(s.cancel)
    support = {monic(s.sympify(f.replace("^", "**")), (c,))
               for f in quadratic_rank_support(source, field)}
    leading = s.Poly(equation, x).LC()
    assert support <= {c, c+2, c-2, leading, c*c+4}
    # The quadratic leading coefficient cannot vanish in the chart.
    # The other quadratic is eliminated by c-d or c+d.
    assert (c*c+4)/c in {s.cancel(unit.subs(d, graph)) for unit in (c-d, c+d)}
    return sorted(map(str, support))


def empty_fibre(equation, graph, supports, base):
    minimal = s.Poly(base, c, domain=s.QQ)
    field = s.QQ.algebraic_field((minimal, s.CRootOf(minimal, 0)))

    def convert(value):
        coefficients = s.Poly(value, x).terms()
        terms = {
            power: field.new(s.Poly(coefficient, c, domain=s.QQ).rem(minimal).rep.to_list())
            for power, coefficient in coefficients
        }
        return s.Poly.from_dict(terms, x, domain=field)

    common = convert(equation)
    initial_degree = common.degree()
    for support in supports:
        if common.degree() == 0:
            break
        product = s.Poly(1, x, domain=field)
        for polynomial in support:
            factor = convert(numerator(polynomial.subs(d, graph)))
            product = (product*factor.rem(common)).rem(common)
        common = common.gcd(product)
    for unit in UNITS:
        if common.degree() == 0:
            break
        factor = common.gcd(convert(numerator(unit.subs(d, graph))))
        while factor.degree() > 0:
            common = common.exquo(factor)
            factor = common.gcd(factor)
    assert common.degree() == 0, (base, common)
    return {"base_factor": str(base), "initial_degree": initial_degree, "remaining_degree": 0}


def main():
    original_witnesses()
    witnesses = list(rank_witnesses())
    certificate = {}
    for name, equation, graph in curves():
        if name in ("cd=-4", "cd=4"):
            certificate[name] = {"direct_rank_support": direct_product_curve(equation, graph)}
        else:
            projected = projection(equation, graph, witnesses)
            remaining = set.intersection(*projected)-{c, c-2, c+2}
            expected_degrees = {"d=c-4": [], "mixed": [8, 18]}[name]
            assert sorted(s.degree(f, c) for f in remaining) == expected_degrees
            certificate[name] = {"fibres": [empty_fibre(equation, graph, witnesses, base)
                                           for base in sorted(remaining, key=str)]}
        print("PASS", name, "no allowed point with a central cubic", flush=True)
    (DIRECTORY / "cubic_CY_one_segre_double_split_FO_nonlinear_certificate.json").write_text(
        json.dumps(certificate, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
