#!/usr/bin/env python3
"""Universal first-order central-cubic obstruction over QQ[h,alpha,1/h,1/(1+h^3)].
All99 inserted degree-four relations are checked symbolically, not sampled.
Full AS4/H3 recognition is an assumption in the obstruction theorem; these
low-degree checks are not a general AS-regularity certification.
"""
import sympy as s
from collections import defaultdict
h,ax,ay,az=s.symbols('h ax ay az');d=1+h**3
# (t power, active word, coefficient); all equations computed modulo t^2.
rules={
 (0,0):[(0,(1,2),1/h),(0,(2,1),1/h),(1,(0,),-ax/h)],
 (0,1):[(0,(1,0),-1),(0,(2,2),h),(1,(2,),az)],
 (0,2):[(0,(2,0),-1),(0,(1,1),h),(1,(1,),ay)],
 (1,1,2):[(0,(2,1,1),1),(1,(1,2),-h*h*ay/d),(1,(2,1),h*h*ay/d),(1,(2,0),h*az/d),(1,(0,2),-h*az/d),(1,(1,0),ax/d),(1,(0,1),-ax/d)],
 (1,2,2):[(0,(2,2,1),1),(1,(1,2),-h*h*az/d),(1,(2,1),h*h*az/d),(1,(0,1),h*ay/d),(1,(1,0),-h*ay/d),(1,(0,2),ax/d),(1,(2,0),-ax/d)]}
from functools import lru_cache
@lru_cache(None)
def normal(t,w):
 if t>=2:return {}
 for i in range(len(w)):
  for lead,rhs in rules.items():
   if w[i:i+len(lead)]!=lead:continue
   ans=defaultdict(lambda:s.Integer(0))
   for tt,ww,cc in rhs:
    for key,c in normal(t+tt,w[:i]+ww+w[i+len(lead):]).items():ans[key]+=cc*c
   return {key:s.cancel(c) for key,c in ans.items() if s.cancel(c)!=0}
 return {(t,w):s.Integer(1)}
def comm(P,x,t=0):
 out=defaultdict(lambda:s.Integer(0))
 for w,c in P.items():
  for sign,ww in [(1,w+(x,)),(-1,(x,)+w)]:
   for key,v in normal(t,ww).items():out[key]+=sign*c*v
 return {key:s.cancel(c) for key,c in out.items() if s.cancel(c)!=0}
g={(0,1,2):1,(2,2,2):-h/2,(1,1,1):h/2,(0,0,0):-h/2}
fun=[(1,(2,1,2)),(1,(2,2,0)),(2,(1,2,1))]
cs=[comm(g,i) for i in range(3)]
values=[s.factor(cs[i].get((1,w),0)) for i,w in fun]
assert all(s.cancel(a-b)==0 for a,b in zip(values,[-3*az/(2*d),3*h*ax/(2*d),3*ay/(2*d)]))
for q in [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]:
 assert all(comm({q:1},i,1).get((1,w),0)==0 for i,w in fun)
from itertools import product
rels=[[(0,(1,2),1),(0,(2,1),1),(0,(0,0),-h),(1,(0,),-ax)],[(0,(2,0),1),(0,(0,2),1),(0,(1,1),-h),(1,(1,),-ay)],[(0,(0,1),1),(0,(1,0),1),(0,(2,2),-h),(1,(2,),-az)]]
count=0
for tt in [0,1]:
 for ln in range(3-tt):
  for l in product(range(3),repeat=ln):
   for r in product(range(3),repeat=2-tt-ln):
    for rel in rels:
     val=defaultdict(lambda:s.Integer(0))
     for t0,w,c in rel:
      for key,v in normal(tt+t0,l+w+r).items():val[key]+=c*v
     assert all(s.cancel(v)==0 for v in val.values()),(tt,l,r,rel,val)
     count+=1
assert count==99
# The same family has a universal signed-cyclic quartic top under the H3 AS4 hypothesis.
bx,by,bz=s.symbols('beta_x beta_y beta_z')
qrels=[{(1,2):1,(2,1):1,(0,0):-h,(3,0):-ax/2,(0,3):-ax/2,(3,3):-bx},
       {(2,0):1,(0,2):1,(1,1):-h,(3,1):-ay/2,(1,3):-ay/2,(3,3):-by},
       {(0,1):1,(1,0):1,(2,2):-h,(3,2):-az/2,(2,3):-az/2,(3,3):-bz}]
top=defaultdict(lambda:s.Integer(0))
for i,qrel in enumerate(qrels):
    krel={(3,i):1,(i,3):-1}
    for a,c in qrel.items():
        for b,v in krel.items():top[a+b]+=c*v;top[b+a]+=v*c
for word in product(range(4),repeat=4):
    assert s.expand(top[word]+top[word[-1:]+word[:-1]])==0
selected=[(1,2),(2,0),(0,1),(3,0),(3,1),(3,2)]
assert s.expand(s.Matrix([[top[a+b] for b in selected] for a in selected]).det())==-1
import json
from pathlib import Path
matrix=s.Matrix([[s.diff(v,a) for a in [ax,ay,az]] for v in values])
assert s.cancel(matrix.det()+27*h/(8*(h**3+1)**3))==0
cert={'version':'classification-v8','ring':'QQ[h,alpha_x,alpha_y,alpha_z,1/h,1/(1+h^3)]',
      'modulus':'t^2=0; t central',
      'rule_leads':['xx','xy','xz','yyz','yzz'],
      'all_inserted_degree4_relation_identities':count,
      'universal_quartic_signed_cyclic_identities':256,
      'universal_quartic_rank6_minor':-1,
      'functional_targets':[{'commutator_generator':i,'active_word':list(w)} for i,w in fun],
      'functional_values':list(map(str,values)),
      'functional_values_on_t_quadratic_corrections':'zero for every quadratic correction',
      'obstruction_determinant':str(s.factor(matrix.det())),
      'conclusion':'In the specified normalized order-two Hesse central extensions, any H3 cubic forces all three diagonal quadratic-potential coefficients alpha_i=0, independently of beta_i.',
      'limits':'A necessary all-parameter H3 condition. The surviving nonsplit beta family is not yet fully classified here.'}
Path(__file__).with_name('cubic_clifford_lift_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS: universal signed-cyclic quartic with rank6 minor -1; all99 universal degree4 relation identities; every quadratic correction killed; central-cubic obstruction determinant -27*h/(8*(1+h^3)^3)')
