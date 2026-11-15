#!/usr/bin/env python3
"""Exact regular-trace radical/simple-count checks for finite central fibers
of cyclic quotient orders, including PI4 good and bad partial generators.
These finite checks do not establish the ordinary general theorem.
"""
import sympy as s,json
from pathlib import Path

def cyclic_fiber(m,r):
 # Fourier-idempotent basis of (k[u,v]/(u^m,v^m,uv))#mu_m,
 # amplified by multiplicities r. A path is (direction,power,source).
 paths=[(0,0,i) for i in range(m)]+[(d,p,i) for d in [-1,1] for p in range(1,m) for i in range(m)]
 def target(w):d,p,i=w;return (i+d*p)%m
 basis=[(w,a,b) for w in paths for a in range(r[target(w)]) for b in range(r[w[2]])]
 idx={v:i for i,v in enumerate(basis)};n=len(basis)
 def product(i,j):
  (w,a,b),(v,c,d)=basis[i],basis[j]
  if w[2]!=target(v) or b!=c:return None
  if w[1] and v[1] and w[0]!=v[0]:return None
  power=w[1]+v[1]
  if power>=m:return None
  direction=w[0] if w[1] else v[0]
  return idx[((direction,power,v[2]),a,d)]
 products=[[product(i,j) for j in range(n)] for i in range(n)]
 trace=[sum(products[i][j]==j for j in range(n)) for i in range(n)]
 gram=s.Matrix([[trace[q] if q is not None else 0 for q in row] for row in products])
 radical=n-gram.rank();rows=[]
 # [a,b] belongs to the radical iff its pairing with every basis element is0.
 for b in range(n):
  for c in range(n):
   row=[]
   for a in range(n):
    p,q=products[a][b],products[b][a]
    row.append((gram[p,c] if p is not None else 0)-(gram[q,c] if q is not None else 0))
   if any(row):rows.append(row)
 central_preimage=n-(s.Matrix(rows).rank() if rows else 0)
 simples=central_preimage-radical
 assert simples==sum(v>0 for v in r)
 assert n-radical==sum(v*v for v in r)
 return {'cyclic_order':m,'multiplicities':r,'PI_degree':sum(r),'fiber_dimension':n,'regular_trace_radical_dimension':radical,'semisimple_dimension':n-radical,'semisimple_center_dimension':simples,'full_generator':all(r)}
cases=[(2,[1,3]),(2,[2,2]),(2,[4,0]),(3,[1,1,2]),(4,[1,1,1,1]),(4,[1,3,0,0])]
out=[cyclic_fiber(m,r) for m,r in cases]
for x in out:print('PASS',x,flush=True)
Path(__file__).with_name('cubic_finite_order_fibers_certificate.json').write_text(json.dumps({'scope':'Exact finite cyclic-quotient central fibers; radical trace and simple count; not full ordinary theorem proof','cases':out},indent=2)+'\n')
