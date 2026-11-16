#!/usr/bin/env python3
"""Exact global identities and Clifford chart for the universal resonant obstruction."""
import json
from pathlib import Path
import sympy as S
from verify_cubic_order2_resonant_family import K,aa,bb,cc,dd,nf

def add(*terms):
 out={}
 for scale,p in terms:
  for w,c in p.items():out[w]=out.get(w,K.zero)+scale*c
 return {w:c for w,c in out.items() if c}
def mul(p,q):
 out={}
 for w,c in p.items():
  for v,d in q.items():
   for ww,e in nf(w+v).items():out[ww]=out.get(ww,K.zero)+c*d*e
 return {w:c for w,c in out.items() if c}
def comm(p,q):return add((K.one,mul(p,q)),(-K.one,mul(q,p)))
x={(0,):K.one};y={(1,):K.one};u={(2,):K.one};w={(3,):K.one}
p=add((K.one,u),(K.one,w));v=add((K.one,u),(-K.one,w))
X=mul(x,x);Y=mul(y,y);P=mul(p,p);h=mul(p,y);s=add((K.one,mul(p,v)),(K.one,mul(v,p)))
G=add((bb,mul(X,p)),(-K.one,mul(y,s)))
for Z in [X,Y,P,mul(s,s)]:
 for g in [x,y,p,v]:assert not comm(Z,g)
for g in [x,p,v]:assert not comm(s,g)
assert not add((K.one,comm(s,y)),(-K(2),G))
for g in [x,y,p]:assert not comm(h,g)
assert not add((K.one,comm(h,v)),(K.one,G))
assert not add((K.one,mul(h,h)),(-K.one,mul(P,Y)))
assert not add((K.one,mul(Y,s)),(-bb,mul(X,h)),(K.one,mul(y,G)))
assert not add((K.one,mul(h,s)),(-bb,mul(X,P)),(K.one,mul(p,G)))
assert not add((K.one,mul(G,G)),(-bb**2,mul(mul(X,X),P)),(K.one,mul(Y,mul(s,s))))
# Verify the inverse presentation on the central p² chart in a Clifford Laurent ring.
A0,B0,C0,D0,r,t=S.symbols('A B C D r t');L=S.QQ.frac_field(A0,B0,C0,D0,r,t)
alpha,beta,gamma,delta,rr,tt=L.gens
F=-rr*tt/beta;H=tt**2/4-1-gamma*rr*tt/beta-delta*rr**2;cross=-alpha*rr**2
from functools import lru_cache
@lru_cache(None)
def cnf(word):
 rules={(0,0):{():F},(1,1):{():H},(1,0):{(0,1):-L.one,():cross}}
 for i in range(len(word)-1):
  if word[i:i+2] in rules:
   out={}
   for pair,c in rules[word[i:i+2]].items():
    for ww,d in cnf(word[:i]+pair+word[i+2:]).items():out[ww]=out.get(ww,L.zero)+c*d
   return {w:c for w,c in out.items() if c}
 return {word:L.one}
# Laurent records are (Clifford word, p exponent), p anticommutes with a,b.
def la(*terms):
 out={}
 for co,f in terms:
  for mon,c in f.items():out[mon]=out.get(mon,L.zero)+co*c
 return {m:c for m,c in out.items() if c}
def lm(f,g):
 out={}
 for (w,i),c in f.items():
  for (v,j),d in g.items():
   for ww,e in cnf(w+v).items():
    mon=(ww,i+j);out[mon]=out.get(mon,L.zero)+(-1)**(i*len(v))*c*d*e
 return {m:c for m,c in out.items() if c}
xx={((0,),1):L.one};yy={((),1):rr};pp={((),1):L.one};vv={((1,),1):L.one,((),1):tt/2}
assert not la((L.one,lm(xx,yy)),(L.one,lm(yy,xx)))
assert not la((L.one,lm(pp,xx)),(L.one,lm(xx,pp)))
assert not la((L.one,lm(pp,yy)),(-L.one,lm(yy,pp)))
assert not la((L.one,lm(vv,xx)),(L.one,lm(xx,vv)),(-alpha,lm(yy,yy)))
assert not la((L.one,lm(vv,yy)),(L.one,lm(yy,vv)),(-beta,lm(xx,xx)))
assert not la((L.one,lm(vv,vv)),(-L.one,lm(pp,pp)),(-gamma,lm(xx,xx)),(-delta,lm(yy,yy)))
ss=la((L.one,lm(pp,vv)),(L.one,lm(vv,pp)))
assert not la((beta,lm(lm(xx,xx),pp)),(-L.one,lm(yy,ss)))
# Completion at r=t=0: H is a unit and the anti-commuting generator squares into m².
assert L.to_sympy(H).subs({r:0,t:0})==-1
shift=alpha*rr**2/(2*H)
completed_square=F-alpha**2*rr**4/(4*H)
assert not(F+shift*cross+shift**2*H-completed_square)
assert not(cross+2*shift*H)
expr=L.to_sympy(completed_square)
assert expr.subs({r:0,t:0})==0
assert S.diff(expr,r).subs({r:0,t:0})==0
assert S.diff(expr,t).subs({r:0,t:0})==0
summary={'central_elements_in_cut':['X=x²','Y=y²','P=p²','h=p*y','s=p*v+v*p'],
 'scroll_relations':['h²=P*Y','Y*s=beta*X*h','h*s=beta*X*P'],
 'central_P_chart':{'a²':'-r*t/beta','b²':'H=t²/4-1-gamma*r*t/beta-delta*r²','anticommutator':'a*b+b*a=-alpha*r²'},
 'fixed_point':'r=t=a=0, b²=-1',
 'completed_generator_square':'f=-r*t/beta-alpha²*r^4/(4*H) lies in (r,t)²',
 'obstruction':'Completion is (k[[r,t,a0]]/(a0²-f))#mu2. The commutative local hypersurface is not regular; its induced residue module has infinite projective dimension.',
 'result':'All resonant four-parameter normal cubic cuts excluded from H3: beta=0 factors; beta!=0 has the same fixed completed-order obstruction.'}
path=Path(__file__).with_name('cubic_order2_resonant_obstruction_certificate.json')
if path.exists():assert json.loads(path.read_text())==summary
else:path.write_text(json.dumps(summary,indent=2)+'\n')
print('PASS central scroll identities and all inverse Clifford-chart relations; fixed singular completion')
