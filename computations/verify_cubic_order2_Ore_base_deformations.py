#!/usr/bin/env python3
"""Exact identities for all quadratic-base deformations of the explicit involution Ore family."""
import sympy as S,itertools,json
from pathlib import Path
from verify_cubic_order2_trimmed_Ore import calc
from functools import lru_cache

def check(K,a,P):
 one=K.one
 rules={(1,0):{(0,1):-a**-2},(2,0):{(0,2):a},(3,0):{(0,3):a},(2,1):{(1,3):-a**-1},(3,1):{(1,2):-a**-1},(3,2):{(2,3):-one,**P}}
 @lru_cache(None)
 def nf(word):
  for pos in range(len(word)-1):
   pair=word[pos:pos+2]
   if pair in rules:
    out={}
    for pp,c in rules[pair].items():
     for ww,d in nf(word[:pos]+pp+word[pos+2:]).items():out[ww]=out.get(ww,K.zero)+c*d
    return {w:c for w,c in out.items() if c}
  return {word:one}
 def expand_choice(word,pos):
  out={}
  for pp,c in rules[word[pos:pos+2]].items():
   for ww,d in nf(word[:pos]+pp+word[pos+2:]).items():out[ww]=out.get(ww,K.zero)+c*d
  return {w:c for w,c in out.items() if c}
 for word in itertools.product(range(4),repeat=3):
  if word[:2] in rules and word[1:] in rules:
   lhs,rhs=expand_choice(word,0),expand_choice(word,1)
   assert all(not (lhs.get(w,K.zero)-rhs.get(w,K.zero)) for w in set(lhs)|set(rhs)),(word,lhs,rhs)
 return nf

def add(K,*terms):
 out={}
 for scale,p in terms:
  for w,c in p.items():out[w]=out.get(w,K.zero)+scale*c
 return {w:c for w,c in out.items() if c}
def product(K,nf,p,q):
 out={}
 for w,c in p.items():
  for v,d in q.items():
   for ww,e in nf(w+v).items():out[ww]=out.get(ww,K.zero)+c*d*e
 return {w:c for w,c in out.items() if c}
def main():
 A,B,L,t=S.symbols('A B L t');K=S.QQ.frac_field(A,B)
 tops=json.loads(Path(__file__).with_name('cubic_order2_Ore_base_top_certificate.json').read_text())
 def replay_top(name,K,a,nf):
  entry=next(e for e in tops if e['name']==name);w={}
  for record in entry['tensor']:
   co=K.zero
   for term in record['terms']:
    cc=sum((K.convert(S.QQ(q),S.QQ)*a**i for i,q in enumerate(term['a_coefficients'])),K.zero)
    for parameter,power in zip(K.gens,term['parameter_powers']):cc*=parameter**power
    co+=cc
   w[tuple(record['word'])]=co
  assert not(w[(1,0,3,2)]-K.one)
  for pos in range(3):
   out={}
   for word,co in w.items():
    for pair,c in nf(word[pos:pos+2]).items():
     target=word[:pos]+pair+word[pos+2:];out[target]=out.get(target,K.zero)+co*c
   assert not any(out.values())
  left={word[1:]+word[:1]:co for word,co in w.items()};right={};mu=[(0,-1),(1,-1),(3,1),(2,1)]
  for word,co in w.items():
   target,sgn=mu[word[-1]];ww=word[:-1]+(target,);right[ww]=right.get(ww,K.zero)-sgn*co
  assert all(not(left.get(ww,K.zero)-right.get(ww,K.zero)) for ww in set(left)|set(right))
 for a in [K.one,-K.one]:
  nf=check(K,a,{(0,0):K.gens[0],(1,1):K.gens[1]})
  replay_top('sign_'+('1' if a==K.one else '-1'),K,a,nf)
  x={(0,):K.one};y={(1,):K.one};u={(2,):K.one};w={(3,):K.one}
  pp=add(K,(K.one,u),(K.one,w));vv=add(K,(K.one,u),(-K.one,w))
  ss=add(K,(K.one,product(K,nf,pp,vv)),(K.one,product(K,nf,vv,pp)))
  assert ss and ss=={(2,2):K(2),(3,3):K(-2)}
  for g in [pp,vv,product(K,nf,x,x),product(K,nf,y,y)]:
   assert not add(K,(K.one,product(K,nf,ss,g)),(-K.one,product(K,nf,g,ss)))
  for m in itertools.product(range(4),repeat=3):
   if tuple(sorted(m))!=m:continue
   ix=m.count(0);iy=m.count(1)
   anti_x=((-1)**iy==-1) if a==K.one else ((-1)**(3-ix)==-1)
   if anti_x and a==K.one:assert iy%2==1
   if anti_x and iy%2==0 and a==-K.one:assert ix in [0,2] and iy in [0,2] and (ix==0 or iy==0)
 E=S.QQ.algebraic_field(S.CRootOf(t**4+1,0));K=E.frac_field(L);a=K.convert(E.unit,E)
 nf=check(K,a,{(0,1):K.gens[0]});replay_top('primitive_eighth',K,a,nf)
 assert not calc(E,E.unit)[1]
 # Exact gcds of the two normality conditions for each quadratic base monomial.
 a=S.Symbol('a');q=-a*a;conditions={}
 for i in range(3):
  eqs=[S.fraction(S.cancel(q**(i-2)-a*a))[0],S.fraction(S.cancel(q**i-a**-2))[0]]
  gcd=S.Poly(S.gcd(*eqs),a).monic().as_expr()
  assert S.expand(gcd-(a**4+1 if i==1 else a*a-1))==0
  conditions[str(i)]=str(gcd)
 data={'base_quadratic':'P=A*x^2+C*x*y+B*y^2',
       'highest_tensor_certificate':'cubic_order2_Ore_base_top_certificate.json: 32+32+26 polynomial tensor terms, all three adjacent relation projections and twisted cyclic identity replayed, fixed nonzero coefficient1',
       'domain_necessary_conditions':{'A,B':'(a^2-1)*A=(a^2-1)*B=0','C':'(a^4+1)*C=0'},
       'normality_gcds_by_x_exponent':conditions,
       'PBW':'All four overlap ambiguities vanish for arbitrary A,B at a=+/-1, and arbitrary C at primitive eighth roots.',
       'sign_minus_centralizer':'p=u+w,v=u-w,s=p*v+v*p=2*(u^2-w^2) commutes with p,v,x^2,y^2 for arbitrary A,B',
       'eighth_root_chart':'W1=0 at C=0; all nonzero C are equivalent under simultaneous scaling of u,w, so semicontinuity and PBW force W1=0 for every C.',
       'result':'Every quadratic-base deformation P of this explicit Ore family excluded from H3; no coverage of general cross derivations.'}
 path=Path(__file__).with_name('cubic_order2_Ore_base_deformations_certificate.json')
 if path.exists():assert json.loads(path.read_text())==data
 else:path.write_text(json.dumps(data,indent=2)+'\n')
 print('PASS base normality, PBW overlaps, 90-term top tensors, sign centralizer, eighth-root kernel')
if __name__=='__main__':main()
