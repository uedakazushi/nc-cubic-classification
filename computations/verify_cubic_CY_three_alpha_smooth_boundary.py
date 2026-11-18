"""Exact Hesse coefficient and singular Sklyanin boundary calculations."""
from itertools import combinations

import sympy as s


def main():
    p, q, r, omega = s.symbols("p q r omega")
    h, x, y, z = s.symbols("h x y z")
    matrix = s.Matrix([[r*x, q*z, p*y], [p*z, r*y, q*x], [q*y, p*x, r*z]])
    equation = (p**3+q**3+r**3)*x*y*z-p*q*r*(x**3+y**3+z**3)
    assert s.expand(matrix.det()-equation) == 0

    factors = (p+q+r)*(p+omega*q+omega**2*r)*(p+omega**2*q+omega*r)
    assert s.rem(s.expand(factors-(p**3+q**3+r**3-3*p*q*r)),
                 omega**2+omega+1, omega) == 0
    fourier_p = omega**2*p+omega*q+r
    fourier_q = omega*p+omega**2*q+r
    assert s.rem(s.expand(fourier_p-omega**2*(p+omega**2*q+omega*r)),
                 omega**2+omega+1, omega) == 0
    assert s.rem(s.expand(fourier_q-omega*(p+omega*q+omega**2*r)),
                 omega**2+omega+1, omega) == 0

    triangle = matrix.subs({p: 1, q: 0, r: -h})
    points = [(x, y, 0), (y, 0, h*x), (0, h**2*x, y), (h**3*x, y, 0)]
    for a, b in zip(points, points[1:]):
        assert (triangle.subs(dict(zip((x, y, z), a)), simultaneous=True)*s.Matrix(b)).applyfunc(s.expand) == s.zeros(3, 1)

    # A basis of degree two maps injectively to sections on the three edges.
    words = [(0, 0), (1, 1), (2, 2), (2, 1), (0, 2), (1, 0)]
    edges = [(points[0], points[1]), ((x, 0, z), (0, h*z, x)), ((0, y, z), (h*y, z, 0))]
    rows = []
    for a, b in edges:
        assert (triangle.subs(dict(zip((x, y, z), a)), simultaneous=True)*s.Matrix(b)).applyfunc(s.expand) == s.zeros(3, 1)
        products = [s.Poly(a[i]*b[j], x, y, z) for i, j in words]
        monomials = sorted(set().union(*(poly.monoms() for poly in products)))
        rows.extend([poly.coeff_monomial(monomial) for poly in products] for monomial in monomials)
    assert s.Matrix(rows).rank() == 6
    evaluation = s.Matrix(rows)
    unit_minors = {sign*h**power for sign in (-1, 1) for power in range(4)}
    assert any(evaluation.extract(indices, range(6)).det() in unit_minors
               for indices in combinations(range(evaluation.rows), 6))
    print("PASS smooth Hesse point determinant, Fourier factors, and cyclic triangle boundary")


if __name__ == "__main__":
    main()
