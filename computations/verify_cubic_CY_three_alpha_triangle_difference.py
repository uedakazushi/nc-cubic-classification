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

    pole_numerator = (q+1)**2*(q*u**4*(by*by+bz*bz)+rho*u**3*(u*u+q)*by*bz)
    for sign in (-1, 1):
        fixed_point = sign/rho
        diagonal_residue = (by+j.subs(u, fixed_point)*bz)/(
            2*j.subs(u, fixed_point)*s.diff(j, u).subs(u, fixed_point)
        )
        norm_double_pole = (pole_numerator/first_denominator).subs(u, q*fixed_point)
        norm_double_pole /= (2*q*q*fixed_point)**2
        assert s.cancel(norm_double_pole+diagonal_residue**2) == 0
    print("PASS polynomial-lattice residue identity at both reflection fixed points")

    parameter = s.Symbol("a")
    pair = (1-parameter/u)*(1-parameter*u/q)
    assert s.cancel(pair-(1+parameter**2/q-parameter*xi/rho)) == 0
    denominator = (1-u**-2)*(1-q*u**-2)*(1-u*u/(q*q))*(1-u*u/q)
    assert s.cancel(denominator-first_denominator*(u*u-q)**2/(q**3*u**4)) == 0
    print("PASS folded orbit factors for the quartic and quintic")

    a, b, c1, c2, c3 = s.symbols("a b c1 c2 c3")
    omega = (1-a*u)*(1-b*u)/((1-a*b)*(1-u*u))
    alpha = s.prod(1-r*u for r in (a,b,c1,c2,c3))/((1-u*u)*(1-q*u*u))
    f = s.cancel(alpha/omega)
    assert s.cancel(omega+omega.subs(u, 1/u)-1) == 0
    assert s.cancel(omega*(u-u**-1)+(1-a*u)*(1-b*u)/((1-a*b)*u)) == 0
    reflected = f.subs(u, 1/(q*u))
    total = s.cancel(f+reflected)
    assert len(s.Poly(s.denom(total), u).terms()) == 1
    for power in (1, 2, 3):
        summand = s.cancel(f*((q*u)**(-power)-u**power))
        # The cross relation has only powers of u as denominators in u.
        assert len(s.Poly(s.denom(summand),u).terms()) == 1
    print("PASS the two reflection-order cross relations and the branch cancellation")

    delta = u-u**-1
    omega_star = omega.subs(u, 1/u)
    multiplier = s.cancel(omega_star*delta)
    reflected_multiplier = multiplier.subs(u, 1/(q*u))
    assert s.cancel(multiplier-(u-a)*(u-b)/((1-a*b)*u)) == 0
    assert s.cancel(omega_star*multiplier.subs(u, 1/u)+omega*multiplier) == 0
    complementary = s.cancel(f*reflected_multiplier/delta)
    expected = -s.prod(1-r*u for r in (q*a,q*b,c1,c2,c3))/(q*(1-u*u)*(1-q*u*u))
    assert s.cancel(complementary-expected) == 0
    psi = s.cancel(f*(reflected_multiplier-multiplier)/delta)
    assert len(s.Poly(s.denom(s.cancel(psi+psi.subs(u,1/u))),u).terms()) == 1
    print("PASS complementary difference coefficient and cancellation of all finite poles")


if __name__ == "__main__":
    main()
