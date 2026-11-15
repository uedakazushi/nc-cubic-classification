"""Weighted vertex quantum Heisenberg model and normal initial Casimir."""
import sympy as s,json
from functools import lru_cache
from pathlib import Path
q=s.symbols('q');h=q*q-1
rules={(1,0):[(q**-3,(0,1)),(-q**-2,(2,))],(2,0):[(q**-1,(0,2))],(2,1):[(q,(1,2))]}
@lru_cache(None)
def nf(w):
 for j in range(len(w)-1):
  if w[j]>w[j+1]:
   out={}
   for a,v in rules[w[j:j+2]]:
    for u,c in nf(w[:j]+v+w[j+2:]).items():out[u]=s.cancel(out.get(u,0)+a*c)
   return {u:c for u,c in out.items() if c!=0}
 return {w:s.Integer(1)}
def add(f,g,a=1):
 out=dict(f)
 for w,c in g.items():out[w]=s.cancel(out.get(w,0)+a*c)
 return {w:c for w,c in out.items() if c!=0}
def mul(f,g):
 out={}
 for u,a in f.items():
  for v,b in g.items():
   for w,c in nf(u+v).items():out[w]=s.cancel(out.get(w,0)+a*b*c)
 return {w:c for w,c in out.items() if c!=0}
def branch(w,j):
 out={}
 for a,v in rules[w[j:j+2]]:
  for u,c in nf(w[:j]+v+w[j+2:]).items():out[u]=s.cancel(out.get(u,0)+a*c)
 return {w:c for w,c in out.items() if c!=0}
assert not add(branch((2,1,0),0),branch((2,1,0),1),-1)
a,b,t=[{(j,):1} for j in range(3)]
g=add(mul(a,b),mul(b,a),-q)
assert not add(mul(g,a),mul(a,g),-q**-3)
assert not add(mul(g,b),mul(b,g),-q**3)
assert not add(mul(g,t),mul(t,g),-1)
g0=add(mul(a,b),t,q/h) # g0=q^-1 ab+s/h, scaled by q.
assert not add(g0,g,-q*q/h)
# Formal coordinate changes killing a^i b^j in ab-qba.
checks=[]
for i in range(6):
 for j in range(6):
  if i+j<3:continue
  ca=1-q**(1-i) if j>=1 else None
  cb=1-q**(1-j) if i>=1 else None
  assert not (ca==0 and cb==0)
  checks.append([i,j])
cert={'version':'classification-v56','weighted_B':'w(x)=0,w(y)=w(z)=1,w(t)=2; PBW reductions do not decrease weight','vertex_gr':'as=qsa,bs=q^-1sb,q^-1ab-q²ba=s','initial_Casimir':'g0=q^-1 ab+s/(q²-1)=q/(q²-1)*(ab-qba)','exact_checks':['only Ore diamond sba','normal initial Casimir with scalars q^-3,q^3','initial quotient quantum plane identity','coordinate-change coefficients on degrees3..10 monomials'],'ordinary_theorems':'Formal vertex microchart has gr quantum plane and gldim2 for every q!=0,+-1,D. For nonroot q all higher relation terms can be killed formally, giving completed quantum plane.','limits':'This is a formal vertex statement; global qgr perfection descent and full good-D nonroot admissibility not inferred.'}
Path(__file__).with_name('cubic_quantum_triangle_vertex_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS weighted vertex Ore diamond and normal initial Casimir')
