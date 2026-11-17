#!/usr/bin/env python3
"""Independent downstream replay of pinned Veronese proof data.
Rebuilds original cyclic matrices, all six integrability kernels and eight
candidate branches; final Hilbert obstructions use our own graded quotient.
"""
from pathlib import Path
import json,itertools,sympy as s
from cubic_incremental_graded import GradedAlgebra
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_CY_Veronese_input.json').read_text());assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
a,b,c,d=s.symbols('a b c d');Y=[a,b,c,d];W=[a,b,c];pairs=list(itertools.combinations(range(4),2));qs=[a*a,b*b,c*c,a*b,a*c,b*c]
def parse(t):return s.sympify(t,locals={'Matrix':s.Matrix})
def quad(p):
 pp=s.Poly(s.expand(p),*Y);col=s.zeros(16,1)
 for i in range(4):
  col[5*i]=pp.coeff_monomial(Y[i]**2)
  for j in range(i+1,4):col[4*i+j]=col[4*j+i]=pp.coeff_monomial(Y[i]*Y[j])/2
 return col
U=s.Matrix.hstack(*map(quad,qs));K=s.zeros(16,6)
for j,(k,l) in enumerate(pairs):K[4*k+l,j]=1;K[4*l+k,j]=-1
A=parse(D['SS_matrix']);B=parse(D['mixed_matrix']);C0=parse(D['KK_fixed']);g=s.Symbol('g');J=s.zeros(6);J[0,5]=J[5,0]=1;J[1,4]=J[4,1]=-1;J[2,3]=J[3,2]=1
assert A.det()==-s.Rational(1,4);x=sorted(B.free_symbols,key=lambda t:int(str(t)[1:]));assert len(x)==25
BM=s.Matrix(list(B)).jacobian(x);assert BM.rank()==25
words=list(itertools.product(range(4),repeat=4));ix={w:i for i,w in enumerate(words)}
def cyc(H):return s.Matrix([s.expand(H[4*w[3]+w[0],4*w[1]+w[2]]+H[4*w[0]+w[1],4*w[2]+w[3]]) for w in words])
H=U*A*U.T+U*B*K.T+K*B.T*U.T+K*(C0+g*J)*K.T;assert cyc(H)==s.zeros(256,1)
columns=[]
for i,j in itertools.product(range(6),repeat=2):columns.append(cyc(U[:,i]*K[:,j].T+K[:,j]*U[:,i].T))
mixed_cyclic=s.Matrix.hstack(*columns);assert mixed_cyclic.rank()==11
kk=[]
for i,j in itertools.combinations_with_replacement(range(6),2):kk.append(cyc(K[:,i]*K[:,j].T+(K[:,j]*K[:,i].T if i!=j else s.zeros(16))))
KKcyc=s.Matrix.hstack(*kk);assert KKcyc.rank()==20 and mixed_cyclic.row_join(KKcyc).rank()==31
z6=s.symbols('z:6');Z=s.Matrix([[z6[0],z6[3],z6[4]],[z6[3],z6[1],z6[5]],[z6[4],z6[5],z6[2]]]);adj=Z.adjugate()
for n0,expected in [(1,3),(2,4),(3,6)]:assert (s.hessian(sum(adj[i,i] for i in range(n0)),z6)/2).rank()==expected
m4=[s.prod(W[i] for i in v) for v in itertools.combinations_with_replacement(range(3),4)];products=s.Matrix.hstack(*[s.Matrix([s.Poly(qs[i]*qs[j],*W).coeff_monomial(v) for v in m4]) for i,j in itertools.combinations_with_replacement(range(6),2)]);assert products.rank()==15

Phi=parse(D['isotropic_plane_isometry']);assert (Phi.T*A.inv()*Phi+8*J).applyfunc(s.expand)==s.zeros(6)
mons3=[s.prod(W[i] for i in z) for z in itertools.combinations_with_replacement(range(3),3)];p=s.symbols('p:10');f=sum(v*m for v,m in zip(p,mons3));grad=s.Matrix([[s.Poly(s.diff(f,v)/3,*W).coeff_monomial(q) for v in W] for q in qs])
plane_records=[]
J4=s.zeros(4);J4[0,3]=1;J4[3,0]=-1;J4[1,2]=-s.Rational(1,3);J4[2,1]=s.Rational(1,3)
def exterior(v,w):return s.Matrix([v[i]*w[j]-v[j]*w[i] for i,j in pairs])

