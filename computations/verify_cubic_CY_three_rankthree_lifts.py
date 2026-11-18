"""Central lifts and factorizations in the three exceptional pencils."""
from itertools import product
from pathlib import Path
import json

import sympy as s

from verify_cubic_CY_one_segre_cross import PivotAlgebra
from verify_cubic_CY_one_segre_square import Q, comm
from verify_cubic_CY_three_rankthree_quotient import eta, fourpoint, zero_drop


def check(name, quotient, central_cubic, linear_factor):
    field = s.QQ.frac_field(eta) if quotient.has(eta) else s.QQ
    inverse_words = [4*(i % 4)+i//4 for i in range(16)]
    symmetric = (quotient+quotient.extract(inverse_words, range(8)))/2
    indices = symmetric.rref()[1]
    assert len(indices) == 5
    symmetric = symmetric.extract(range(16), indices).applyfunc(s.cancel)
    source = s.Matrix.hstack(comm(0, 1), comm(2, 3), comm(0, 3)-comm(1, 2), symmetric)
    relations = [
        {divmod(i, 4): field.from_sympy(source[i, j])
         for i in range(16) if source[i, j]}
        for j in range(8)
    ]
    algebra = PivotAlgebra(field, 4, relations, [0]*4)
    algebra.pivot_product = field.one
    algebra.build(2)
    assert len(algebra.basis[2]) == 8

    def change(target, source, multiplier):
        algebra.addto(target, source, multiplier)

    def index(word):
        result = 0
        for i in word:
            result = 4*result+i
        return result

    # Track the contribution of each symmetric relation to C_2 when
    # the central quadratic coefficients are varied.
    active = []
    for length in range(3):
        for prefix in product(range(4), repeat=length):
            for suffix in product(range(4), repeat=2-length):
                for j, relation in enumerate(relations):
                    row = {index(prefix+w+suffix): c for w, c in relation.items()}
                    marks = ({(j-3)*8+i: c for i, c in algebra.word(prefix+suffix).items()}
                             if j >= 3 else {})
                    active.append((row, marks))
    insertion_pivots = {}
    while active:
        row, marks = active.pop(min(range(len(active)), key=lambda i: len(active[i][0])))
        column = min(row)
        pivot = row[column]
        row = {i: x/pivot for i, x in row.items()}
        marks = {i: x/pivot for i, x in marks.items()}
        insertion_pivots[column] = (row, marks)
        remaining = []
        for other, other_marks in active:
            if column in other:
                multiplier = -other[column]
                change(other, row, multiplier)
                change(other_marks, marks, multiplier)
            if other:
                remaining.append((other, other_marks))
        active = remaining
    assert len(insertion_pivots) == 240

    equations = [{} for _ in range(32)]
    for gen in range(4):
        commutator = {}
        for w, scalar in central_cubic.items():
            coefficient = field.from_sympy(s.sympify(scalar))
            change(commutator, {index((gen,)+w): coefficient}, field.one)
            change(commutator, {index(w+(gen,)): coefficient}, -field.one)
        correction_directions = {}
        for column, (row, marks) in sorted(insertion_pivots.items()):
            if column in commutator:
                multiplier = commutator[column]
                change(commutator, row, -multiplier)
                change(correction_directions, marks, multiplier)
        assert not commutator
        for direction, coefficient in correction_directions.items():
            equations[8*gen+direction % 8][direction//8] = coefficient
        for j in range(4):
            correction = algebra.word((gen, j))
            change(correction, algebra.word((j, gen)), -field.one)
            for output, coefficient in correction.items():
                equations[8*gen+output][5+j] = coefficient
    algebra.pivot_product = field.one
    rows = algebra.echelon(equations)
    correction_rows = [{i: c for i, c in row.items() if i >= 5} for row in equations]
    assert len(rows) == len(algebra.echelon(correction_rows)) == 4
    # Pivot first on the four correction variables, then back-substitute.
    reordered = [{i+4 if i < 5 else i-5: c for i, c in row.items()}
                 for row in equations]
    triangular = algebra.echelon(reordered)
    assert set(triangular) == set(range(4))
    corrections = [{} for _ in range(4)]
    for pivot, row in reversed(list(triangular.items())):
        answer = {i-4: -c for i, c in row.items() if i >= 4}
        for column, coefficient in row.items():
            if pivot < column < 4:
                change(answer, corrections[column], -coefficient)
        corrections[pivot] = answer

    # The factorization holds with only the three original commutators.
    commutator_algebra = PivotAlgebra(field, 4, relations[:3], [0]*4)
    commutator_algebra.pivot_product = field.one
    for degree in (2, 3):
        commutator_algebra.build(degree)
    difference = {}
    for word, c in central_cubic.items():
        change(difference, commutator_algebra.word(word), field.from_sympy(s.sympify(c)))
    for var, correction in enumerate(corrections):
        for mark, coefficient in correction.items():
            for word, c in relations[3+mark].items():
                change(difference, commutator_algebra.word(word+(var,)), coefficient*c)
    for var, c in enumerate(linear_factor):
        coefficient = field.from_sympy(s.sympify(c))
        change(difference, commutator_algebra.word((var, 3, 0)), -coefficient)
        change(difference, commutator_algebra.word((var, 2, 1)), coefficient)
    assert not difference
    print("PASS", name, "all five lift directions and exact factorization")
    return {
        "chart": name,
        "linear_factor_times_da_minus_cb": [str(s.factor(c)) for c in linear_factor],
        "lift_rows": [{str(i): str(field.to_sympy(c)) for i, c in row.items()} for row in rows.values()],
        "symmetric_relations": [{str(i): str(symmetric[i, j]) for i in range(16) if symmetric[i, j]}
                                for j in range(5)],
    }


def main():
    mu = s.cancel((-1-2*eta)/(eta*eta-1))
    lam = s.cancel(2*mu**3-3*mu**2+2*mu+2*mu*(mu-1)*(1+eta*mu))
    scale = -(eta-1)**2/(6*(eta+2)**2*(2*eta+1)**2)
    fourpoint_factor = [
        scale*c for c in (3*(eta-1)**2*(eta+1), (eta-1)**2*(2*eta+1),
                          (eta-1)*(2*eta+1)**2, -3*(2*eta+1)**2)
    ]
    result = [
        check("double_at_2", zero_drop(s.diag(1, -Q(1, 2), 1)), {(2, 2, 2): 1},
              [0, 1, -1, 0]),
        check("J21_at_one_quarter",
              zero_drop(s.Matrix([[1, -Q(3, 4), 0], [0, Q(1, 4), 0], [0, 0, Q(1, 4)]])),
              {(2, 2, 2): 1}, [Q(3, 8), Q(1, 4), Q(1, 2), 0]),
        check("fourpoint_B", fourpoint(lam, mu),
              {(3, 2, 2): 1, (2, 2, 2): (1-eta)/3}, fourpoint_factor),
    ]
    Path(__file__).with_name("cubic_CY_three_rankthree_lifts_certificate.json").write_text(
        json.dumps(result, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
