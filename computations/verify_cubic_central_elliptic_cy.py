#!/usr/bin/env python3
"""Universal exact Moore-graph, CY syzygy and central-extension constraints.
Ordinary Hesse group-law and AS3/Nakayama arguments remain in the paper.
"""
import sympy as s,json
from pathlib import Path
from itertools import product
A,B,C,l=s.symbols('a b c lambda');x,y,z=s.symbols('x y z');X,Y,Z=s.symbols('X Y Z');P=s.Matrix([x,y,z]);Q=s.Matrix([X,Y,Z]);pars=[A,B,C]
def matrix(p,a,b,c):
 x,y,z=p;return s.Matrix([[c*x,b*z,a*y],[a*z,c*y,b*x],[b*y,a*x,c*z]])
M=matrix(P,A,B,C);F=x**3+y**3+z**3-3*l*x*y*z
assert s.expand(M.det()-((A**3+B**3+C**3)*x*y*z-A*B*C*(x**3+y**3+z**3)))==0
assert matrix(s.Matrix([1,-1,0]),A,B,C)*s.Matrix(pars)==s.zeros(3,1)
assert matrix(Q,B,A,C)*P==M*Q
# Cyclic order3 translations preserve the multilinear graph.
cyc=lambda v:s.Matrix([v[1],v[2],v[0]])
assert matrix(cyc(P),A,B,C)*cyc(Q)==cyc(M*Q)
u=s.symbols('u');diag=s.diag(1,u,u*u)
for row in matrix(diag*P,A,B,C)*diag*Q-s.diag(1,u*u,u)*(M*Q):assert s.rem(s.expand(row),u*u+u+1,u)==0
q=s.symbols('q')
for aa,bb,cc,qq in [(1,-q,0,s.Matrix([x,q*y,q*q*z])),(0,-q,1,s.Matrix([q*z,x,q*q*y])),(-q,0,1,s.Matrix([y,q*z,q*q*x]))]:
 for expr in matrix(P,aa,bb,cc)*qq:assert s.rem(s.expand(expr),q**3-1,q)==0
# Degree3 cyclic tensor identity and degree2 skew-alpha obstruction.
rel=[{(1,2):A,(2,1):B,(0,0):C},{(2,0):A,(0,2):B,(1,1):C},{(0,1):A,(1,0):B,(2,2):C}]
def plus(d,w,c):d[w]=s.expand(d.get(w,0)+c)
left={};right={}
for i,r in enumerate(rel):
 for w,c in r.items():plus(left,(i,)+w,c);plus(right,w+(i,),c)
assert left==right
v=s.symbols('v0:3');shift=s.Matrix([[2*C,0,0],[0,2*C,0],[0,0,2*C], [0,A+B,0],[0,0,A+B],[A+B,0,0]])
assert shift[:3,:].det()==8*C**3 and s.factor(shift[3:,:].det())==(A+B)**3
alpha=s.Matrix(3,3,lambda i,j:s.Symbol(f'L{i}{j}'));skew=s.Matrix([alpha[0,1]-alpha[1,0],alpha[0,2]-alpha[2,0],alpha[1,2]-alpha[2,1]])
# If c!=0 or a+b!=0, relation space has no nonzero antisymmetric tensor.
coords=[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
mat=s.Matrix([[r.get(w,0) for r in rel] for w in coords])
assert mat[[0,4,8],:].det()==C**3

# Normal-form positive/negative minors for the symmetrization projection.
projection=s.Matrix([[sum(r.get(w,0) for w in [(1,2),(2,1)]) for r in rel], [sum(r.get(w,0) for w in [(2,0),(0,2)]) for r in rel], [sum(r.get(w,0) for w in [(0,1),(1,0)]) for r in rel]])
assert s.factor(projection.det())==(A+B)**3
result={'version':'classification-v24','Moore_determinant':str(s.factor(M.det())),'origin_kernel':'(a:b:c)','opposite_graph_identity':True,'Heisenberg_graph_covariance':True,'all_three_zero_coefficient_flex_cases':True,'cyclic_W3_identity':True,'Nakayama_translation_minors':[str(8*C**3),str((A+B)**3)],'relation_antisymmetry_minors':[str(C**3),str((A+B)**3)],'exceptional_case':'c=0,a+b=0 is the commutative polynomial three-variable algebra','scope':'Exact universal polynomial identities; does not replace Hesse translation identification, AS regular/CY or intrinsic-boundary proofs'}
Path(__file__).with_name('cubic_central_elliptic_cy_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS Moore graph identities, cyclic W3, translation-killing and antisymmetry minors')
