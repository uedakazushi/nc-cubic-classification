#!/usr/bin/env python3
"""Exact finite witnesses for the sixth-root cone, curvature and AS2 exclusions.
Infinite Ext and complete Ore/AS2 arguments are ordinary proofs in the paper.
"""
import itertools
import json
from pathlib import Path
import sympy as S

source=json.loads(Path(__file__).with_name('cubic_three_eigenvalue_finite_spectra_certificate.json').read_text())
rows=[r for r in source['final_survivors'] if r['N']!=5]
CUBIC=[v for v in itertools.product(range(4),repeat=3) if sum(v)==3]
MULT=(2,1,1)
def cubes(N,lam):return [v for v in CUBIC if sum(x*y for x,y in zip(v,lam))%N==0]
def owners(N,lam,w):return {(i,j) for i in range(3) for j in range(3) if (lam[i]+lam[j])%N==w}
cones=[];curves=[];opposite=[];two=[];final=[]
for row in rows:
    N=row['N'];lam=tuple(row['spectrum']);patterns=row['relation_weight_multiplicities'];C=cubes(N,lam)
    cone_witness=[]
    for rel in patterns:
        witnesses=[]
        for v in (1,2):
            if any(c[v] for c in C) or rel[2*lam[v]%N]:continue
            if all(owners(N,lam,(lam[v]+lam[j])%N)=={(v,j),(j,v)} and rel[(lam[v]+lam[j])%N]==MULT[j]
                   for j in range(3) if j!=v):witnesses.append(v)
        if witnesses:cone_witness.append({'relation_pattern':rel,'normal_variable_index':witnesses[0]})
    if len(cone_witness)==len(patterns):
        cones.append({'N':N,'spectrum':lam,'cubic_support':C,'witnesses':cone_witness});continue
    if N==6 and lam[1]==0 and lam[2]==4*lam[0]%6 and lam[0] in (1,5):
        assert C==[(0,0,3),(0,3,0),(2,0,1)]
        assert all([rel[j*lam[0]%6] for j in range(6)]==[0,2,1,0,1,2] for rel in patterns)
        curves.append({'N':N,'spectrum':lam,'cubic_support':C});continue
    if N==6 and lam==(3,2,4):
        assert C==[(0,0,3),(0,3,0)]
        for rel in patterns:
            for w,m in enumerate(rel):
                if m:assert len({(i==1)-(i==2)+(j==1)-(j==2) for i,j in owners(N,lam,w)})==1
        opposite.append({'N':N,'spectrum':lam,'cubic_support':C,'auxiliary_Z_grading':'U:0,b:+1,c:-1'});continue
    if N==6 and lam in ((2,1,4),(4,2,5)):
        assert all(v[0]==3 or v[0]==0 for v in C)
        for rel in patterns:
            assert owners(N,lam,2*lam[0]%N)=={(0,0)} and rel[2*lam[0]%N]==1
            assert owners(N,lam,2*lam[1]%N)=={(1,1),(2,2)} and rel[2*lam[1]%N]==1
            for j in (1,2):assert owners(N,lam,(lam[0]+lam[j])%N)=={(0,j),(j,0)} and rel[(lam[0]+lam[j])%N]==2
        two.append({'N':N,'spectrum':lam,'cubic_support':C});continue
    final.append(row)
assert len(cones)==4 and len(curves)==2 and len(opposite)==1 and len(two)==2
assert len(final)==17 and sum(r['N']==6 for r in final)==2
assert [r['spectrum'] for r in final if r['N']==6]==[[2,0,5],[4,0,1]]
xi=S.Symbol('xi');cyc=S.Poly(xi**2-xi+1,xi)
def red(x):return S.rem(S.Poly(x,xi),cyc).as_expr()
omega=xi**2
assert red(xi**2-1)!=0 and red(omega**2-1)!=0
for p in (omega,omega**2):assert red((p*omega**2)**3)==1
lam=S.symbols('lambda',nonzero=True)
assert all(S.simplify(lam*lam**(-n-1)-lam**(-n))==0 for n in range(6))
t=S.Symbol('t')
assert S.rem(S.Poly((1-t)**2,t),S.Poly(1+t+t**2,t)).as_expr()!=0
result={'status':'PASS','scope':'exact spectral support and relation owners, scalar module twist, curvature/AS2 constants; ordinary proofs separate',
        'cone_exclusions':cones,'curvature_exclusions':curves,'auxiliary_grading_exclusion':opposite,
        'two_AS2_exclusions':two,'final_survivors':final,'final_spectrum_count':17,
        'remaining_orders':[3,4,6],'remaining_counts':{'3':3,'4':12,'6':2},
        'remaining_sixth_order_exponents':[[2,0,5],[4,0,1]],
        'cone_vertex_reciprocal_Hilbert_series_nonpolynomial':True,
        'not_claimed':['remaining17 spectra exist','all order6 excluded','complete H3 classification']}
Path(__file__).with_name('cubic_sixth_root_spectrum_reductions_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','cone':4,'curvature':2,'auxiliary_grading':1,'two_AS2':2,'remaining_spectra':17}))
