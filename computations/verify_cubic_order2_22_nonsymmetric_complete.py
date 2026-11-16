"""Entire nonsymmetric negative top: uniform odd atlas, fourth-power obstruction, singular boundary."""
import itertools,json
from pathlib import Path
import sympy as S
z=S.symbols('z:6');A=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),z):A[i,j]=v;A[j,i]=-v
sharp=S.Matrix([[0,-z[5],z[4],-z[3]],[z[5],0,-z[2],z[1]],[-z[4],z[2],0,-z[0]],[z[3],-z[1],z[0],0]])
tau=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):tau[2*j+i,2*l+k]=A[2*i+l,2*k+j]
flip=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
cU=S.Matrix([[0,1],[-1,0]]);sym=S.Matrix([[0,1],[1,0]]);b1=S.Matrix([[0,1],[S.I,0]]);b2=S.Matrix([[0,1],[-S.I,0]])
r,loc,s,k=S.symbols('r loc s k');records=[]
for name,h in [('square',S.diag(1,0)),('nondeg',r*sym)]:
 M=-(S.kronecker_product(cU.T,b2)+S.kronecker_product(h.T,b1))*flip
 root=S.I if name=='square' else S.I*(1-r*r)
 assert S.expand(M.det()+root*root)==0
 for eps in [1,-1]:
  p=eps*root;eq=[S.expand(v) for v in p*tau+M.T*sharp*M if S.expand(v)]
  target=list(z) if eps==1 else ([z[1],z[4],z[5],z[2]+z[3]] if name=='square' else [z[1],z[2],z[3],z[4]])
  unit=[] if name=='square' else [1-loc*r*(r*r-1)]
  variables=list(z)+([] if name=='square' else [loc,r])
  assert list(S.groebner(eq+unit,*variables,extension=S.I))==list(S.groebner(target+unit,*variables,extension=S.I))
 records.append({'positive':name,'detM':str(S.factor(M.det())),'plus_Pfaffian':'all A=0, impossible','minus_Pfaffian':'A=(z0,0,-s,s,0,0), s2=i' if name=='square' else 'A=(z0,0,0,0,0,z5), z0*z5=i*(r2-1)'})
 if name=='square':
  vals=[0,0,-s,s,0,0];rewrite=(-M.inv()*A).subs(dict(zip(z,vals)));F=S.Matrix([[S.I*s,-S.I*s],[0,-S.I*s]])
  assert rewrite.extract([0,1],[1,3])==S.zeros(2)
  assert (S.Matrix([[rewrite[0,0],rewrite[1,0]],[rewrite[0,2],rewrite[1,2]]])-F)==S.zeros(2)
  assert all(S.rem(S.expand(v),s*s-S.I,s)==0 for v in F*F+S.I*S.eye(2))
  # The positive shear removes every z0 without altering the other top coordinates.
  J=S.kronecker_product(S.Matrix([[1,k],[0,1]]),S.eye(2));As=A.subs(dict(zip(z,[z[0],0,-s,s,0,0])))
  assert J*As*J.T==A.subs(dict(zip(z,[z[0]-2*k*s,0,-s,s,0,0])))
 else:
  vals=[1,0,0,0,0,S.I*(r*r-1)];rewrite=(-M.inv()*A).subs(dict(zip(z,vals))).applyfunc(S.cancel);F=S.Matrix([[0,S.I/(r+1)],[-r-1,0]])
  assert rewrite.extract([0,1],[1,3])==S.zeros(2)
  assert (S.Matrix([[rewrite[0,0],rewrite[1,0]],[rewrite[0,2],rewrite[1,2]]])-F).applyfunc(S.cancel)==S.zeros(2)
  assert (F*F+S.I*S.eye(2)).applyfunc(S.cancel)==S.zeros(2)
 # Free positive quadratic identities uv=a(U), vu=b(U), F(b)=a, F(a)=-b.
 hv=S.Matrix([h[0,0],h[0,1],h[1,0],h[1,1]]);cv=S.Matrix([0,1,-1,0]);aa=-(hv+cv)/2;bb=(hv-cv)/(2*S.I)
 diff=S.kronecker_product(F,F)*bb-aa
 if name=='square':assert all(S.rem(S.expand(v),s*s-S.I,s)==0 for v in diff)
 else:assert diff.applyfunc(S.cancel)==S.zeros(4,1)
# Singular r=1: normalize the pure UV relation to xv+yu; rank4 odd top has A=p wedge v.
a,b,c=S.symbols('a b c');AA=A.subs(dict(zip(z,[a,a,0,b,c,c])));DD=tau.subs(dict(zip(z,[a,a,0,b,c,c])))
MM=-(S.kronecker_product(cU.T,b2)+S.kronecker_product(sym.T,b1))*flip
assert MM.rank()==2
O=AA.row_join(MM).col_join((-MM.T).row_join(DD))
def pf(matrix):
 if not matrix.rows:return S.Integer(1)
 return S.expand(sum((-1)**(j+1)*matrix[0,j]*pf(matrix.extract([i for i in range(1,matrix.rows) if i!=j],[i for i in range(1,matrix.cols) if i!=j])) for j in range(1,matrix.rows)))
eq=[pf(O.extract(ii,ii)) for ii in itertools.combinations(range(8),6)]
assert list(S.groebner(eq,a,b,c,extension=S.I))==[a*a,a*c,b,c*c]
# Both assignments are equivalent; the nonsymmetric factor pair is interchanged by u<->v.
P=S.Matrix([[0,1],[1,0]])
assert P*b1*P.T==S.I*b2 and P*b2*P.T==-S.I*b1
out={'status':'PASS','scope':'entire nonsymmetric rank2 negative-top type, all positive top and all Jordan types','full_cross_atlas':records,'fourth_power_obstruction':'uU=F(U)u, F2=-i*I, uv=a(U),vu=b(U),F(b)=a,F(a)=-b imply u2*v=-v*u2 and u4 anticommutes with U, commutes with V. A normal positive cubic both commutes and anticommutes with u4, hence is zero in a domain.','singular_r_plus_minus_one':'r=-1 equivalent to r=1; rank2-cross normalized A=(a,a,0,b,c,c), six-Pfaffian ideal=(a2,ac,b,c2), hence A=0 on geometric points, contradicting projection rank3','conclusion':'no H3 with this nonsymmetric negative top; only symmetric secant remains when P,Q are both nonzero','not_claimed':['nonreduced singular atlas is reduced','symmetric secant classification','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_nonsymmetric_complete_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire nonsymmetric type: four exact localized odd atlases, both fourth-power identities, singular Pfaffian obstruction')
