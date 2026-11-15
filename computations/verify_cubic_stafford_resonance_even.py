#!/usr/bin/env python3
"""Exact five-relation identities for the even Stafford resonant pencil."""
import json
from pathlib import Path
from functools import reduce
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_stafford_resonance import graded_projections


def main():
    a,t=S.symbols('a t');field=S.QQ.frac_field(a)
    b,c=(1-a)/(a+3),(a+1)/(a-3)
    fs=[]
    for (i,j,k),v in zip([(1,2,3),(2,3,1),(3,1,2)],[a,b,c]):
        fs += [{(0,i):1,(i,0):-1,(j,k):-v,(k,j):-v},
               {(0,i):1,(i,0):1,(j,k):-1,(k,j):1}]
    projections,dimensions=graded_projections(fs[:1]+fs[2:],field)
    degree=lambda w:reduce(int.__xor__,w,0)
    def add(*ps):
        result={}
        for p in ps:
            for w,v in p.items():result[w]=result.get(w,0)+v
        return result
    def scale(k,p):return {w:k*v for w,v in p.items()}
    def left(i,p):return {(i,)+w:v for w,v in p.items()}
    def right(p,i):return {w+(i,):v for w,v in p.items()}
    def zero(poly,n):
        pp=projections[n]
        out={g:S.zeros(len(next(iter(block.values()))),1) for g,block in pp.items()}
        for w,v in poly.items():out[degree(w)]+=pp[degree(w)][w]*v
        return all(DomainMatrix.from_Matrix(v).convert_to(field).is_zero_matrix for v in out.values())
    q0={(0,0):2,(1,1):2,(2,2):-2*a,(3,3):2*a}
    q1={(0,0):2*(a*a-9),(1,1):2*(a*a-1),
        (2,2):-2*a*(a+1)*(a+3),(3,3):2*a*(a-1)*(a-3)}
    h={(1,0):-16,(2,3):8*a*(a-1),(3,2):-8*a*(a+1)}
    f0,f1=left(0,q0),left(1,q1)
    assert zero(add(f0,scale(-1,right(q0,0))),3)
    assert zero(add(f1,scale(-1,right(q1,1))),3)
    signs=[1,1,-1,-1]
    for f in [f0,f1]:
        for i in range(4):assert zero(add(right(f,i),scale(-signs[i],left(i,f))),4)
    g1={(0,0):-1,(1,1):1,(2,2):1,(3,3):1}
    g2={(1,1):1,(2,2):(a+3)/2,(3,3):(3-a)/2}
    for q,ss in [(g1,[1]*4),(g2,[1]*4),(fs[1],signs)]:
        for i in range(4):assert zero(add(right(q,i),scale(-ss[i],left(i,q))),3)
    assert zero(add(left(0,h),scale(a*a-1,left(1,q0)),scale(-1,f1)),3)
    assert zero(add(left(0,q1),left(1,h),scale(9-a*a,f0)),3)
    resultant=S.factor(S.resultant(t*(t*t+1),(a*a-9)*t*t+a*a-1,t))
    assert S.expand(resultant-64*(a*a-1))==0
    cert={'version':'classification-v66','field':'QQ(a)',
          'five_relation_quotient_group_dimensions':dimensions,
          'Q0':{str(w):str(v) for w,v in q0.items()},
          'Q1':{str(w):str(v) for w,v in q1.items()},
          'H0':{str(w):str(v) for w,v in h.items()},
          'normality_equations':8,'quadratic_normality_equations':12,
          'factorization_coefficient_equations':2,'left_right_factor_equations':2,
          'factor_map_ratio':str(t*(t*t+1)/((a*a-9)*t*t+a*a-1)),
          'resultant':str(resultant),
          'scope':'Exact rational-function identities. Paper gives all-special flatness extension, dimension two and cocycle centre dimension one, not inferred from these identities alone.'}
    Path(__file__).with_name('cubic_stafford_resonance_even_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS even Stafford normal pencil, degree-three factor map and central quadratic identities')


if __name__=='__main__':main()
