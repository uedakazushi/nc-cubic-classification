"""Verify the difference formulas for triangular and secant leading forms."""
from collections import defaultdict
from functools import cache

import sympy as s


def main():
    rho, u = s.symbols("rho u", nonzero=True)
    bx, by, bz, D, ax, P = s.symbols("bx by bz D ax P")
    q = rho**2
    h = q*q-1
    parameters = (bx, by, bz, D, ax, P)
    x = -rho*(u+1/u)/h
    j = (1-q)*x
    y0 = s.factor((by+j*bz)/(j*j-1))
    z0 = s.factor((j*by+bz)/(j*j-1))
    first_denominator = (u*u-q*q)*(u*u-1)
    xi = u/rho+rho/u
    b0 = q*(u*u+1)*(u*u+q*q)/(h*h*first_denominator)
    b = (
        (ax-q*P*xi/(q**3-1))*b0 + u*u*h*D/first_denominator
        -rho*bx*u*(u*u+q)/((q-1)*first_denominator)
        +(q+1)**2*(q*u**4*(by*by+bz*bz)+rho*u**3*(u*u+q)*by*bz)
        /((u*u-q)**2*first_denominator)
    )

    field = s.QQ.frac_field(rho, u)
    polynomial_ring = field.poly_ring(*parameters)
    rho_field, u_field = field.gens
    q_field = rho_field**2

    def polynomial(expr):
        return polynomial_ring.from_sympy(expr)

    @cache
    def substitute(coefficient, new_u):
        def evaluate(part):
            return sum((rho_field**i*new_u**j*field.convert(value, s.QQ)
                        for (i, j), value in part.items()), field.zero)
        return evaluate(coefficient.numer)/evaluate(coefficient.denom)

    def act(poly, new_u):
        return polynomial_ring.ring.from_dict({
            monomial: substitute(coefficient, new_u) for monomial, coefficient in poly.items()
        })

    def combine(*vectors):
        result = defaultdict(lambda: polynomial_ring.zero)
        for vector in vectors:
            for power, value in vector.items():
                result[power] += value
        return result

    def scale(vector, scalar):
        return {power: scalar*value for power, value in vector.items()}

    def multiply(first, second):
        result = defaultdict(lambda: polynomial_ring.zero)
        for i, coeff in first.items():
            shifted_u = q_field**i*u_field
            for j, value in second.items():
                result[i+j] += coeff*act(value, shifted_u)
        return dict(result)

    X = {0: polynomial(x)}
    Y = {1: polynomial_ring.one, 0: polynomial(y0), -1: polynomial(b)}
    Z = {1: polynomial(rho*u), 0: polynomial(z0), -1: polynomial(rho*b/u)}
    right_first = combine(scale(multiply(X, X), polynomial(P)), scale(X, polynomial(ax)))
    for A, B, C, constant in [(Y, Z, right_first, bx), (Z, X, Y, by), (X, Y, Z, bz)]:
        residual = combine(multiply(A, B), scale(multiply(B, A), polynomial(-q)),
                           scale(C, -polynomial_ring.one), {0: polynomial(-constant)})
        assert not any(residual.values())
    quadratic = combine(scale(multiply(X, X), polynomial(ax)),
                        scale(multiply(Y, Y), polynomial(q*q)), multiply(Z, Z))
    linear = combine(scale(X, polynomial(bx)), scale(Y, polynomial(q*by)), scale(Z, polynomial(bz)))
    cubic_correction = scale(combine(multiply(multiply(X, X), X), scale(X, polynomial(-q/(q+1)))),
                             polynomial(P/(q**3-1)))
    residual = combine(multiply(multiply(X, Y), Z), scale(quadratic, polynomial(1/h)),
                       scale(linear, polynomial(1/(q-1))), cubic_correction, {0: polynomial(D)})
    assert not any(residual.values())
    assert act(Y[-1], 1/u_field) == act(Y[-1], q_field*u_field)
    defining = ((ax-q*P*xi/(q**3-1))*(q*xi*xi+(q-1)**2)/h**2+h*D/q-bx*xi/(q-1)
                +(q+1)**2*(by*by+bz*bz+xi*by*bz)/(q*(xi*xi-4)))
    assert Y[-1]*polynomial(first_denominator/(q*u*u)) == polynomial(defining)
    print("PASS three relations, scalar cut, reflection, and defining function for both leading forms")


if __name__ == "__main__":
    main()
