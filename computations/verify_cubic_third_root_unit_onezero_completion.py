#!/usr/bin/env python3
"""Exact identities for the remaining one-zero unit-repeat strata.
Ordinary normalizer/actual-Ore arguments are in the TeX proof.
"""
from pathlib import Path
import itertools,json,sympy as s
from sympy.polys.matrices import DomainMatrix
from cubic_incremental_graded import GradedAlgebra
from cubic_third_root_original22 import top_matrix,relation_vector
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));O=s.Symbol('omega')
def red(e):return s.rem(s.expand(e),O*O+O+1,O)
# The normal-b obstruction only needs these triangular eigenvalues.
spectral=[]
for eps in [1,-1]:
 eigen=[F.unit,eps*F.unit,F.one,eps*F.unit**2]
 vals=[]
 for w in itertools.product(range(4),repeat=3):
  if sum([0,0,1,2][j] for j in w)%3:continue
  c=F.one
  for j in w:c*=eigen[j]
  assert c in [F.one,-F.one] and c!=F.unit;vals.append(str(F.to_sympy(c)))
 spectral.append({'epsilon':eps,'fixed_tensor_words':len(vals),'eigenvalues':sorted(set(vals))})
# Minus branch: three normal-b relations are explicit source column identities.
K=F.frac_field('A','r','h','s','T');A,r,h,ss,T=K.gens;o=K.convert(F.unit,F);one,zero=K.one,K.zero
co=[zero]*22
for j,c in {2:A,3:(o+one)*A,6:-o*r,7:r,8:(o+one)*A,9:r,10:one,11:-o*h,12:-o*h,13:h,15:-o*ss,16:ss,17:ss,21:T}.items():co[j]=c
H=top_matrix(K,o,co).to_list()
col=lambda j:[row[j] for row in H]
def vec(poly):
 d=relation_vector(K,poly);return [d.get(j,zero) for j in range(16)]
assert all(not(a-b) for a,b in zip(col(10),vec({(0,2):one,(2,0):-o**2})))
assert all(not(a-r*b-ss*c) for a,b,c in zip(col(7),col(10),vec({(1,2):one,(2,1):-o**2})))
assert all(not(a+o*b-T*c) for a,b,c in zip(col(11),col(14),vec({(2,3):one,(3,2):-o**2})))
# In the matched a16zero branches the same exact source column identity
# makes b normal on c; the row ratio fixes the second eigenvalue on U.
for sign in [1,-1]:
 K=F.frac_field('B','r','h','Z','T');bb,r,h,Z,T=K.gens;o=K.convert(F.unit,F);one,zero=K.one,K.zero;lam=sign*o
 co=[zero]*22
 for j,c in {2:lam*bb,3:bb,6:lam*r,7:r,8:Z,9:r,10:one,11:lam*h,12:lam*h,13:h,21:T}.items():co[j]=c
 HM=top_matrix(K,o,co).to_list()
 assert all(not(row[11]-lam*row[14]-T*c) for row,c in zip(HM,[relation_vector(K,{(2,3):one,(3,2):lam*o}).get(j,zero) for j in range(16)]))
 assert all(not(a-lam*b) for a,b in zip(HM[6],HM[9]))
# Primitive4 lambda: Schur conditions determine the whole chart.
aa,rr,hh,kk,sc,lam=s.symbols('A r h k s lambda');I=s.I
R=s.Matrix([aa,lam*rr,-lam*(hh+kk*sc),lam**2*(O+1)*sc])
S=s.Matrix([(O+1)*aa+kk*(rr-hh),rr+kk*sc,-hh,sc]);P=R*R.T-O**2*S*S.T
assert red((P[1,3]+P[2,3]).subs(lam,-O)-2*(O+1)*kk*sc**2)==0
sub={lam:I*O,hh:rr+I*kk*sc}
assert red((P[1,1]+P[2,2]).subs(sub)-4*(O+1)*(rr+(1+I)*kk*sc/2)**2)==0
rsub=-(1+I)*kk*sc/2
expected=-2*(-aa*O*sc+I*(O+1)*kk**2*sc**2/2)
assert red((P[0,3]+P[1,2]).subs(sub).subs(rr,rsub)-expected)==0
# Fresh two points over Q(omega,i), all four embeddings.
L=s.QQ.alg_field_from_poly(s.Poly(z**4-z*z+1,z));q=L.unit;o=q**4;ii=q**3;one,zero=L.one,L.zero
assert not(o*o+o+one) and not(ii*ii+one)
fresh=[]
for k in [zero,one]:
 lam=ii*o;r=-(one+ii)*k/2;h=(-one+ii)*k/2;A=-ii*o*k*k/2
 co=[zero]*22
 for j,c in {2:A,17:lam*(o+one),15:lam**2*(o+one),16:one,6:lam*r,12:lam*h,7:r+k,11:lam*h+k*lam,8:(o+one)*A+k*r,3:(o+one)*A+k*(r-h),9:r,13:h,10:one,21:one}.items():co[j]=c
 R=[co[2],co[6],-co[11],co[15]];S=[co[3],co[7],-co[13],co[16]];P=[[R[i]*R[j]-o**2*S[i]*S[j] for j in range(4)] for i in range(4)]
 for j,c in {0:P[0][1],1:P[0][3],4:P[1][1],5:P[1][3]}.items():co[j]=c
 D=top_matrix(L,o,co);dv=D.to_list();ids0=[0,1,4,5]
 assert all(not(dv[ids0[i]][ids0[j]]-P[i][j]) for i in range(4) for j in range(4))
 dr,_=D.transpose().rref();rels=[{divmod(j,4):c for j,c in enumerate(row) if c} for row in dr.to_list() if any(row)];assert len(rels)==6
 B=GradedAlgebra(L,4,rels,[0,0,1,2]);B.build(3);dims=[len(B.basis[j]) for j in range(4)]
 assert dims==[1,4,10,23]
 fresh.append({'k':0 if not k else 1,'dimensions':dims,'excluded':'degree3 is23, AS4 requires20'})
