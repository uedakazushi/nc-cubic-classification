#!/usr/bin/env python3
"""Universal controls for the seven necessary CI22 projection types.
Algebraic AS4 coefficient normal forms and existence are not imported here.
"""
from pathlib import Path
import sympy as s,itertools,json
ROOT=Path(__file__).resolve().parent
a,b,c,d=s.symbols('a b c d');xs=[a,b,c,d];mons2=[xs[i]*xs[j] for i,j in itertools.combinations_with_replacement(range(4),2)];mons4=[s.prod(xs[i] for i in w) for w in itertools.combinations_with_replacement(range(4),4)];pairs=list(itertools.combinations_with_replacement(range(6),2));z=s.symbols('z:6');mu,la=s.symbols('mu la')
cases={'1111':[a*b,a*c,a*d,b*c,b*d,c*d],'211':[b*b,a*c,a*d,b*c,b*d,c*d],'22':[b*b,d*d,a*c,a*d,b*c,b*d],'31':[a*c-b*b,b*c,c*c,a*d,b*d,c*d],'4':[a*c-b*b,a*d-b*c,b*d,c*c,c*d,d*d],'L':[a*a,a*b,b*b,b*c,a*c-b*d,a*d],'D':[a*a,a*b,b*b,c*c,c*d,d*d]}
records=[]
for name,qs in cases.items():
 mult=s.Matrix.hstack(*[s.Matrix([s.Poly(qs[i]*qs[j],*xs).coeff_monomial(w) for w in mons4]) for i,j in pairs]);assert mult.rank()==19;null=mult.nullspace();rels=[sum(v*z[i]*z[j] for v,(i,j) in zip(col,pairs)) for col in null];mat=[s.hessian(q,z)/2 for q in rels]
 chosen=None
 for k in range(-4,5):
  A=mat[0]+k*mat[1]
  if A.det():chosen=k;break
 assert chosen is not None;A=mat[0]+chosen*mat[1];T=A.inv()*mat[1];rank=s.Matrix.hstack(s.Matrix(list(s.eye(6))),s.Matrix(list(T)),s.Matrix(list(T*T))).rank();assert (rank==2)==(name in ['L','D']);det=s.factor((mu*mat[0]+la*mat[1]).det());records.append({'type':name,'quadrics':list(map(str,qs)),'all_two_quadric_relations':list(map(str,rels)),'full_rank_combination':[1,chosen],'full_rank_det':str(A.det()),'pencil_det':str(det),'span_I_T_T2_dimension':rank})
# Finite curvilinear algebras: coordinate bases1,t,... on each component.
partitions={'1111':[1,1,1,1],'211':[2,1,1],'22':[2,2],'31':[3,1],'4':[4]}
for name,parts in partitions.items():
 labels=[(j,k) for j,n in enumerate(parts) for k in range(n)];loc={v:i for i,v in enumerate(labels)};PM=s.zeros(4,10)
 for col,(i,j) in enumerate(itertools.combinations_with_replacement(range(4),2)):
  ci,ei=labels[i];cj,ej=labels[j]
  if ci==cj and ei+ej<parts[ci]:PM[loc[ci,ei+ej],col]=1
 assert PM.rank()==4
 Q=s.Matrix.hstack(*[s.Matrix([s.Poly(q,*xs).coeff_monomial(v) for v in mons2]) for q in cases[name]]);assert Q.rank()==6 and PM*Q==s.zeros(4,6)
