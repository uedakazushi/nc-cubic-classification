"""Central quadratics in the commuting planes of TD1 and FO1–FO2."""
import argparse
from functools import cache
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctions as FIELD, VARIABLES
from verify_cubic_CY_one_segre_cross import PivotAlgebra, centre_calculation
from verify_cubic_CY_one_segre_double_split_isolated import marked

Q = s.Rational
p, u, w = VARIABLES


@cache
def three_cross():
    t = p-Q(1, 4)
    h = -p*t
    slope = 8*p-1
    x2, x6, x8 = u+1/p, u*w, u*w*w
    x5 = h*u+Q(1, 4)-slope*u*w
    x1 = 1/p+x5/w
    x0 = 8+p/w+x1*(h/w-slope)
    x7 = h*x6-slope*x8
    x3 = h*x1-slope*x5+2*p-Q(1, 4)
    x4 = h*(x5+t)-slope*x7
    coefficients = dict(enumerate([x0, x1, x2, x3, x4, x5, x6, x7, x8]))
    relations = marked({**coefficients, 9: p, 10: 1, 11: 1, 12: h, 14: t}, Q(1, 8))
    line1, line2 = (1, 0, t, 0), (0, p, 1, 1)
    quadratic = (p*p, p*w*(16*p+64*w-2), w*w)
    return relations, line1, line2, quadratic


@cache
def four_cross_one_outer(linear_columns=False):
    h = Q(1, 64)-p*p/4
    x2 = 1/p+32*w+256*p*p*u*w*w
    delta = 16*p*u*w
    x1, x0 = x2+delta, x2+2*delta+u
    value = w-h*x2+2*h/p
    coefficients = dict(enumerate([
        x0, x1, x2, value+p-h*(x0-x2), h*h*x0, value-h*(x1-x2),
        value, h*h*x1, h*h*x2,
    ]))
    relations = marked({**coefficients, 10: 1, 11: 1, 12: h, 13: h, 14: p}, Q(1, 8), linear_columns)
    line1, line2 = (1, h, p/2, -p/2), (0, 0, 1, 1)
    eta = p*w+Q(1, 32)
    quadratic = (p, 2*eta, 16*p*(eta*eta+(1-16*p*p)/1024))
    return relations, line1, line2, quadratic


def check(name, data, field=FIELD):
    source, line1, line2, coefficients = data
    relations = [
        {divmod(i, 4): field.from_sympy(s.cancel(source[i, j]))
         for i in range(16) if s.cancel(source[i, j])}
        for j in range(6)
    ]
    algebra = PivotAlgebra(field, 4, relations, [0]*4)
    algebra.pivot_product = field.one
    algebra.build(3)
    assert [len(algebra.basis[n]) for n in (2, 3)] == [10, 20]
    support = list(range(4))
    commute = {}
    for i in support:
        for j in support:
            coeff = field.from_sympy(s.sympify(line1[i]*line2[j]))
            if coeff:
                algebra.addto(commute, algebra.word((i, j)), coeff)
                algebra.addto(commute, algebra.word((j, i)), -coeff)
    assert not commute

    coefficients_free = [
        field.from_sympy(s.cancel(coefficients[0]*line1[i]*line1[j]
                                  +coefficients[1]*line1[i]*line2[j]
                                  +coefficients[2]*line2[i]*line2[j]))
        for i in support for j in support
    ]
    for gen in support:
        commutator = {}
        for position, coefficient in enumerate(coefficients_free):
            if coefficient:
                i, j = divmod(position, 4)
                algebra.addto(commutator, algebra.word((gen, i, j)), coefficient)
                algebra.addto(commutator, algebra.word((i, j, gen)), -coefficient)
        assert not commutator
    print("PASS", name, "central quadratic on the commuting plane", flush=True)


def fraction_factors(values):
    return sorted({str(factor) for value in values for factor, _ in value.factor()[1]})


def quadratic_quotient(data):
    source, U, V, (a, b, c) = data
    coefficients = s.Matrix([a*U[i]*U[j]+b*U[i]*V[j]+c*V[i]*V[j]
                             for i in range(4) for j in range(4)])
    return source.row_join(coefficients)


def cubic_exclusion(name, source, permutation, dimensions):
    algebra, rank = centre_calculation(source, permutation, FIELD, FIELD.from_sympy, dimensions)
    assert rank == dimensions[1]
    projection_denominators = {
        str(value.d): value.d
        for degree in (2, 3, 4) for coordinates in algebra.right[degree].values()
        for value in coordinates.values()
    }
    projection_denominators.update({
        str(value.d): value.d for value in (FIELD.from_sympy(coefficient) for coefficient in source)
    })
    result = {
        "chart": name,
        "centre_rank": rank,
        "minor_numerator_factors": fraction_factors([algebra.pivot_product.n]),
        "minor_denominator_factors": fraction_factors([algebra.pivot_product.d]),
        "projection_denominator_factors": fraction_factors(projection_denominators.values()),
    }
    path = Path(__file__).with_name(f"cubic_CY_one_segre_double_split_{name}_open_certificate.json")
    path.write_text(json.dumps(result, indent=2)+"\n")
    print("PASS", name, f"generic rank {rank} with explicit factor support")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cubic", choices=("TD1", "FO1", "FO1_linear_columns",
                                           "FO1_quotient", "FO1_quotient_alternate"))
    args = parser.parse_args()
    charts = {"TD1": three_cross, "FO1": four_cross_one_outer}
    if args.cubic:
        name = args.cubic
        if name.startswith("FO1_quotient"):
            alternate = name.endswith("alternate")
            source = quadratic_quotient(four_cross_one_outer(linear_columns=not alternate))
            permutation = (0, 1, 3, 2) if alternate else (0, 1, 2, 3)
            dimensions = (9, 16, 25)
        else:
            source = (four_cross_one_outer(linear_columns=True)[0]
                      if name == "FO1_linear_columns" else charts[name]()[0])
            permutation = (0, 1, 3, 2) if name == "FO1_linear_columns" else (0, 1, 2, 3)
            dimensions = (10, 20, 35)
        cubic_exclusion(name, source, permutation, dimensions)
    else:
        for name, chart in charts.items():
            check(name, chart())


if __name__ == "__main__":
    main()
