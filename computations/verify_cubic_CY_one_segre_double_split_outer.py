"""Exact identities for cubic cuts of the two-product outer Ore families."""
from itertools import combinations

import sympy as s


def main():
    kappa, sigma, h, p, r, q = s.symbols("kappa sigma h p r q")
    matrix = s.Matrix([[kappa-2*h-s.Rational(1, 2), -2*r],
                       [2*p, kappa+2*h-s.Rational(1, 2)]])/(kappa-sigma)
    determinant = (kappa+sigma)/(kappa-sigma)
    kappa_value = sigma**2+4*(p*r-h**2)+s.Rational(1, 4)
    assert s.cancel((matrix.det()-determinant).subs(kappa, kappa_value)) == 0
    assert s.cancel(s.trace(matrix)-1-determinant) == -1/(kappa-sigma)
    scalar = s.cancel(matrix[0, 0].subs({h: 0, kappa: sigma**2+s.Rational(1, 4)}))
    assert scalar == (2*sigma+1)/(2*sigma-1)
    assert s.cancel(scalar**2+scalar+1) == (12*sigma**2+1)/(4*sigma**2-4*sigma+1)
    correction = 8*sigma/(2*sigma-1)**2
    nu = s.cancel(scalar*correction/(1-scalar))
    assert s.rem(s.fraction(s.cancel(nu**3-1))[0], 12*sigma**2+1, sigma) == 0
    z = s.Symbol("z")
    delta = s.Poly((1+2*z**3)**2-4*z**3, z)
    assert delta.gcd(delta.diff()).degree() == 0

    # In the twisted axis algebra with a unit, the other base variable
    # is proportional to dc-qcd. The two centrality relations and
    # the cubic cut give three independent initial minimal relations.
    c3, d3 = s.symbols("C D")
    coefficients = s.Matrix([
        [1, -(1+q), q, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 1+q, -q, 0, 0],
        [0, 0, 0, 0, 0, 0, c3, d3],
    ])
    assert {s.factor(coefficients.extract(range(3), columns).det())
            for columns in combinations(range(8), 3)
            if coefficients.extract(range(3), columns).det()} >= {-c3, -d3}

    # The three factors giving c^3 d^3 in the shifted q-Weyl model.
    w, u = s.symbols("w u")
    assert s.rem(s.expand((w+u)*(q*w+u)*(q**2*w+u)-(w**3+u**3)),
                 q**2+q+1, q) == 0
    print("PASS outer Ore trace, scalar resonance, cyclic norm, and minimal cubic relations")


if __name__ == "__main__":
    main()
