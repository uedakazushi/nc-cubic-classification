#!/usr/bin/env python3
"""Exact K0/Picard compatibility audit for elliptic boundary data (hearts-v22).

This tests the proposed recovery identities and reproduces the obstruction to
using AOU v1 (9.2),(9.3),(9.25),(9.47) literally in one boundary convention.
It does NOT decide which printed formula needs relabeling/correction, nor prove
that a candidate boundary triple is the actual geometric comparison.
Python standard library only. Run from the repository or bundle root.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
from random import Random


def transpose(a):
    return [list(x) for x in zip(*a)]


def multiply(a, b):
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]


def inverse(a):
    n=len(a)
    m=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p=next((i for i in range(j,n) if m[i][j]),None)
        if p is None: raise ValueError('Singular matrix')
        m[p],m[j]=m[j],m[p]
        c=m[j][j];m[j]=[x/c for x in m[j]]
        for i in range(n):
            if i!=j:
                c=m[i][j];m[i]=[x-c*y for x,y in zip(m[i],m[j])]
    return [row[n:] for row in m]


def numeric_from_basis(v, r):
    """Return (rank, h coefficient, exceptional coefficients..., Euler)."""
    return (sum(v[r:]),-2*v[r]-v[r+1],*v[:r],v[r+2])


def tensor_H(x, r):
    u,a,*rest=x; ci=rest[:-1];c=rest[-1]
    delta=3*a+sum(ci);d=9-r
    return (u,a+3*u,*(b-u for b in ci),c+delta+u*d)


def determinant(x):
    """Exponents of L, O(p_i), q in det F(x)."""
    u,a,*rest=x;ci=rest[:-1];c=rest[-1]
    return (a,*ci,c-u)


def boundary_on_determinant(x, r):
    u,a,*rest=x;ci=rest[:-1];c=rest[-1]
    delta=3*a+sum(ci);d=9-r
    z=list(determinant(x));z[0]+=3*u
    for i in range(r):z[i+1]-=u
    z[-1]+=delta+u*d
    return tuple(z)


# A line class: degree; coefficients of AJ(L0), b (sigma=t_b), D=sum p_i;
# two independent E[3] coordinates. The AJ part is a formal abelian group.
def line(degree,l=0,b=0,D=0,e1=0,e2=0):
    return (degree,l,b,D,e1%3,e2%3)


def add(*classes):
    return line(*(sum(t) for t in zip(*classes)))


def scale(k,x):
    return line(*(k*a for a in x))


def push(k,x):
    """t_{k b,*} on line bundles."""
    d,l,b,D,e1,e2=x
    return line(d,l,b+k*d,D,e1,e2)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path('build/four_hearts_boundary_checks.json'))
    args=ap.parse_args()
    rng=Random(20261116)
    matrix_cases=[];nchecks=0
    for r in range(3,9):
        n=r+3;C=[[int(i==j) for j in range(n)] for i in range(n)]
        for i in range(r):
            for j in range(r,n): C[i][j]=-1
        C[r][r+1]=3;C[r][r+2]=6;C[r+1][r+2]=3
        si=multiply(inverse(transpose(C)),C)
        assert all(x.denominator==1 for row in si for x in row)
        si=[[int(x) for x in row] for row in si]
        vv=[[int(i==j) for i in range(n)] for j in range(n)]
        vv += [[rng.randrange(-9,10) for _ in range(n)] for _ in range(256)]
        for v in vv:
            x=numeric_from_basis(v,r)
            sv=[sum(a*b for a,b in zip(row,v)) for row in si]
            sx=numeric_from_basis(sv,r)
            assert sx==tensor_H(x,r)
            assert determinant(sx)==boundary_on_determinant(x,r)
            nchecks+=1
        d=9-r
        point=[0]*r+[1,-2,1]
        assert numeric_from_basis(point,r)==(0,0,*([0]*r),1)
        assert si[-3][-1]==d-3 and si[-2][-1]==3-2*d and si[-1][-1]==d+1
        matrix_cases.append({'blowups':r,'degree':d,'rank_K0':n,
                             'inverse_Serre_structure_column':[row[-1] for row in si]})
        if r==6:
            cubic_si=si;cubic_C=C
    L0=line(3,1);L1=push(-1,L0);L2=push(-2,L0);D=line(6,D=1)
    Q=add(L1,scale(-1,L0))
    U1=add(scale(-2,L0),L1);U2=add(scale(-5,L0),scale(3,L1))
    qres=add(U2,scale(-2,U1));Lres=add(U1,scale(-1,U2))
    assert qres==Q
    Nlit=add(L0,L1,L2,scale(-1,D))
    assert Nlit==add(scale(3,L1),scale(-1,D))
    required_O=add(scale(-3,U1),scale(-1,D))
    literal_O=push(3,Nlit)
    assert literal_O==add(scale(3,L0),scale(-1,D))
    structure_residual=add(required_O,scale(-1,literal_O))
    point_residual=add(Q,scale(-1,line(0,b=3)))
    assert point_residual==scale(2,Q)==line(0,b=-6)
    assert structure_residual==scale(-3,Q)==line(0,b=9)
    # Two independent identities would require Q^2=Q^3=1; hence Q=1.
    assert add(scale(-1,point_residual),scale(-1,structure_residual))==Q
    qb=scale(-1,Q)
    candidates=[]
    for a,b in product(range(3),repeat=2):
        eps=line(0,e1=a,e2=b);L=add(L1,eps)
        v1=add(scale(-1,L0),scale(-1,eps))
        v2=add(scale(-1,L0),scale(-1,L1),scale(-2,eps))
        assert add(v2,scale(-2,v1))==qb
        assert add(v1,scale(-1,v2))==L
        assert add(scale(3,L),scale(-1,D))==Nlit
        assert add(scale(-3,v1),scale(-1,D))==literal_O
        candidates.append({'epsilon':[a,b],'U1':v1,'U2':v2,'L':L})
    assert len({tuple(c['U1']) for c in candidates})==9
    # q=1 (formally b=0) removes the discrepancy, but is not the infinite-order case.
    assert point_residual[1]==point_residual[3]==structure_residual[1]==structure_residual[3]==0
    result={'date':'2026-11-16','version':'hearts-v22','arithmetic':'QQ exact / formal Picard group / (Z/3)^2',
            'K0_cases':matrix_cases,'basis_and_random_vectors_checked':nchecks,
            'cubic_Euler_matrix':cubic_C,'cubic_inverse_Serre':cubic_si,
            'formal_line_coordinates':['degree','AJ_L0','translation_b','D','epsilon1_mod3','epsilon2_mod3'],
            'restriction_recovered_q':qres,'literal_boundary_translation_q':qb,
            'point_residual_required_minus_literal':point_residual,
            'structure_residual_required_minus_literal':structure_residual,
            'literal_common_convention_obstruction':['Q^2=O','Q^3=O','therefore Q=O'],
            'boundary_first_candidates':candidates,'candidate_count':9,
            'boundary_first_geometric_dictionary_confirmed':False,
            'which_original_formula_requires_relabeling_or_correction_decided':False,
            'scope':'The literal-common-convention test is negative. It does not identify the corrected original construction or prove a new geometric existence theorem.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('cubic_Euler_matrix','cubic_inverse_Serre','boundary_first_candidates')},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
