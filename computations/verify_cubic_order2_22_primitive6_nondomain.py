"""Primitive6 normal cuts: explicit order3 norm produces zero divisors after Ore localization."""
import json
from functools import lru_cache
from pathlib import Path
import sympy as S
lv=(1+S.sqrt(-3))/2;F=S.QQ.algebraic_field(lv);lf=F.from_sympy(lv)
R=F.poly_ring('alpha','beta');alpha,beta=R.gens;l=R(lf);li=R.one-l;omega=l*l
# Laurent u-normal form: x=0,y=1,v=2,u=3,u^-1=4, with u-powers at the right.
rules={(1,0):{(0,1):R.one,(3,3):-alpha,(2,2):-beta},(3,2):{(2,3):-R.one},(4,2):{(2,4):-R.one},(3,0):{(0,3):l},(3,1):{(1,3):li},(4,0):{(0,4):li},(4,1):{(1,4):l},(2,0):{(0,2):li},(2,1):{(1,2):l},(3,4):{():R.one},(4,3):{():R.one}}
@lru_cache(None)
def nf(word):
 for pos in range(len(word)-1):
  if word[pos:pos+2] in rules:
   out={}
   for mid,c in rules[word[pos:pos+2]].items():
    for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,R.zero)+c*d
   return {w:c for w,c in out.items() if c}
 return {word:R.one}
def add(*terms):
 out={}
 for expr,c in terms:
  for w,d in expr.items():out[w]=out.get(w,R.zero)+c*d
 return {w:c for w,c in out.items() if c}
def mul(A,B):
 out={}
 for w,a in A.items():
  for v,b in B.items():
   for t,c in nf(w+v).items():out[t]=out.get(t,R.zero)+a*b*c
 return {w:c for w,c in out.items() if c}
def power(A,n):
 out={():R.one}
 for _ in range(n):out=mul(out,A)
 return out
one={():R.one};X=nf((0,4));Y=nf((1,4));V=nf((2,4))
assert not add((mul(V,X),R.one),(mul(X,V),-l))
assert not add((mul(V,Y),R.one),(mul(Y,V),-li))
assert not add((mul(X,Y),R.one),(mul(Y,X),-omega),(one,-l*alpha),(power(V,2),l*beta))
assert not add((nf((0,0,0,4,4,4)),R.one),(power(X,3),R.one))
assert not add((nf((1,1,1,4,4,4)),R.one),(power(Y,3),R.one))
delta=(R.one-2*l)*alpha/3;gamma=(l-2)*beta/3
C=add((mul(Y,X),R.one),(one,delta),(power(V,2),gamma))
assert not add((mul(X,C),R.one),(mul(C,X),-omega))
assert not add((mul(Y,C),R.one),(mul(C,Y),-(li*li)))
assert not add((mul(V,C),R.one),(mul(C,V),-R.one))
assert not add((mul(X,Y),R.one),(C,-omega),(one,delta),(power(V,2),gamma*li*li))
# All remaining computations take place in the freely embedded commutative base.
K=F.frac_field('alpha','beta','C','V','r');aa,bb,cc,vv,rr=K.gens
ll=K(lf);ww=ll*ll;dl=(1-2*ll)*aa/3;gm=(ll-2)*bb/3
aval=cc-dl-gm*vv*vv
P=cc**3-dl**3-gm**3*vv**6-3*dl*gm*cc*vv**2
ring=K.field.ring
def sigma(c,n=1):
 def transform(p):return ring.from_dict({m:a*lf**(2*n*m[2]-n*m[3]) for m,a in p.items()})
 return K(transform(c.numer))/K(transform(c.denom))
assert not (sigma(aval,3)-aval)
assert not (aval*sigma(aval)*sigma(aval,2)-P)
assert not (aval*sigma(aval,2)*sigma(aval,4)-P) and not (sigma(P)-P)
assert not (aval*sigma(aval,-1)*sigma(aval,-2)-P)
# Monic Laurent quotient K[X^+/-1;sigma]/(X^6-r^3*P), free of dimension6.
constant=rr**3*P
assert constant and aval
Z={2:1/(rr*aval)}
def product(A,B):
 out={}
 for i,a in A.items():
  for j,b in B.items():
   n=i+j;c=a*sigma(b,i)
   if n>=6:n-=6;c*=constant
   out[n]=out.get(n,K.zero)+c
 return {n:c for n,c in out.items() if c}
def summ(*terms):
 out={}
 for A,c in terms:
  for n,a in A.items():out[n]=out.get(n,K.zero)+c*a
 return {n:a for n,a in out.items() if a}
Z2=product(Z,Z);Z3=product(Z2,Z);assert set(Z3)=={0} and not (Z3[0]-K.one)
left=summ((Z,K.one),({0:K.one},-K.one));right=summ((Z2,K.one),(Z,K.one),({0:K.one},K.one))
assert set(left)=={0,2} and set(right)=={0,2,4} and not product(left,right)
out={'status':'PASS','scope':'every primitive6 cut A*x^3+B*y^3 with A*B!=0, all alpha,beta',
 'dehomogenization':['VX=lambda*XV','VY=lambda^-1*YV','XY-lambda^2*YX=lambda*alpha-lambda*beta*V^2'],
 'GWA_base':'k[C,V], sigma(C)=lambda^2*C, sigma(V)=lambda^-1*V',
 'delta':'(1-2*lambda)*alpha/3','gamma':'(lambda-2)*beta/3',
 'norm':'P=C^3-delta^3-gamma^3*V^6-3*delta*gamma*C*V^2',
 'cut_ratio':'r^3=-B/A','localized_relation':'X^6=r^3*P',
 'zero_divisor':'Z=(r*(C-delta-gamma*V^2))^-1*X^2; Z^3=1',
 'nonzero_factor_supports':[[0,2],[0,2,4]],
 'conclusion':'the localization has zero divisors; the cubic quotient cannot be a domain and cannot be H3',
 'not_claimed':['global nonzero-top rank4 classification','all curved non-diagonal graphs']}
Path(__file__).with_name('cubic_order2_22_primitive6_nondomain_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS primitive6 nondomain: Laurent chart, exact 3-norm and two nonzero factors with zero product')
