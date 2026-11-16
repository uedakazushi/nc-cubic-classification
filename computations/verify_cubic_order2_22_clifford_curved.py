"""Universal curved Clifford PBW, exact normal kernel, scroll and quartic checks."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
h0,h1,h2=S.symbols('h0 h1 h2')
rules={(1,0):{(0,1):1},(2,0):{(0,2):-1},(2,1):{(1,2):-1},(3,0):{(0,3):-1},(3,1):{(1,3):-1},(3,2):{(2,3):-1,(0,0):h0,(0,1):2*h1,(1,1):h2}}
@lru_cache(None)
def nf(w):
 for i in range(len(w)-1):
  if w[i:i+2] in rules:
   out={}
   for m,c in rules[w[i:i+2]].items():
    for v,d in nf(w[:i]+m+w[i+2:]).items():out[v]=out.get(v,0)+c*d
   return {v:S.expand(c) for v,c in out.items() if S.expand(c)}
 return {w:S.Integer(1)}
overlap=0
for w in itertools.product(range(4),repeat=3):
 if w[:2] not in rules or w[1:] not in rules:continue
 out={}
 for i,sgn in [(0,1),(1,-1)]:
  for m,c in rules[w[i:i+2]].items():
   for v,d in nf(w[:i]+m+w[i+2:]).items():out[v]=out.get(v,0)+sgn*c*d
 assert all(S.expand(c)==0 for c in out.values());overlap+=1
E=[w for w in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in w)%2==0]
rows=list(itertools.combinations_with_replacement(range(4),4));idx={w:i for i,w in enumerate(rows)}
N=S.zeros(4*len(rows),len(E))
for j,w in enumerate(E):
 for i in range(4):
  # G*i - mu^-1(i)*G
  for raw,c in [(w+(i,),1),((i,)+w,-1 if i<2 else 1)]:
   for v,d in nf(raw).items():N[i*len(rows)+idx[v],j]+=c*d
normal=[w for w in E if w not in [(0,2,3),(1,2,3)]]
assert all(N[:,E.index(w)]==S.zeros(4*len(rows),1) for w in normal)
minor=S.expand(N.extract([2*len(rows)+idx[(0,2,2,3)],2*len(rows)+idx[(1,2,2,3)]],[E.index((0,2,3)),E.index((1,2,3))]).det())
assert minor==4
s,t,lam,mu=S.symbols('s t lam mu');a,b,c,d=S.symbols('a b c d');X,Y,Z=S.symbols('X Y Z')
f2=a*s*s+b*s*t+c*t*t;g2=d*t*t
A=-mu*t-lam*f2;B=mu*s-lam*g2;h=lam*(h0*s*s+2*h1*s*t+h2*t*t)
q=S.Matrix([[lam,0,0],[0,A,h/2],[0,h/2,B]])
F=4*(-Y*Z-a*X*X-b*X*Y-c*Y*Y)*(X*Z-d*Y*Y)-(h0*X*X+2*h1*X*Y+h2*Y*Y)**2
assert S.expand(F.subs({X:lam*s,Y:lam*t,Z:mu})-4*lam*q.det())==0
assert S.expand((A*B-h*h/4).subs(lam,0))==-mu**2*s*t
example=S.expand(F.subs({a:1,b:0,c:0,d:1,h0:0,h1:S.Rational(1,2),h2:0}))
f=example.subs(X,1)
assert list(S.groebner([f,S.diff(f,Y),S.diff(f,Z)],Y,Z))==[1]
assert S.diff(example,Z).subs({X:0,Y:1})==4
assert S.Poly(example.subs(Z,1),X,Y).coeff_monomial(X*Y)==-4
assert all(S.Poly(example.subs(Z,1),X,Y).coeff_monomial(m)==0 for m in [1,X,Y,X**2,Y**2])
out={'status':'PASS','scope':'B_h: commuting positive generators, anticommuting cross, uv+vu=h2(U); independent linear coefficients of u2,v2', 'universal_PBW_overlaps':overlap,'positive_cubic_dimension':len(E),'normal_basis':['x3','x2y','xy2','y3','xu2','yu2','xv2','yv2'],'complement_minor':str(minor),'quartic_identity':'F4(lambda*s,lambda*t,mu)=4*lambda*det(q)','exceptional_residual_discriminant':'-mu^2*s*t','example_quartic':str(example),'example_singularities':'only [0:0:1], ordinary node','not_claimed':['full nonzero-positive-top coverage','dependent linear-coefficient cuts','global intrinsic family descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_clifford_curved_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: universal PBW, eight-dimensional normal kernel (minor4), scroll determinant, nodal example')
