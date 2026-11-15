#!/usr/bin/env python3
"""Exact overlap obstruction before imposing the PBW condition."""
import sympy as s,json
from pathlib import Path
from functools import lru_cache
b1,b2,b3=s.symbols('beta1 beta2 beta3')
rules={(1,0):[(-1,(0,1))],(2,0):[(-1,(0,2))],(3,0):[(-1,(0,3))],(2,1):[(1,(1,2)),(b1,(0,0))],(3,1):[(-1,(1,3)),(-b2,(0,0))],(3,2):[(-1,(2,3)),(-b3,(0,0))]}
def add(out,w,c):out[w]=s.expand(out.get(w,0)+c)
@lru_cache(None)
def nf(w):
 for i in range(len(w)-1):
  if w[i]>w[i+1]:
   out={}
   for c,v in rules[w[i:i+2]]:
    for u,a in nf(w[:i]+v+w[i+2:]).items():add(out,u,c*a)
   return {w:c for w,c in out.items() if c!=0}
 return {w:s.Integer(1)}
def branch(w,pos):
 out={}
 for c,v in rules[w[pos:pos+2]]:
  for u,a in nf(w[:pos]+v+w[pos+2:]).items():add(out,u,c*a)
 return out
w=(3,2,1);left=branch(w,0);right=branch(w,1);out=dict(left)
for u,c in right.items():add(out,u,-c)
out={u:c for u,c in out.items() if c!=0}
assert out=={(0,0,1):-2*b3,(0,0,2):2*b2}
cert={'version':'classification-v33','relations':'t anticommutes x,y,z; xy-yx+beta1*t^2=xz+zx+beta2*t^2=yz+zy+beta3*t^2=0','overlap':'zyx, reduce zy first minus reduce yx first','difference':'-2*beta3*t^2*x+2*beta2*t^2*y','PBW_forces':'beta2=beta3=0','remaining_exclusion':'beta1 nonzero gives affine Weyl parity extension; its simultaneous u,v centralizer is k[w^2], so no nonzero odd anticanonical cubic can exist. Ordinary proof in cubic_normal_order2_quantum.tex.','scope':'Exact free-word overlap only; no numeric sampling or replacement of Weyl-centralizer proof'}
Path(__file__).with_name('cubic_normal_order2_quantum_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS exact zyx overlap: PBW forces beta2=beta3=0')
