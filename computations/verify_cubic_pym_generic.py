#!/usr/bin/env python3
"""Exact QQ degree-three center obstructions in Pym's non-skew CY charts.

AS-regularity/CY and generic-chart coverage are external inputs from Pym;
this program certifies only the stated multiplication/derivation ranks.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
import json
from math import comb
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix


def words(n):return list(product(range(4),repeat=n))


def relation_rows(relations,n):
    basis=words(n);index={w:i for i,w in enumerate(basis)};rows=[]
    for left_length in range(n-1):
        for left in words(left_length):
            for right in words(n-2-left_length):
                for rel in relations:
                    row={}
                    for w,c in rel.items():row[index[left+w+right]]=c
                    rows.append(row)
    return S.MutableSparseMatrix(len(rows),len(basis),{(i,j):c for i,row in enumerate(rows) for j,c in row.items()})


def quotient_projection(relations,n):
    rels=relation_rows(relations,n)
    rref,pivots=DomainMatrix.from_Matrix(rels).convert_to(S.QQ).rref()
    rr=rref.to_Matrix();free=[j for j in range(4**n) if j not in pivots]
    pivot_index={j:i for i,j in enumerate(pivots)}
    projection=S.zeros(len(free),4**n)
    for j,col in enumerate(free):projection[j,col]=1
    for col,row in pivot_index.items():
        for j,freecol in enumerate(free):projection[j,col]=-rr[row,freecol]
    assert projection*rels.T==S.zeros(len(free),rels.rows)
    return free,projection,len(pivots)


def main():
    params=[S.Rational(2),S.Rational(3),S.Rational(-5,7)]
    assert sum(params)+S.prod(params)==0
    relations=[]
    for (i,j,k),p in zip([(1,2,3),(2,3,1),(3,1,2)],params):
        relations.append({(0,i):1,(i,0):-1,(j,k):-p,(k,j):-p})
        relations.append({(0,i):1,(i,0):1,(j,k):-1,(k,j):1})
    free3,projection3,rank3=quotient_projection(relations,3)
    free4,projection4,rank4=quotient_projection(relations,4)
    assert len(free3)==20 and len(free4)==35 and (rank3,rank4)==(44,221)
    b3=words(3);i4={w:i for i,w in enumerate(words(4))}
    center=S.zeros(140,20)
    for col,j in enumerate(free3):
        word=b3[j]
        for i in range(4):
            vector=projection4[:,i4[word+(i,)]]-projection4[:,i4[(i,)+word]]
            center[35*i:35*(i+1),col]=vector
    _,minor_rows=DomainMatrix.from_Matrix(center.T).convert_to(S.QQ).rref()
    assert len(minor_rows)==20
    minor=center[list(minor_rows),:]
    determinant=S.QQ.to_sympy(DomainMatrix.from_Matrix(minor).convert_to(S.QQ).det())
    assert determinant!=0

    # A divergence-free S(2,3) Ore derivation with no cubic first integral.
    x,y,z=S.symbols('x y z');v=(x,y,z)
    delta=(x*x-x*y-x*z,y*y-y*x-y*z,z*z-z*x-z*y)
    assert sum(S.diff(f,a) for f,a in zip(delta,v))==0
    ex3=[a for a in product(range(4),repeat=3) if sum(a)==3]
    ex4=[a for a in product(range(5),repeat=3) if sum(a)==4]
    cols=[]
    for a in ex3:
        monomial=S.prod(b**c for b,c in zip(v,a))
        image=S.Poly(sum(S.diff(monomial,b)*c for b,c in zip(v,delta)),*v)
        cols.append([image.coeff_monomial(e) for e in ex4])
    dm=S.Matrix(cols).T
    _,ore_rows=dm.T.rref();assert len(ore_rows)==10
    ore_det=dm[list(ore_rows),:].det();assert ore_det!=0

    # E(3): the displayed CGG X has no zero weight in degree three.
    monomials4=[a for a in product(range(4),repeat=4) if sum(a)==3]
    weights=[sum(c*w for c,w in zip(a,[-5,-1,3,7])) for a in monomials4]
    assert all(w!=0 and w%4==1 for w in weights)

    # L(1,1,2): two algebraically independent parameters, not a finite-field sample.
    qexp=[[None]*4 for _ in range(4)]
    upper=[(0,0),(1,0),(-1,0),(0,-1),(0,1),(1,-1)]
    from itertools import combinations
    for i in range(4):qexp[i][i]=(0,0)
    for (i,j),e in zip(combinations(range(4),2),upper):
        qexp[i][j]=e;qexp[j][i]=tuple(-a for a in e)
    assert all(all(sum(qexp[i][j][d] for j in range(4))==0 for d in range(2)) for i in range(4))
    for a in monomials4:
        assert any(sum(qexp[j][i][d]*a[j] for j in range(4)) for i in range(4) for d in range(2))

    cert={'date':'2026-11-15','primary_source':'Pym arXiv:1403.6444v1, sections 3.2,3.3,3.5,3.6',
          'R22_witness':{'parameters':list(map(str,params)),'relation_ranks_degrees3_4':[rank3,rank4],
                         'quotient_dimensions':[20,35],'center_commutator_matrix':[140,20],
                         'nonzero_minor_rows':list(minor_rows),'nonzero_minor_determinant':str(determinant)},
          'S23_witness':{'b':[-1,-1,-1],'c':[-1,-1,-1],'d':[0,0,0],
                         'derivation_matrix':[15,10],'minor_rows':list(ore_rows),'minor_determinant':str(ore_det)},
          'E3_degree3_X_weight_numerators':weights,
          'L112_independent_parameter_center_degree3':0,
          'scope':'Generic center-degree-three exclusion in the four displayed non-skew CY charts. Not classification of special loci, all AS4, or all H3.',
          'external_input':'The displayed Pym charts are Koszul AS4 and CY on the cited standard loci; low-degree ranks alone do not establish AS regularity.'}
    Path(__file__).with_name('cubic_pym_generic_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: QQ R22 center-rank20 witness; S23 cubic derivation-rank10 witness; exact E3 and L112 weight obstructions')

if __name__=='__main__':main()