for r in D['plane_and_cubic_audits']:
 L=parse(r['plane']);sv={'triple':s.Matrix([1,0,0,0]),'double':s.Matrix([0,1,0,0]),'distinct':s.Matrix([0,1,-1,0])}[r['root_type']]
 if r['type']=='alpha':raw=s.Matrix.hstack(*[exterior(sv,s.eye(4)[:,j]) for j in range(4)])
 else:
  hh=(sv.T*J4).nullspace();raw=s.Matrix.hstack(*[exterior(hh[i],hh[j]) for i,j in itertools.combinations(range(3),2)])
 assert L.row_join(Phi*raw).rank()==3
 assert L.rank()==3 and (L.T*A.inv()*L).applyfunc(s.expand)==s.zeros(3)
 perp=s.Matrix.hstack(*L.T.nullspace());eq=list(perp.T*grad);AA,_=s.linear_eq_to_matrix(eq,p);ps=list(map(parse,r['cubic_kernel']));basis=s.Matrix.hstack(*[s.Matrix([s.Poly(q,*W).coeff_monomial(v) for v in mons3]) for q in ps]);assert AA*basis==s.zeros(AA.rows,basis.cols) and basis.rank()==10-AA.rank()==r['dimension'];plane_records.append({'type':r['type'],'root_type':r['root_type'],'cubic_dimension':basis.cols})
# Equivariance of the isometry under both generators of sl2.
def wedge4(v,w):return s.Matrix([v[i]*w[j]-v[j]*w[i] for i,j in pairs])
for deriv,M in [([-c,-s.I*c,a+s.I*b],s.Matrix([[0,1,0,0],[0,0,2,0],[0,0,0,3],[0,0,0,0]])),([c,-s.I*c,-a+s.I*b],s.Matrix([[0,0,0,0],[3,0,0,0],[0,2,0,0],[0,0,1,0]]))]:
 E=s.Matrix.hstack(*[wedge4(M[:,i],s.eye(4)[:,j])+wedge4(s.eye(4)[:,i],M[:,j]) for i,j in pairs]);Q=s.Matrix.hstack(*[s.Matrix([s.Poly(sum(s.diff(q,W[j])*deriv[j] for j in range(3)),*W).coeff_monomial(v) for v in qs]) for q in qs]);assert (Q*Phi-Phi*E).applyfunc(s.expand)==s.zeros(6)
