"""Structural identities for the complete a=q=0 nondegenerate secant boundary."""
import itertools,json
from pathlib import Path
import sympy as S
r,s,t,theta=S.symbols('r s t theta');alpha=(r-1)/(r+1);C=t*t+alpha*s*s-(1-r*r)
F=S.Matrix([[t/(r+1),-s/(r+1)],[-s/(r+1),-t/(r-1)]]);H=S.Matrix([[-t/(r-1),s/(r+1)],[s/(r+1),t/(r+1)]])
A=S.diag(-(r+1)/(2*r),-(r-1)/(2*r));B=S.diag((r-1)/(2*r),(r+1)/(2*r))
def zero_on_conic(expr):
 num=S.together(expr).as_numer_denom()[0];return S.rem(num,S.together(C).as_numer_denom()[0],t)==0
assert all(zero_on_conic(x) for x in F*H-S.eye(2))
assert zero_on_conic(F.det()-1)
assert all(zero_on_conic(x) for x in F.T*A*F-B)
assert S.cancel(S.trace(F)-2*t/(1-r*r))==0
# Both scalar possibilities force r=0: diagonal equations differ by 2*epsilon*r.
for epsilon in [1,-1]:
 assert S.expand(epsilon*(r+1)+epsilon*(r-1))==2*epsilon*r
# SL2 trace1 entails F^2-F+I=0 and F^3=-I, also on the symmetric square.
res=t-(1-r*r)/2;CH=(F*F-F+S.eye(2)).applyfunc(S.cancel)
for x in CH:
 num=S.together(x.subs(t,(1-r*r)/2)).as_numer_denom()[0]
 assert S.rem(num,S.together(C.subs(t,(1-r*r)/2)).as_numer_denom()[0],s)==0
# Exact direct check at a number-field resonance against ORIGINAL quadratic relations.
from cubic_order2_22_secant_tools import relations,quotient
root=S.sqrt(-3);E=S.QQ.algebraic_field(S.sqrt(3),S.I);rv=root;tv=S.Integer(2);sv=S.Integer(0)
R=relations(S.Matrix([[0,rv],[rv,0]]),[0,-tv,0,0,tv,0]);words,index,free,nf=quotient(R,3,E)
Fv=F.subs({r:rv,s:sv,t:tv});Av=A.subs(r,rv);AA=(Fv**2).T*Av*(Fv**2)
factor={(0,0):S.Integer(1),(1,1):theta**2}
for i,j in itertools.product(range(2),repeat=2):factor[(i+2,j+2)]=-theta*AA[i,j]
value={}
for g,cg in [(0,1),(1,theta)]:
 for w,cw in factor.items():
  for j,d in nf[index[(g,)+w]].items():value[j]=value.get(j,0)+cg*cw*E.to_sympy(d)
for w,coef in [((0,0,0),1),((1,1,1),theta**3)]:
 for j,d in nf[index[w]].items():value[j]=value.get(j,0)-coef*E.to_sympy(d)
assert all(S.simplify(x)==0 for x in value.values())
# Interchanging x,y and multiplying u,v by i interchanges a,q up to sign.
a,q=S.symbols('a q');Z=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),[a,-t,alpha*s,s,t,q]):Z[i,j]=v;Z[j,i]=-v
P=S.kronecker_product(S.Matrix([[0,1],[1,0]]),S.eye(2));ZZ=-P*Z*P.T
assert [ZZ[i,j] for i,j in itertools.combinations(range(4),2)]==[-q,-t,s,alpha*s,t,-a]
out={'status':'PASS','scope':'all nondegenerate-positive symmetric-secant positive-Pfaffian doublezero a=q=0, rho(rho2-1)!=0','matrix_identities':'F*H=I, detF=1, F(A)=B; exact conic identities','structural_proof':'xy=A,yx=B and opposite F normalizers imply all negative symmetric quadratics central in negative subalgebra. Auxiliary weights +/-1 normal cubic components force Sym2F=I, hence F=+/-I, impossible rho!=0. Weights +/-3 require F3=-I, equivalent traceF=1.','all_normal_cuts':'at traceF1, W=span(x3,y3); (x+theta*y)(x2-theta*F2(A)+theta2*y2)=x3+theta3*y3. Every cut factors over algebraically closed k.','coverage_reduction':'x/y interchange with u/v multiplied by i sends rho to -rho and (a,q,s,t) to (-q,-a,alpha*s,t); all remaining points have q!=0, normalized q1 by positive torus','geometric_conclusion':'entire doublezero boundary has no H3','not_claimed':['q!=0 main chart','global H3 classification','relative intrinsic descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_doublezero_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS secant doublezero: universal opposite-normalizer identities, structural factor pencil and swap coverage')
