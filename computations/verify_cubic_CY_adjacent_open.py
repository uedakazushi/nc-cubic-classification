"""Independent exact Hilbert obstruction for the two AO2 presentations."""
import sympy as s

from cubic_sparse_hilbert import SparseGradedAlgebra
from verify_cubic_as4_four_simple import W2, source_matrix

lam = s.Symbol("lambda")
field = s.QQ.frac_field(lam)
for sign in (-1, 1):
    relations, _ = source_matrix(lam, {
        0: 1, 1: 1, 2: 1, 4: 1, 5: 1,
        8: sign * (lam + 1) / 4,
        10: -sign * lam / 4, 12: sign * lam / 4, 15: s.Rational(sign, 4),
    })
    columns = []
    for column in range(6):
        coefficients = {}
        for row, word in enumerate(W2):
            value = s.cancel(relations[row, column])
            denominator = value.as_numer_denom()[1]
            assert all(factor in (lam, lam + 1)
                       for factor, _ in s.factor_list(denominator)[1])
            if value:
                coefficients[word] = field.from_sympy(value)
        columns.append(coefficients)
    algebra = SparseGradedAlgebra(field, 4, columns, [0] * 4)
    algebra.build(3)
    assert len(algebra.basis[3]) >= 21
print("PASS both AO2 signs, all allowed specializations by relation rank")