# Complete normalizations in both three-dimensional integrable cubic spaces.
u0,v0,w0,t0,aa,bb0,cc0=s.symbols('u0 v0 w0 t0 aa bb0 cc0');sub0={v0:v0+t0*u0,w0:w0+2*t0*v0+t0*t0*u0}
assert s.expand((u0*u0*(aa*u0+bb0*v0+cc0*w0)).subs(sub0,simultaneous=True)-u0*u0*((aa+bb0*t0+cc0*t0*t0)*u0+(bb0+2*cc0*t0)*v0+cc0*w0))==0
assert s.expand((aa*u0**3+bb0*u0*u0*v0+cc0*u0*(-u0*w0+8*v0*v0)).subs(sub0,simultaneous=True)-((aa+bb0*t0+7*cc0*t0*t0)*u0**3+(bb0+14*cc0*t0)*u0*u0*v0+cc0*u0*(-u0*w0+8*v0*v0)))==0
R=U+K*B.T*A.inv();res=(C0+g*J-B.T*A.inv()*B).applyfunc(s.expand);ext=[2,4,5];inside=[0,1,3];audit=[]
zero_variables=set().union(*(v.free_symbols for v in B[:,ext]));zero={v:0 for v in zero_variables};assert s.expand(res[0,5].subs(zero))==g
Rzero=R.subs({**zero,g:0});assert all(not Rzero[i,j] for i in [3,7,11,12,13,14,15] for j in range(6));assert 1+3*3+2*3+3*3==25
for record in D['candidate_audits']:
 name=record['name'];values={s.Symbol(k):parse(v) for k,v in record['cubic_coefficients'].items()};lin={s.Symbol(k):parse(v) for k,v in record['linear_substitution'].items()};D1=res.subs(values).applyfunc(s.expand);vars0=[z for z in x if z not in values]+[g];AA,bb=s.linear_eq_to_matrix(list(D1.extract(inside,ext)),vars0);sol=s.Matrix([lin[z] for z in vars0]);assert (AA*sol-bb).applyfunc(s.expand)==s.zeros(AA.rows,1)
 free=sorted(set().union(*(z.free_symbols for z in sol)),key=str);assert sol.jacobian(free).rank()==len(vars0)-AA.rank()
 DD=D1.subs(lin,simultaneous=True).applyfunc(s.expand);RR=R.subs(values).subs(lin,simultaneous=True).applyfunc(s.expand)
 if name in ['cube','tangent','transverse','transverse_cube']:
  assert lin[g]==0;ell=a+s.I*b;coeff=s.Matrix([s.Poly(s.expand(ell*ell),*W).coeff_monomial(q) for q in qs]);assert (RR*coeff-quad(ell*ell)).applyfunc(s.expand)==s.zeros(16,1);audit.append({'case':name,'exclusion':'actual square relation'});continue
 variables=sorted(set().union(*(z.free_symbols for z in DD)),key=str);GB=s.groebner(list(DD),*variables,order='grevlex',domain=s.QQ_I);target=s.groebner(list(map(parse,record['basis'])),*variables,order='grevlex',domain=s.QQ_I);assert all(GB.reduce(q.as_expr())[1]==0 for q in target.polys) and all(target.reduce(q.as_expr())[1]==0 for q in GB.polys)
 if name in ['mixed','mixed_cube']:assert list(GB)==[1];audit.append({'case':name,'exclusion':'unit residual ideal'});continue
 normal={s.Symbol(k):parse(v) for k,v in record['normal'].items()};RN=R.subs(normal).applyfunc(s.simplify);assert res.subs(normal).applyfunc(s.simplify)==s.zeros(6)
 field=s.QQ_I if name=='alpha_distinct' else s.QQ.algebraic_field(s.I,s.sqrt(3));rels=[{divmod(i,4):field.from_sympy(RN[i,j]) for i in range(16) if RN[i,j]} for j in range(6)];C=GradedAlgebra(field,4,rels,[0]*4);C.build(3 if name=='alpha_distinct' else 4);dims=[len(C.basis[i]) for i in range(4 if name=='alpha_distinct' else 5)];assert dims==record['dimensions']
 # Translate d by an arbitrary vector in W. Recover graph coefficients in
 # the original tensor frame, and verify the full three-parameter orbit.
 zt=s.symbols('z0:3');E=s.eye(4)
 for j in range(3):E[j,3]=zt[j]
 image=(s.kronecker_product(E,E)*RN).applyfunc(s.expand);F=(K.T*K).inv()*K.T*(image-U);BT=(A*F.T).applyfunc(s.expand);rp=list(BM.T.rref()[1]);coords=(BM.extract(rp,range(25)).inv()*s.Matrix(list(BT)).extract(rp,[0])).applyfunc(s.expand);frees=list(map(parse,record['translation_parameters']));links=[next(k for k,v in lin.items() if v==t) for t in frees];ims=[coords[x.index(k)] for k in links];assert all(s.simplify(u-v)==0 for u,v in zip(ims,map(parse,record['translation_images'])));jac=s.factor(s.Matrix(ims).jacobian(zt).det());assert jac==parse(record['translation_jacobian']) and jac
 tau6=s.Symbol('tau6');gamma=normal[g];subtau={tau6:gamma,**dict(zip(frees,ims))};remaining=sorted(set(variables)-set(frees)-{tau6},key=str);eq=[s.expand(q.as_expr().subs(subtau,simultaneous=True)) for q in GB.polys];soltau=s.solve(eq,remaining,dict=True);assert len(soltau)==1;alltau={**subtau,**soltau[0]};params={**values,**{k:s.simplify(v.subs(alltau,simultaneous=True)) for k,v in lin.items()}};targetR=R.subs(params).applyfunc(s.simplify);assert (image-targetR).applyfunc(s.simplify)==s.zeros(16,6)
 # Both signs: the literal diagonal flip preserves the external cubic and
 # sends the full graph's gamma to its negative.
 flip=s.diag(1,-1,-1,-1);symflip=s.diag(1,1,1,-1,-1,1);RF=(s.kronecker_product(flip,flip)*RN*symflip).applyfunc(s.expand);FF=(K.T*K).inv()*K.T*(RF-U);BF=(A*FF.T).applyfunc(s.expand);assert (BF[:,ext]-B[:,ext].subs(normal)).applyfunc(s.simplify)==s.zeros(6,3);assert (BF.T*A.inv()*BF-C0+gamma*J).applyfunc(s.simplify)==s.zeros(6)
 audit.append({'case':name,'independent_dimensions':dims,'translation_jacobian':str(jac),'both_signs':True,'exclusion':'entire translation orbit has nonAS4 Hilbert values'})
report={'status':'PASS','scope':'scoped complete Veronese projection exclusion, independent original-frame/downstream controls using pinned minimal proof input','source_commit':D['source_commit'],'mixed_cyclic_kernel_dimension':25,'all_six_integrability_planes':plane_records,'zero_cubic_degree3_lower_bound':25,'all_eight_candidates':audit,'independent_Hilbert_method':'our GradedAlgebra, original defining relation insertions over exact QQ(i) and QQ(i,sqrt3)','ordinary_dependencies':['all maximal isotropic plane and binary cubic root orbit coverage','normalization of integrable cubic strata','geometric projection recovery in paper'],'not_claimed':['whole CY atlas audited','all CI22 charts imported','full H3 classification','novelty confirmed','ordinary geometric proof mechanically formalized']}
(ROOT/'cubic_CY_Veronese_certificate.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS all25 mixed directions, six cubic kernels, eight complete strata, both entire final orbits and fresh exact Hilbert obstructions')
