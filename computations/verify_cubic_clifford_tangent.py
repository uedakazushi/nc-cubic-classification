#!/usr/bin/env python3
"""Universal degree-four central-incidence tangent certificate.
Ring QQ[h,beta,A,B,C,D,1/h,1/(1+h^3)]; no specialization or interpolation.
Only the specified four envelope directions are classified. Neither formal
integration nor an ambient component/relative intrinsic stack is asserted.
"""
import sympy as s
from itertools import product
from sympy.polys.matrices import DomainMatrix
from pathlib import Path
words=lambda n:[w for k in range(n,-1,-1) for w in product(range(3),repeat=k)]
A,B,C,D=s.symbols('A B C D');b=list(s.symbols('beta_x beta_y beta_z')); h=s.symbols('h'); K=s.QQ.frac_field(h,*b)
rels=[];dr=[[],[],[],[]]
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
 rels.append({(j,k):1,(k,j):1,(i,i):-h,():-b[i]})
 dr[0].append({(j,k):1,(k,j):-1})
 for l in range(3):dr[l+1].append({(i,):-1} if l==i else {})
def matrix(n,rs):
 ws=words(n);ix={w:i for i,w in enumerate(ws)};cols=[]
 for d in range(n-1):
  for dl in range(d+1):
   for l in product(range(3),repeat=dl):
    for r in product(range(3),repeat=d-dl):
     for rel in rs:
      v={ix[l+w+r]:c for w,c in rel.items() if c};cols.append(v)
 return ws,s.MutableSparseMatrix(len(ws),len(cols),{(i,j):v for j,c in enumerate(cols) for i,v in c.items()})
w4,M=matrix(4,rels);ix={w:i for i,w in enumerate(w4)}
r,p=DomainMatrix.from_Matrix(M.T).convert_to(K).rref();r=r.to_Matrix();free=[i for i in range(len(w4)) if i not in p]
P=s.zeros(len(free),len(w4))
for i,j in enumerate(free):P[i,j]=1
for i,j in enumerate(p):
 for k,l in enumerate(free):P[k,j]=-r[i,l]
_,pc=DomainMatrix.from_Matrix(M).convert_to(K).rref();N=M[:,list(pc)]
_,rows=DomainMatrix.from_Matrix(N.T).convert_to(K).rref();L=N[list(rows),:].inv()
assert (P*M).applyfunc(s.cancel)==s.zeros(35,M.cols)
DM=[matrix(4,rs)[1][:,list(pc)] for rs in dr]
# Flatness through filtered degree4: all base syzygies lift for every direction.
T=s.zeros(len(pc),M.cols);T[:,:]=L*M[list(rows),:]
assert (N*T-M).applyfunc(s.cancel)==s.zeros(*M.shape)
for rs,Q in zip(dr,DM):assert (P*(matrix(4,rs)[1]-Q*T)).applyfunc(s.cancel)==s.zeros(35,M.cols)
w3,M3=matrix(3,rels);_,p3=DomainMatrix.from_Matrix(M3.T).convert_to(K).rref();f3=[w for i,w in enumerate(w3) if i not in p3]
def cv(poly,x):
 v=s.zeros(len(w4),1)
 for w,c in poly.items():v[ix[w+(x,)]]+=c;v[ix[(x,)+w]]-=c
 return v
Z=s.Matrix.vstack(*[s.Matrix.hstack(*[P*cv({w:1},x) for w in f3]) for x in range(3)])
# g=Alt(xyz)=xyz-((w+beta_z)z-(v+beta_y)y+(u+beta_x)x)/2.
g={(0,1,2):1,(2,2,2):-h/2,(1,1,1):h/2,(0,0,0):-h/2,(2,):-b[2]/2,(1,):b[1]/2,(0,):-b[0]/2,(0,0):A,(1,1):B,(2,2):C,():D}
obs=[]
for Q in DM:
 vs=[]
 for x in range(3):
  v=cv(g,x);coeff=L*v[list(rows),:];assert (N*coeff-v).applyfunc(s.cancel)==s.zeros(len(w4),1)
  vs.append(-P*Q*coeff)
 obs.append(s.Matrix.vstack(*vs))
