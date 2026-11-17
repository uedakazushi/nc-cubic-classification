#!/usr/bin/env python3
"""Exact original degree-two/three relation ranks supporting the four-line dg frame. Compact generation, cohomology vanishing and duality are separate ordinary proofs."""
import itertools,json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
import sympy as S
K=S.QQ.alg_field_from_poly(S.Poly(S.Symbol("Q")**2+S.Symbol("Q")+1))
q=K.unit;zero=K.zero;one=K.one
def cv(x):return K.convert(x)
rules={(1,0):{(0,1):q*q,(2,3):-q*q},(2,0):{(0,2):q,(1,3):one},(2,1):{(1,2):q*q,(0,3):-q*q},**{(3,j):{(j,3):one} for j in range(3)}}
rels=[]
for w,rr in rules.items():
 row={w:one}
 for v,c in rr.items():row[v]=row.get(v,zero)-c
 rels.append({v:c for v,c in row.items() if c})
w2=list(itertools.product(range(4),repeat=2));w3=list(itertools.product(range(4),repeat=3));i2={w:j for j,w in enumerate(w2)};i3={w:j for j,w in enumerate(w3)}
D2=DomainMatrix.from_dod({j:{i2[w]:c for w,c in row.items()} for j,row in enumerate(rels)},(6,16),K)
G={(0,1,2):cv(2),(0,0,3):cv(2)*(q-one)/cv(3),(1,1,3):cv(2)*(q+cv(2))/cv(3),(2,2,3):cv(2)*(q-one)/cv(3),(0,0,0):one,(1,1,1):cv(2),(2,2,2):cv(3),(0,3,3):q*q,(1,3,3):cv(2)*q*q,(2,3,3):cv(3)*q*q,(3,3,3):cv(5)}
rows=[]
for rel in rels:
 for g in range(4):
  rows.append({i3[(g,)+w]:c for w,c in rel.items()});rows.append({i3[w+(g,)]:c for w,c in rel.items()})
rows.append({i3[w]:c for w,c in G.items()})
D3=DomainMatrix.from_dod(dict(enumerate(rows)),(49,64),K)
assert D2.rank()==6 and D3.rank()==45
h=[1,4,16-D2.rank(),64-D3.rank()];H0=[[h[j-i] if j>=i else 0 for j in range(4)] for i in range(4)];H2=[[h[i-j-1] if i>j else 0 for j in range(4)] for i in range(4)]
assert sum(map(sum,H0))==55 and sum(map(sum,H2))==21
out={'status':'PASS','field':'Q(q), q^2+q+1=0','quadratic_relation_rank':6,'cubic_relation_plus_cut_rank':45,'cut':[2,1,2,3,5],'four_line_frame':['O','O(1)','O(2)','O(3)'],'R_dimensions_0_to_3':h,'Hom_dimension_matrix':H0,'Ext2_dimension_matrix_by_AS_Gorenstein_duality':H2,'dg_frame_type':{'H0':55,'H1':0,'H2':21},'separate_mathematical_inputs':['ambient AS4 Beilinson generation','hypersurface restriction adjunction','AS Cohen-Macaulay vanishing and AS Gorenstein duality'],'not_claimed':['finite truncation determines arbitrary nonsmooth dg algebras','H3 openness','full exceptional collection on the cubic surface']}
Path(__file__).with_name('cubic_hypersurface_frame_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
