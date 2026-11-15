"""Exact cyclic eigentensor model and all traceless Jordan point determinants."""
import sympy as s,json
from pathlib import Path
from itertools import permutations
q,a,b=s.symbols('q a b');x,y,z=s.symbols('x y z');P=[x,y,z]
def red(c):return s.rem(s.expand(c),q*q+q+1,q).expand()
def tensor(A):
 T={}
 for perm in permutations(range(3)):
  sign=s.LeviCivita(*perm)
  for l in range(3):
   w=(l,perm[1],perm[2]);c=sign*A[l,perm[0]]
   for k in range(3):
    v=w[k:]+w[:k];T[v]=red(T.get(v,0)+q**(-k%3)*c)
 return {w:c for w,c in T.items() if c}
def mat(A):
 T=tensor(A);return s.Matrix(3,3,lambda i,k:red(sum(c*P[w[1]] for w,c in T.items() if w[0]==i and w[2]==k)))
basis=[s.diag(1,-1,0),s.diag(0,1,-1)]
for i in range(3):
 for j in range(3):
  if i!=j:
   E=s.zeros(3);E[i,j]=1;basis.append(E)
ws=list(__import__('itertools').product(range(3),repeat=3));T=s.Matrix([[tensor(A).get(w,0) for A in basis] for w in ws])
_,rows=T.T.rref();minor=red(T[list(rows),:].det());assert minor!=0
for A in basis:
 w=tensor(A)
 for v in ws:assert red(w.get(v[1:]+v[:1],0)-q*q*w.get(v,0))==0
cases=[('diagonal',s.diag(a,b,-a-b),3*x*y*z*(a-b)*(a+2*b)*(2*a+b)*(2*q+1)),('J2',s.Matrix([[a,1,0],[0,a,0],[0,0,-2*a]]),-27*a*a*x*x*z*(2*q+1)),('J3',s.Matrix([[0,1,0],[0,0,1],[0,0,0]]),-3*x**3*(2*q+1))]
dets={}
for name,A,expected in cases:
 M=mat(A);det=red(M.det());assert red(det-expected)==0;dets[name]=str(s.factor(det))
assert mat(cases[1][1]).subs(a,0)[1,:]==s.zeros(1,3)
# Repeated nonzero eigenvalue gives the quantum projective plane.
M=mat(s.diag(1,1,-2))
expected=s.Matrix([[0,3*q*z,3*(q+1)*y],[-3*q*z,0,-3*(q+1)*x],[3*y,-3*x,0]])
assert all(red(c)==0 for c in M-expected)
cert={'version':'classification-v36','cyclic_eigenvalue':'q, q^2+q+1=0; algebra Nakayama scalar q^-1','tensor_map':'project q eigenspace of (A tensor1 tensor1)*alternating tensor, A traceless','rank8_minor':str(minor),'rank8_minor_rows':[list(ws[i]) for i in rows],'column_basis':'diag(1,-1,0),diag(0,1,-1), then Eij i!=j in lex order','all_traceless_Jordan_determinants':dets,'nilpotent_J2_has_zero_relation':True,'smooth_elliptic_boundary_forces':'repeated nonzero diagonal eigenvalue; S=quantum P2 with xy=yx,xz=q^2*zx,yz=q^2*zy','scope':'Exact 8-dimensional eigentensor rank, cyclic identities and Jordan determinant formulas; ordinary proof links AS3 top Koszul tensor and geometric boundary.'}
Path(__file__).with_name('cubic_scalar_nakayama_as3_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS rank8 cyclic eigentensors, all Jordan determinants, unique quantum P2 boundary case')
