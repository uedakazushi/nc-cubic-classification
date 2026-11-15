#!/usr/bin/env python3
"""Exact leading cubic relation of the quartic center generators.
Evaluation in an elliptic coordinate ring, no finite-point interpolation.
"""
import sympy as s,json
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
from sympy.polys.rings import ring
T=s.symbols('g');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));g=K.unit;R,x=ring('x',K);o=R.one;zz=R.zero
p=1+g;q=1-g;kappa=(1+6*g*g)/(p*q)
def cst(c):return (R(c),zz,zz)
def add(a,b):return tuple(u+v for u,v in zip(a,b))
def mul(a,b):
 out=[zz for _ in range(5)]
 for i,c in enumerate(a):
  for j,d in enumerate(b):out[i+j]+=c*d
 for i in [4,3]:
  out[i-2]-=out[i]*kappa*x;out[i-3]-=out[i]*(x**3+1)
 return tuple(out[:3])
def sc(c,a):return tuple(c*v for v in a)
Q=[((x,zz,zz),(o,zz,zz),(zz,o,zz))]
for step in range(3):
 X,Y,Z=Q[-1]
 Q.append((add(sc(q*q,mul(X,Z)),sc(p,mul(Y,Y))),add(sc(p*p,mul(Y,Z)),sc(q,mul(X,X))),add(mul(X,Y),sc(-p*q,mul(Z,Z)))))
for j in range(3):
 for i,k,l in [(0,1,2),(1,2,0),(2,0,1)]:
  assert add(add(sc(p,mul(Q[j][k],Q[j+1][l])),sc(q,mul(Q[j][l],Q[j+1][k]))),sc(-K.one,mul(Q[j][i],Q[j+1][i])))==(zz,zz,zz)
print('point graph chain built',flush=True)
def cv(expr):
 poly=s.Poly(s.sympify(expr),T,domain=s.QQ);return K.new(poly.all_coeffs())
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
data=json.load(Path(__file__).with_name('cubic_order4_center_certificate.json').open());sections=[]
for zi in data['basis'][:3]:
 f=(zz,zz,zz)
 for row in zi:
  word=row['word']
  if 3 in word:continue
  c=cv(row['coefficient']);term=cst(K.one)
  for j,i in enumerate(word):term=mul(term,Q[j][i])
  f=add(f,sc(c,term))
 sections.append(f)
print('three central sections built',flush=True)
monoms=[(i,j,3-i-j) for i in range(4) for j in range(4-i)];values=[]
for exps in monoms:
 term=cst(K.one)
 for z,n in zip(sections,exps):
  for _ in range(n):term=mul(term,z)
 values.append(term)
print('cubic monomials reduced in elliptic function ring',flush=True)
rows={};degree=max((poly.degree() for value in values for poly in value),default=0)
for j,value in enumerate(values):
 for z,poly in enumerate(value):
  for (d,),c in poly.to_dict().items():
   if c:rows.setdefault(z*(degree+1)+d,{})[j]=c
M=DomainMatrix.from_dod(rows,(3*(degree+1),10),K);ker=M.nullspace();assert ker.shape[0]==1,ker.shape
row=ker.to_list()[0];chosen=monoms.index((0,0,3));assert row[chosen]
row=[c/row[chosen] for c in row]
assert (M*DomainMatrix.from_dod({i:{0:c} for i,c in enumerate(row) if c},(10,1),K)).is_zero_matrix
result={'version':'classification-v15','field':'QQ(g),g^4=2','direct_multilinear_relation_checks':9,'method':'Exact point-graph evaluation in K[x,z]/(z^3+kappa*x*z+x^3+1), no point sampling','monomials':[list(e) for e in monoms],'coefficients':list(map(txt,row)),'z3_cube_coefficient':1,'matrix_shape':list(M.shape),'kernel_dimension':1}
Path(__file__).with_name('cubic_order4_leading_center_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('leading center cubic',[(e,txt(c)) for e,c in zip(monoms,row) if c],flush=True)
