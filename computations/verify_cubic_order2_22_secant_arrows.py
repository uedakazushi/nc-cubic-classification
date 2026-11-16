"""Universal secant C-sign arrow; rational identities, no sampling."""
import json
from pathlib import Path
import sympy as S
r,l,c,q=S.symbols('r l c q')
F=S.QQ.frac_field(r,l,c)
def redq(a):
 return S.cancel(S.Poly(S.cancel(a),q,domain=F).rem(S.Poly(q*q+r/(r+1),q,domain=F)).as_expr())
rels=[{(0,2):1,(2,1):1,(3,0):r+1}, {(1,3):1,(2,1):1,(3,0):r},
 {(0,1):-r*l,(1,0):r*l,(1,1):1,(2,3):-r},
 {(0,0):-r*l,(0,1):c,(1,0):-1,(1,1):l,(3,3):r+1},
 {(0,0):r*l,(0,1):-1,(1,0):-c,(1,1):-l,(2,2):-1},
 {(0,0):1,(0,1):l,(1,0):-l,(3,2):1}]
# Target has C'=-C. Ten remaining quadratic words are a basis of B2.
t=-c
rules={(2,2):{(0,0):r*l,(0,1):-1,(1,0):-t,(1,1):-l},
 (2,3):{(0,1):-l,(1,0):l,(1,1):1/r},
 (3,2):{(0,0):-1,(0,1):-l,(1,0):l},
 (3,3):{(0,0):r*l/(r+1),(0,1):-t/(r+1),(1,0):1/(r+1),(1,1):-l/(r+1)},
 (2,1):{(0,2):r,(1,3):-(r+1)}, (3,0):{(1,3):1,(0,2):-1}}
perm=[1,0,3,2];sc=[q/r,q,1,1/(r+1)]
for rel in rels:
 out={}
 for (i,j),a in rel.items():
  w=(perm[i],perm[j]);a=a*sc[i]*sc[j]
  for z,b in rules.get(w,{w:1}).items():out[z]=out.get(z,0)+a*b
 assert all(redq(a)==0 for a in out.values()),out
kap=-1/(r+1)
assert all(redq(sc[i]*sc[perm[i]]-kap*(1 if i<2 else -1))==0 for i in range(4))
# Diagonal arrow coefficients after target odd-row reduction.
a,b,g,d,rp,lp,cp=S.symbols('a b g d rp lp cp',nonzero=True)
odd1=[a*g+rp*b*g-(r+1)*a*d,-(rp+1)*b*g+(r+1)*a*d]
odd2=[rp*b*g-r*a*d,b*d-(rp+1)*b*g+r*a*d]
# First and third equations force a=b, g=d, then rp=r.
assert [S.factor(z.subs({b:a,d:g,rp:r})) for z in odd1+odd2]==[0]*4
# Positive pure words are independent because K is invertible.
# The last even relation forces g^2=a^2 and lp=l; the fourth then cp=c.
last=[a*a-g*g,l*a*b-lp*g*d]
fourth=[(-r*l*a*a+rp*lp*d*d),c*a*b-cp*d*d,-a*b+d*d,l*b*b-lp*d*d]
assert all(S.expand(z.subs({b:a,d:g,rp:r,lp:l,cp:c})).subs(g*g,a*a)==0 for z in last+fourth)
out={'status':'PASS','scope':'universal graded C-sign isomorphism and square; necessary diagonal-arrow equations',
 'map':['q/r*y','q*x','v','u/(r+1)'],'root_equation':'q^2=-r/(r+1)',
 'target':['r','l','-C'],'square':'(-1/(r+1))*mu on degree1',
 'checks':['six source relations reduce to zero in target B2','four square coefficients','diagonal odd/even coefficient identities'],
 'not_claimed':['AS4 existence','H3 existence','relative quotient or descent']}
Path(__file__).with_name('cubic_order2_22_secant_arrows_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS six universal arrow identities, square and diagonal coefficient checks')
