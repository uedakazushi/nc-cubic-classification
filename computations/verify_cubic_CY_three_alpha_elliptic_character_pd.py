"""Verify the periodic resolution and the scalar-character projective dimension."""
import json
from itertools import permutations, product
from pathlib import Path

import sympy as s

from verify_cubic_CY_three_alpha_elliptic_character_boundary import (
    A, B, C, D, E, F, FIELD, PARAMETERS, Q, R, SparseGradedAlgebra, central_lift,
)

ZERO, ONE = FIELD.zero, FIELD.one
GENS = tuple((i,) for i in range(4))
HESSIAN = s.Matrix([[A,B,D], [B,C,E], [D,E,F]])
NAMES = {str(value): value for value in PARAMETERS}


def expression(value):
    numerator, denominator = [s.sympify(str(f).replace("^", "**"), locals=NAMES) for f in (value.n, value.d)]
    return s.cancel(numerator/denominator)


class AugmentationResolution:
    """Four free terms for the character at the affine origin, homogenized by t."""

    def __init__(self):
        q, r = [FIELD.from_sympy(value) for value in (Q, R)]
        coefficients = [[FIELD.from_sympy(HESSIAN[i,j]) for j in range(3)] for i in range(3)]
        relations = []
        self.d1 = [[{word: ONE} for word in GENS[:3]]]
        self.d2 = [[{} for _ in range(3)] for _ in range(3)]
        self.d3 = [[{word: ONE}] for word in GENS[:3]]
        for i in range(3):
            j, k = (i+1)%3, (i+2)%3
            polynomial = {(j,k): ONE, (k,j): q, (i,i): r}
            polynomial.update({(col,3): -value for col, value in enumerate(coefficients[i])})
            relations.extend([polynomial, {(3,i): ONE, (i,3): -ONE}])
            for (left, right), value in polynomial.items():
                self.d2[left][i][(right,)] = value
        self.algebra = SparseGradedAlgebra(FIELD, 4, relations, [0]*4)
        self.algebra.build(4)

    def multiply(self, left, right, degree):
        result = {}
        for left_word, a in left.items():
            for right_word, b in right.items():
                self.algebra.addto(result, self.algebra.word(left_word+right_word), a*b)
        return {self.algebra.basis[degree][i]: value for i, value in result.items()}

    def matrix_product(self, left, right, degree):
        result = [[{} for _ in right[0]] for _ in left]
        for i, j, k in product(range(len(left)), range(len(right[0])), range(len(right))):
            entry = self.multiply(left[i][k], right[k][j], degree)
            self.algebra.addto(result[i][j], entry, ONE)
        return result

    def add_matrix(self, target, source, scalar):
        for i, j in product(range(len(target)), range(len(target[0]))):
            self.algebra.addto(target[i][j], source[i][j], scalar)
        return target

    def solve_on_right(self, left, right, degree):
        basis, next_basis = self.algebra.basis[degree], self.algebra.basis[degree+1]
        rows, cols, targets = len(left), len(left[0]), len(right[0])
        coefficients = [[{} for _ in next_basis] for _ in left]
        locations = {word: i for i, word in enumerate(next_basis)}
        for i, k, b in product(range(rows), range(cols), range(len(basis))):
            entry = self.multiply(left[i][k], {basis[b]: ONE}, degree+1)
            for word, value in entry.items():
                coefficients[i][locations[word]][k*len(basis)+b] = value
        result = [[{} for _ in range(targets)] for _ in range(cols)]
        rhs_index = cols*len(basis)
        for j in range(targets):
            equations = []
            for i, k in product(range(rows), range(len(next_basis))):
                row = dict(coefficients[i][k])
                value = right[i][j].get(next_basis[k], ZERO)
                if value:
                    row[rhs_index] = value
                if row:
                    equations.append(row)
            pivots = self.algebra.echelon(equations)
            assert rhs_index not in pivots
            solution = {rhs_index: -ONE}
            for k, row in sorted(pivots.items(), reverse=True):
                value = -sum((v*solution[i] for i, v in row.items() if i != k and i in solution), ZERO)
                if value:
                    solution[k] = value
            del solution[rhs_index]
            for k, value in solution.items():
                i, b = divmod(k, len(basis))
                result[i][j][basis[b]] = value
        check = self.add_matrix(self.matrix_product(left, result, degree+1), right, -ONE)
        assert not any(entry for row in check for entry in row)
        return result


