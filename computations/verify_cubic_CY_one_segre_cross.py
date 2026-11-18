"""Exact central-cubic exclusion for the two crossed two-square charts."""
import json
from pathlib import Path

import sympy as s
from flint import fmpq

from cubic_gaussian_rational_function import CTX, F
from cubic_sparse_hilbert import SparseGradedAlgebra
from verify_cubic_CY_one_segre_square import Q, all_values, comm, h, word

p = s.Symbol("p")


def source(middle):
    aa, bb, cc, dd, ee = middle
    pairs = [(0, 2), (0, 3), (1, 2), (1, 3)]
    symmetric = [(word(i, j)+word(j, i))/2 for i, j in pairs]
    U = s.Matrix.hstack(*symmetric, word(0, 0)+word(2, 2))
    K = s.Matrix.hstack(*(comm(i, j) for i in range(4) for j in range(i+1, 4)))
    A = s.zeros(4)
    A[0, 3] = A[3, 0] = Q(1, 2)
    A[1, 2] = A[2, 1] = -Q(1, 2)
    B = s.Matrix([[0, aa, 2-bb, bb-2, cc, 0],
                  [-Q(1, 4), -bb, -cc, cc, -dd, 0],
                  [0, bb, cc, -cc, dd, Q(1, 4)],
                  [0, cc, -dd, dd, ee, 0],
                  [1, 8, 0, 0, Q(1, 8), 1]])
    C, J = s.zeros(6), s.zeros(6)
    C[1, 4] = C[4, 1] = Q(1, 8)
    C[2, 3] = C[3, 2] = -Q(1, 8)
    for i, j, value in [(0, 5, 1), (1, 4, -1), (2, 3, 1)]:
        J[i, j] = J[j, i] = value
    C += J/8
    D = C - B[:4, :].T*A.inv()*B[:4, :]
    E = U.row_join(K)
    block = s.diag(A, 0).row_join(B).col_join(B.T.row_join(C))
    coordinates = s.zeros(11, 6)
    coordinates[:4, :4] = s.eye(4)
    coordinates[5:, :4] = B[:4, :].T*A.inv()
    coordinates[5:, 4] = B[4, :].T
    coordinates[4, 5] = 1
    coordinates[5:, 5] = D[:, 0]
    minor = coordinates[:6, :]
    assert minor.det() == -1
    difference = block-coordinates*minor.inv()*block[:6, :]
    assert difference.applyfunc(s.cancel) == s.zeros(11)
    return (E*coordinates).applyfunc(s.cancel)


class Coefficients:
    """Use the rational subfield of the existing FLINT fraction arithmetic."""
    zero = F(0)
    one = F(1)

    @staticmethod
    def from_sympy(value):
        numerator, denominator = s.cancel(value).as_numer_denom()

        def polynomial(expr):
            terms = s.Poly(expr, p, h, domain=s.QQ).terms()
            return CTX.from_dict({(i, 0, j): fmpq(int(c.p), int(c.q))
                                  for (i, j), c in terms if c})

        return F(polynomial(numerator), polynomial(denominator))


class PivotAlgebra(SparseGradedAlgebra):
    """Retain exact centre pivots to compute a nonzero maximal minor."""
    def echelon(self, rows):
        active = [dict(row) for row in rows if row]
        reduced = {}
        while active:
            row = active.pop(min(range(len(active)), key=lambda i: len(active[i])))
            column = min(row)
            pivot = row[column]
            self.pivot_product *= pivot
            reduced[column] = {key: value/pivot for key, value in row.items()}
            remaining = []
            for other in active:
                if column in other:
                    self.addto(other, reduced[column], -other[column])
                if other:
                    remaining.append(other)
            active = remaining
        return reduced


def factor_set(polynomials):
    for polynomial in polynomials:
        if polynomial.total_degree() <= 0:
            continue
        for factor, _ in polynomial.factor()[1]:
            terms = { (i, j): Q(str(co))
                      for (i, imaginary, j), co in factor.to_dict().items()
                      if not imaginary }
            assert len(terms) == len(factor.to_dict())
            yield s.Poly.from_dict(terms, (p, h), domain=s.QQ).monic().as_expr()