_,zc=DomainMatrix.from_Matrix(Z.subs({bb:0 for bb in b})).convert_to(s.QQ.frac_field(h)).rref();ZN=Z[:,list(zc)]
_,zr=DomainMatrix.from_Matrix(ZN.T.subs({bb:0 for bb in b})).convert_to(s.QQ.frac_field(h)).rref();ZL=ZN[list(zr),:].inv()
v=s.Matrix([1,-4*A,-4*B,-4*C]);rhs=(-s.Matrix.hstack(*obs)*v).applyfunc(s.cancel)
sol0=(ZL*rhs[list(zr),:]).applyfunc(s.cancel);sol=s.zeros(20,1)
for i,j in enumerate(zc):sol[j]=sol0[i]
assert (Z*sol-rhs).applyfunc(s.cancel)==s.zeros(105,1)
Sel=s.zeros(len(zr),105)
for i,j in enumerate(zr):Sel[i,j]=1
E=s.eye(105)-ZN*ZL*Sel
OO=(E*s.Matrix.hstack(*obs)).applyfunc(s.cancel)

# Three polynomial functionals kill every cubic correction; each alpha pivot is a unit.
selected=[55,88,20]
expected=s.Matrix([[-4*A/h,-1/h,0,0],
                   [6*B/(h**3+1),0,3/(2*(h**3+1)),0],
                   [6*C*h/(h**3+1),0,0,3*h/(2*(h**3+1))]])
assert (E*Z).applyfunc(s.cancel)==s.zeros(105,20)
assert (OO[selected,:]-expected).applyfunc(s.cancel)==s.zeros(3,4)
assert s.cancel(expected[:,1:].det()+9/(4*(1+h**3)**2))==0
# The rank15 commutator chart and rank86 relation chart work at EVERY allowed h,beta.
minor4=s.factor(N[list(rows),:].det())
minorZ=s.factor(ZN[list(zr),:].det())
assert s.cancel(minor4-h**14*(1+h**3)**11)==0
assert s.cancel(minorZ+256*h**6)==0
# All coefficients used by the proof lie in the stated localization.
def localized(q):
    q=s.cancel(q);den=s.denom(q)
    if den.free_symbols-{h}:return False
    return all(s.rem(h*(1+h**3),factor,h)==0 for factor,power in s.factor_list(den,h)[1])
_,pc3=DomainMatrix.from_Matrix(M3).convert_to(K).rref()
W3=s.zeros(40,20)
for j,w in enumerate(f3):W3[w3.index(w),j]=1
minor3=s.factor(M3[:,list(pc3)].row_join(W3).det())
assert minor3 and localized(1/minor3)
for mat in [P,L,T,Z,ZL,E,sol]:
    assert all(localized(q) for q in mat)
# Explicit lift: t powers are restored by total degree to obtain a homogeneous cubic.
d=1+h**3
explicit={(1,1,1):-3*h/d,(2,1,0):(h**3-2)/d,
          (1,0):2*C*h**2/d,(1,2):-2*A*h**2/d,(2,0):-2*B*h**2/d,
          (0,):-(4*A**2*h**2+4*B*C*h-b[0])/d,
          (1,):-2*(2*A*C*h+2*B**2*h**2+b[1])/d,
          (2,):-(4*A*B*h+4*C**2*h**2-b[2])/d}
assert all(s.cancel(q-explicit.get(w,0))==0 for w,q in zip(f3,sol))
import json
certificate={
    'version':'classification-v10',
    'ring':'QQ[h,beta_x,beta_y,beta_z,A,B,C,D,1/h,1/(1+h^3)]',
    'envelope_directions':['gamma: yz-zy cyclic','alpha_x: -tx','alpha_y: -ty','alpha_z: -tz'],
    'degree4_relation_matrix':[121,102], 'degree4_relation_rank':86,
    'degree4_unit_minor':str(minor4), 'degree3_basis_unit_minor':str(minor3),
    'degree4_all_syzygies_lift':True,
    'cubic_correction_basis_dimension':20,
    'cubic_commutator_rank':15, 'commutator_unit_minor':str(minorZ),
    'obstruction_functionals':[[str(s.factor(q)) for q in expected.row(i)] for i in range(3)],
    'obstruction_alpha_minor':str(s.factor(expected[:,1:].det())),
    'criterion':'alpha_x=-4*A*gamma, alpha_y=-4*B*gamma, alpha_z=-4*C*gamma',
    'explicit_delta_G_for_gamma1':[{'active_word':list(w),'t_power':3-len(w),'coefficient':str(s.factor(q))} for w,q in explicit.items()],
    'lift_space_for_fixed_envelope_direction':'Affine translate of the five-dimensional central-cubic space',
    'scope':'All good h and every beta,A,B,C,D, with epsilon^2=0 and the four specified envelope directions. No higher-order integration, full ambient tangent space, deformation rigidity, componenthood or full intrinsic relative-stack assertion.'}
Path(__file__).with_name('cubic_clifford_tangent_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS: universal all-parameter central-incidence tangent; rank86 and rank15 unit charts; all degree4 syzygies; alpha=-4 gamma(A,B,C), explicit lift, unit obstruction determinant')
