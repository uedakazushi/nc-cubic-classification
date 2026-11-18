"""Central cut and character obstruction for a non-split non-torsion elliptic family."""
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctionField
from cubic_sparse_hilbert import SparseGradedAlgebra


def elliptic_relations(field, a, b):
    x, y, z, t = range(4)
    one = field.one
    two, three = field.from_sympy(2), field.from_sympy(3)
    left = {
        x: {(y,z): one, (z,y): two, (x,x): three, (t,x): -a, (t,y): -a},
        y: {(z,x): one, (x,z): two, (y,y): three, (t,x): -a, (t,y): -a},
        z: {(x,y): one, (y,x): two, (z,z): three, (t,z): -b},
    }
    return [*left.values(), *({(t,i): one, (i,t): -one} for i in (x,y,z))]


def cubic(a, b):
    x, y, z, t = range(4)
    return {
        (y,y,y): 13, (y,z,x): s.Rational(19,6), (z,y,x): -s.Rational(26,3),
        (z,z,z): -s.Rational(19,2),
        (t,y,x): -25*a/6+3*b, (t,y,y): -a/2, (t,y,z): -25*a/9,
        (t,z,x): -3*a/2, (t,z,y): -23*a/9, (t,z,z): (-27*a+23*b)/2,
        (t,t,x): -31*a*a/18+a*b, (t,t,y): -31*a*a/18+a*b, (t,t,z): 11*a*b/2-3*b*b,
    }


def check_central():
    a, b = s.symbols("a b")
    field = RationalFunctionField((a,b))
    relations = elliptic_relations(field, field.from_sympy(a), field.from_sympy(b))
    algebra = SparseGradedAlgebra(field, 4, relations, [0]*4)
    algebra.build(4)
    assert [len(algebra.basis[i]) for i in (2,3,4)] == [10,20,35]
    coefficients = cubic(a,b)
    for generator in range(4):
        commutator = {}
        for word, value in coefficients.items():
            scalar = field.from_sympy(value)
            algebra.addto(commutator, algebra.word(word+(generator,)), scalar)
            algebra.addto(commutator, algebra.word((generator,)+word), -scalar)
        assert not commutator
    top = {word: value for word, value in coefficients.items() if 3 not in word}
    homogeneous = SparseGradedAlgebra(field, 4,
        elliptic_relations(field, field.zero, field.zero), [0]*4)
    homogeneous.build(3)
    image = {}
    for word, value in top.items():
        homogeneous.addto(image, homogeneous.word(word), field.from_sympy(value))
    assert image and all(3 not in homogeneous.basis[3][index] for index in image)
    hessian = s.Matrix([[a,a,0],[a,a,0],[0,0,b]])
    jacobian = hessian.col_join(s.Matrix([[coefficients[3,3,i] for i in range(3)]]))
    assert jacobian.rank() == 2 and jacobian.nullspace()[0] == s.Matrix([-1,1,0])
    print("PASS exact central lift and one-dimensional tangent at the affine character", flush=True)


def check_reduction():
    counts = {}
    for prime in (5,17):
        assert (6**3-27)%prime
        affine = sum((x**3+y**3+1-6*x*y)%prime == 0 for x in range(prime) for y in range(prime))
        infinity = sum((x**3+1)%prime == 0 for x in range(prime))
        counts[prime] = affine+infinity
    assert counts == {5: 9, 17: 21}
    print("PASS good reduction counts for the non-torsion boundary", flush=True)
    return counts


def main():
    check_central()
    result = {"reduction_counts": check_reduction(),
              "central_lift": {"".join("xyzt"[i] for i in word): str(value)
                               for word, value in cubic(*s.symbols("a b")).items()},
              "affine_character": {"point": [0,0,0], "Jacobian_rank": 2}}
    Path(__file__).with_name("cubic_CY_three_alpha_elliptic_character_certificate.json").write_text(
        json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
