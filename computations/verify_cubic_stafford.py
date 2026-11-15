#!/usr/bin/env python3
"""Exact Frobenius and W1 witnesses for Stafford's three elliptic families.

All-degree regularity is an external input (Davies, Theorem 6.1.10).
Ranks at this point imply generic exclusions, not exclusions at every point.
"""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_pym_generic import words, relation_rows, quotient_projection


def nakayama(rels):
    r = S.Matrix([[f.get(w, 0) for w in words(2)] for f in rels])
    perpendicular = r.nullspace()
    assert len(perpendicular) == 10
    dual = [{w: v[j] for j, w in enumerate(words(2)) if v[j]}
            for v in perpendicular]
    m3 = DomainMatrix.from_Matrix(relation_rows(dual, 3)).convert_to(S.QQ)
    _, pivots = m3.rref()
    basis = [w for j, w in enumerate(words(3)) if j not in pivots]
    top = DomainMatrix.from_Matrix(relation_rows(dual, 4)).convert_to(S.QQ).nullspace().to_Matrix()
    assert len(basis) == 4 and top.rows == 1
    phi = dict(zip(words(4), list(top)))
    left = S.Matrix([[phi[(i,) + w] for w in basis] for i in range(4)])
    right = S.Matrix([[phi[w + (i,)] for i in range(4)] for w in basis])
    assert left.det() != 0 and right.det() != 0
    mu_e = (left * right.T.inv()).T
    mu = -mu_e.T.inv()
    return mu, {'dual_dimensions_3_4': [4, 1],
                'left_pairing_determinant': str(left.det()),
                'right_pairing_determinant': str(right.det()),
                'socle_functional': [{'word': list(w), 'coefficient': str(c)}
                                     for w, c in phi.items() if c]}


def main():
    a, b, c = S.Rational(2), S.Rational(3), -S.Rational(5, 7)
    assert a + b + c + a*b*c == 0
    d = S.Rational(4)
    assert d not in [0, -1-b*c, b-1, -1-c]
    fs = []
    for (i, j, k), v in zip([(1, 2, 3), (2, 3, 1), (3, 1, 2)], [a, b, c]):
        fs += [{(0, i): 1, (i, 0): -1, (j, k): -v, (k, j): -v},
               {(0, i): 1, (i, 0): 1, (j, k): -1, (k, j): 1}]
    g1 = {(0, 0): -1, (1, 1): 1, (2, 2): 1, (3, 3): 1}
    g2 = {(1, 1): 1, (2, 2): (1+a)/(1-b), (3, 3): (1-a)/(1+c)}
    q = {w: g1.get(w, 0) + d*g2.get(w, 0) for w in set(g1) | set(g2)}
    families = [('S_infinity', fs[:4]+[g1, g2]),
                ('S_d_1', fs[1:]+[q]), ('S_d_2', fs[:1]+fs[2:]+[q])]
    expected = [[[-1]*4, [-1]*4], [[-1, -1, 1, 1], [-1]*4],
                [[1, 1, -1, -1], [1]*4]]
    degrees = [(0, 0), (1, 0), (0, 1), (1, 1)]
    index4 = {w: j for j, w in enumerate(words(4))}
    results = []
    for f, (label, relations) in enumerate(families):
        for twist in [False, True]:
            rr = [{(i, j): v*(-1)**(degrees[i][0]*degrees[j][1])
                   for (i, j), v in r.items()} for r in relations] if twist else relations
            mu, audit = nakayama(rr)
            signs = expected[f][int(twist)]
            assert mu == S.diag(*signs)
            free3, _, _ = quotient_projection(rr, 3)
            free4, projection4, _ = quotient_projection(rr, 4)
            assert len(free3) == 20 and len(free4) == 35
            matrix = S.zeros(140, 20)
            for col, j in enumerate(free3):
                w = words(3)[j]
                for i in range(4):
                    matrix[35*i:35*(i+1), col] = (
                        projection4[:, index4[w+(i,)]] - signs[i]*projection4[:, index4[(i,)+w]])
            _, rows = DomainMatrix.from_Matrix(matrix.T).convert_to(S.QQ).rref()
            assert len(rows) == 20
            det = DomainMatrix.from_Matrix(matrix[list(rows), :]).convert_to(S.QQ).det()
            assert det != 0
            audit.update(family=label, cocycle_twist=twist, nakayama_diagonal=signs,
                         dimensions_3_4=[20, 35], W1_dimension=0,
                         minor_rows=list(rows), minor_determinant=str(det))
            results.append(audit)
            print('PASS', label, 'cocycle', twist, 'Nakayama', signs, 'W1=0', flush=True)
    cert = {'version': 'classification-v64', 'parameters': ['2', '3', '-5/7'],
            'd': ['1', '4'], 'field': 'QQ', 'witnesses': results,
            'external_input': 'Davies arXiv:1502.06101, (6.1.3)-(6.1.4), Theorem 6.1.10',
            'scope': 'Six exact witnesses. Generic W1 vanishing follows from minors and the paper family argument; exceptional rank-drop loci not classified.'}
    Path(__file__).with_name('cubic_stafford_certificate.json').write_text(json.dumps(cert, indent=2)+'\n')


if __name__ == '__main__':
    main()
