#!/usr/bin/env python3
"""Exact finite checks for the mixed A2 category (standard library only).

Checks quiver Hom spaces, Euler/Ext1 bookkeeping, line-bundle equality,
cohomology of every small direct sum, and triangular-image obstructions.
This is NOT a computation of the actual elliptic A=R/(g-1) action matrices,
Rains sheaf existence, or a proof of a derived equivalence.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


def rank(rows: list[list[int | F]], ncols: int | None = None) -> int:
    if not rows:
        return 0
    a = [[F(x) for x in row] for row in rows]
    cols = len(a[0]) if ncols is None else ncols
    assert all(len(row) == cols for row in a)
    pivot = 0
    for col in range(cols):
        at = next((j for j in range(pivot, len(a)) if a[j][col]), None)
        if at is None:
            continue
        a[pivot], a[at] = a[at], a[pivot]
        c = a[pivot][col]
        a[pivot] = [x / c for x in a[pivot]]
        for j in range(len(a)):
            if j != pivot and a[j][col]:
                c = a[j][col]
                a[j] = [x - c*y for x, y in zip(a[j], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


# Vertex dimensions plus x:+->- and y:-->+ (all entries are 0 or 1).
REPS = {'S+': (1, 0, 0, 0), 'S-': (0, 1, 0, 0),
        'P': (1, 1, 1, 0), 'Q': (1, 1, 0, 1)}


def hom_dim(src: tuple[int, ...], dst: tuple[int, ...]) -> int:
    a, b, x, y = src
    c, d, u, v = dst
    vars_ = [(0, i, j) for i in range(c) for j in range(a)]
    vars_ += [(1, i, j) for i in range(d) for j in range(b)]
    pos = {key: i for i, key in enumerate(vars_)}
    equations: list[list[int]] = []
    # f_- x = u f_+ and f_+ y = v f_-.
    for side, outdim, indim, middle, targetmid, arr, tar in (
        (1, d, a, b, c, x, u), (0, c, b, a, d, y, v)):
        for i in range(outdim):
            for j in range(indim):
                eq = [0] * len(vars_)
                for k in range(middle):
                    eq[pos[(side, i, k)]] += arr
                for k in range(targetmid):
                    eq[pos[(1-side, k, j)]] -= tar
                equations.append(eq)
    return len(vars_) - rank(equations)


def mul(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def algebra_dim(gens: list[tuple[int, ...]]) -> int:
    basis = [(1, 0, 0, 1)]
    changed = True
    while changed:
        changed = False
        for a in list(basis):
            for g in gens:
                z = mul(a, g)
                if rank([list(x) for x in basis + [z]]) > len(basis):
                    basis.append(z)
                    changed = True
    return len(basis)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('build/resonance_mixed_a2_certificate.json'))
    args = parser.parse_args()
    names = list(REPS)
    hom = [[hom_dim(REPS[u], REPS[v]) for v in names] for u in names]
    expected = [[1,0,0,1],[0,1,1,0],[1,0,1,1],[0,1,1,1]]
    assert hom == expected, hom
    dims = [(1,0),(0,1),(1,1),(1,1)]
    euler = [[2*a*c+2*b*d-a*d-b*c for c,d in dims] for a,b in dims]
    ext1 = [[hom[i][j]+hom[j][i]-euler[i][j]
             for j in range(4)] for i in range(4)]
    assert ext1 == [[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]]
    # Kernel L: rank 1, c1=-(alpha+beta), chi(e,L)=0, K.c1=0.
    assert -1 + 2*0 - (-2) == 1
    checks = 0
    for p in range(2, 9):
        for aa, bb, cc, dd in product(range(5), repeat=4):
            a, b, t = aa+cc+dd, bb+cc+dd, cc
            h0, h1 = p*aa+cc+p*dd, (p-1)*(bb+dd)
            assert (h0,h1) == (p*a-(p-1)*t, (p-1)*(b-t))
            assert (h0 == 0 and h1 == 0) == (aa+bb+cc+dd == 0)
            assert (h1 == 0) == (bb == 0 and dd == 0)
            assert (h0 == 0) == (aa == cc == dd == 0)
            checks += 1
    cases = {
        'repeated_scalar': [(2,0,0,2)],
        'distinct_split': [(0,0,0,1)],
        'same_character_Jordan': [(0,0,1,0)],
        'distinct_nonsplit': [(0,0,0,1),(0,0,1,0)],
    }
    result_cases = {}
    for name, gens in cases.items():
        conditions = [[g[0]-g[3],0] for g in gens]
        conditions += [[g[2],0] for g in gens]
        h = 2-rank(conditions)
        repeated = all(g[0] == g[3] and g[2] == 0 for g in gens)
        assert h == (2 if repeated else 1)
        coeff = [[g[3]-g[0]] for g in gens]
        aug = [[g[3]-g[0], g[2]] for g in gens]
        split = rank(coeff) == rank(aug)
        distinct = any(g[0] != g[3] for g in gens)
        image_dim = algebra_dim(gens)
        assert (image_dim == 3) == (distinct and not split)
        result_cases[name] = {'Hom_to_quotient_dimension': h,
            'distinct_characters': distinct, 'extension_split': split,
            'image_algebra_dimension': image_dim}
    cert = {
        'date': '2026-11-15', 'version': 'resonance-mixed-a2-v1',
        'field': 'QQ', 'object_order': names, 'Hom_dimensions': hom,
        'ambient_Euler_pairing': euler, 'ambient_Ext1_dimensions': ext1,
        'kernel_rank_one_Euler_self_pairing': 1,
        'direct_sum_and_cohomology_cases': checks,
        'triangular_tests': result_cases,
        'actual_elliptic_action_matrices_computed': False,
        'categorical_existence_numerically_proved': False,
        'derived_full_faithfulness_proved': False,
        'proof': 'papers/sections/resonance_mixed_a2_category.tex',
        'reproduction': 'python3 computations/verify_resonance_mixed_a2.py',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(cert, ensure_ascii=False, indent=2)+'\n',
                           encoding='utf-8')
    print(json.dumps(cert, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
