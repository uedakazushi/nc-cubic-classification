#!/usr/bin/env python3
"""All-parameter normal-cubic exclusion of one explicit involution Ore family."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix

def mons(d):return [p for p in itertools.product(range(d+1),repeat=4) if sum(p)==d]
def calc(K,a):
 m3=mons(3);m4=mons(4);ix={m:i for i,m in enumerate(m4)};gens=[tuple(int(i==j) for i in range(4)) for j in range(4)]
 def prod(m,n):
  aa,b,c,d=m;A,B,C,D=n
  power=d*(-2*A+B+C);sign=(-1)**(d*(A+B+C))
  if d%2:sign*=(-1)**(B*C);B,C=C,B
  power+=A*(b+c);sign*=(-1)**(c*B)
  return (aa+A,b+B,c+C,d+D),K(sign)*a**power
 rows={}
 mu=[(0,-1),(2,1),(1,1),(3,-1)]
 for j,m in enumerate(m3):
  for g in range(4):
   target,sgn=mu[g];o,c=prod(m,gens[g]);row=35*g+ix[o];rows.setdefault(row,{})[j]=rows.get(row,{}).get(j,K.zero)+c
   o,c=prod(gens[target],m);row=35*g+ix[o];rows.setdefault(row,{})[j]=rows.get(row,{}).get(j,K.zero)-sgn*c
 rows={r:{j:c for j,c in rr.items() if c} for r,rr in rows.items()};rows={r:rr for r,rr in rows.items() if rr}
 M=DomainMatrix(rows,(140,20),K);ns=M.nullspace().to_list()
 return m3,ns,prod

def main():
 t=S.Symbol('t');exception_orders=set();universal=[]
 for m in mons(3):
  aa,b,c,d=m;exponent=b+c-2*d;sign=(-1)**(d+1)
  if exponent==0:
   if sign==1:universal.append(m)
  else:
   for N in range(1,13):
    if (sign==1 and exponent%N==0) or (sign==-1 and N%2==0 and exponent%N==N//2):exception_orders.add(N)
 assert exception_orders=={1,2,3,4,6,8}
 assert set(universal)=={(0,2,0,1),(0,1,1,1),(0,0,2,1)}
 results=[]
 for N in sorted(exception_orders):
  if N==1:K=S.QQ;a=K.one
  elif N==2:K=S.QQ;a=-K.one
  else:K=S.QQ.algebraic_field(S.CRootOf(S.cyclotomic_poly(N,t),0));a=K.unit
  m3,ns,prod=calc(K,a)
  assert len(ns)==(1 if N in [1,2] else 0)
  if ns:
   v=ns[0];first=next(c for c in v if c);v=[c/first for c in v]
   expected={(0,1,1,1):K.one} if N==1 else {(0,0,2,1):K.one,(0,2,0,1):-K.one}
   assert {m:c for m,c in zip(m3,v) if c}==expected
  results.append({'primitive_order':N,'dimension_W1':len(ns)})
 A=S.Symbol('A');K=S.QQ.frac_field(A);m3,ns,prod=calc(K,K.gens[0]);assert not ns
 gens=[tuple(int(i==j) for i in range(4)) for j in range(4)]
 for i,j,k in itertools.product(range(4),repeat=3):
  ij,c1=prod(gens[i],gens[j]);lhs,c2=prod(ij,gens[k])
  jk,d1=prod(gens[j],gens[k]);rhs,d2=prod(gens[i],jk)
  assert lhs==rhs and c1*c2==d1*d2
 # The quantum three-space top is negated by tau=(-x,w,u).
 top={(0,1,2):K.one,(0,2,1):K.one,(1,0,2):-K.gens[0]**-1,
      (1,2,0):K.gens[0]**-2,(2,0,1):-K.gens[0]**-1,(2,1,0):K.gens[0]**-2}
 perm=[0,2,1]
 transformed={tuple(perm[i] for i in word):-co for word,co in top.items()}
 assert transformed=={word:-co for word,co in top.items()}
 data={'family':'T3[y;sigma], T3=(u*x=a*x*u,w*x=a*x*w,u*w=-w*u); sigma(x)=-a^-2*x,sigma(u)=-a*w,sigma(w)=-a*u',
       'Nakayama':'mu(x)=-x,mu(y)=-y,mu(u)=w,mu(w)=u',
       'x_filter_exception_orders':sorted(exception_orders),
       'finite_W1':results,
       'nonzero_W1':{'a=1':'span(u*w*y)','a=-1':'span((w^2-u^2)*y)'},
       'result':'Every envelope in this explicit all-parameter monomial Ore family excluded: W1 zero or every cubic factors by y.',
       'scope':'This is one explicit trimmed Ore family, not coverage of all common-plane or nontrimmed double Ore data.'}
 path=Path(__file__).with_name('cubic_order2_trimmed_Ore_certificate.json')
 if path.exists():assert json.loads(path.read_text())==data
 else:path.write_text(json.dumps(data,indent=2)+'\n')
 print('PASS generic and all exceptional W1, PBW triple products, top character; entire explicit Ore family excluded')

if __name__=='__main__':main()