def centre_calculation(relations, permutation, field, convert, dimensions=(10, 20, 35)):
    relations = relations.applyfunc(s.cancel)
    ordered = []
    for j in range(relations.cols):
        column = {}
        for i in range(16):
            if relations[i, j]:
                a, b = divmod(i, 4)
                coefficient = convert(relations[i, j])
                if coefficient:
                    column[permutation[a], permutation[b]] = coefficient
        ordered.append(column)
    algebra = PivotAlgebra(field, 4, ordered, [0]*4)
    algebra.pivot_product = field.one
    algebra.build(4)
    assert tuple(len(algebra.basis[n]) for n in (2, 3, 4)) == dimensions
    algebra.pivot_product = field.one
    degree_four = dimensions[-1]
    source_rows = [{} for _ in range(4*degree_four)]
    for column, cubic in enumerate(algebra.basis[3]):
        for gen in range(4):
            commutator = algebra.word(cubic+(gen,))
            algebra.addto(commutator, algebra.word((gen,)+cubic), -field.one)
            for row, coefficient in commutator.items():
                source_rows[degree_four*gen+row][column] = coefficient
    rank = len(algebra.echelon(source_rows))
    return algebra, rank


def rank_chart(relations, permutation):
    algebra, rank = centre_calculation(relations, permutation, Coefficients,
                                       Coefficients.from_sympy)
    denominator_polynomials = {str(value.d): value.d
                               for n in (2, 3, 4)
                               for row in algebra.right[n].values()
                               for value in row.values()}
    determinant = algebra.pivot_product
    exceptions = set(factor_set([determinant.n, determinant.d,
                                 *denominator_polynomials.values()]))
    return rank, exceptions


def finite_source():
    v = h/8
    aa = (p+2)/v
    return source((aa, aa*v, 2*v-aa*v*v, 2*v*v-aa*v**3,
                   v/32-2*v**3+aa*v**4))


def main():
    infinity = all_values("infinity", source((0, 2, 0, Q(1, 32), h)),
                          [128*h-1, 128*h+1])
    records = [infinity]
    print("PASS infinity", flush=True)

    relations = finite_source()
    units = [h, p*(h-1)**2+2, p*(h+1)**2+2]
    normalized_units = {s.Poly(unit, p, h).monic().as_expr() for unit in units}
    rank, exceptions = rank_chart(relations, (0, 2, 1, 3))
    assert rank == 20
    curves = exceptions-normalized_units
    assert curves == {s.expand(value) for value in [p, p+2, (h+1)*p+2,
                      (h+Q(1, 2))*p+1, (h-1)*p-2]}, curves
    for curve in sorted(curves, key=str):
        ratio, = s.solve(curve, p)
        coefficient = s.Poly(curve, p).coeff_monomial(p)
        assert s.gcd(coefficient, s.Poly(curve, p).coeff_monomial(1)) == 1
        new_units = set()
        for unit in units:
            numerator, denominator = s.cancel(unit.subs(p, ratio)).as_numer_denom()
            assert numerator
            new_units.update([numerator, denominator])
        new_units.add(coefficient)
        RR = relations.subs(p, ratio, simultaneous=True).applyfunc(s.cancel)
        rank, exceptional = rank_chart(RR, (0, 2, 1, 3))
        print("curve", curve, rank, sorted(map(str, exceptional)), flush=True)
        assert rank == 20
        forbidden = {term for unit in new_units
                     for term, _ in s.factor_list(unit, h)[1]}
        forbidden = {s.Poly(term, h).monic().as_expr() for term in forbidden}
        roots = []
        for term in sorted(exceptional-forbidden, key=str):
            polynomial = s.Poly(term, h, domain=s.QQ)
            assert polynomial.is_irreducible
            root = s.CRootOf(polynomial, 0)
            field = s.QQ if root.is_Rational else s.QQ.algebraic_field(root)
            alpha = field.from_sympy(root) if root.is_Rational else field.unit

            def evaluate(value):
                num, den = s.cancel(value).as_numer_denom()

                def at(expr):
                    answer = field.zero
                    for coefficient in s.Poly(expr, h, domain=s.QQ).all_coeffs():
                        answer = answer*alpha+field.from_sympy(coefficient)
                    return answer

                return at(num)/at(den)

            result, rank = centre_calculation(RR, (0, 2, 1, 3), field, evaluate)
            assert rank == 20, (curve, term, rank)
            roots.append({"factor": str(term), "degree": polynomial.degree(),
                          "minor_up_to_sign": str(result.pivot_product)})
            print("PASS exceptional", curve, term, flush=True)
        records.append({"curve": str(curve), "ratio": str(ratio),
                        "exceptions": sorted(map(str, exceptional)), "roots": roots})
    Path(__file__).with_name("cubic_CY_one_segre_cross_certificate.json").write_text(
        json.dumps({"finite_open_complement": sorted(map(str, curves)),
                    "rank": 20, "checks": records}, indent=2) + "\n"
    )
    print("PASS both crossed two-square charts at every allowed value", flush=True)



if __name__ == "__main__":
    main()
