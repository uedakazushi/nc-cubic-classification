"""Complete reverse-tangent plus cover: universal minor, eight curves, exact finite exceptions."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
# Shared exact original-relation quotient construction; remove native algebraic zeros explicitly.
source=Path(__file__).with_name('verify_cubic_order2_22_tangent_negative.py').read_text()
source=source[:source.index('R=relations(S.diag(1,0),')]
source=source.replace('{i:row for i,row in enumerate(rows)}','{i:{j:c for j,c in row.items() if c} for i,row in enumerate(rows) if any(row.values())}')
exec(source)
B,C,theta=S.symbols('B C theta');field=S.QQ.frac_field(B,C)
J=S.Matrix([[0,1],[-1,0]]);H=S.Matrix([[0,1],[1,0]]);b1=S.diag(1,0)
MM=-(S.kronecker_product(J.T,b1)+S.kronecker_product(H.T,H))*flip;qwords=[(0,0),(0,1),(1,0),(1,1),(2,3),(3,3)]
source=Path(__file__).with_name('verify_cubic_order2_22_reverse_resonant.py').read_text()
exec(source[source.index('def reverse('):source.index('R=reverse(B+')])
entry=json.loads(Path(__file__).with_name('cubic_order2_22_reverse_plus_cover_input.json').read_text())
D=C*(B-1)*(B+1)*(2*B+C)*(2*B*C+C*C+1)*(4*B*C+C*C+3)*(4*B*C+C*C+4)
R=reverse(1+B*C+C*C/4,B,C,S.Integer(1));N,L,info,nf4=coordinates(R,field)
for nf in [info[3],nf4]:
 for row in nf.values():
  for coeff in row.values():
   den=S.denom(field.to_sympy(coeff))
   for f,n in S.factor_list(den)[1]:assert S.rem(S.Poly(D,B,C),S.Poly(f,B,C)).is_zero
selected=N[entry['generic_rows'],:];scale=[];poly=[]
for i in range(10):
 dd=S.lcm([S.denom(S.cancel(c)) for c in selected[i,:]]);scale.append(dd);poly.append([S.cancel(c*dd) for c in selected[i,:]])
expected=-(C-1)**2*(C+1)**2/(2*(2*B*C+C*C+1)**2*(4*B*C+C*C+3)*(4*B*C+C*C+4))
ring=S.QQ.poly_ring(B,C)
assert DomainMatrix.from_Matrix(S.Matrix(poly)).convert_to(ring).det()==ring.from_sympy(S.cancel(expected*S.prod(scale)))
print('PASS universal two-parameter rank10 minor',flush=True)
t=S.symbols('t');K=S.QQ.frac_field(t)
finite_rational=[(0,0),(1,-1),(-1,-1),(S.Rational(1,2),-1),(S.Rational(5,4),-1),(1,0),(1,-2),(1,-4),(-1,0),(-1,2),(-1,3),(1,-3)]
def divisible(expr,p):return S.rem(S.Poly(S.fraction(S.cancel(expr))[0],t),p).is_zero
cover=[]
for rec in entry['curves']:
 bb=S.sympify(rec['B'],locals={'t':t});cc=S.sympify(rec['C'],locals={'t':t})
 NN,_,inf,nf=coordinates(reverse(S.cancel(1+bb*cc+cc*cc/4),bb,cc,S.Integer(1)),K)
 den=S.lcm([S.denom(K.to_sympy(c)) for ff in [inf[3],nf] for row in ff.values() for c in row.values()])
 rows=[]
 for i in range(NN.rows):
  row=[S.cancel(c) for c in NN[i,:]];dd=S.lcm([S.denom(c) for c in row]);row=[S.cancel(c*dd) for c in row]
  if any(row):rows.append(row)
 Q=S.Matrix(rows);polys=[]
 for witness in rec['rows']:
  value=K.to_sympy(DomainMatrix.from_Matrix(Q[witness,:]).convert_to(K).det());polys.append(S.Poly(value,t))
 gcd=S.gcd(*polys);assert not gcd.is_zero
 e=S.Poly(den*gcd.as_expr(),t).sqf_part().monic()
 if rec['unit']=='t' and e.eval(0)==0:e=e.exquo(S.Poly(t,t))
 if S.cancel(cc-t)==0 and e.eval(1)==0:e=e.exquo(S.Poly(t-1,t))
 assert e.monic()==S.Poly(S.sympify(rec['finite_exception_polynomial'],locals={'t':t}),t).monic()
 # Every remaining irreducible factor maps to the stated rational point or one of two quadratic Galois orbits.
 for factor,multiplicity in S.factor_list(e.as_expr())[1]:
  p=S.Poly(factor,t)
  rational=any(divisible(bb-b0,p) and divisible(cc-c0,p) for b0,c0 in finite_rational)
  quadratic=(divisible(cc*cc-2,p) and divisible(4*bb+3*cc,p)) or (divisible(cc*cc-3,p) and divisible(2*bb+cc,p))
  assert rational or quadratic
 cover.append({'curve':rec['name'],'functional_denominator':str(S.factor(den)),'two_minor_gcd':str(S.factor(gcd.as_expr())),'finite_exception_polynomial':str(S.factor(e.as_expr()))})
 print('PASS curve',rec['name'],flush=True)
finite=[]
for bb,cc in finite_rational+[(-3*S.sqrt(2)/4,S.sqrt(2)),(-S.sqrt(3)/2,S.sqrt(3))]:
 bb,cc=S.sympify(bb),S.sympify(cc);F=S.QQ.algebraic_field(cc) if cc.is_irrational else S.QQ
 NN,LL,_,_=coordinates(reverse(S.expand(1+bb*cc+cc*cc/4),bb,cc,S.Integer(1)),F)
 rank=DomainMatrix.from_Matrix(NN).convert_to(F).rank()
 if (bb,cc)==(1,-1):
  assert rank==9
  q=S.Matrix([-S.Rational(1,12),S.Rational(1,6),S.Rational(1,6),-S.Rational(1,3),0,-S.Rational(1,3)])
  G=LL.subs(theta,-2)*q;assert G!=S.zeros(10,1) and NN*G==S.zeros(NN.rows,1)
 else:assert rank==10
 finite.append({'B':str(bb),'C':str(cc),'normal_dimension':10-rank,'factor':'(x-2y)*((x-2y)^2+4v2)' if rank==9 else None})
# The missing z0=z5=0 torus boundary has f,g inverse, determinant +1, trace C.
v=S.symbols('v',nonzero=True);loc=S.symbols('loc')
f=S.Matrix([[v/2,1/v-v/4],[-v,v/2]])
assert f.det()==1
polys=[S.fraction(S.cancel(e))[0] for e in f**3+S.eye(2)]
ideal=S.groebner(polys+[1-loc*v],loc,v)
assert all(ideal.reduce(p)[1]==0 for p in [v-1,loc-1])
out={'status':'PASS','scope':'entire reverse-tangent nondegenerate positive-top plus-Pfaffian stratum, combined with the previously certified z4=1 factor incidence','generic_normal_minor':str(expected),'generic_functional_pole_divisor':str(D),'complete_exception_curve_cover':cover,'finite_checks':finite,'quadratic_conjugates':'the two quadratic-field checks cover both Galois conjugates','missing_double_zero_boundary':'opposite normalizers with det+1; odd centralizer eliminates auxiliary degrees +/-1; degrees +/-3 require f3=-I, which exact localized ideal forces C=1, already excluded by norm factorization','conclusion':'no H3 anywhere in reverse-tangent nondegenerate positive-top plus branch','not_claimed':['reverse square rank2-cross boundary','other negative rank2 types','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_reverse_plus_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS full reverse tangent plus: universal minor, eight complete curves, all finite fields and isolated linear factor, double-zero boundary')
