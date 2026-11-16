#!/usr/bin/env python3
"""Universal three-generator normalizer-zero witnesses for both common-plane signs."""
import itertools,json,sympy as S
from pathlib import Path
b=S.symbols('b')
def pivots(rows,n):
 rows=[dict(row) for row in rows];ps=[];cols=set(range(n))
 while 1:
  hit=next(((i,j,c) for i,row in enumerate(rows) for j,c in row.items() if j in cols and c!=0 and not S.sympify(c).free_symbols),None)
  if hit is None:break
  i,j,c=hit;row={k:S.expand(v/S.sympify(c)) for k,v in rows.pop(i).items()};ps.append((j,row));cols.remove(j)
  for rr in rows:
   co=rr.get(j,0)
   if not co:continue
   for k,v in row.items():
    cc=S.expand(rr.get(k,0)-co*v)
    if cc==0:rr.pop(k,None)
    else:rr[k]=cc
 return ps,cols,rows

def quotient(n,eps):
 words=list(itertools.product(range(3),repeat=n));ix={w:i for i,w in enumerate(words)}
 rel=[{(1,1):1,(0,0):-1},{(2,0):1,(0,2):-eps},{(2,2):1,(0,1):-1,(1,0):-1,(0,0):-b}]
 rows=[]
 for rr in rel:
  for pos in range(n-1):
   for rest in itertools.product(range(3),repeat=n-2):rows.append({ix[rest[:pos]+w+rest[pos:]]:c for w,c in rr.items()})
 ps,free,remaining=pivots(rows,len(words));assert not any(remaining),(n,eps,remaining)
 free=sorted(free);proj={j:{i:1} for i,j in enumerate(free)}
 for j,row in reversed(ps):
  out={}
  for k,c in row.items():
   if k==j:continue
   for i,v in proj[k].items():out[i]=S.expand(out.get(i,0)-c*v)
  proj[j]={i:c for i,c in out.items() if c!=0}
 return words,ix,free,proj
checks=[]
for eps in [1,-1]:
 w3,i3,f3,p3=quotient(3,eps);w4,i4,f4,p4=quotient(4,eps);rows={}
 for j,k in enumerate(f3):
  for g,mu in enumerate([1,1,-1]):
   for word,sign in [(w3[k]+(g,),1),((g,)+w3[k],-mu)]:
    for i,c in p4[i4[word]].items():
     rr=rows.setdefault((g,i),{});rr[j]=S.expand(rr.get(j,0)+sign*c)
 rows=[{j:c for j,c in row.items() if c!=0} for row in rows.values()]
 ps,cols,rem=pivots(rows,10)
 assert len(f3)==10 and len(f4)==15
 assert len(ps)==10 and not cols and not any(rem)
 checks.append({'epsilon':eps,'degree3_dimension':len(f3),'degree4_dimension':len(f4),'normalizer_constant_pivot_rank':len(ps)})

data={'presentation':['v²=t²','zt=epsilon*tz','z²=tv+vt+beta*t²'],
 'normalizer':'t->t,v->v,z->-z',
 'checks':checks,
 'parameter_scope':'all beta over any characteristic-zero field, epsilon=+1 or-1; all reductions divide only rational constants',
 'conclusion':'No nonzero degree3 normalizer exists in either epsilon-family.',
 'application':'Every (3,1) semisimple gamma0 H3 candidate with commutative common plane has G divisible by its normal positive linear ell, hence is excluded.',
 'scope':'Universal degree3/4 relation quotients and full cubic-normalizer rank checked. Recognition of the quotient family and H3 exclusion are structural proofs.'}
path=Path(__file__).with_name('cubic_positive3_commutative_plane_certificate.json')
if path.exists():assert json.loads(path.read_text())==data
else:path.write_text(json.dumps(data,indent=2)+'\n')
print('PASS both universal AS3 quotient normalizers: constant rank10 and commutative-plane exclusion')
