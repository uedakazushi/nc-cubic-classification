#!/usr/bin/env python3
"""Exact finite nine-cycle matrix fiber and central regular-sequence data.
The trace-closed center-lifting theorem, elliptic divisor geometry and H3
obstruction are ordinary manuscript proofs, not verified by this program.
"""
from pathlib import Path
import json,sympy as s
from sympy.polys.matrices import DomainMatrix
n=9
basis=[(i,r) for i in range(n) for r in range(n)]
units={(i,r):(i,(i-r)%n) for i,r in basis}
assert len(set(units.values()))==81
checked=0
for i,r in basis:
 for j,t in basis:
  a,b=units[i,r];c,d=units[j,t]
  product=(a,d) if b==c else None
  expected=units[i,(r+t)%n] if i==(j+r)%n else None
  assert product==expected;checked+=1
# Regular trace on M9 is 9 times ordinary matrix trace.
gram={}
for a,(i,r) in enumerate(basis):
 for b,(j,t) in enumerate(basis):
  u,v=units[i,r];w,z=units[j,t]
  if v==w and u==z:gram.setdefault(a,{})[b]=s.QQ(n)
G=DomainMatrix.from_dod(gram,(81,81),s.QQ)
det=G.det();assert det==s.QQ(n**81)
# H is the degree3 elliptic THCR; gamma has degree3 and z degree9.
def h(d):return 0 if d<0 else (1 if d==0 else 3*d)
def q(d):return 0 if d<0 else h(d)-h(d-3)
qdims=[q(d) for d in range(14)]
tdims=[q(d)-q(d-9) for d in range(14)]
t=s.Symbol('t');poly=s.Poly((1+t+t*t)**2*sum(t**j for j in range(9)),t)
assert tdims==[int(poly.nth(d)) for d in range(14)]
assert sum(tdims)==81 and tdims[-1]==0
out={'status':'PASS','scope':'finite nine-cycle crossed product and Hilbert regular-sequence arithmetic only','cyclic_order':9,'matrix_units':81,'all_basis_products_checked':checked,'regular_trace_Gram_determinant':str(det),'Artinian_dimensions':tdims,'boundary_Q_dimensions':qdims,'central_degrees':[1,3,9],'central_free_rank':81,'not_claimed':['Stafford or Rains theorem computer verified','elliptic divisor geometry computer verified','all H3 classification completed']}
Path(__file__).with_name('cubic_third_root_unit_boundary_L_orbit_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','matrix_size':9,'basis_products':checked,'Artinian_total':81}))
