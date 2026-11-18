"""Point-curve and vertex identities for the quantum triangle, secant, and node."""
import sympy as s


def main():
    x, y, z, p, r, q, v = s.symbols("x y z p r q v", nonzero=True)
    matrix = s.Matrix([[-p*x, -q*z, y], [z, -r*y, -q*x], [-q*y, x, 0]])
    assert s.expand(matrix.det() - ((1-q**3)*x*y*z-q*p*x**3-q*r*y**3)) == 0

    def check_path(point_at, scale, px, py):
        points = [point_at(q**i*v) for i in range(3)]
        rows = dict(zip((x, y, z, p, r), (*points[0], px, py)))
        assert (matrix.subs(rows, simultaneous=True)*s.Matrix(points[1])).applyfunc(s.cancel) == s.zeros(3, 1)
        a, b, c = points
        value = scale*a[0]*b[1]*c[2]+px*a[0]*b[0]*c[0]+q**3*py*a[1]*b[1]*c[1]
        assert s.cancel(value) == 0

    check_path(lambda u: (1, u, -q*(p+r*u**3)/((q**3-1)*u)), q**3-1, p, r)
    check_path(lambda u: (1, u, -q*p/((q**3-1)*u)), q**3-1, p, 0)
    check_path(lambda u: (0, 1, u), q**3-1, p, 0)
    for component in (lambda u: (1, u, 0), lambda u: (0, 1, u), lambda u: (u, 0, 1)):
        check_path(component, 1, 0, 0)

    # With the active coordinate first, eliminate t from the initial cubic.
    at, yz = s.symbols("at yz")
    initial_relation = yz-q*s.Symbol("zy")-at
    relation = s.cancel(initial_relation.subs(at, -(q**2-1)*yz))
    assert s.expand(relation-q*(q*yz-s.Symbol("zy"))) == 0
    print("PASS point matrices, six boundary paths, central cubic values, and vertex elimination")


if __name__ == "__main__":
    main()
