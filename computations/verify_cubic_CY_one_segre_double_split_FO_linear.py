"""Degree-four centre exclusions on the four linear-factor orbits for FO1."""
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctions as BASE
from verify_cubic_CY_one_segre_cross import centre_calculation, h, p
from verify_cubic_CY_one_segre_double_split_quadratics import four_cross_one_outer, u, w
from verify_cubic_CY_one_segre_double_split_remaining_small import check, factors, rank_factors

Q = s.Rational
X, V = p, h
UNITS = [X, X-1, X+1, V, V+1]
CURVES = [
    (X-1)*V**2+(X-1)*V+X**2+X,
    (X-1)*V**2+(2*X**2+X-1)*V+X**2+X,
]


def quadratic_curve(source, equation, number):
    polynomial = s.Poly(equation, V)
    discriminant = s.discriminant(polynomial)
    assert any(power % 2 for _, power in s.factor_list(discriminant, X)[1])
    trace = BASE.from_sympy(-polynomial.nth(1)/polynomial.nth(2))
    norm = BASE.from_sympy(polynomial.nth(0)/polynomial.nth(2))

    class Element:
        __slots__ = ("a", "b")

        def __init__(self, a, b):
            self.a, self.b = a, b

        def __bool__(self):
            return bool(self.a or self.b)

        def __neg__(self):
            return Element(-self.a, -self.b)

        def __add__(self, other):
            return Element(self.a+other.a, self.b+other.b)

        def __sub__(self, other):
            return self + -other

        def __mul__(self, other):
            second = self.b*other.b
            return Element(self.a*other.a-second*norm,
                           self.a*other.b+self.b*other.a+second*trace)

        def norm(self):
            return self.a*self.a+trace*self.a*self.b+norm*self.b*self.b

        def __truediv__(self, other):
            numerator = self*Element(other.a+trace*other.b, -other.b)
            divisor = other.norm()
            return Element(numerator.a/divisor, numerator.b/divisor)

    class Field:
        zero = Element(BASE.zero, BASE.zero)
        one = Element(BASE.one, BASE.zero)

        @staticmethod
        def from_sympy(expression):
            def reduce(value):
                output = Field.zero
                variable = Element(BASE.zero, BASE.one)
                for coefficient in s.Poly(value, V).all_coeffs():
                    output = output*variable+Element(BASE.from_sympy(coefficient), BASE.zero)
                return output

            numerator, denominator = s.cancel(expression).as_numer_denom()
            return reduce(numerator)/reduce(denominator)

    algebra, rank = centre_calculation(source, (0, 1, 2, 3), Field, Field.from_sympy)
    assert rank == 20
    denominators = [
        part.d for n in (2, 3, 4) for row in algebra.right[n].values()
        for coefficient in row.values() for part in (coefficient.a, coefficient.b)
    ]
    denominators.extend(part.d for value in source for part in
                        (Field.from_sympy(value).a, Field.from_sympy(value).b))
    minor = algebra.pivot_product.norm()
    support = {str(factor) for value in [minor.n, minor.d, *denominators]
               for factor, _ in value.factor()[1]}
    expected = {"p", "p - 1", "p + 1"} | ({"3*p + 1"} if number == 1 else set())
    assert support <= expected, support
    if number == 1:
        for v in s.solve(equation.subs(X, -Q(1, 3)), V):
            specialization = source.subs({X: -Q(1, 3), V: v})
            _, rank_at_point = centre_calculation(specialization, (0, 1, 2, 3),
                                                 s.QQ, s.QQ.from_sympy)
            assert rank_at_point == 20
    print("PASS quadratic curve", number, sorted(support))
    return sorted(support)


def main():
    normal = four_cross_one_outer()[0].subs({p: X/4, u: 4*u/X, w: V/(4*X)},
                                            simultaneous=True).applyfunc(s.cancel)
    specs = [
        ("L0", -2*X/(V*(X-1)), [2*V+X+1, V+X+1, V*X-V-X-1, *CURVES]),
        ("L3", -2*X**2/((V+1)*(X**2-1)), []),
        ("L4", -4*X**2/((V+1)*(X**2-1)), [-2*V+X-1, V+Q(1, 2), V*X-V-X-1]),
        ("L5", -4*X**2/((2*V+1)*(X**2-1)), [2*V+X+1, -2*V+X-1]),
    ]
    certificate = []
    for name, solution, extra in specs:
        source = normal.subs(u, solution).applyfunc(s.cancel)
        units = UNITS+[s.denom(solution)]
        support = rank_factors(source, (X, V))
        assert support-factors(units, (X, V)) == factors(extra, (X, V)), (name, support)
        graph_records, curve_records = [], []
        for equation in extra:
            if s.Poly(equation, V).degree() == 1:
                graph = s.solve(equation, V)[0]
                target = source.subs(V, graph).subs(X, h).applyfunc(s.cancel)
                graph_records.append(check(str(equation), target, (h,), [h, h-1, h+1]))
            else:
                curve_records.append(quadratic_curve(source, equation, CURVES.index(equation)))
        certificate.append({
            "chart": name, "factor_support": sorted(map(str, support)),
            "graphs": graph_records, "quadratic_curve_norm_factors": curve_records,
        })
        print("PASS all specializations on", name)
    Path(__file__).with_name("cubic_CY_one_segre_double_split_FO_linear_certificate.json").write_text(
        json.dumps(certificate, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
