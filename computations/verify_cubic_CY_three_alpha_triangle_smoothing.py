"""A regular cubic whose first jet spans every extra centre direction at q^3=1."""
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctionField
from cubic_sparse_hilbert import SparseGradedAlgebra

Q, PX, PY, PZ, AX, AY, AZ, BX, BY, BZ = s.symbols("q P_x P_y P_z A_x A_y A_z B_x B_y B_z")
PARAMETERS = (Q,PX,PY,PZ,AX,AY,AZ,BX,BY,BZ)
PURE = (PX,PY,PZ)
PRODUCT = PX*PY*PZ
CYCLOTOMIC = Q**2+Q+1


def central_polynomial():
    x, y, z, t = range(4)
    return {
        (z,y,x): Q*(Q**3-1-2*PRODUCT),
        (x,x,x): (Q**3-PRODUCT)*PX,
        (y,y,y): (1+PRODUCT)*PY,
        (z,z,z): (Q**3-PRODUCT)*PZ,
        (t,x,x): AX*(Q**2*CYCLOTOMIC/(Q+1)-PRODUCT),
        (t,y,y): AY*(CYCLOTOMIC+(Q+2)*PRODUCT)/(Q+1),
        (t,z,z): AZ*(Q**2*CYCLOTOMIC-(2*Q+1)*PRODUCT)/(Q+1),
        (t,y,x): -Q*AZ*PX*PY,
        (t,z,x): -AY*PX*PZ,
        (t,y,z): -Q*AX*PY*PZ/(Q+1),
        (t,z,y): -Q*AX*PY*PZ/(Q+1),
        (t,t,x): BX*(Q*CYCLOTOMIC-PRODUCT)-Q*AY*AZ*PX/(Q+1),
        (t,t,y): BY*(CYCLOTOMIC+PRODUCT)+(AY**2*PX*PZ-Q*AX*AZ*PY)/(Q+1),
        (t,t,z): BZ*(Q*CYCLOTOMIC-PRODUCT)-Q*(AX*AY*PZ+AZ**2*PX*PY)/(Q+1),
    }


def verify_central(cubic):
    field = RationalFunctionField(PARAMETERS)
    q = field.from_sympy(Q)
    relations = []
    for i, (pure, linear, constant) in enumerate(zip(PURE, (AX,AY,AZ), (BX,BY,BZ), strict=True)):
        j, k = (i+1)%3, (i+2)%3
        relations.extend([{(j,k): field.one, (k,j): -q, (i,i): -field.from_sympy(pure),
                           (3,i): -field.from_sympy(linear), (3,3): -field.from_sympy(constant)},
                          {(3,i): field.one, (i,3): -field.one}])
    algebra = SparseGradedAlgebra(field, 4, relations, [0]*4)
    algebra.build(4)
    assert [len(algebra.basis[i]) for i in (2,3,4)] == [10,20,35]
    for i in range(4):
        commutator = {}
        for word, raw in cubic.items():
            c = field.from_sympy(raw)
            algebra.addto(commutator, algebra.word(word+(i,)), c)
            algebra.addto(commutator, algebra.word((i,)+word), -c)
        assert not commutator
    print("PASS the regular central cubic with three independent pure squares", flush=True)


def verify_first_jet(cubic):
    x, y, z, t = range(4)
    q = Q
    special = dict.fromkeys(PURE, 0)
    omega = {
        (z,y,x): q, (t,x,x): q**2*AX/(q*q-1), (t,y,y): AY/(q*q-1), (t,z,z): q**2*AZ/(q*q-1),
        (t,t,x): q*BX/(q-1), (t,t,y): BY/(q-1), (t,t,z): q*BZ/(q-1),
    }
    assert all(s.cancel(cubic.get(word, s.S.Zero).subs(special)-(q**3-1)*omega.get(word, 0)) == 0
               for word in cubic.keys() | omega.keys())
    for parameter, axis, correction in zip(PURE, range(3), (AY*AZ, AZ*AX, AX*AY), strict=True):
        expected = {(axis,axis,axis): 1, (t,t,axis): q**2*correction}
        for word, value in cubic.items():
            difference = s.cancel(value.diff(parameter).subs(special)-expected.get(word, 0))
            assert s.rem(s.numer(difference), CYCLOTOMIC, q) == 0
    print("PASS the first jet spans the volume and all three extra central cubes", flush=True)


def verify_clifford_limit(cubic):
    x, y, z, t = range(4)
    u, v, w = s.symbols("U_x U_y U_z")
    slopes = {AX:(Q+1)*u, AY:(Q+1)*v, AZ:(Q+1)*w}
    specialised = {word: s.cancel(value.subs(slopes, simultaneous=True)).subs(Q,-1)
                   for word, value in cubic.items()}
    assert s.cancel(specialised.pop((t,y,z))-u*PY*PZ) == 0
    assert s.cancel(specialised.pop((t,z,y))-u*PY*PZ) == 0
    specialised[t,x,x] += u*PRODUCT
    specialised[t,t,t] = u*PY*PZ*BX
    volume = {(z,y,x):2, (x,x,x):-PX, (y,y,y):PY, (z,z,z):-PZ,
              (t,t,x):-BX, (t,t,y):BY, (t,t,z):-BZ,
              (t,x,x):u, (t,y,y):v, (t,z,z):w}
    expected = {word: (1+PRODUCT)*value for word, value in volume.items()}
    expected[t,t,t] = u*PY*PZ*BX
    assert all(s.cancel(specialised.get(word,0)-expected.get(word,0)) == 0
               for word in specialised.keys() | expected.keys())
    print("PASS the full Clifford pencil is obtained when q approaches -1", flush=True)
    return expected


def verify_commutative_jet(cubic):
    x, y, z, t = range(4)
    origin = dict.fromkeys(PARAMETERS, 0) | {Q:1}
    expected = {
        (z,y,x):(Q,3), (x,x,x):(PX,1), (y,y,y):(PY,1), (z,z,z):(PZ,1),
        (t,x,x):(AX,s.Rational(3,2)), (t,y,y):(AY,s.Rational(3,2)),
        (t,z,z):(AZ,s.Rational(3,2)), (t,t,x):(BX,3), (t,t,y):(BY,3), (t,t,z):(BZ,3),
    }
    assert all(not s.cancel(value.subs(origin)) for value in cubic.values())
    for word, value in cubic.items():
        for variable in PARAMETERS:
            derivative = s.cancel(value.diff(variable).subs(origin))
            term = expected.get(word)
            assert derivative == (term[1] if term is not None and term[0] == variable else 0)
    print("PASS the commutative first jet spans the normalized cubic coefficients", flush=True)


def main():
    cubic = central_polynomial()
    verify_central(cubic)
    verify_first_jet(cubic)
    clifford = verify_clifford_limit(cubic)
    verify_commutative_jet(cubic)
    path = Path(__file__).with_name("cubic_CY_three_alpha_triangle_smoothing_certificate.json")
    path.write_text(json.dumps({"regular_centre": {"".join("xyzt"[i] for i in word): str(s.factor(co))
                                                   for word, co in cubic.items()},
                                "volume_parameter": "q^3-1", "pure_square_parameters": list(map(str,PURE)),
                                "commutative_first_jet": ["3", "1", "3/2", "3"],
                                "clifford_limit": {"".join("xyzt"[i] for i in word): str(co)
                                                   for word,co in clifford.items()}},
                               indent=2)+"\n")


if __name__ == "__main__":
    main()
