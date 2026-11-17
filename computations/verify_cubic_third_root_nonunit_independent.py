#!/usr/bin/env python3
"""Complete independent-b^2-coupling obstruction in the nonunit-repeat atlas.
Original22 normal form, homogeneous determinant, all-value Smith compatibilities,
then fresh unique node normal-cubic rank. Characteristic zero throughout.
"""
from pathlib import Path
import sympy as s,json
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
from cubic_third_root_original22 import top_matrix
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));os=F.to_sympy(F.unit);O=s.Symbol('omega');a=s.symbols('a:22')
def red(e):return s.rem(s.expand(e),O*O+O+1,O)
P0=F.poly_ring(*a);oo=P0.convert(F.unit,F)
HS=top_matrix(P0,oo,list(P0.gens),[1,1,0,2]).to_Matrix().xreplace({os:O}).applyfunc(red)
H0=HS.extract([3,7,10,12,13],[3,7,10,12,13]);M=HS.extract([2,6,8,9,15],[0,1,4,5,11,14])
assert H0==H0.T and not H0[2,2]
t,m,n,T=s.symbols('t m n T')
sub={a[13]:1,a[20]:0,a[9]:0,a[17]:-O**2,a[11]:0,a[19]:0,a[12]:t,a[3]:t,a[14]:0,a[7]:0,a[16]:-O**2*t,a[10]:m,a[18]:n,a[21]:T}
N=M.subs(sub).applyfunc(red);Hn=H0.subs(sub).applyfunc(red)
p=s.Matrix([1,0,0,0,1]);v=s.Matrix([0,t,1,-O*t,0]);assert (Hn-p*v.T-v*p.T).applyfunc(red)==s.zeros(5)
P=N.extract([1,2],[4,5]);J=m*n-O-1
assert red(P.det()-J)==0 and red(N.extract([0,3],[4,5]).det()-m*n)==0
res=[]
for j in [0,3,4]:res.extend(list((J*N[j,:]-N[j,4:6]*P.adjugate()*N[[1,2],:]).applyfunc(red))[:4])
vs=[a[j] for j in [0,1,2,4,5,6,8,15]]
CM,rhs=s.linear_eq_to_matrix([e.subs(O,os) for e in res],vs)
K=F.frac_field(t,m,n,T);A=DomainMatrix.from_Matrix(CM).convert_to(K)
homdet=A.extract(range(8),range(8)).det()
Fc=m**3+O*m*n-n**3;Lc=m+(O+1)*(n+1)
expected=O*Fc*J**4*Lc
assert not(homdet-K.from_sympy(expected.subs(O,os)))
print('PASS canonical self block and homogeneous determinant',flush=True)
q=s.Symbol('q');cases=[]
for name,ss0 in [('F',{m:-O*q*q/(q**3-1),n:-O*q/(q**3-1),t:1,T:1}),('L',{m:O**2*(q+1),n:q,t:1,T:1}),('J',{m:q,n:-O**2/q,t:1,T:1})]:
 if name=='J':
  NN=N.subs(ss0).applyfunc(lambda e:s.cancel(e).subs(O,os));pivot=NN.extract([0,3],[4,5]);eq=[]
  for j in [1,2,4]:eq.extend(list(NN[j,:]-NN[j,4:6]*pivot.inv()*NN[[0,3],:])[:4])
  C,b=s.linear_eq_to_matrix(eq,vs)
 else:
  C,b=s.linear_eq_to_matrix([s.cancel(e.subs(ss0)).subs(O,os) for e in res],vs)
 L=F.frac_field(q);Q=F.poly_ring(q);D=DomainMatrix.from_Matrix(C.row_join(b)).convert_to(L);ad={};bd={}
 allowed=L.field.ring.from_expr(q**3-1 if name=='F' else q if name=='J' else s.Integer(1))
 for i,row in D.to_dod().items():
  den=L.field.ring.one
  for cc in row.values():den=den.lcm(cc.denom)
  poly=den
  while poly.degree()>0:
   gg=poly.gcd(allowed);assert gg.degree()>0;poly=poly.exquo(gg)
  ad[i]={j:Q.convert(cc*L.new(den),L) for j,cc in row.items() if j<8}
  if 8 in row:bd[i]={0:Q.convert(row[8]*L.new(den),L)}
 AP=DomainMatrix.from_dod(ad,(12,8),Q).to_dense();BP=DomainMatrix.from_dod(bd,(12,1),Q).to_dense()
 SD,U,V=smith_normal_decomp(AP);assert U.matmul(AP).matmul(V)==SD
 assert U.det() and V.det() and U.det().degree()==V.det().degree()==0
 assert all(SD.to_list()[j][j] for j in range(8))
 last=[row[0] for row in U.matmul(BP).to_list()[8:]];g=Q.zero
 for cc in last:g=g.gcd(cc)
 g=g.monic();expected={'F':q*(q**6-q**3+1),'L':q*q+q+1,'J':q}[name]
 assert g==Q.from_sympy(expected)
 cases.append({'case':name,'coordinate_units':'q^3-1' if name=='F' else 'q' if name=='J' else 'none','matrix_shape':[12,8],'Smith_left_right_identity':'PASS','Smith_transform_determinants_constant':True,'compatibility_gcd':str(g.as_expr())})
 print('PASS allvalue Smith',name,g.as_expr(),flush=True)
# The remaining m=n=0 node has exactly one solution for the eight cube entries.
node={m:0,n:0,t:1,T:1};C0=CM.subs(node);b0=rhs.subs(node)
D0=DomainMatrix.from_Matrix(C0.row_join(b0)).convert_to(F);nr,np=D0.rref();assert list(np)==list(range(8))
solution=[row[8] for row in nr.to_list()[:8]]
assert solution==[F.zero,-F.one,F.zero,F.zero,F.unit,F.zero,F.zero,F.zero]
co=[F.zero]*22
for j,c in {1:-F.one,3:F.one,5:F.unit,12:F.one,13:F.one,16:-F.unit**2,17:-F.unit**2,21:F.one}.items():co[j]=c
D=top_matrix(F,F.unit,co,[1,1,0,2]);dr,_=D.transpose().rref();rels=[{divmod(j,4):c for j,c in enumerate(row) if c} for row in dr.to_list() if any(row)];assert len(rels)==6
B=GradedAlgebra(F,4,rels,[1,1,0,2]);NM,ids=B.normal_matrix(3,[F.unit**2,F.unit**2,F.one,F.unit],fixed=True)
assert len(ids)==7 and NM.rank()==7
_,minorrows=NM.transpose().rref();minor=NM.extract(minorrows,range(7)).det();assert minor
out={'status':'PASS','spectrum_weights':[1,1,0,2],'scope':'all independent left/right b-squared couplings; normal-form proof uses H3 domain and rank2; not whole nonunit atlas','canonical_self_relations':['xc+cy','b2+t*yc-omega*t*cx'],'canonical_parameters':['t','T','m','n'],'t_and_T_nonzero_necessary':True,'homogeneous_determinant':'omega*(m^3+omega*m*n-n^3)*(m*n-omega-1)^4*(m+(omega+1)*(n+1))','curves':cases,'unique_node_cube_coefficients':[list(map(str,c.to_list())) for c in solution],'node_normal_matrix':list(NM.shape),'node_normal_rank':7,'node_minor_rows':list(minorrows),'node_minor_determinant':list(map(str,minor.to_list())),'not_claimed':['proportional b-squared coupling excluded','zero b-squared coupling excluded','whole H3 complete']}
Path(__file__).with_name('cubic_third_root_nonunit_independent_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all independent nonunit b-squared couplings excluded',flush=True)
