"""Exclude all central cubics in the decomposable three-cross TD1 family."""
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctionField, VARIABLES
from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_double_split_quadratics import fraction_factors, three_cross

Q = s.Rational
p, u, w = VARIABLES
a, b, e, z = s.symbols("a b e z")
h = (1-a*a)/64
PARAMETERS = {p: (a+1)/8, w: h/(b+a/2), u: e*(b+a/2)**2/h**2}
UNITS = [a-1, a+1, a-2*b, a+2*b, e, a*a-64*e*(2*b-1)**2-1]
DIRECTORY = Path(__file__).parent


def factors(expressions, variables):
    return {s.Poly(factor, *variables, domain=s.QQ).monic().as_expr()
            for value in expressions for factor, _ in s.factor_list(value, *variables)[1]}


def fraction(expression):
    return s.cancel(expression).as_numer_denom()


def witness(name):
    certificate = json.loads((DIRECTORY / f"cubic_CY_one_segre_double_split_{name}_open_certificate.json").read_text())
    support = certificate["minor_numerator_factors"]+certificate["minor_denominator_factors"]
    support += certificate["projection_denominator_factors"]
    return [fraction(s.sympify(f.replace("^", "**")).subs(PARAMETERS, simultaneous=True))[0]
            for f in sorted(set(support))]


def cover():
    C = a*a-1+64*e*(2*b-1)*(a-2*b)
    B = a+2*b-2
    assert factors(witness("TD1_quotient"), (a, b, e))-factors(UNITS, (a, b, e)) == factors(
        [2*b-1, B, C.subs(a, -a)], (a, b, e)
    )

    e0 = (1-a)/(64*(a+1))
    e1 = -Q(1, 64)
    surface_support = factors([f.subs(b, Q(1, 2)) for f in witness("TD1")], (a, e))
    surface_units = factors([f.subs(b, Q(1, 2)) for f in UNITS], (a, e))
    linear0 = 64*(a+1)*e+a-1
    assert surface_support-surface_units == factors(
        [linear0, linear0.subs(a, -a), e-e1], (a, e)
    )
    assert s.cancel(linear0.subs(e, e0)) == 0

    mixed = (a+1)/(128*(a-1))
    assert s.expand(C.subs(b, (2-a)/2)+(a-1)*(128*a*e-a-128*e-1)) == 0
    assert s.cancel(C.subs(b, (2-a)/2).subs(e, mixed)) == 0
    assert s.factor(C-C.subs(a, -a)) == 128*a*e*(2*b-1)
    common = 1/(128*b*(1-2*b))
    assert s.cancel(C.subs(a, 0).subs(e, common)) == 0
    return [
        ("b=1/2, varying e", z, Q(1, 2), e0.subs(a, z)),
        ("b=1/2, constant e", z, Q(1, 2), e1),
        ("B=B'=0", 0, 1, z),
        ("B=C=0", z, (2-z)/2, mixed.subs(a, z)),
        ("C=C'=0", 0, z, common.subs(b, z)),
    ]


def rank_on_curve(name, A, B, E):
    chart = {a: A, b: B, e: E}
    parameters = {key: s.cancel(value.subs(chart, simultaneous=True))
                  for key, value in PARAMETERS.items()}
    source = three_cross()[0].subs(parameters, simultaneous=True).applyfunc(s.cancel)
    restrictions = [fraction(unit.subs(chart, simultaneous=True))[0] for unit in UNITS]
    restrictions.extend(fraction(value)[1] for value in (A, B, E, *parameters.values()))
    assert all(restrictions)

    field = RationalFunctionField((z,))
    algebra, rank = centre_calculation(source, (0, 1, 2, 3), field, field.from_sympy)
    assert rank == 20, name
    denominators = {str(co.d): co.d for n in (2, 3, 4)
                    for row in algebra.right[n].values() for co in row.values()}
    denominators.update({str(co.d): co.d for co in map(field.from_sympy, source)})
    raw = fraction_factors([algebra.pivot_product.n, algebra.pivot_product.d, *denominators.values()])
    support = factors([s.sympify(f.replace("^", "**")) for f in raw], (z,))
    exceptional = sorted(support-factors(restrictions, (z,)), key=str)
    for polynomial in exceptional:
        minimal = s.Poly(polynomial, z, domain=s.QQ)
        extension = s.QQ.algebraic_field((minimal, s.CRootOf(minimal, 0)))

        def convert(value):
            numerator, denominator = fraction(value)
            top = s.Poly(numerator, z, domain=s.QQ).rem(minimal).rep.to_list()
            bottom = s.Poly(denominator, z, domain=s.QQ).rem(minimal).rep.to_list()
            return extension.new(top)/extension.new(bottom)

        _, special_rank = centre_calculation(source, (0, 1, 2, 3), extension, convert)
        assert special_rank == 20, (name, polynomial)
    print("PASS", name, "rank 20 on the curve and every allowed exceptional fibre", flush=True)
    return {"chart": name, "factor_support": sorted(map(str, support)),
            "recomputed_irreducible_factors": list(map(str, exceptional))}


def main():
    result = [rank_on_curve(*data) for data in cover()]
    (DIRECTORY / "cubic_CY_one_segre_double_split_TD_certificate.json").write_text(
        json.dumps(result, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
