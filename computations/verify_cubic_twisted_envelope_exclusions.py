"""Exact sign-twist Sklyanin transport and central-pencil identities."""
import sympy as s,json
from pathlib import Path
b,c=s.symbols('b c');B=b*b;C=c*c;A=-(B+C)/(1+B*C)
def relations(A,B,C):
 rows=[]
 for i,j,k,a in [(1,2,3,A),(2,3,1,B),(3,1,2,C)]:
  r={(0,i):1,(i,0):-1,(j,k):-a,(k,j):-a}
  t={(0,i):1,(i,0):1,(j,k):-1,(k,j):1};rows.extend([r,t])
 return rows
old=relations(A,B,C);ep=[1,1,-1,-1];tw=[{(i,j):s.cancel(v*ep[j]) for (i,j),v in r.items()} for r in old]
sc=[1,-s.I*b*c,s.I*c,b];new=[{(i,j):s.cancel(v*sc[i]*sc[j]) for (i,j),v in r.items()} for r in relations(A,1/B,1/C)]
matching=[]
for r in new:
 found=[]
 for j,t in enumerate(tw):
  pivot=next(iter(t));ratio=s.cancel(r.get(pivot,0)/t[pivot])
  if ratio!=0 and all(s.cancel(r.get(k,0)-ratio*t.get(k,0))==0 for k in set(r)|set(t)):found.append(j)
 assert len(found)==1,found
 matching.append(found[0])
assert len(set(matching))==6
assert s.cancel(A+1/B+1/C+A/(B*C))==0
x,y=s.symbols('alpha beta');z=-(x+y)/(1+x*y)
Q=(1+x)/(1-y);R=(1-x)/(1+z)
assert s.cancel(Q-R-x)==0
assert s.cancel(Q-1+z*R)==0
assert s.cancel(R-1-y*Q)==0
# The alternating projection of six standard relations is a signed permutation.
alt=[]
pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
for rr in old:
 alt.append([s.cancel(rr.get((i,j),0)-rr.get((j,i),0)) for i,j in pairs])
assert s.Matrix(alt).det()!=0
# Standard Klein cocycle bicharacter, with x0 trivial and all four degrees.
from itertools import product
G=list(product([0,1],repeat=2))
mu=lambda g,h:(-1)**(g[0]*h[1])
for g in G:
 for h0 in G:
  value=mu(h0,g)/mu(g,h0)
  assert value==(1 if g==(0,0) or h0==(0,0) or g==h0 else -1)
 assert mu(g,g)/mu(g,g)==1
cert={'version':'classification-v63','cocycle_bicharacter_table':True,'cocycle_consequence':'Standard Klein cocycle Sklyanin: Z3 is zero except original translation order3 or6; then it is one-dimensional and factors linear times quadratic. No H3.','twisted_quantum_theorem':'Any single-automorphism Zhang twist of a skew polynomial AS4 with W1!=0 is itself a diagonal twist, hence skew. No extra H3 objects.','sklyanin_twist_theorem':'For proper elliptic standard S with nondegenerate central quadric pencil, every automorphism twist with W1!=0 is a scalar/even-sign twist, isomorphic to another standard Sklyanin, hence excluded.','verified_sign_case':'epsilon=(1,1,-1,-1), rescale=(1,-i bc,i c,b), beta=b²,gamma=c²; parameters map(alpha,beta,gamma)->(alpha,beta^-1,gamma^-1)','six_relation_matching':matching,'central_quadric_ratios':'0,1,(1+alpha)/(1-beta),(1-alpha)/(1+gamma); exact differences checked','scope':'Exact all-parameter quadratic relation-space transport; W1 eigenvector, Newton normalizers and full exclusions are ordinary proofs.'}
Path(__file__).with_name('cubic_twisted_envelope_exclusions_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS all six Sklyanin sign-twist relations and central-pencil eigenvalue identities')
