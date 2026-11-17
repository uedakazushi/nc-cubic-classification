#!/usr/bin/env python3
"""Independent polynomial controls for the scoped as4 second-quadric input.
Covers every local branch; geometric normalization/exhaustiveness is proved in
our paper and pinned upstream proofs, not inferred from numerical samples.
"""
from pathlib import Path
import sympy as s,itertools,json
ROOT=Path(__file__).resolve().parent
b,c,d,a=s.symbols('b c d a');Y=[b,c,d];mon=[b*b,b*c,b*d,c*c,c*d,d*d];l=s.symbols('l:3');m=s.symbols('m:3');n=s.symbols('n:3');L=sum(x*y for x,y in zip(l,Y));M=sum(x*y for x,y in zip(m,Y));NN=sum(x*y for x,y in zip(n,Y));f=[b*L+d*M,-c*L+d*NN,-c*M-b*NN]
assert s.expand(c*f[0]+b*f[1]+d*f[2])==0
u=s.symbols('u:18');unknown=[sum(u[6*j+k]*mon[k] for k in range(6)) for j in range(3)];equations=s.Poly(c*unknown[0]+b*unknown[1]+d*unknown[2],*Y).coeffs();SM,_=s.linear_eq_to_matrix(equations,u);assert SM.rank()==10
coeff=[s.Poly(x,*Y).coeff_monomial(v) for x in f for v in mon];PM,_=s.linear_eq_to_matrix(coeff,l+m+n);assert PM.rank()==8
fc=s.symbols('g:6');g=sum(x*y for x,y in zip(fc,mon));E1=s.expand(d*d*NN-c*d*L-c*g).subs(b,0);E2=s.expand(b*d*L-b*g+d*d*M).subs(c,0);e=s.Poly(E1,c,d).coeffs()+s.Poly(E2,b,d).coeffs();EM,_=s.linear_eq_to_matrix(e,l+m+n+fc);desired=[m[2],n[2],fc[0],fc[3],fc[2]-l[0],fc[4]+l[1],fc[5]-l[2]-m[0],n[1]-m[0]-2*l[2]];DM,_=s.linear_eq_to_matrix(desired,l+m+n+fc);assert EM.rank()==DM.rank()==EM.col_join(DM).rank()==8
al,be,mu,nu,xi,ka,X=s.symbols('al be mu nu xi ka X');ll=al*b+be*c;mm=mu*b+nu*c;nn=xi*b+mu*c;ff1=b*ll+d*mm;ff2=-c*ll+d*nn;ff4=-c*mm-b*nn;ff3=al*b*d-be*c*d+mu*d*d+ka*b*c;h=s.cancel((ff1*ff2+ff3*ff4)/(b*c));assert s.denom(h)==1
q=s.Matrix([a*a+h,a*b+ff1,a*c+ff2,a*d+ff3,ff4,b*c]);T=s.eye(6);T[0,:]=s.Matrix([[1,2*al,-2*be,2*mu,-ka,-2*(2*al*be+ka*mu)]]);T[1,5]=-2*be;T[2,5]=2*al;T[3,5]=-ka;T[4,5]=2*mu;assert T.det()==1
normal=[X*X+nu*xi*d*d,X*b+nu*c*d,X*c+xi*b*d,X*d,-xi*b*b-nu*c*c,b*c];assert all(s.expand(x-y)==0 for x,y in zip((T*q).subs(a,X-mu*d-al*b+be*c),normal))
z=s.symbols('z:6');Q0=z[0]*z[5]-z[1]*z[2]-z[3]*z[4];Q1=z[0]*z[4]+xi*z[1]**2+nu*z[2]**2-4*nu*xi*z[3]*z[5];assert all(s.expand(p.subs(dict(zip(z,normal)),simultaneous=True))==0 for p in [Q0,Q1]);assert s.Poly(Q1,*z).coeff_monomial(z[0]*z[4])==1
# Asymmetric branch and every identically singular pencil.
tc=s.symbols('t:3');tt=sum(x*y for x,y in zip(tc,Y));A,alpha,beta=s.symbols('A alpha beta');q=[A*(A-2*L)-NN*tt,b*A,c*(A-2*L)+d*NN,d*A+c*tt,-b*NN,b*c];uv=s.Matrix([A,NN,-c,0]);vv=s.Matrix([tt,A-2*L,d,b]);pairs=list(itertools.combinations(range(4),2))
def exterior(x,y):return s.Matrix([s.expand(x[i]*y[j]-x[j]*y[i]) for i,j in pairs])
def wedge(x,y):return s.expand(x[0]*y[5]-x[1]*y[4]+x[2]*y[3]+x[3]*y[2]-x[4]*y[1]+x[5]*y[0])
assert (exterior(uv,vv)-s.Matrix([q[0],q[3],q[1],q[2],-q[4],-q[5]])).applyfunc(s.expand)==s.zeros(6,1)
pencil=(alpha*uv+beta*vv).jacobian([A,b,c,d]);PD=beta*(n[2]*alpha**3+(n[1]-2*l[2])*alpha**2*beta-(2*l[1]+tc[2])*alpha*beta**2-tc[1]*beta**3);assert s.expand(pencil.det()-PD)==0
spec={n[2]:0,n[1]:2*l[2],tc[2]:-2*l[1],tc[1]:0};qs=[s.expand(v.subs(spec,simultaneous=True).subs(A,X+2*l[1]*c)) for v in q];b2=-(qs[4]+2*l[2]*qs[5])/n[0];normal2=[b2,qs[1]-2*l[1]*qs[5],qs[5],qs[3]-tc[0]*qs[5],qs[2]+2*l[0]*qs[5],qs[0]+2*l[0]*qs[1]+2*l[2]*qs[3]-2*l[1]*qs[2]+n[0]*tc[0]*b2-4*l[0]*l[1]*qs[5]];assert all(s.cancel(x-y)==0 for x,y in zip(normal2,[b*b,b*X,b*c,X*d,c*X+n[0]*b*d,X*X]))
# Generic cyclic pencil; no invertibility or semisimplicity of its matrix.
TT=s.Matrix(4,4,s.symbols('h:16'));xx=s.Matrix(s.symbols('x:4'));zz=exterior(xx,TT*xx);ET=s.Matrix([[TT.extract(ij,kl).det() for kl in pairs] for ij in pairs]);assert (ET*zz-exterior(TT*xx,TT**2*xx)).applyfunc(s.expand)==s.zeros(6,1) and wedge(zz,ET*zz)==0
co=s.symbols('c:4');comp=s.Matrix([[0,0,0,-co[0]],[1,0,0,-co[1]],[0,1,0,-co[2]],[0,0,1,-co[3]]]);w=exterior(s.eye(4)[:,0],s.eye(4)[:,2]);assert wedge(w,w)==0 and wedge(w,exterior(comp[:,0],comp[:,2]))==-1
# Nondegenerate tangent chart, all six symmetric matrix coefficients.
ms=s.symbols('m:6');MM=s.Matrix([[ms[0],ms[1],ms[2]],[ms[1],ms[3],ms[4]],[ms[2],ms[4],ms[5]]]);bb=s.Matrix(Y);cross=bb.cross(MM*bb);B2=(bb.T*bb)[0];r=(bb.T*MM*bb)[0];e2=(s.trace(MM)**2-s.trace(MM**2))/2;q=[a*a+(bb.T*MM**2*bb)[0],*(a*bb+cross),r,B2];P=z[0]*z[4]-(s.Matrix(z[1:4]).T*MM*s.Matrix(z[1:4]))[0]-s.trace(MM)*z[4]**2+e2*z[4]*z[5]-MM.det()*z[5]**2;Q=z[0]*z[5]-sum(v*v for v in z[1:5]);assert s.expand(P.subs(dict(zip(z,q)),simultaneous=True))==0 and s.expand(Q.subs(dict(zip(z,q)),simultaneous=True))==0
mu0,la=s.symbols('mu0 la');small=s.Matrix([[0,la/2,mu0/2],[la/2,-mu0-la*s.trace(MM),la*e2/2],[mu0/2,la*e2/2,-la*MM.det()]]);assert s.expand(4*small.det()-(mu0*s.eye(3)+la*MM).det())==0
ww=s.Matrix(s.symbols('w:3'));skew=s.Matrix([[0,-ww[2],ww[1]],[ww[2],0,-ww[0]],[-ww[1],ww[0],0]]);NN=MM+skew;qv=a*bb+bb.cross(NN*bb);qzero=a*a+(NN*bb).dot(NN*bb);ap=a-ww.dot(bb);assert (qv-ww*B2-ap*bb-bb.cross(MM*bb)).applyfunc(s.expand)==s.zeros(3,1);assert s.expand(qzero-2*ww.dot(qv)+ww.dot(ww)*B2-ap*ap-(MM*bb).dot(MM*bb))==0
out={'status':'PASS','scope':'scoped as4 import: every full-rank differential tangent branch for six quadrics has a second independent quadratic relation','source_commit':'6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0','degenerate_syzygy_map_rank':10,'syzygy_parameter_rank':8,'both_nondivisible_condition_rank':8,'both_nondivisible_target_change_det':1,'degenerate_second_quadric':str(Q1),'asymmetric_pencil_det':str(PD),'singular_pencil_new_quadric':'z0*z5-z1^2, rank3','cyclic_basis_independence_witness':-1,'nondegenerate_second_quadric':str(P),'nondegenerate_pencil_det':'-det(mu I+lambda M)^2/4','ordinary_dependencies':['all tangent Witt normalizations','integral-domain exhaustive factor branches and nonzero divisors','cyclicity from independence of six minors','generic differential rank for three-dimensional image'],'not_claimed':['full CY classification audited','Veronese AS4 exclusion independently replayed here','all CI22 charts imported','novelty confirmed','geometric arguments mechanically formalized']}
(ROOT/'cubic_CY_second_quadric_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all degenerate and nondegenerate tangent branches, universal identities and second quadrics')