# All quadratic syzygies of (a^2,ab,b^2), not a sampled pencil.
u=s.symbols('u:30');vec=[sum(u[10*j+k]*m for k,m in enumerate(mons2)) for j in range(3)];pol=a*a*vec[0]+a*b*vec[1]+b*b*vec[2];AA,_=s.linear_eq_to_matrix(s.Poly(pol,*xs).coeffs(),u);assert AA.rank()==22
l=s.symbols('l:4');m=s.symbols('m:4');ell=sum(v*x for v,x in zip(l,xs));mm=sum(v*x for v,x in zip(m,xs));sy=[-b*ell,a*ell-b*mm,a*mm];assert s.expand(a*a*sy[0]+a*b*sy[1]+b*b*sy[2])==0;SM=s.Matrix([s.Poly(q,*xs).coeff_monomial(v) for q in sy for v in mons2]).jacobian(l+m);assert SM.rank()==8
# Full marked smooth-quadric orbit for the reduced-line projection.
al,be,ga,de=s.symbols('al be ga de');Q=z[0]*z[3]-z[1]*z[4]-z[2]*z[5];P=z[0]*z[2]-z[1]**2;tr=[z[0],z[1],z[2],z[3]+al*z[1]+be*z[2],z[4]+al*z[0]+(be-ga)*z[1]-de*z[2],z[5]+ga*z[0]+de*z[1]];assert s.expand(Q.subs(dict(zip(z,tr)),simultaneous=True)-Q-(be-ga)*P)==0
# Universal base-scheme elimination identities in the nondegenerate chart.
y=s.Matrix(s.symbols('y:3'));v=s.symbols('v:6');M=s.Matrix([[v[0],v[1],v[2]],[v[1],v[3],v[4]],[v[2],v[4],v[5]]]);t=M*y;cross=y.cross(t);B=y.dot(y);r=y.dot(t)
assert s.expand(y[0]*cross[1]-y[1]*cross[0]-y[2]*r+t[2]*B)==0
assert s.expand(y[0]*cross[2]-y[2]*cross[0]+y[1]*r-t[1]*B)==0
assert s.expand(cross[0]**2+y[0]**2*t.dot(t)-B*(t[1]**2+t[2]**2)-r*(2*y[0]*t[0]-r))==0
# All five finite schemes occur, including nonsemisimple symmetric matrices.
p,q=s.symbols('p q');conic=s.Matrix([p*p-q*q,s.I*(p*p+q*q),2*p*q]);examples={'1111':s.diag(0,1,2),'211':s.Matrix([[1,s.I,0],[s.I,-1,0],[0,0,1]]),'22':s.diag(0,0,1),'31':s.Matrix([[0,0,1],[0,0,s.I],[1,s.I,0]]),'4':s.Matrix([[1,s.I,0],[s.I,-1,0],[0,0,0]])};expected={'1111':-p**4+6*p*p*q*q-q**4,'211':4*q*q*(p*p+q*q),'22':4*p*p*q*q,'31':-8*p*q**3,'4':4*q**4}
for name,M in examples.items():assert s.expand(conic.dot(M*conic)-expected[name])==0
f=s.Poly(expected['1111'].subs(p,1),q);assert s.gcd(f,f.diff()).degree()==0
out={'status':'PASS','scope':'all seven necessary six-quadric projection types for integral CI(2,2) image, not algebra coefficient classification','all_seven_projection_records':records,'all_five_finite_scheme_multiplication_kernels':True,'full_binary_syzygy_rank':22,'syzygy_parameter_rank':8,'line_marked_quadric_translation':True,'all_three_basepoint_elimination_identities':True,'all_five_symmetric_matrix_examples':{k:str(v) for k,v in examples.items()},'ordinary_dependencies':['tangent degeneracy criterion T^2 in span(I,T)','self-adjoint minimal polynomial degree2 gives direct Veronese double cover or reduced line','nondegenerate tangent chart base scheme equals smooth conic cut of length4 and spans P3','complete linear series of a finite curvilinear length4 scheme gives five projective types'],'not_claimed':['all AS4 candidates over each projection classified','all zero-commutator CY H3 excluded','whole CY classification imported','novelty confirmed','geometric proofs mechanically formalized']}
(ROOT/'cubic_CY_CI22_projection_atlas_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all seven pencil types, five full finite multiplication kernels and all basepoint/syzygy identities')