# a16=0: corrected residual determinant and Schur identities.
A,Bb,Z,r,h,lam,T=s.symbols('A B Z r h lambda T')
N=s.Matrix([[(O+1)*(Bb-Z),-Z+(O+1)*A],[-(O+1)*h,-r]])
assert red(N.det()+(O+1)*(r*(Bb-Z)+h*(Z-(O+1)*A)))==0
R=s.Matrix([A,lam*r,-lam*h,0]);S=s.Matrix([Bb,r,-h,0]);P=R*R.T-O**2*S*S.T
assert red(P[1,2]+(lam**2-O**2)*r*h)==0
assert red(P[1,1]+P[2,2]-(lam**2-O**2)*(r*r+h*h))==0
assert red(P[0,1]+P[0,2]-(A*lam-O**2*Bb)*(r-h))==0
# Crossed branch: exact original relation image equals quantum-Weyl base Ore.
K=F.frac_field('B','r','Z','T');Bb,r,Z,T=K.gens;o=K.convert(F.unit,F);one,zero=K.one,K.zero;A=-o*Bb;lam=o
co=[zero]*22
for j,c in {0:-2*o**2*Bb*r/T,2:A,3:Bb,6:o*r,7:r,8:Z,9:r,10:one,11:o*r,12:o*r,13:r,21:T}.items():co[j]=c
D=top_matrix(K,o,co);q=-o**2;hb=2*o*Bb/T
rels=[{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},{(2,3):one,(3,2):-q,(0,0):-hb},
 {(1,0):one,(0,1):-one,(0,0):Bb/r,(2,3):-T/(o*r)},
 {(1,2):one,(2,1):-q,(2,0):(Z-Bb)/(o*r)},
 {(1,3):one,(3,1):o,(2,2):one/r,(0,3):(Z+Bb)/r}]
RV=[[rel.get(divmod(j,4),zero) for rel in rels] for j in range(16)]
RDM=DomainMatrix.from_dod({i:{j:c for j,c in enumerate(row) if c} for i,row in enumerate(RV)},(16,6),K)
assert D.rank()==RDM.rank()==D.hstack(RDM).rank()==6
lead=[2,3,11,4,6,7];small=RDM.extract(lead,range(6));assert not(small.det()-one)
coordinates=small.inv().matmul(D.extract(lead,range(16)))
assert not any((RDM.matmul(coordinates)-D).to_list_flat())
support=(r*T).numer
for c in coordinates.to_list_flat():
 poly=c.denom
 while any(sum(mm)>0 for mm in poly.monoms()):
  gg=poly.gcd(support);assert any(sum(mm)>0 for mm in gg.monoms());poly=poly.exquo(gg)

out={'status':'PASS','normal_b_spectral_check':spectral,'minus_explicit_source_normal_b_relations':'PASS with only s,T denominators','primitive4_lambda_field':'t^4-t^2+1, omega=t4,i=t3','primitive4_fresh':fresh,'a16zero_residual_determinant':'r*(B-Z)+h*(Z-(omega+1)*A)=0','a16zero_Schur_identities':'PASS','crossed_branch_original_image_equals_actual_Ore_relations':'PASS; displayed relation unit6minor, originalH=displayedR*coordinates reinserted, all coordinate denominators supported onlyrT','crossed_F':'-B/r*x2+T/(omega*r)*bc nonzero','scope':'ordinary exhaustive onezero completion proof uses domain, full AS4 Hilbert series and previously proved Fnonzero Ore obstruction','not_claimed':['nonunit-repeat spectra excluded','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_onezero_completion_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS remaining onezero Schur/normalizer/fresh/Ore identities')
