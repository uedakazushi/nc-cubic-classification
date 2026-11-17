"""Exact original relation and centre computation for the isolated VT presentation."""
import sympy as s

from verify_cubic_as4_four_simple_remaining import centre
from verify_cubic_as4_four_simple import IX, W2

Q = s.Rational
words = s.eye(16)


def word(i, j):
    return words[:, IX[i, j]]


def sym(i, j):
    return (word(i, j) + word(j, i)) / 2


U = s.Matrix.hstack(word(0, 0), sym(0, 1), word(1, 1),
                    sym(0, 2) + sym(1, 3))
K = s.Matrix.hstack(*(word(i, j) - word(j, i)
                     for i, j in W2 if i < j))
A = s.zeros(4)
A[0, 2] = A[2, 0] = Q(1, 2)
A[1, 1] = -1
B = s.Matrix([[0, Q(3, 4), -Q(9, 16), -Q(1, 3), Q(1, 4), 0],
              [0, Q(1, 3), Q(1, 2), 0, -Q(1, 3), 0],
              [0, 0, Q(1, 3), 0, 0, 0],
              [1, 0, 0, 0, 0, 0]])
C, J = s.zeros(6), s.zeros(6)
C[0, 0] = Q(1, 4)
for i, j, value in [(0, 5, 1), (1, 4, -1), (2, 3, 1)]:
    J[i, j] = J[j, i] = value
E = U.row_join(K)
top = E * A.row_join(B).col_join(B.T.row_join(C - Q(2, 9) * J)) * E.T
relations = s.Matrix.hstack(*top.columnspace())
assert relations.cols == 6
rows, determinant, _, _ = centre(relations, s.QQ)
assert len(rows) == 20 and determinant != 0
print("PASS isolated VT: centre rank 20, determinant", determinant)
