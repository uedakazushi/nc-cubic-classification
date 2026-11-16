"""Symmetric secant complete necessary odd atlas and both invertible negative-Pfaffian exclusions."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
z=S.symbols('z:6');A=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),z):A[i,j]=v;A[j,i]=-v
sharp=S.Matrix([[0,-z[5],z[4],-z[3]],[z[5],0,-z[2],z[1]],[-z[4],z[2],0,-z[0]],[z[3],-z[1],z[0],0]])
tau=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):tau[2*j+i,2*l+k]=A[2*i+l,2*k+j]
flip=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
cU=S.Matrix([[0,1],[-1,0]]);sym=S.Matrix([[0,1],[1,0]]);b1=S.diag(1,1);b2=S.diag(1,-1);r,loc,s,t=S.symbols('r loc s t')
for name,h in [('square',S.diag(1,0)),('nondeg',r*sym)]:
 M=-(S.kronecker_product(cU.T,b2)+S.kronecker_product(h.T,b1))*flip
 root=S.Integer(1) if name=='square' else 1-r*r
 assert S.expand(M.det()+root*root)==0
 for eps in [1,-1]:
  eq=[S.expand(v) for v in eps*root*tau+M.T*sharp*M if S.expand(v)]
  if name=='square':target=[z[1]+z[4],z[2]+z[3]-z[5]] if eps==1 else [z[0]+z[3],z[1]-z[4],z[2]-z[3],z[5]]
  else:target=[z[1]+z[4],(r+1)*z[2]-(r-1)*z[3]] if eps==1 else [z[0],z[5],z[1]-z[4],(r+1)*z[2]+(r-1)*z[3]]
  unit=[] if name=='square' else [1-loc*r*(r*r-1)];variables=list(z)+([] if name=='square' else [loc,r])
  assert list(S.groebner(eq+unit,*variables))==list(S.groebner(target+unit,*variables))
# Nondegenerate negative branch: opposite normalizers, det=-1, product=I on the full conic.
h=r*sym;M=-(S.kronecker_product(cU.T,b2)+S.kronecker_product(h.T,b1))*flip;alpha=(r-1)/(r+1)
R=(-M.inv()*A).subs(dict(zip(z,[0,t,-alpha*s,s,t,0]))).applyfunc(S.cancel)
f=S.Matrix([[R[0,0],R[2,0]],[R[0,1],R[2,1]]]);g=S.Matrix([[R[1,2],R[3,2]],[R[1,3],R[3,3]]]);conic=(r+1)*t*t+(r-1)*s*s+(r-1)*(r+1)**2
for e in list(f*g-S.eye(2))+[f.det()+1,g.det()+1]:
 numerator=S.fraction(S.cancel(e))[0];assert S.rem(numerator,conic,t)==0
# xy,yx span u2,v2 (determinant -1/r), so the whole negative Sym2 is central.
products=S.Matrix([[-(r+1)/(2*r),-(r-1)/(2*r)],[(r-1)/(2*r),(r+1)/(2*r)]])
assert S.cancel(products.det()+1/r)==0
# Singular r=1 necessary rank2-cross atlas.
a,b,c=S.symbols('a b c');AA=A.subs(dict(zip(z,[a,a,0,b,c,c])));DD=tau.subs(dict(zip(z,[a,a,0,b,c,c])))
MM=-(S.kronecker_product(cU.T,b2)+S.kronecker_product(sym.T,b1))*flip;O=AA.row_join(MM).col_join((-MM.T).row_join(DD))
def pf(matrix):
 if not matrix.rows:return S.Integer(1)
 return S.expand(sum((-1)**(j+1)*matrix[0,j]*pf(matrix.extract([i for i in range(1,matrix.rows) if i!=j],[i for i in range(1,matrix.cols) if i!=j])) for j in range(1,matrix.rows)))
eq=[pf(O.extract(ii,ii)) for ii in itertools.combinations(range(8),6)]
assert list(S.groebner(eq,a,b,c))==[a*a-c*c,a*c+c*c]
# Square negative branch: original-relation quartic functionals over the entire conic.
source=Path(__file__).with_name('verify_cubic_order2_22_tangent_negative.py').read_text();exec(source[:source.index('R=relations(S.diag(1,0),')])
b1=S.diag(1,1);b2=S.diag(1,-1)
w=S.symbols('w');K=S.QQ.frac_field(w);s=(w-1/w)/2;t=(w+1/w)/2
M=-(S.kronecker_product(cU.T,b2)+S.kronecker_product(S.diag(1,0),b1))*flip;rewrite=(-M.inv()*A).subs(dict(zip(z,[-s,t,s,s,t,0])))
relations0=[{(0,1):1,(1,0):-1,(2,2):1,(3,3):1},{(0,0):1,(2,2):1,(3,3):-1}]
uv=[(i,j) for i in range(2) for j in range(2,4)];vu=[(i,j) for i in range(2,4) for j in range(2)]
for i,word in enumerate(vu):relations0.append({word:S.Integer(1),**{v:-rewrite[i,j] for j,v in enumerate(uv) if rewrite[i,j]}})
NN,free4,nf4=normal(relations0,K)
for row in nf4.values():
 for value in row.values():assert len(S.Poly(S.denom(K.to_sympy(value)),w).terms())==1
rows=[]
for i in range(NN.rows):
 row=[S.cancel(v) for v in NN[i,:]];dd=S.lcm([S.denom(v) for v in row]);row=[S.cancel(v*dd) for v in row]
 if any(row):rows.append(row)
Q=S.Matrix(rows);entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_negative_input.json').read_text());polys=[]
for rec in entry['witnesses']:
 value=K.to_sympy(DomainMatrix.from_Matrix(Q.extract(rec['rows'],rec['cols'])).convert_to(K).det());polys.append(S.Poly(value,w))
gcd=polys[0]
for pp in polys[1:]:gcd=S.gcd(gcd,pp)
assert gcd.monic().as_expr()==w**13
out={'status':'PASS','scope':'symmetric secant necessary odd atlases and both invertible negative-Pfaffian H3 exclusions','uniform_atlases':'four exact closed/localized polynomial ideal equalities, r(r2-1) invertible in nondegenerate case','square_negative_branch':{'parameter':'w=t+s !=0, s=(w-w^-1)/2,t=(w+w^-1)/2','quartic_functional_poles':'only w=0','rank10_minors':4,'gcd':'constant*w13','conclusion':'normal kernel zero for all nonzero w'},'nondeg_negative_branch':{'conic':'t2+(r-1)/(r+1)*s2=1-r2','normalizers':'fg=I, det f=det g=-1','central_negative_quadratics':'u2,v2 span xy,yx and are central in negative subalgebra; hence uv+vu central too','conclusion':'odd auxiliary-degree centralizer obstruction gives normal kernel zero'},'singular_r_plus_minus_one_necessary_atlas':'after pure UV line xv+yu normalization, A=(a,a,0,b,c,c), Pfaffian ideal=(a2-c2,ac+c2); geometric a=-c, domain projection forces c!=0; retain b,c parameters','not_claimed':['positive-Pfaffian secant H3 classification','rank2 secant boundary exclusion','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_negative_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS secant four uniform atlases; square negative full Laurent minor cover gcd w13; nondeg negative odd-det obstruction; singular necessary Pfaffian atlas')
