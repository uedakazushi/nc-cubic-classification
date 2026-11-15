#!/usr/bin/env python3
"""Exact j0-normalization specialization and a non-torsion elliptic example.
Centrality over the whole PBW family is a specialization argument in the paper.
"""
import sympy as s,json
from pathlib import Path
from itertools import product
root=Path(__file__).parent
h,z=s.symbols('h z');A,B,C,D=s.symbols('A B C D');bx,by,bz=s.symbols('beta_x beta_y beta_z')
old=json.loads((root/'cubic_clifford_integration_certificate.json').read_text())
cut={tuple(e['active_word']):s.factor(s.cancel((1+h**3)*s.sympify(e['coefficient'])).subs(h,-1)) for e in old['integrated_cut_coefficients']}
cut[()]=D
assert all(s.denom(c).free_symbols <= {z} for c in cut.values())
# Fixed nonsplit example: alpha=(-8,0,0), beta=0, gamma=2.
example={w:s.cancel(c.subs({z:2,A:1,B:0,C:0,bx:0,by:0,bz:0,D:0})) for w,c in cut.items()}
rels=[]
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
 r={(j,k):s.Integer(3),(k,j):s.Integer(-1),(i,i):s.Integer(1)}
 if i==0:r[(i,)]=s.Integer(8)
 rels.append(r)
def words(n):return [w for d in range(n+1) for w in product(range(3),repeat=d)]
def matrix(n,rels):
 ws=words(n);ix={w:i for i,w in enumerate(ws)};cols=[]
 for d in range(n-1):
  for l in range(d+1):
   for left in product(range(3),repeat=l):
    for right in product(range(3),repeat=d-l):
     for r in rels:cols.append({ix[left+w+right]:c for w,c in r.items()})
 return ws,s.SparseMatrix(len(ws),len(cols),{(i,j):c for j,col in enumerate(cols) for i,c in col.items()})
ws,M=matrix(4,rels);ix={w:i for i,w in enumerate(ws)};rank=M.rank();assert rank==86
for x in range(3):
 v=s.zeros(len(ws),1)
 for w,c in example.items():v[ix[w+(x,)]]+=c;v[ix[(x,)+w]]-=c
 assert M.row_join(v).rank()==rank
ws3,M3=matrix(3,[{w:c for w,c in r.items() if len(w)==2} for r in rels]);ix3={w:i for i,w in enumerate(ws3)}
v=s.zeros(len(ws3),1)
for w,c in example.items():
 if len(w)==3:v[ix3[w]]=c
assert M3.row_join(v).rank()==M3.rank()+1
# Smooth cubic x^3+y^3+z^3+9xyz: singular primes divide 3*(1+27)=84.
def cross(a,b,p):return tuple((a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3])%p for i in range(3))
def norm(a,p):
 v=next(v for v in a if v%p);return tuple(x*pow(v,-1,p)%p for x in a)
orders={}
for p in [5,13]:
 o=norm((1,-1,0),p);P=o
 for n in range(1,3*p+10):
  x,y,zz=P;rows=[(x,-zz,3*y),(3*zz,y,-x),(-y,3*x,zz)]
  Q=next(cross(rows[i],rows[k],p) for i,k in [(0,1),(0,2),(1,2)] if any(cross(rows[i],rows[k],p)))
  assert all(sum(a*b for a,b in zip(row,Q))%p==0 for row in rows)
  P=norm(Q,p);assert (sum(a**3 for a in P)+9*P[0]*P[1]*P[2])%p==0
  if P==o:orders[p]=n;break
assert orders=={5:9,13:6}
result={'version':'classification-v26','boundary':'h=-1; multiply old cut by 1+h^3 before specialization; restore free D*t^3', 'coefficients':[{'active_word':list(w),'t_power':3-len(w),'coefficient':str(c)} for w,c in cut.items()], 'example':{'gamma':2,'A_B_C':[1,0,0],'beta':[0,0,0],'cut_D0':[{'word':list(w),'coefficient':str(c)} for w,c in example.items() if c],'degree4_relation_rank':rank,'three_exact_central_commutators':True,'leading_cubic_nonzero':True,'elliptic_curve':'x^3+y^3+z^3+9xyz=0','translation_point':[3,-1,1],'good_reduction_orders':orders,'infinite_order_argument':'If torsion order m, good reduction at5 implies m=9*5^a, at13 implies m=6*13^b; impossible.'},'scope':'Universal regularized coefficients; exact centrality and leading nonvanishing at the specified rational example. No all-D admissibility classification.'}
(root/'cubic_j0_boundary_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS j0 regularization, exact nonsplit central cubic, nonzero leading term, non-torsion translation')
