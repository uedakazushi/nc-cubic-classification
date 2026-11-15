#!/usr/bin/env python3
"""Exact QQ(a) identities; all-special extension uses AS4 flatness in the paper."""
import json
from pathlib import Path
from functools import reduce
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_pym_generic import words, relation_rows


def main():
    a = S.Symbol('a')
    field = S.QQ.frac_field(a)
    b, c = (1-a)/(a+3), (a+1)/(a-3)
    assert S.cancel(a+b+c+a*b*c) == 0
    fs = []
    for (i,j,k), v in zip([(1,2,3),(2,3,1),(3,1,2)], [a,b,c]):
        fs += [{(0,i):1,(i,0):-1,(j,k):-v,(k,j):-v},
               {(0,i):1,(i,0):1,(j,k):-1,(k,j):1}]
    # Work before imposing ANY pencil quadric, with the five retained f's.
    relations = fs[1:]
    degree = lambda w: reduce(int.__xor__, w, 0)
    projections = {}
    dimensions = {}
    for n in [3,4]:
        ws = words(n)
        matrix = relation_rows(relations,n)
        lookup = {}
        dimensions[n] = []
        for g in range(4):
            cols = [j for j,w in enumerate(ws) if degree(w)==g]
            rows = [i for i in range(matrix.rows) if any(matrix[i,j] for j in cols)]
            rr, pivots = DomainMatrix.from_Matrix(matrix[rows,cols]).convert_to(field).rref()
            rr = rr.to_Matrix()
            free = [j for j in range(len(cols)) if j not in pivots]
            dimensions[n].append(len(free))
            p = S.zeros(len(free),len(cols))
            for j,k in enumerate(free): p[j,k]=1
            for i,k in enumerate(pivots):
                for j,l in enumerate(free): p[j,k]=-rr[i,l]
            lookup[g] = {ws[k]:p[:,j] for j,k in enumerate(cols)}
        projections[n] = lookup

    def add(*polys):
        result = {}
        for poly in polys:
            for w,v in poly.items(): result[w]=result.get(w,0)+v
        return result
    def scale(k,p): return {w:k*v for w,v in p.items()}
    def left(i,p): return {(i,)+w:v for w,v in p.items()}
    def right(p,i): return {w+(i,):v for w,v in p.items()}
    def zero(poly,n):
        pp = projections[n]
        result = {g:S.zeros(len(next(iter(block.values()))),1) for g,block in pp.items()}
        for w,v in poly.items(): result[degree(w)]+=pp[degree(w)][w]*v
        return all(DomainMatrix.from_Matrix(v).convert_to(field).is_zero_matrix for v in result.values())

    q2 = {(0,0):2*(a-3),(1,1):-2*(a+1),(2,2):2*(a+1),(3,3):2*(a-3)}
    q3 = {(0,0):-2*(a+3),(1,1):2*(a-1),(2,2):-2*(a+3),(3,3):-2*(a-1)}
    h = {(1,0):-16*a,(2,3):8*(a-1),(3,2):-8*(a+1)}
    f2, f3 = left(2,q2), left(3,q3)
    signs = [-1,-1,1,1]
    for f in [f2,f3]:
        for i in range(4): assert zero(add(right(f,i),scale(-signs[i],left(i,f))),4)
    g1={(0,0):-1,(1,1):1,(2,2):1,(3,3):1}
    g2={(1,1):1,(2,2):(a+3)/2,(3,3):(3-a)/2}
    for q,ss in [(g1,[1]*4),(g2,[1]*4),(fs[0],signs)]:
        for i in range(4): assert zero(add(right(q,i),scale(-ss[i],left(i,q))),3)
    # Coefficients of t and t^2 in the polynomial factorization identity.
    assert zero(add(left(2,h),scale(a-1,left(3,q2)),scale(a-3,f3)),3)
    assert zero(add(scale(-a-1,left(2,q3)),left(3,h),scale(-a-3,f2)),3)
    t = S.Symbol('t')
    numerator = -t*((a+1)*t*t+a-3)
    denominator = (a+3)*t*t+a-1
    resultant = S.factor(S.resultant(numerator,denominator,t))
    assert S.expand(resultant - 64*(a-1)) == 0
    cert = {'version':'classification-v65','field':'QQ(a)',
            'curve':{'alpha':'a','beta':str(b),'gamma':str(c)},
            'five_relation_quotient_group_dimensions':dimensions,
            'Q2':{str(w):str(v) for w,v in q2.items()},
            'Q3':{str(w):str(v) for w,v in q3.items()},
            'H':{str(w):str(v) for w,v in h.items()},
            'normality_equations_verified':8,'factorization_coefficient_equations_verified':2,
            'factor_map_ratio':str(numerator/denominator),'affine_resultant':str(resultant),
            'scope':'Exact rational-function identities before the pencil relation. The paper uses AS4 flatness for all allowed parameters and THCR descent for W1 dimension two; neither follows just from low-degree ranks.'}
    Path(__file__).with_name('cubic_stafford_resonance_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS eight normality identities; universal factorization; degree-three surjective factor map')


if __name__=='__main__': main()
