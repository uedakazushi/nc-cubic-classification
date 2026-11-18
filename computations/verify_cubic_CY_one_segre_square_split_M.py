"""Central quadratic for the final M square-split chart."""
from functools import cache

import sympy as s

from cubic_flint_rational_function import VARIABLES
from verify_cubic_CY_one_segre_double_split_quadratics import check
from verify_cubic_CY_one_segre_square_split_lower import h, lower_open, p as w0

p, u, w = VARIABLES
Q = s.Rational


@cache
def lower_m():
    source, _, z0 = lower_open(linear_columns=True)
    source = source.subs({h: p, w0: w, z0: u}, simultaneous=True).applyfunc(s.cancel)
    k = p*p/4-Q(1, 64)
    m = ((32*k+1)*w+32)/(16*p*(k*w+1))
    U, V = (1, 0, -1/p, -k/p), (0, p, 0, -p)
    quadratic = ((p*w/(4*(k*w+1)))**2, -2*p*m, 1)
    return source, U, V, quadratic


def normalized_coordinates():
    x, z, t = VARIABLES
    k = (x*x-1)/64
    w0 = (1+t)/(k*(1-t))
    z0 = k*(z+1)/w0
    change = {p: x/4, w: w0, u: z0}
    coefficients = [s.cancel(s.sympify(value).subs(change, simultaneous=True))
                    for value in lower_m()[-1]]
    assert s.cancel(coefficients[1]+4*(x*x+t)/(x*x-1)) == 0
    assert s.cancel(coefficients[1]**2-4*coefficients[0]-16*(x*x-t*t)/(x*x-1)) == 0
    for sign in (-1, 1):
        W = (x+sign)**2*w0+64
        condition = 32*z0*W**2-(x+sign)**4*64*(k*w0+1)+128*(x+sign)**2
        expected = 128*(x+sign)**2*(z*(x+sign*t)**2-t*(x*x+1)-2*sign*x)/(1-t*t)
        assert s.cancel(condition-expected) == 0


if __name__ == "__main__":
    normalized_coordinates()
    check("M", lower_m())
