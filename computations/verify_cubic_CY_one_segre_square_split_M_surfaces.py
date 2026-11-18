"""Exclude central cubics on the common exceptional surfaces of the M certificate."""
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctionField, VARIABLES
from verify_cubic_CY_one_segre_double_split_quadratics import centre_witness
from verify_cubic_CY_one_segre_double_split_TD import factors, fraction, rank_univariate
from verify_cubic_CY_one_segre_square_split_M import lower_m

p, u, w = VARIABLES
x, z, t = p, u, w
v = s.Symbol("v")
PERMUTATION = (0, 1, 2, 3)
DIMENSIONS = (10, 20, 35)


def support(witness, variables):
    return factors([s.sympify(value.replace("^", "**"))
                    for name, entries in witness.items() if name.endswith("_factors")
                    for value in entries], variables)


def main():
    k = (x*x-1)/64
    w0 = (1+t)/(k*(1-t))
    z0 = k*(z+1)/w0
    normal = {p: x/4, u: z0, w: w0}
    source = lower_m()[0].subs(normal, simultaneous=True).applyfunc(s.cancel)
    t0 = source.subs(t, 0).applyfunc(s.cancel)
    zt1 = source.subs(z, 1/t).applyfunc(s.cancel)
    witnesses = {
        "T=0": centre_witness(t0, PERMUTATION, DIMENSIONS, RationalFunctionField((x, z))),
        "ZT=1": centre_witness(zt1, PERMUTATION, DIMENSIONS, RationalFunctionField((x, t))),
    }
    units_t0 = (x, x*x-1, x*z-2, x*z+2)
    units_zt1 = (x, x*x-1, t, t*t-1, x*x-t*t, x**4-t*t)
    assert not support(witnesses["ZT=1"], (x, t))-factors(units_zt1, (x, t))
    xi = x*z
    curves = [
        (z-2, v, 2, False),
        (xi-x-1, v, 1+1/v, False),
        (x*(xi-x)-1, v, 1+1/v**2, False),
        (3*xi*xi-3*x*x-8*xi+7, (-5/v-v)/6, (4+(v-5/v)/2)/3, True),
        (xi*xi-x*x-3, (v-3/v)/2, (v+3/v)/2, True),
        ((xi-2*x)**2-x*x+1, (v+1/v)/2, (3*v+1/v)/2, True),
    ]
    exceptional = support(witnesses["T=0"], (x, z))-factors(units_t0, (x, z))
    assert exceptional == factors([equation for equation, *_ in curves], (x, z))
    records = []
    for equation, x0, z0, in_xi in curves:
        chart = {x: x0, z: z0/x0 if in_xi else z0}
        assert s.cancel(equation.subs(chart, simultaneous=True)) == 0
        restrictions = [v]
        restrictions.extend(fraction(value)[1] for value in chart.values())
        restrictions.extend(fraction(value.subs(chart, simultaneous=True))[0] for value in units_t0)
        assert all(restrictions)
        target = t0.subs(chart, simultaneous=True).applyfunc(s.cancel)
        records.append(rank_univariate(str(equation), target, v, restrictions))
    record = {"witnesses": witnesses, "rational_curves": records}
    Path(__file__).with_name("cubic_CY_one_segre_square_split_M_surfaces_certificate.json").write_text(
        json.dumps(record, indent=2)+"\n"
    )
    print("PASS both surfaces, all six rational curves and all exceptional fibres")


if __name__ == "__main__":
    main()
