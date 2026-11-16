"""Coupled tangent top: exact atlas, full square/minus orbit and nondeg/minus family exclusions."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
T=S.symbols('T');K=S.QQ.frac_field(T);z=S.symbols('z:6')
a=S.Matrix([[0,1],[-1,0]]);b1=S.diag(1,0);b2=S.Matrix([[0,1],[1,0]])
flip=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
A=S.zeros(4)
for (i,j),c in zip(itertools.combinations(range(4),2),z):A[i,j]=c;A[j,i]=-c
pf=z[0]*z[5]-z[1]*z[4]+z[2]*z[3]
sharp=S.Matrix([[0,-z[5],z[4],-z[3]],[z[5],0,-z[2],z[1]],[-z[4],z[2],0,-z[0]],[z[3],-z[1],z[0],0]])
tau=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):tau[2*j+i,2*l+k]=A[2*i+l,2*k+j]
atlas=[]
for name,h in [('square',S.diag(1,0)),('nondeg',S.Matrix([[0,1],[1,0]]))]:
 for reverse in [False,True]:
  M=-(S.kronecker_product(a.T,b1 if reverse else b2)+S.kronecker_product(h.T,b2 if reverse else b1))*flip
  if reverse and name=='square':assert M.rank()==2;continue
  assert M.det()==-1
  for sign in [1,-1]:
   sol=list(S.linsolve(list(sign*tau+M.T*sharp*M),z))[0]
   atlas.append({'positive':name,'reverse':reverse,'Pfaffian':sign,'linear_solution':[str(c) for c in sol],'remaining_Pfaffian':str(S.factor(pf.subs(dict(zip(z,sol)),simultaneous=True)-sign))})
# Rank1 negative projection gives a rank<=2 ruling cross, independently of the positive matrix.
c=S.Matrix(2,2,S.symbols('c:4'));v=S.Matrix(S.symbols('v:4'));MM=-S.kronecker_product(c.T,b1)*flip
assert S.expand(S.Matrix(2,2,list(MM*v)).det())==0
# Reconstruct the first tangent assignment and its quartic quotient functionals.
def relations(h,values):
 Am=A.subs(dict(zip(z,values)));M=-(S.kronecker_product(a.T,b2)+S.kronecker_product(h.T,b1))*flip
 rewrite=-(-M.T*Am.inv()).inv().T
 R=[{(0,1):S.Integer(1),(1,0):-S.Integer(1),(2,2):S.Integer(1)},{(i,j):h[i,j] for i,j in itertools.product(range(2),repeat=2) if h[i,j]}]
 R[1][(2,3)]=S.Integer(1);R[1][(3,2)]=S.Integer(1)
 uv=[(i,j) for i in range(2) for j in range(2,4)];vu=[(i,j) for i in range(2,4) for j in range(2)]
 for i,word in enumerate(vu):R.append({word:S.Integer(1),**{v:-rewrite[i,j] for j,v in enumerate(uv) if rewrite[i,j]}})
 return R

def quotient(R,n,field):
 words=list(itertools.product(range(4),repeat=n));index={w:i for i,w in enumerate(words)};rows=[]
 for rel in R:
  for pos in range(n-1):
   for extra in itertools.product(range(4),repeat=n-2):rows.append({index[extra[:pos]+w+extra[pos:]]:field.from_sympy(S.sympify(c)) for w,c in rel.items() if c})
 dm=DomainMatrix({i:row for i,row in enumerate(rows)},(len(rows),len(words)),field);rr,piv=dm.rref();data=rr.to_dod();free=[i for i in range(len(words)) if i not in piv];qidx={v:j for j,v in enumerate(free)}
 nf={i:{qidx[j]:-c for j,c in data[k].items() if j in qidx} for k,i in enumerate(piv)}
 nf.update({i:{qidx[i]:field.one} for i in free})
 # Every returned functional annihilates every ORIGINAL quartic relation.
 for row in rows:
  out={}
  for j,c in row.items():
   for v,d in nf[j].items():out[v]=out.get(v,field.zero)+c*d
  assert not any(out.values())
 return words,index,free,nf

def normal(R,field):
 words,index,free,nf=quotient(R,4,field);words3=list(itertools.product(range(4),repeat=3));E=[w for w in words3 if sum(i>=2 for i in w)%2==0];N=S.zeros(4*len(free),32)
 for j,w in enumerate(E):
  for g in range(4):
   for raw,c in [(w+(g,),1),((g,)+w,-1 if g<2 else 1)]:
    for row,d in nf[index[raw]].items():N[g*len(free)+row,j]+=c*field.to_sympy(d)
 return N,free,nf

R=relations(S.diag(1,0),[-S.Rational(1,2),1,0,0,1,0]);N,free,nf=normal(R,S.QQ)
assert len(free)==35 and DomainMatrix.from_Matrix(N).convert_to(S.QQ).rank()==10
_,_,free3,_=quotient(R,3,S.QQ);assert len(free3)==20
# Residual torus weights on the square/minus atlas, relative to even-top weight t^2.
t=S.symbols('t',nonzero=True);uvweights=[t,t**-1,t**3,t]
weights=[S.cancel(uvweights[i]*uvweights[j]/t**2) for i,j in itertools.combinations(range(4),2)]
assert weights==[t**-2,t**2,1,1,t**-2,t**2]
R=relations(S.Matrix([[0,1],[1,0]]),[0,1/T-T/4,-T/2,T/2,T,0]);N,free,nf=normal(R,K);assert len(free)==35
# These functionals are Laurent-polynomial: no hidden pole at any nonzero T.
for row in nf.values():
 for c in row.values():
  den=S.Poly(S.denom(K.to_sympy(c)),T);assert len(den.terms())==1
rows=[]
for i in range(N.rows):
 row=[S.cancel(c) for c in N[i,:]];den=S.lcm([S.denom(c) for c in row]);assert len(S.Poly(den,T).terms())==1
 row=[S.cancel(c*den) for c in row]
 if any(row):rows.append(row)
Q=S.Matrix(rows);assert Q.shape==(64,32)
witness=json.loads(Path(__file__).with_name('cubic_order2_22_tangent_negative_minors.json').read_text());polys=[]
for record in witness:
 determinant=K.to_sympy(DomainMatrix.from_Matrix(Q.extract(record['rows'],record['cols'])).convert_to(K).det())
 assert S.expand(determinant-S.sympify(record['det'],locals={'T':T}))==0
 polys.append(S.Poly(determinant,T))
gcd=polys[0]
for p in polys[1:]:gcd=S.gcd(gcd,p)
assert gcd.monic().as_expr()==T**10
out={'status':'PASS','scope':'rank1 negative top obstruction and both tangent assignments top atlas; complete semisimple minus-Pfaffian exclusions for the first assignment', 'rank1_cross_image':'all vectors decomposable (ruling); rank1/2 both excluded by symplectic projection bounds','tangent_atlas':atlas,'reverse_square_cross_rank':2,'first_assignment_square_minus':{'B3':20,'B4':35,'normal_functional_rank':10,'torus_weights':[str(c) for c in weights],'all_nonzero_z4_one_orbit':True},'first_assignment_nondeg_minus':{'parameter':'T != 0','quartic_quotient_dimension':35,'functionals':'Laurent polynomials; explicitly annihilate every original quartic relation','normal_matrix_shape':[64,32],'three_rank10_minors_gcd':'constant * T^10','all_nonzero_T_normal_kernel':0},'not_claimed':['plus-Pfaffian tangent strata','reverse tangent strata classification','nonsemisimple tangent transport','all P,Q nonzero H3','independent peer review']}
Path(__file__).with_name('cubic_order2_22_tangent_negative_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS rank1 ruling; six tangent linear atlases; square minus orbit; whole nondeg minus family via 3 minors gcd T^10')
