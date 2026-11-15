#!/usr/bin/env python3
"""Exact affine normalization and swap symmetry of the reconstructed order4 center."""
import sympy as s,json
from pathlib import Path
T=s.symbols('g');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));g=K.unit;zero,one=K.zero,K.one
root=Path(__file__).parent;cert=json.loads((root/'cubic_order4_center_relation_certificate.json').read_text());assert cert['status'].startswith('complete exact')
def cv(text):
 n,d=s.fraction(s.cancel(s.sympify(text)))
 return K.new(s.Poly(n,T,domain=s.QQ).all_coeffs())/K.new(s.Poly(d,T,domain=s.QQ).all_coeffs())
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
terms=[]
for exps,name in [((0,0,3),'Z3^3'),((0,3,0),'Z2^3'),((3,0,0),'Z1^3'),((1,1,1),'Z1*Z2*Z3')]:terms.append((0,*exps,cv(cert['leading_cubic'][name])))
for k,block in zip([2,1,0],cert['coefficient_blocks']):
 for row in block:
  if row['coefficient']!='0':d,i,j=row['exponents'];terms.append((d,i,j,k,cv(row['coefficient'])))
r=[(g-1)*(g*g-1)/2,(g*g-1)**2/2,one]
assert r[0]**3==cv(cert['leading_cubic']['Z1^3']) and r[1]**3==cv(cert['leading_cubic']['Z2^3'])
assert cv(cert['leading_cubic']['Z1*Z2*Z3'])/(r[0]*r[1])==7*g*g-13
shift=[]
for j in range(3):
 row=[zero,zero]
 for d,i,k,l,c in terms:
  e=[i,k,l]
  if sum(e)==2 and e[j]==2:row[d]-=c/(3*r[j]**2)
 shift.append(row)
def pmul(P,Q):
 out={}
 for a,c in P.items():
  for b,d in Q.items():
   e=tuple(i+j for i,j in zip(a,b));out[e]=out.get(e,zero)+c*d
 return {e:c for e,c in out.items() if c}
sub=[]
for i in range(3):
 e=[0]*4;e[i+1]=1;v={tuple(e):one/r[i]}
 for d,c in enumerate(shift[i]):
  if c:v[(d,0,0,0)]=c/r[i]
 sub.append(v)
poly={}
for d,i,j,k,c in terms:
 term={(d,0,0,0):c}
 for n,P in zip([i,j,k],sub):
  for _ in range(n):term=pmul(term,P)
 for e,c in term.items():poly[e]=poly.get(e,zero)+c
poly={e:c for e,c in poly.items() if c}
assert all(not c for (d,i,j,k),c in poly.items() if [i,j,k] in [[2,0,0],[0,2,0],[0,0,2]])
assert all(poly.get((d,j,i,k),zero)==c for (d,i,j,k),c in poly.items())
result={'version':'classification-v17','field':'QQ(g),g^4=2','substitution':'Z_i=(X_i+shift_i(D))/root_i',
 'roots':list(map(txt,r)),'shifts':[[txt(c) for c in row] for row in shift],
 'leading_Hesse_coefficient':txt(7*g*g-13),'pure_square_terms':'zero identically','swap_X1_X2_symmetry':True,
 'terms':[{'powers':list(e),'coefficient':txt(c)} for e,c in poly.items()],
 'scope':'Exact affine identity for the full reconstructed center; not a bad-D/H3 criterion by itself.'}
(root/'cubic_order4_symmetric_center_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: exact cube-root normalization, pure-square elimination and X1/X2 symmetry of full center')
