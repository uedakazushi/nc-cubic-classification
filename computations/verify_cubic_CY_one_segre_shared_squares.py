"""All central-cubic ranks in the two remaining shared Segre projections."""
from itertools import product
import json
from pathlib import Path

import sympy as s

from verify_cubic_CY_one_segre_cross import centre_calculation, h, p
from verify_cubic_CY_one_segre_square import Q, comm, word

ell = s.Symbol("ell")
PARAMETERS = (p, ell, h)  # exchange ratio, off-diagonal coefficient, lower coefficient


def relations(ratio, left, right, diagonal, z, three_squares):
    """The six original relations from SRT1 and SRQ1."""
    ab, ac, bc, bd, cd = (comm(i, j) for i, j in [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)])
    return s.Matrix.hstack(
        word(0, 0)+2*z*bc+4*bd+4*ratio*cd*three_squares,
        word(0, 1)+word(1, 0)-4*diagonal*ab-4*right*ac,
        word(0, 2)+word(2, 0)-4*left*ab-4*diagonal*ac,
        word(1, 2)+word(2, 1), ratio*bd+cd,
        word(3, 3)+word(1, 1)+three_squares*word(2, 2),
    )


def factors(expressions):
    all_factors = set()
    for expr in expressions:
        # Taking the norm to QQ covers all possible zeros over the algebraic closure.
        polynomial = s.Poly(expr*expr.xreplace({s.I: -s.I}), *PARAMETERS, domain=s.QQ)
        assert not polynomial.is_zero
        all_factors.update(factor.monic().as_expr() for factor, _ in polynomial.factor_list()[1])
    return all_factors


def check(label, source, units):
    field = (s.QQ_I if source.has(s.I) else s.QQ).frac_field(*PARAMETERS)
    algebra, rank = centre_calculation(source, (0, 1, 2, 3), field, field.from_sympy)
    assert rank == 20, label
    minor = algebra.pivot_product
    projection_denominators = {str(c.denom): c.denom.as_expr()
                               for degree in (2, 3, 4)
                               for row in algebra.right[degree].values()
                               for c in row.values()}
    exceptional = factors([minor.numer.as_expr(), minor.denom.as_expr(),
                           *projection_denominators.values()])
    assert exceptional <= factors(units), (label, exceptional-factors(units))
    return {
        "chart": label, "center_rank": rank,
        "minor": str(field.to_sympy(minor)),
        "all_required_units": sorted(map(str, exceptional)),
    }


def charts():
    resonances = [Q(1, 4), -Q(1, 4), s.I/4, -s.I/4]
    for k, l, z in product((p, 0), (ell, *resonances), (h, 0)):
        units = [p, p-1, p+1] if k == p else []
        if l == ell:
            units += [ell, 4*ell-1, 4*ell+1, 16*ell**2+1]
        if z == h:
            units.append(h)
        yield f"SRQ off-diagonal k={k}, ell={l}, z={z}", relations(k, l, -Q(1, 16)/l, 0, z, 1), units
    for sign, k, z in product((1, -1), (p, 0), (h, 0)):
        units = [p, p-1, p+1] if k == p else []
        if z == h:
            units.append(h)
        yield f"SRQ diagonal sign={sign}, k={k}, z={z}", relations(k, 0, 0, sign*s.I/4, z, 1), units
    for k, z in product((0, 1), (h, 0)):
        l = ell if k else s.Integer(1)
        units = [ell] if k else []
        if z == h:
            units.append(h)
        yield f"SRT off-diagonal k={k}, z={z}", relations(k, l, -Q(1, 16)/l, 0, z, 0), units
    for sign in (1, -1):
        for k, z in [(1, h), (1, 0), (0, 0), (0, 1)]:
            units = [h] if z == h else []
            yield f"SRT diagonal sign={sign}, k={k}, z={z}", relations(k, 0, 0, sign*s.I/4, z, 0), units


def main():
    records = []
    for label, source, units in charts():
        records.append(check(label, source, units))
        print("PASS", label, flush=True)
    assert len(records) == 40
    Path(__file__).with_name("cubic_CY_one_segre_shared_squares_certificate.json").write_text(
        json.dumps(records, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
