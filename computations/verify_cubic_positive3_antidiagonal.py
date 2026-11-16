#!/usr/bin/env python3
"""Exact quaternion anti-diagonal top and filtered no-cubic certificate."""
import itertools,json,sympy as S
from pathlib import Path
from functools import lru_cache
from sympy.polys.matrices import DomainMatrix
I=S.I
rules={(1,0):{(0,1):-1},
(2,0):{(1,2):S.Rational(1,2),(0,2):I/2,(1,3):S.Rational(1,2),(0,3):-I/2},
(2,1):{(0,2):-S.Rational(1,2),(1,2):-I/2,(0,3):-S.Rational(1,2),(1,3):I/2},
(3,0):{(1,2):S.Rational(1,2),(0,2):-I/2,(1,3):S.Rational(1,2),(0,3):I/2},
(3,1):{(0,2):-S.Rational(1,2),(1,2):I/2,(0,3):-S.Rational(1,2),(1,3):-I/2},
(3,2):{(2,3):-1}}
def add(*terms):
 out={}
 for cc,p in terms:
  for w,c in p.items():out[w]=S.expand(out.get(w,0)+cc*c)
 return {w:c for w,c in out.items() if c!=0}
@lru_cache(None)
def nf(w):
 for j in range(len(w)-1):
  if w[j:j+2] in rules:return add(*[(cc,nf(w[:j]+v+w[j+2:])) for v,cc in rules[w[j:j+2]].items()])
 return {w:S.Integer(1)}
for w in itertools.product(range(4),repeat=3):
 if w[:2] in rules and w[1:] in rules:
  assert add(*[(cc,nf(v+w[2:])) for v,cc in rules[w[:2]].items()])==add(*[(cc,nf(w[:1]+v)) for v,cc in rules[w[1:]].items()])
bs3=list(itertools.combinations_with_replacement(range(4),3));bs4=list(itertools.combinations_with_replacement(range(4),4));ix={w:i for i,w in enumerate(bs4)};M=S.zeros(140,20)
mu=[(0,1),(1,1),(3,1),(2,1)]
for j,w in enumerate(bs3):
 for g,(h,sign) in enumerate(mu):
  q=add((1,nf(w+(g,))),(-sign,nf((h,)+w)))
  for ww,cc in q.items():M[35*g+ix[ww],j]=cc
K=S.QQ.algebraic_field(I);dm=DomainMatrix.from_Matrix(M).convert_to(K)
assert dm.rank()==20
pivot_rows=list(dm.transpose().rref()[1])
minor=M.extract(pivot_rows,list(range(20)))
determinant=K.to_sympy(DomainMatrix.from_Matrix(minor).convert_to(K).det())
assert determinant!=0
data={
 'top_algebra':['xy=-yx','zx=i*xz','zy=-i*yz','vx=yv','vy=-xv','v²=z²'],
 'PBW':'x^i*y^j*r^k*s^l, r=v+z,s=v-z; all four quadratic overlap ambiguities resolve',
 'normalizer':'x->x,y->y,r->s,s->r',
 'normal_cubic_matrix_shape':[140,20],'rank':20,'nonzero_minor_rows':pivot_rows,
 'minor_determinant':str(determinant),
 'filtered_consequence':'All lower-weight skew-derivation and outer-square corrections preserving the H3 normalizer have no normal cubic.',
 'scope':'Exact PBW overlaps and a fixed full-rank Gaussian-rational minor; no coverage beyond the specified quaternion anti-diagonal chart.'}
path=Path(__file__).with_name('cubic_positive3_antidiagonal_certificate.json')
if path.exists():assert json.loads(path.read_text())==data
else:path.write_text(json.dumps(data,indent=2)+'\n')
print('PASS positive-three quaternion anti-diagonal top: PBW and full cubic rank20')
