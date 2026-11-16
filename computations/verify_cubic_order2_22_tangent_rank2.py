"""Last tangent rank2-cross boundary: necessary atlas, all-parameter normal exclusion, Jordan rigidity."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
# Negative cyclic top fixed by a nontrivial unipotent has rank <=1 when rank <=2.
z=S.symbols('z:6');Q=S.Matrix([[z[0],z[1],z[1],z[2]],[z[1],z[3],z[2],z[4]],[z[1],z[2],z[3],z[4]],[z[2],z[4],z[4],z[5]]])
J=S.Matrix([[1,1],[0,1]]);HH=S.kronecker_product(J,J);sol=list(S.linsolve(list(HH*Q*HH.T-Q),z))[0]
assert sol==(z[0],0,-z[3]/2,z[3],0,0)
assert S.factor(Q.subs(dict(zip(z,sol)),simultaneous=True).det())==-3*z[3]**4/16
# One-sided unipotent-fixed UV tensors are products.
N=S.kronecker_product(J,S.eye(2))-S.eye(4);x0,x1=S.symbols('x0 x1')
assert N*S.Matrix([x0,x1,0,0])==S.zeros(4,1)
assert N.rank()==2 and S.Matrix([[x0,x1],[0,0]]).det()==0
# After normalizing the nondecomposable pure UV line to p=xv+yu, A=p wedge r.
a,b,c=S.symbols('a b c');values=[a,a,0,b,c,c];A=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),values):A[i,j]=v;A[j,i]=-v
D=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):D[2*j+i,2*l+k]=A[2*i+l,2*k+j]
M=S.Matrix([[0,1,-1,0],[-1,0,0,0],[-1,0,0,0],[0,0,0,0]])
O=A.row_join(M).col_join((-M.T).row_join(D))
def pf(matrix):
 if not matrix.rows:return S.Integer(1)
 return S.expand(sum((-1)**(j+1)*matrix[0,j]*pf(matrix.extract([i for i in range(1,matrix.rows) if i!=j],[i for i in range(1,matrix.cols) if i!=j])) for j in range(1,matrix.rows)))
eq=[pf(O.extract(ii,ii)) for ii in itertools.combinations(range(8),6)]
assert list(S.groebner(eq,a,b,c))==[b*b,b*c]
# Projected rank is 3 iff c!=0; an explicit minor is a unit multiple of c.
projection=A.row_join(M).subs(b,0);minors=[S.factor(projection.extract(rr,cc).det()) for rr in itertools.combinations(range(4),3) for cc in itertools.combinations(range(8),3)]
nonzero=[m for m in minors if m];assert nonzero and all(S.rem(m,c,c)==0 for m in nonzero)
assert any(m==c or m==-c for m in nonzero)
# Extract the canonical one-parameter relations directly from the alternating top image.
Rodd=S.Matrix([[0,1,1,0,0,0,0,0],[0,0,0,0,0,1,-1,0],[a,0,0,-1,1,0,0,0],[1,0,0,0,a,0,0,1]])
OO=O.subs({b:0,c:1})
assert S.Matrix.hstack(OO[:,3],-OO[:,7],OO[:,1],OO[:,5])==Rodd.T
assert Rodd[:,[1,5,3,7]].det()==-1
coeff=S.Matrix([[-a,0,0,1,-1,0,0,0],[-1,0,0,0,-a,0,0,-1],[0,1,1,0,0,0,0,0],[0,0,0,0,0,1,-1,0]])
assert Rodd.T*coeff==OO
# Exact original-relation quotient functions.
source=Path(__file__).with_name('verify_cubic_order2_22_tangent_negative.py').read_text();source=source[:source.index('R=relations(S.diag(1,0),')];exec(source)
def rel(value):return [{(0,1):1,(1,0):-1,(2,3):1,(3,2):1},{(0,0):1,(2,2):1},{(0,3):1,(1,2):1},{(2,1):1,(3,0):-1},{(2,0):1,(0,2):value,(1,3):-1},{(0,2):1,(2,0):value,(3,1):1}]
a=S.symbols('a');K=S.QQ.frac_field(a);NN,free4,nf4=normal(rel(a),K)
for row in nf4.values():
 for coeff in row.values():
  den=S.Poly(S.denom(K.to_sympy(coeff)),a)
  while den.degree():
   gg=S.gcd(den,S.Poly(a*a-1,a));assert gg.degree()>0;den=den.exquo(gg)
rows=[]
for i in range(NN.rows):
 row=[S.cancel(v) for v in NN[i,:]];dd=S.lcm([S.denom(v) for v in row]);row=[S.cancel(v*dd) for v in row]
 if any(row):rows.append(row)
Qm=S.Matrix(rows);entry=json.loads(Path(__file__).with_name('cubic_order2_22_tangent_rank2_input.json').read_text());polys=[]
for rec in entry['witnesses']:
 det=K.to_sympy(DomainMatrix.from_Matrix(Qm.extract(rec['rows'],rec['cols'])).convert_to(K).det());polys.append(S.Poly(det,a))
assert S.gcd(*polys).monic().as_expr()==a
points=[]
for value in [0,1,-1]:
 _,_,free3,_=quotient(rel(value),3,S.QQ);NM,free4,_=normal(rel(value),S.QQ)
 assert len(free3)==20 and len(free4)==35 and DomainMatrix.from_Matrix(NM).convert_to(S.QQ).rank()==10
 points.append({'a':value,'B3':20,'B4':35,'normal_functional_rank':10})
out={'status':'PASS','scope':'entire reverse-tangent square-positive-top rank2-cross boundary, all Jordan types','unipotent_negative_top':'fixed cyclic Q has determinant -3*z3^4/16; rank<=2 forces Q=a*u4, so nonzero rank2 Q admits no negative Jordan part','one_sided_positive_Jordan':'the pure UV relation line would lie in x tensor V and be a product, contradicting domain','geometric_necessary_atlas':'A=(a,a,0,b,c,c), all 6-Pfaffian ideal=(b2,bc); b=0 over geometric fields, projected rank forces c!=0, residual torus makes c=1','normal_family':'six explicit quadratic relations rel(a), no AS4 sufficiency assumption','quartic_annihilator_poles':'only a=+/-1','two_rank10_minor_gcd':'constant*a','exceptional_values':points,'conclusion':'no H3 on this last boundary; combined with previous results the entire negative tangent top type is empty','not_claimed':['relative nonreduced scheme b=0','negative secant or nonsymmetric rank2 types','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_tangent_rank2_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS last tangent boundary: exact Pfaffian atlas, one-parameter rank10 cover and all three exceptions, all Jordan rigidity')
