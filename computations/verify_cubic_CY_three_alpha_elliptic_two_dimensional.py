"""A non-torsion elliptic cut with a bad two-dimensional simple and no characters."""
import json
from pathlib import Path

import sympy as s
from sympy.polys.matrices import DomainMatrix

from cubic_flint_rational_function import RationalFunctionField
from cubic_sparse_hilbert import SparseGradedAlgebra

S = s.Symbol("s")


def presentation():
    x, y, z, t = range(4)
    slopes, constants = (S,S,-1/S), (3,3,-3*S**2)
    relations = []
    for i in range(3):
        j, k = (i+1)%3, (i+2)%3
        relations.append({(j,k): 1, (k,j): 2, (i,i): 3, (t,i): -slopes[i], (t,t): -constants[i]})
    cubic = {
        (y,y,y): 1, (y,z,x): s.Rational(19,78), (z,y,x): -s.Rational(2,3), (z,z,z): -s.Rational(19,26),
        (t,y,x): -3/(13*S), (t,y,y): -S/26, (t,y,z): -25*S/117,
        (t,z,x): -3*S/26, (t,z,y): -23*S/117, (t,z,z): -23/(26*S),
        (t,t,x): -2*S**2/117, (t,t,y): -(3*S**2+26)/26,
        (t,t,z): -(19*S**4+6)/(26*S**2), (t,t,t): 5*S/78,
    }
    return relations, cubic


def check_central(relations, cubic):
    field = RationalFunctionField((S,))
    source = [*relations, *({(3,i):1, (i,3):-1} for i in range(3))]
    relations = [{word: field.from_sympy(value) for word, value in f.items()} for f in source]
    algebra = SparseGradedAlgebra(field, 4, relations, [0]*4)
    algebra.build(4)
    assert [len(algebra.basis[i]) for i in (2,3,4)] == [10,20,35]
    for gen in range(4):
        residual = {}
        for word, value in cubic.items():
            coefficient = field.from_sympy(value)
            algebra.addto(residual, algebra.word(word+(gen,)), coefficient)
            algebra.addto(residual, algebra.word((gen,)+word), -coefficient)
        assert not residual


def check_matrix_simple(relations, cubic):
    x = s.Matrix([[0,1],[1,0]])
    y = s.diag(1,-1)
    values = (x, y, S*x*y, s.eye(2))
    assert s.Matrix.hstack(*(m.reshape(4,1) for m in values)).rank() == 4

    def evaluate(word, position=None):
        result = s.eye(2)
        for index, letter in enumerate(word):
            result *= (deltas if index == position else values)[letter]
        return result

    variables = s.symbols("v0:12")
    deltas = tuple(s.Matrix(2,2,variables[4*i:4*i+4]) for i in range(3))+(s.zeros(2),)
    equations = []
    for polynomial in (*relations, cubic):
        assert not any(s.cancel(v) for v in sum((c*evaluate(word) for word,c in polynomial.items()), s.zeros(2)))
        derivative = s.zeros(2)
        for word, coefficient in polynomial.items():
            for position in range(len(word)):
                derivative += coefficient*evaluate(word, position)
        equations.extend(derivative)
    jacobian = s.Matrix([[s.cancel(s.expand(v).coeff(parameter)) for parameter in variables] for v in equations])
    number = s.QQ.algebraic_field(s.sqrt(5))
    specialized = jacobian.subs(S, 3/s.sqrt(5)).applyfunc(s.simplify)
    rank = DomainMatrix.from_Matrix(specialized).convert_to(number).rank()
    assert rank == 8
    print("PASS simple two-dimensional module with one-dimensional self-Ext^1", flush=True)
    return rank


def check_no_characters(relations, cubic):
    variables = s.symbols("x y z")
    values = (*variables, 1)
    raw = [s.cancel(sum(coefficient*s.prod(values[i] for i in word)
                       for word, coefficient in polynomial.items()))
           for polynomial in (*relations, cubic)]
    ideal = [v.as_numer_denom()[0] for v in raw]+[5*S**2-9]
    basis = s.groebner(ideal, *variables, S, domain=s.QQ)
    assert [f.as_expr() for f in basis.polys] == [1]
    print("PASS the scalar representation scheme is empty on this cut", flush=True)


def main():
    relations, cubic = presentation()
    check_central(relations, cubic)
    rank = check_matrix_simple(relations, cubic)
    check_no_characters(relations, cubic)
    certificate = {
        "s_polynomial": "5*s^2-9",
        "central_cut": {"".join("xyzt"[i] for i in word): str(value) for word,value in cubic.items()},
        "matrix_tangent_rank": rank,
        "scalar_ideal_groebner_basis": [1],
    }
    Path(__file__).with_name("cubic_CY_three_alpha_elliptic_two_dimensional_certificate.json").write_text(
        json.dumps(certificate, indent=2)+"\n")


if __name__ == "__main__":
    main()
