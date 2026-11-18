"""Recover the elliptic boundary equation from the rank-two character Hessian."""
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctionField
from cubic_sparse_hilbert import SparseGradedAlgebra

Q, R, A, B, C, D, E, F = s.symbols("q r a b c d e f")
PARAMETERS = (Q, R, A, B, C, D, E, F)
FIELD = RationalFunctionField(PARAMETERS)


def central_lift():
    q, r = [FIELD.from_sympy(v) for v in (Q, R)]
    lower = ((A,B,D),(B,C,E),(D,E,F))
    relations = []
    for i in range(3):
        j, k = (i+1)%3, (i+2)%3
        source = {(j,k): FIELD.one, (k,j): q, (i,i): r}
        source.update({(3,col): -FIELD.from_sympy(c) for col, c in enumerate(lower[i])})
        relations.extend([source, {(3,i): FIELD.one, (i,3): -FIELD.one}])
    algebra = SparseGradedAlgebra(FIELD, 4, relations, [0]*4)
    algebra.build(4)
    assert [len(algebra.basis[i]) for i in (2,3,4)] == [10,20,35]
    commutators = [{} for _ in range(4*35)]
    for col, word in enumerate(algebra.basis[3]):
        for i in range(4):
            difference = algebra.word(word+(i,))
            algebra.addto(difference, algebra.word((i,)+word), -FIELD.one)
            for row, value in difference.items():
                commutators[i*35+row][col] = value

    pivots = algebra.echelon(commutators)
    non_pivots = [i for i in range(20) if i not in pivots]
    assert [algebra.basis[3][i] for i in non_pivots] == [(3,3,2),(3,3,3)]
    kernel = {non_pivots[0]: FIELD.one}
    for index, pivot in sorted(pivots.items(), reverse=True):
        value = FIELD.zero
        for col, coefficient in pivot.items():
            if col != index and col in kernel:
                value -= coefficient*kernel[col]
        if value:
            kernel[index] = value
    assert all(not sum((kernel[i]*co for i, co in row.items() if i in kernel), FIELD.zero)
               for row in commutators)

    terms = {"".join("xyzt"[i] for i in algebra.basis[3][col]): value for col, value in kernel.items()}
    scale = FIELD.from_sympy(R*(R**3-1))/terms["yyy"]
    names = {str(v):v for v in PARAMETERS}

    def expression(value):
        num, den = [s.sympify(str(poly).replace("^", "**"), locals=names) for poly in (value.n, value.d)]
        return s.cancel(num/den)

    return {word: expression(value*scale) for word, value in sorted(terms.items())}


def check_all_terms(terms):
    reference = {"yyy": R*(R**3-1), "yzx": R**3-Q**3,
                 "zyx": -Q*(R**3-1), "zzz": R*(Q**3-R**3)}
    assert {word: s.factor(co) for word, co in terms.items() if "t" not in word} == {
        word: s.factor(co) for word, co in reference.items()
    }
    for coefficient in terms.values():
        denominator = s.denom(coefficient)
        assert s.denom(s.cancel(R*(Q-1)/denominator)) == 1
    gradient = s.Matrix([terms["tt"+name] for name in "xyz"])
    u, v, x, y, z = s.symbols("u v x y z")
    rank_two = {D: -A*u-B*v, E: -B*u-C*v, F: A*u*u+2*B*u*v+C*v*v}
    boundary = (1+Q**3+R**3)*u*v-Q*R*(u**3+v**3+1)
    contraction = (s.Matrix([[u,v,1]])*gradient)[0].subs(rank_two, simultaneous=True)
    assert s.cancel(contraction+(A*C-B**2)*boundary/(Q-1)) == 0
    rank_one = {A:x*x, B:x*y, C:y*y, D:x*z, E:y*z, F:z*z}
    cross = gradient.subs(rank_one, simultaneous=True).cross(s.Matrix([x,y,z]))
    assert all(s.cancel(coefficient) == 0 for coefficient in cross)
    assert all(s.cancel(coefficient.subs(dict.fromkeys((A,B,C,D,E,F), 0))) == 0 for coefficient in gradient)
    print("PASS universal central lift, rank-two boundary contraction and rank-one alignment", flush=True)
    return str(s.factor(contraction))


def main():
    terms = central_lift()
    factorization = check_all_terms(terms)
    Path(__file__).with_name("cubic_CY_three_alpha_elliptic_character_boundary_certificate.json").write_text(
        json.dumps({"central_lift": {k:str(v) for k,v in terms.items()},
                    "rank_two_contraction": factorization}, indent=2)+"\n")


if __name__ == "__main__":
    main()
