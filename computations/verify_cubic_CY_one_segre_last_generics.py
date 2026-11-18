"""Exact rank witnesses for the two remaining one-commutator families."""
import sympy as sym

from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_double_split_isolated import marked
from verify_cubic_CY_one_segre_double_split_quadratics import (
    four_cross_one_outer,
    p,
    quadratic_quotient,
    u,
    w,
)
from verify_cubic_CY_one_segre_square_split_M import lower_m
from verify_cubic_CY_one_segre_square_split_lower import h as square_s, lower_open, p as square_w

Q = sym.Rational
PERMUTATION = (0, 1, 2, 3)


def square_split():
    source, units, z = lower_open()
    point = {square_s: 1, square_w: 1, z: 1}
    assert all(f.subs(point) for f in units)
    _, rank = centre_calculation(source.subs(point), PERMUTATION, sym.QQ, sym.QQ.from_sympy)
    assert rank == 20
    quotient = quadratic_quotient(lower_m()).subs({p: 1, u: 1, w: 1})
    _, rank = centre_calculation(quotient, PERMUTATION, sym.QQ, sym.QQ.from_sympy, (9, 16, 25))
    assert rank == 16
    print("PASS M at (s,w,z)=(1,1,1), original and quadratic-quotient ranks")


def both_outer_limit():
    s = sym.Symbol("s")
    t, z, v = Q(1), Q(1), Q(1)
    P, m = s+t, s-t
    h, k = Q(1, 64)-P*P/4, Q(1, 64)-m*m/4
    d = k*P*z-m*v-2*k*k
    f = v-k*k/t
    N = m*h*z*v+2*k*k*h*z+k*m*P*v-P*v*v+k**3*P
    J = m*h*z-P*v+k*m*t-2*k*k
    slope = m/(k*P)
    x2 = (s*z*z+v)/(s*v+k*k)
    x4 = -h*h/t+2*h*k*J/(t*d)+f*J*J/(d*d)
    x6, x7, x8 = z, -N/d, v
    x5 = slope*(x7-h*x6)+x8/k
    x1 = slope*(x5-h*x2-s)+x6/k
    x3 = slope*(x4-h*x5-h*t)+x7/k
    x0 = slope*(x3-h*x1)+(x5-m)/k
    coefficients = (x0, x1, x2, x3, x4, x5, x6, x7, x8, s, 1, 1, h, k, t)
    source = marked(dict(enumerate(coefficients)), Q(1, 8), linear_columns=True)
    source = source.applyfunc(sym.cancel)
    assert all(sym.denom(value).subs(s, 0) for value in source)
    endpoint = source.subs(s, 0)
    point = {p: 1, u: Q(1216, 22831), w: -Q(1343, 480)}
    assert (p*u*w*(16*p*p-1)*(16*p*w+1)).subs(point)
    assert endpoint == four_cross_one_outer(linear_columns=True)[0].subs(point)

    e = v+k*k/s
    A = s*z-k
    C = 32*(P*v-m*h*z)+k*(1-16*P*m)
    units = [s, t, h, k, P, e, d, A, C]
    for sign in (-1, 1):
        B = 4*m+sign
        U = (4*P-sign)*B*z+64*v
        units.append(s*U*U+128*k*k*U-16*t*B*B*(sign*v+4*k*k))
    assert all(unit.subs(s, Q(1, 2)) for unit in units)
    _, rank = centre_calculation(endpoint, PERMUTATION, sym.QQ, sym.QQ.from_sympy)
    assert rank == 20
    print("PASS FDC3 path to the allowed FO1 endpoint, rank 20 there")


if __name__ == "__main__":
    square_split()
    both_outer_limit()
