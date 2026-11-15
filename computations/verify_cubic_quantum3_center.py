"""Exact PBW center identities for the three-torsion quantum Weyl chart."""
import sympy as s,json
from pathlib import Path
from functools import lru_cache
q,b1,b2,b3=s.symbols('q b1 b2 b3')
def red(c):return s.rem(s.expand(c),q*q+q+1,q).expand()
rules={(1,0):[(q*q,(0,1)),(-q*q*b3,())],(2,0):[(q,(0,2)),(b2,())],(2,1):[(q*q,(1,2)),(-q*q*b1,())]}
@lru_cache(None)
def nf(w):
 for i in range(len(w)-1):
  if w[i]>w[i+1]:
   out={}
   for a,v in rules[w[i:i+2]]:
    for u,c in nf(w[:i]+v+w[i+2:]).items():out[u]=red(out.get(u,0)+a*c)
   return {u:c for u,c in out.items() if c!=0}
 return {w:s.Integer(1)}
def mul(f,g):
 out={}
 for w,a in f.items():
  for v,b in g.items():
   for u,c in nf(w+v).items():out[u]=red(out.get(u,0)+a*b*c)
 return {u:c for u,c in out.items() if c!=0}
# 1/(q-1)=-(q+2)/3.
d=-(q+2)/3
O={(0,1,2):s.Integer(1),(0,):red(d*b1),(1,):red(q*d*b2),(2,):red(d*b3)}
O3=mul(mul(O,O),O)
def subtract(f,g):
 out=dict(f)
 for w,c in g.items():out[w]=red(out.get(w,0)-c)
 return {w:c for w,c in out.items() if c!=0}
for i in range(3):
 v={(i,):s.Integer(1)}
 assert not subtract(mul(O,v),mul(v,O))
 power={(i,i,i):s.Integer(1)}
 for j in range(3):assert not subtract(mul(power,{(j,):s.Integer(1)}),mul({(j,):s.Integer(1)},power))
e=-(2*q+1)/9
expected={(0,0,0,1,1,1,2,2,2):s.Integer(1),(0,0,0):e*b1**3,(1,1,1):e*b2**3,(2,2,2):e*b3**3}
for w,c in O.items():expected[w]=red(expected.get(w,0)+d*b1*b2*b3*c)
assert not subtract(O3,expected)
# The only overlap zyx resolves in both orders.
w=(2,1,0)
branches=[]
for pos in [0,1]:
 out={}
 for a,v in rules[w[pos:pos+2]]:
  for u,c in nf(w[:pos]+v+w[pos+2:]).items():out[u]=red(out.get(u,0)+a*c)
 branches.append(out)
assert not subtract(*branches)
result={'version':'classification-v26','relations':'yz=q*zy+b1; zx=q*xz+b2; xy=q*yx+b3; q^2+q+1=0','PBW_overlap_zyx':True,'central_generators':['X=x^3','Y=y^3','Z=z^3','Omega=xyz+(b1*x+q*b2*y+b3*z)/(q-1)'],'d':'1/(q-1)=-(q+2)/3','e':'-(2*q+1)/9','center_relation':'Omega^3-d*b1*b2*b3*Omega-X*Y*Z-e*(b1^3*X+b2^3*Y+b3^3*Z)=0','checks':'All 12 generator commutators and exact degree9 center relation','scope':'Exact polynomial identities over Q(q)[b1,b2,b3]; exhaustion of center by filtered leading terms proved separately.'}
Path(__file__).with_name('cubic_quantum3_center_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS PBW overlap, four central generators, full center relation')