def extract_constants():
    complex_ = AugmentationResolution()
    d1, d2, d3 = complex_.d1, complex_.d2, complex_.d3
    cubic = {tuple("xyzt".index(v) for v in word): FIELD.from_sympy(value)
             for word, value in central_lift().items()}
    reduced = complex_.multiply(cubic, {(): ONE}, 3)

    def multiplication_by_cubic(size):
        return [[dict(reduced) if i == j else {} for j in range(size)] for i in range(size)]

    s0 = [[{}] for _ in range(3)]
    for word, value in cubic.items():
        normal = tuple(letter for letter in word if letter != 3)+(3,)*word.count(3)
        complex_.algebra.addto(s0[normal[0]][0], {normal[1:]: value}, ONE)
    assert not complex_.add_matrix(complex_.matrix_product(d1, s0, 3), [[reduced]], -ONE)[0][0]
    first = complex_.add_matrix(multiplication_by_cubic(3), complex_.matrix_product(s0, d1, 3), -ONE)
    s1 = complex_.solve_on_right(d2, first, 2)
    second = complex_.add_matrix(multiplication_by_cubic(3), complex_.matrix_product(s1, d2, 3), -ONE)
    s2 = complex_.solve_on_right(d3, second, 2)
    assert not complex_.add_matrix(complex_.matrix_product(s2, d3, 3), [[reduced]], -ONE)[0][0]
    square = complex_.matrix_product(s1, s0, 4)
    minus_square = [[{word: -co for word, co in row[0].items()}] for row in square]
    twice = complex_.solve_on_right(d3, minus_square, 3)
    check = complex_.add_matrix(complex_.matrix_product(s2, s1, 4),
                                complex_.matrix_product(twice, d1, 4), ONE)
    assert not any(entry for row in check for entry in row)

    for matrix in (s0, s1, s2, twice):
        for row in matrix:
            for entry in row:
                for coefficient in entry.values():
                    for factor, _ in coefficient.d.factor()[1]:
                        factor = s.sympify(str(factor).replace("^", "**"), locals=NAMES)
                        assert s.denom(s.cancel(R*(Q-1)/factor)) == 1
    assert all((3,3) not in entry for row in s1 for entry in row)
    upper = [expression(s2[0][j].get((3,3), ZERO)) for j in range(3)]
    lower = [expression(s0[i][0].get((3,3), ZERO)) for i in range(3)]
    corner = expression(twice[0][0].get((3,3,3), ZERO))
    print("PASS homotopies regular on the full elliptic domain and odd differential zero", flush=True)
    return s.Matrix([upper+[corner]]+[
        [-HESSIAN[i,j] for j in range(3)]+[lower[i]] for i in range(3)
    ])


def character_cubic(matrix):
    a, b, c, d, e, f = (matrix[0,0], matrix[0,1], matrix[1,1], matrix[0,2], matrix[1,2], matrix[2,2])
    g, h = Q*R, 1+Q**3+R**3
    offset = Q*((Q**2-Q+1)**2+(Q+1)*R**3)
    return (g**2*(a**3+c**3+f**3-b**3-d**3-e**3+3*(a*b*c+a*d*f+c*e*f))
            -g*h*(a**2*e+c**2*d+f**2*b+a*b*d+b*c*e+d*e*f)
            +h**2*b*d*e-offset*matrix.det())


def main():
    differential = extract_constants()
    determinant = differential.det(method="domain-ge")
    expected = character_cubic(HESSIAN.adjugate())
    assert s.cancel((Q-1)**2*determinant-expected) == 0
    print("PASS the projective-dimension determinant is the cubic of the adjugate", flush=True)
    path = Path(__file__).with_name("cubic_CY_three_alpha_elliptic_character_pd_certificate.json")
    path.write_text(json.dumps({"even_differential": [[str(differential[i,j]) for j in range(4)] for i in range(4)],
                                "odd_differential": "zero", "determinant_denominator": "(q - 1)^2"},
                               indent=2)+"\n")


if __name__ == "__main__":
    main()
