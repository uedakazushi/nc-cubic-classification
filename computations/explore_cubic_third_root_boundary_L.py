#!/usr/bin/env python3
"""Exploratory generic L-curve normal kernel and first x-adic lift.
Exact function-field checks, not all closed fibers, AS4 existence or H3 claims.
"""
import sympy as s,itertools,json
from cubic_function_extension import CubicField
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));D,E=s.symbols('D E');J=F.frac_field(E);ee=J.gens[0];oo=J.convert(F.to_sympy(F.unit));K=CubicField(J,-oo*ee**3-oo**2);d=K.generator;e=K.convert(E);o=K.convert(F.to_sympy(F.unit));one,zero=K.one,K.zero
# y,b,c with w=1
R=[{(0,1):d,(1,0):e,(2,2):one},{(0,2):e,(2,0):d,(1,1):one},{(1,2):d,(2,1):e,(0,0):one}]
log=[]
def echelon(rows):
 piv={}
 for row in rows:
  row={j:c for j,c in row.items() if c}
  while row:
   j=min(row)
   if j not in piv:
    co=row[j];log.append(co);piv[j]={k:v/co for k,v in row.items()};break
   co=row[j]
   for k,v in piv[j].items():
    row[k]=row.get(k,zero)-co*v
    if not row[k]:row.pop(k,None)
 return piv
def reduce(row,P):
 row=dict(row)
 for j,poly in sorted(P.items()):
  co=row.get(j,zero)
  if co:
   for k,v in poly.items():
    row[k]=row.get(k,zero)-co*v
    if not row[k]:row.pop(k,None)
 return row
Ws={n:list(itertools.product(range(3),repeat=n)) for n in [3,4]};Is={n:{w:j for j,w in enumerate(Ws[n])} for n in [3,4]};Ps={}
for n in [3,4]:
 rows=[]
 for rel in R:
  for left in range(n-1):
   for pre in itertools.product(range(3),repeat=left):
    for post in itertools.product(range(3),repeat=n-left-2):rows.append({Is[n][pre+w+post]:c for w,c in rel.items()})
 Ps[n]=echelon(rows)
 print('dim',n,3**n-len(Ps[n]),flush=True)
free=[w for j,w in enumerate(Ws[3]) if j not in Ps[3] and sum([0,1,2][t] for t in w)%3==0]
print('free',free,flush=True)
cols=[]
for w in free:
 col={}
 for j,phase in enumerate([one,o**2,o]):
  row={Is[4][w+(j,)]:one};k=Is[4][(j,)+w];row[k]=row.get(k,zero)-phase
  for k,c in reduce(row,Ps[4]).items():col[j*81+k]=c
 cols.append(col)
keys=sorted(set().union(*(set(c) for c in cols)));rows=[{j:c[k] for j,c in enumerate(cols) if k in c} for k in keys]
log=[];piv=echelon(rows);print('L curve normal rank',len(piv),flush=True)
if len(piv)<4:print('kernel dimension',4-len(piv),flush=True)

# Recover normalized Gamma in the four quotient cubic classes.
coeff={3:one}
for j in sorted(piv,reverse=True):coeff[j]=-sum((c*coeff.get(k,zero) for k,c in piv[j].items() if k!=j),zero)
Gamma={tuple(t+1 for t in w):coeff[i] for i,w in enumerate(free)}
print('Gamma normalized recovered',flush=True)

def truncated(Z,v):
 R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):d,(2,1):e,(3,3):one,(0,2):o*Z},
 {(1,3):e,(3,1):d,(2,2):one,(0,3):Z},
 {(2,3):d,(3,2):e,(0,1):v,(1,1):one}]
 words=sorted([w for w in itertools.product(range(4),repeat=4) if w.count(0)<2],key=lambda w:(w.count(0),w));ix={w:j for j,w in enumerate(words)}
 rows=[]
 for rel in R:
  for left in range(3):
   for pre in itertools.product(range(4),repeat=left):
    for post in itertools.product(range(4),repeat=2-left):
     row={}
     for w,c in rel.items():
      ww=pre+w+post
      if ww in ix:row[ix[ww]]=c
     rows.append(row)
 P=echelon(rows);print('truncated degree4 dimension',len(words)-len(P),'Z,v',bool(Z),bool(v),flush=True)
 def residual(G):
  out={}
  for j,phase in enumerate([one,one,o**2,o]):
   row={}
   for w,c in G.items():
    for ww,cc in [(w+(j,),c),((j,)+w,-phase*c)]:
     if ww in ix:row[ix[ww]]=row.get(ix[ww],zero)+cc
   for k,c in reduce(row,P).items():out[j,k]=c
  return out
 return [j for j in range(len(words)) if j not in P],residual
fr,r0=truncated(zero,zero);assert not r0(Gamma)
correction=[r0({(1,1,0):one}),r0({(2,3,0):one})]
for Z,v in [(one,zero),(zero,one)]:
 f,r=truncated(Z,v);assert f==fr;correction.append(r(Gamma))
keys=sorted(set().union(*(set(c) for c in correction)));rows=[{j:c[k] for j,c in enumerate(correction) if k in c} for k in keys]
log=[];N=echelon(rows);print('first order obstruction matrix rank',len(N),flush=True)
print('kernel dimension',4-len(N),flush=True)

assert len(piv)==3 and len(N)==2
print('PASS: generic L kernel dimension1; first-order lifting has no parameter obstruction')
