#!/usr/bin/env python3
"""Complete isolated nonzero-T phase: rank-one Groebner consequences, a global
one-variable model, all source pivots, and four fresh points incl. Q=0 branch.
"""
from pathlib import Path
import itertools,json,sympy as s
from sympy.polys.matrices import DomainMatrix
from cubic_third_root_original22 import top_matrix
from cubic_third_root_nonunit_proportional_model import analyze,isolated_relations
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));os=F.to_sympy(F.unit);O=s.Symbol('omega');a=s.symbols('a:22')
def red(e):return s.rem(s.expand(e),O*O+O+1,O)
P=F.poly_ring(*a);o=P.convert(F.unit,F)
H=top_matrix(P,o,list(P.gens),[1,1,0,2]).to_Matrix().xreplace({os:O}).applyfunc(red)
M=H.extract([2,6,8,9,15],[0,1,4,5,11,14])
sub={a[13]:1,a[20]:0,a[9]:O,a[17]:0,a[11]:0,a[19]:0,a[12]:1,a[3]:0,a[14]:O**2,a[7]:O,a[16]:0,a[10]:-O**2,a[18]:0,a[21]:1}
N=M.subs(sub).applyfunc(red)
R=s.Matrix.vstack(N[2,:]-N[4,:],N[0,:]-O**2*N[4,:],N[1,:],N[3,:])[:,:4].applyfunc(red)
vs=[a[j] for j in [0,1,2,4,5,6,8,15]];eq=[]
for ii in itertools.combinations(range(4),2):
 for jj in itertools.combinations(range(4),2):eq.append(red(R.extract(ii,jj).det()).subs(O,os))
gb=s.groebner(eq,*vs,domain=F,order='grevlex');assert len(gb.polys)==11
A,B,d,C,E=a[0],a[2],a[4],a[8],a[15];W=B+O*d-2*O
consequences=[a[1]-(1+O)*B,a[5]-O*C,a[6]-(1+O)*C,A*W,E*W,C*C+O*E*(1-d),B*B-O*B-A*C,B*(d-1)+O**2*A*C,d*d-2*d+O**2*B-O*A*C,A*E+B*C]
for ff in consequences:assert not gb.reduce(red(ff).subs(O,os))[1]
Qdet=R[0,:].reshape(2,2).det();assert not gb.reduce(red(Qdet-O*B*W-1+d).subs(O,os))[1]
# All-zero cube sector has a pure c² relation; Qzero,E0 has pure x².
assert all(not N[j,1].subs({v:0 for v in vs}) for j in range(4)) and N[4,1]
qzero0={a[0]:0,a[1]:-1,a[2]:O,a[4]:1,a[5]:0,a[6]:0,a[8]:0,a[15]:0}
assert (N[1,:].subs(qzero0)-s.Matrix([[-O**2,0,0,0,0,0]])).applyfunc(red)==s.zeros(1,6)
# Necessary one-parameter and three fixed models, with source identities.
def coefficients(K,o,aa,dd,cc,ee):
 one,zero=K.one,K.zero;bb=o*(2-dd);co=[zero]*22
 for j,c in {13:one,9:o,12:one,14:o**2,7:o,10:-o**2,21:one,0:aa,1:(one+o)*bb,2:bb,4:dd,5:o*cc,6:(one+o)*cc,8:cc,15:ee}.items():co[j]=c
 return co
Dsym=s.Symbol('D');K=F.frac_field(Dsym);dd=K.gens[0];o=K.convert(F.unit,F);one,zero=K.one,K.zero
co=coefficients(K,o,one,dd,o**2*(2-dd)*(one-dd),-(2-dd)**2*(one-dd));DS=top_matrix(K,o,co,[1,1,0,2]);rels=isolated_relations(K,o,dd)
RM=DomainMatrix.from_dod({i:{j:rel.get(divmod(i,4),zero) for j,rel in enumerate(rels) if rel.get(divmod(i,4),zero)} for i in range(16)},(16,6),K)
lead=[3,10,15,2,0,14];small=RM.extract(lead,range(6));minor=small.det();assert minor and minor.numer.is_ground and minor.denom.is_ground
coords=small.inv().matmul(DS.extract(lead,range(16)));assert not any((RM.matmul(coords)-DS).to_list_flat())
assert all(c.denom.is_ground for c in coords.to_list_flat())
rs=analyze(K,o,zero,zero,source_relations=rels);bad=K.field.ring.one
for cc in rs['source_pivots']+rs['normal_pivots']:bad=bad.lcm(cc.numer).lcm(cc.denom)
bad=bad.sqf_part().monic();assert bad==K.field.ring.from_expr((Dsym-1)*(Dsym-2))
assert len(rs['normal_pivots'])==7 and all(c.numer.is_ground and c.denom.is_ground for c in rs['normal_pivots'])
# D1 with A1 has nonzero rank1 Q, so domain excludes it; D1 with A0 is
# a different Q=0 branch and MUST be tested separately, not discarded.
fresh=[];o=F.unit;one,zero=F.one,F.zero
for name,aa,dd,cc,ee in [('curveD2',one,2*one,zero,zero),('A0C1',zero,2*one,one,o**2),('A0C0',zero,2*one,zero,zero),('Qzero',zero,one,zero,one)]:
 co=coefficients(F,o,aa,dd,cc,ee);D0=top_matrix(F,o,co,[1,1,0,2]);dr,_=D0.transpose().rref();rels0=[{divmod(j,4):c for j,c in enumerate(row) if c} for row in dr.to_list() if any(row)]
 assert len(rels0)==6
 BB=GradedAlgebra(F,4,rels0,[1,1,0,2]);NM,ids=BB.normal_matrix(3,[o**2,o**2,one,o],fixed=True);dims=[len(BB.basis[j]) for j in range(5)];nr=NM.rank()
 assert dims[3:]!=[20,35] or nr==len(ids)
 fresh.append({'case':name,'dimensions':dims,'normal_shape':list(NM.shape),'normal_dimension':len(ids)-nr})
out={'status':'PASS','scope':'all v1,n0,Tnonzero proportional nonunit boundary; includes Q=0 exceptional branch','rankone_minors':len(eq),'Groebner_basis':[str(p.as_expr()) for p in gb.polys],'cover':['A1,Dneq1 curve','A0,D2,C1','A0,D2,C0','Qzero:A0,D1,C0,E1'],'source_curve_identity':'unit6minor and originalH=displayedR*coords, only coefficient-field denominators','curve_normal_shape':rs['normal_shape'],'curve_constant_normal_pivots':7,'curve_bad_polynomial':'(D-1)*(D-2)','fresh_points':fresh,'not_claimed':['v0 self excluded','zero coupling excluded','wholeH3 complete']}
Path(__file__).with_name('cubic_third_root_nonunit_isolated_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire isolated nonzero-T proportional nonunit phase')
