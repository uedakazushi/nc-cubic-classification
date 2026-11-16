"""Whole reverse-tangent plus resonance: normal pencil and surjective linear-factor incidence."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
source=Path(__file__).with_name('verify_cubic_order2_22_tangent_negative.py').read_text()
exec(source[:source.index('R=relations(S.diag(1,0),')])
B,theta=S.symbols('B theta');field=S.QQ.frac_field(B);D=(B-1)*(B+1)*(2*B+1)*(4*B+5)
J=S.Matrix([[0,1],[-1,0]]);H=S.Matrix([[0,1],[1,0]]);b1=S.diag(1,0)
MM=-(S.kronecker_product(J.T,b1)+S.kronecker_product(H.T,H))*flip
qwords=[(0,0),(0,1),(1,0),(1,1),(2,3),(3,3)]
def reverse(z0,z1,z4,z5):
 values=[z0,z1,-z4/2,z4/2,z4,z5];rewrite=(-MM.inv()*A).subs(dict(zip(z,values)))
 R=[{(0,1):S.Integer(1),(1,0):-S.Integer(1),(2,3):S.Integer(1),(3,2):S.Integer(1)},{(0,1):S.Integer(1),(1,0):S.Integer(1),(2,2):S.Integer(1)}]
 uv=[(i,j) for i in range(2) for j in range(2,4)];vu=[(i,j) for i in range(2,4) for j in range(2)]
 for i,word in enumerate(vu):R.append({word:S.Integer(1),**{v:-rewrite[i,j] for j,v in enumerate(uv) if rewrite[i,j]}})
 return R

def coordinates(R,K):
 w3,i3,free3,nf3=quotient(R,3,K);w4,i4,free4,nf4=quotient(R,4,K)
 E=[v for v in free3 if sum(i>=2 for i in w3[v])%2==0];assert len(E)==10
 ind={v:j for j,v in enumerate(E)};N=S.zeros(4*len(free4),10);L=S.zeros(10,6)
 for j,v in enumerate(E):
  for g in range(4):
   for raw,c in [(w3[v]+(g,),1),((g,)+w3[v],-1 if g<2 else 1)]:
    for row,d in nf4[i4[raw]].items():N[g*len(free4)+row,j]+=c*K.to_sympy(d)
 for j,ww in enumerate(qwords):
  for ii,cc in [(0,S.Integer(1)),(1,theta)]:
   for row,d in nf3[i3[(ii,)+ww]].items():L[ind[free3[row]],j]+=cc*K.to_sympy(d)
 return N.applyfunc(S.cancel),L.applyfunc(S.cancel),(w3,i3,free3,nf3,E),nf4
R=reverse(B+S.Rational(5,4),B,S.Integer(1),S.Integer(1));N,L,info,nf4=coordinates(R,field)
# Denominators of ORIGINAL-relation annihilators have no roots outside D.
for nf in [info[3],nf4]:
 for row in nf.values():
  for c in row.values():
   den=S.Poly(S.denom(field.to_sympy(c)),B)
   while den.degree():
    gg=S.gcd(den,S.Poly(D,B));assert gg.degree()>0;den=den.exquo(gg)
# Canonical normal-pencil basis, in lexicographic positive B3 free-word coordinates.
d=B+S.Rational(5,4)
W=S.Matrix([[-1,-d],[-1/d,-1/d],[B+2,d],[1,B+2],[-1,-d],[1,1],[1,d],[-1,-1],[1,0],[0,1]])
assert (N*W).applyfunc(S.cancel)==S.zeros(N.rows,2)
rows=[]
for i in range(N.rows):
 row=[S.cancel(c) for c in N[i,:]];den=S.lcm([S.denom(c) for c in row]);row=[S.cancel(c*den) for c in row]
 if any(row):rows.append(row)
Q=S.Matrix(rows);witness=json.loads(Path(__file__).with_name('cubic_order2_22_reverse_resonant_minors.json').read_text());polys=[]
for rec in witness:
 value=field.to_sympy(DomainMatrix.from_Matrix(Q.extract(rec['rows'],list(range(8)))).convert_to(field).det())
 assert S.expand(value-S.sympify(rec['det'],locals={'B':B}))==0;polys.append(S.Poly(value,B))
gcd=polys[0]
for pp in polys[1:]:gcd=S.gcd(gcd,pp)
assert S.rem(gcd.as_expr(),S.expand(D**2),B)==0
assert gcd.monic()==S.Poly(D**2,B).monic()
entry=json.loads(Path(__file__).with_name('cubic_order2_22_reverse_resonant_factor.json').read_text());qfactor=S.Matrix([S.sympify(c,locals={'B':B,'theta':theta}) for c in entry['coefficients']])
assert all(S.Poly(c,theta).degree()<=2 for c in qfactor)
G=(L*qfactor).applyfunc(S.cancel);coeff=G[-2:,0]
assert (G-W*coeff).applyfunc(S.cancel)==S.zeros(10,1)
assert (N*G).applyfunc(S.cancel)==S.zeros(N.rows,1)
# A single nonconstant specialization proves generic dominance of the projective factor incidence.
C=S.Matrix([[S.Poly(c.subs(B,0),theta).coeff_monomial(theta**i) for i in range(4)] for c in coeff]);assert C.rank()==2
exception=[]
for value in [S.Integer(1),-S.Integer(1),-S.Rational(1,2),-S.Rational(5,4)]:
 NN,LL,_,_=coordinates(reverse(value+S.Rational(5,4),value,S.Integer(1),S.Integer(1)),S.QQ)
 GG=(LL*qfactor.subs(B,value)).applyfunc(S.expand);assert (NN*GG).applyfunc(S.expand)==S.zeros(NN.rows,1)
 CC=S.Matrix([[S.Poly(c,theta).coeff_monomial(theta**i) for i in range(4)] for c in GG])
 assert NN.rank()==8 and CC.rank()==2
 exception.append({'B':str(value),'normal_dimension':2,'factor_image_span':2})
# The remaining z0=z5=0 point: a cubic Chebyshev/period-three norm identity.
NN,LL,info,_=coordinates(reverse(S.Integer(0),-S.Rational(5,4),S.Integer(1),S.Integer(0)),S.QQ)
w3,i3,free3,nf3,E=info;ind={v:j for j,v in enumerate(E)}
def vector(poly):
 out=S.zeros(10,1)
 for word,c in poly.items():
  for row,e in nf3[i3[word]].items():out[ind[free3[row]]]+=c*S.QQ.to_sympy(e)
 return out
# ell^3 - theta*C*ell = x3+theta3*y3, C=-3u2/4-v2.
left={}
for choices in itertools.product([(0,1),(1,theta)],repeat=3):
 word=tuple(v[0] for v in choices);left[word]=S.prod(v[1] for v in choices)
for vv,cc in [(2,S.Rational(3,4)),(3,S.Integer(1))]:
 for ii,dd in [(0,theta),(1,theta**2)]:left[(vv,vv,ii)]=left.get((vv,vv,ii),0)+cc*dd
left[(0,0,0)]-=1;left[(1,1,1)]-=theta**3
assert vector(left).applyfunc(S.expand)==S.zeros(10,1)
x3=vector({(0,0,0):S.Integer(1)});y3=vector({(1,1,1):S.Integer(1)})
assert NN.rank()==8 and (NN*x3)==S.zeros(NN.rows,1) and (NN*y3)==S.zeros(NN.rows,1) and x3.row_join(y3).rank()==2
f0=S.Matrix([[S.Rational(1,2),S.Rational(3,4)],[-1,S.Rational(1,2)]])
assert f0**3==-S.eye(2)
C0=S.Matrix([-S.Rational(3,4),0,0,-1])
assert S.kronecker_product(f0,f0)*C0==C0
# Positive-axis swap with v -> -v swaps z0,z5 and preserves the resonance.
zz0,zz5=S.symbols('zz0 zz5');AA=A.subs(dict(zip(z,[zz0,zz0*zz5-S.Rational(5,4),-S.Rational(1,2),S.Rational(1,2),1,zz5])))
P=S.kronecker_product(S.Matrix([[0,1],[1,0]]),S.diag(1,-1));BB=-P*AA*P.T
assert [S.expand(BB[i,j]) for i,j in itertools.combinations(range(4),2)]==[zz5,zz0*zz5-S.Rational(5,4),-S.Rational(1,2),S.Rational(1,2),1,zz0]
out={'status':'PASS','scope':'entire reverse-tangent plus resonance z4=1, including all z0,z5 torus boundaries','generic_open':'D=(B-1)(B+1)(2B+1)(4B+5) != 0','normal_pencil_rank_cover':'two rank8 minors gcd constant*D^2; explicit independent kernel basis','linear_factor_identity':'(x+theta*y)*Q2(B,theta) lies in the normal pencil; Q2 coefficients supplied as exact input and verified from original relations','dominance':'normal coefficient map nonconstant at B=0, hence generically; proper projective matrix incidence extends factorization throughout D-open','exceptional_values':exception,'remaining_double_zero_boundary':'ell^3-theta*C*ell=x3+theta3*y3, C=-3u2/4-v2; theta3 map surjective','conclusion':'every normal cubic on the full resonance has a nontrivial linear left factor, so no H3','not_claimed':['reverse plus away from resonance','reverse square rank2-cross boundary','other negative rank2 types','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_reverse_resonant_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS reverse tangent resonance: rank8 cover, universal factor incidence, four exceptions and exact double-zero norm identity')
