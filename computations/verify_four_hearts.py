#!/usr/bin/env python3
"""Exact finite checks for nc_del_pezzo_hearts.tex, hearts-v17.

Python standard library only. Checks mixed A2 linear algebra and source
references. It does not prove sheaf existence, derived equivalence or novelty.
Run from the repository/bundle root.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import re


def rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    a = [[Fraction(x) for x in row] for row in rows]
    if any(len(row) != len(a[0]) for row in a):
        raise ValueError('Nonrectangular matrix')
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][c]
        a[r] = [x / d for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                d = a[i][c]
                a[i] = [x - d * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def hom(src: tuple[int, ...], dst: tuple[int, ...]) -> int:
    a, b, x, y = src
    c, d, u, v = dst
    variables = [(0, i, j) for i in range(c) for j in range(a)]
    variables += [(1, i, j) for i in range(d) for j in range(b)]
    index = {key: i for i, key in enumerate(variables)}
    equations = []
    for side, outdim, indim, mid, tmid, arr, target in (
        (1, d, a, b, c, x, u), (0, c, b, a, d, y, v)
    ):
        for i in range(outdim):
            for j in range(indim):
                eq = [0] * len(variables)
                for k in range(mid):
                    eq[index[(side, i, k)]] += arr
                for k in range(tmid):
                    eq[index[(1 - side, k, j)]] -= target
                equations.append(eq)
    return len(variables) - rank(equations)


def mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]


def matrix_unit(i: int, j: int) -> list[list[int]]:
    return [[int(r == i and c == j) for c in range(4)] for r in range(4)]


def add(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def flatten(a: list[list[int]]) -> list[int]:
    return [x for row in a for x in row]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path('build/four_hearts_checks.json'))
    args = parser.parse_args()
    reps = [(1,0,0,0), (0,1,0,0), (1,1,1,0), (1,1,0,1)]
    h = [[hom(a,b) for b in reps] for a in reps]
    assert h == [[1,0,0,1],[0,1,1,0],[1,0,1,1],[0,1,1,1]]
    dims = [(1,0), (0,1), (1,1), (1,1)]
    euler = [[2*a*c + 2*b*d - a*d - b*c for c,d in dims] for a,b in dims]
    ext1 = [[h[i][j]+h[j][i]-euler[i][j] for j in range(4)] for i in range(4)]
    assert ext1 == [[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]]
    counts = dict(positive=0, negative=0, balanced_hypothetical=0)
    for p,n in product(range(1,9), repeat=2):
        r = min(p,n)
        for aa,bb,cc,dd in product(range(5), repeat=4):
            a,b,t = aa+cc+dd, bb+cc+dd, cc
            h0 = p*aa + max(p-n,0)*cc + p*dd
            h1 = n*bb + max(n-p,0)*cc + n*dd
            assert (h0,h1) == (p*a-r*t, n*b-r*t)
            assert h0-h1 == p*a-n*b
            if p>n:
                counts['positive'] += 1
                assert (h1 == 0) == (bb == dd == 0)
                assert (h0 == 0) == (aa == cc == dd == 0)
            elif p<n:
                counts['negative'] += 1
                assert (h1 == 0) == (bb == cc == dd == 0)
                assert (h0 == 0) == (aa == dd == 0)
            else:
                counts['balanced_hypothetical'] += 1
                assert (h0 == h1 == 0) == (aa == bb == dd == 0)
            if p != n:
                assert (h0 == h1 == 0) == (aa+bb+cc+dd == 0)
    e0 = add(matrix_unit(0,0),matrix_unit(2,2))
    e1 = add(matrix_unit(1,1),matrix_unit(3,3))
    a,b = matrix_unit(1,0),matrix_unit(2,3)
    basis = [e0,e1,a,b]
    zero = [[0]*4 for _ in range(4)]
    assert rank([flatten(x) for x in basis]) == 4
    assert mul(e0,e0)==e0 and mul(e1,e1)==e1
    assert mul(e0,e1)==mul(e1,e0)==zero
    assert mul(e1,a)==mul(a,e0)==a and mul(e0,b)==mul(b,e1)==b
    assert all(mul(x,y)==zero for x,y in product([a,b],repeat=2))
    image_dims=[]
    for start in [0,2]:
        block = [flatten([row[start:start+2] for row in g[start:start+2]]) for g in basis]
        image_dims.append(rank(block))
    assert image_dims == [3,3]
    reflection=[[1,0],[1,-1]]
    form=[[-2,1],[1,-2]]
    assert mul(mul([list(r) for r in zip(*reflection)],form),reflection)==form
    assert mul([[2,-1]],reflection)==[[1,1]]
    def read_tex(path: Path, seen: set[Path]) -> str:
        if path in seen:
            raise ValueError(f'Repeated TeX input: {path}')
        seen.add(path)
        text = path.read_text(encoding='utf-8')
        for child in re.findall(r'\\input\{([^}]+)\}', text):
            child_path = Path(child)
            if not child_path.suffix:
                child_path = child_path.with_suffix('.tex')
            text += '\n' + read_tex(child_path, seen)
        return text
    source=read_tex(Path('papers/nc_del_pezzo_hearts.tex'), set())
    labels=re.findall(r'\\label\{([^}]+)\}',source)
    references=re.findall(r'\\(?:eqref|ref)\{([^}]+)\}',source)
    assert len(labels)==len(set(labels)), 'Duplicate labels'
    assert not set(references)-set(labels), 'Unresolved labels'
    bib=set(re.findall(r'\\bibitem\{([^}]+)\}',source))
    cites={k.strip() for group in re.findall(r'\\cite(?:\[[^]]*\])?\{([^}]+)\}',source)
           for k in group.split(',')}
    assert not cites-bib, 'Unresolved bibliography keys'
    result={
        'date':'2026-11-16','version':'hearts-v17','arithmetic':'QQ exact',
        'object_order':['S+','S-','P','Q'],'Hom':h,'ambient_Ext1':ext1,
        'cohomology_cases':counts,'total_cases':sum(counts.values()),
        'quotient_dimension':4,'radical_square_zero':True,
        'two_representation_image_dimensions':image_dims,
        'reflection_matrix':reflection,'reflected_indices':[1,1],
        'source_labels':len(labels),'bibliography_entries':len(bib),
        'all_source_references_resolved':True,
        'actual_elliptic_generator_coefficients_computed':False,
        'category_existence_or_equivalence_proved_by_computation':False
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
