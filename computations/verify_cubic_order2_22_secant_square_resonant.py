"""Entire square-positive secant plus main resonance: all normal cubics have linear factors."""
import json,itertools
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import relations,coordinates,polynomial_rows,THETA
q=S.symbols('q');theta=THETA;K=S.QQ.frac_field(q);t=S.Rational(1,2)
z0,s0,t0,k=S.symbols('z0 s0 t0 k');A=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),[z0,-t0,-s0+q,s0,t0,q]):A[i,j]=v;A[j,i]=-v
H=S.kronecker_product(S.Matrix([[1,k],[0,1]]),S.eye(2));target=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),[z0+k*(q-2*s0)+k*k*q,-t0,-s0+q+k*q,s0-k*q,t0,q]):target[i,j]=v;target[j,i]=-v
assert (H*A*H.T-target).applyfunc(S.expand)==S.zeros(4)
R=relations(S.diag(1,0),[(1-t*t)/q,-t,q,0,t,q]);N,L,nf3,nf4=coordinates(R,K)
for row in nf3.values():
 for c in row.values():assert len(S.Poly(S.denom(K.to_sympy(c)),q).terms())==1
for nf in [nf3,nf4]:
 for row in nf.values():
  for c in row.values():
   den=S.Poly(S.denom(K.to_sympy(c)),q)
   while den.degree():
    g=S.gcd(den,S.Poly(q*(q*q+1),q));assert g.degree()>0;den=den.exquo(g)
entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_square_resonant_input.json').read_text());Q=polynomial_rows(N,q);polys=[]
for rec in entry['normal_minor_positions']:
 value=K.to_sympy(DomainMatrix.from_Matrix(Q.extract(rec['rows'],rec['cols'])).convert_to(K).det());polys.append(S.Poly(value,q))
assert S.gcd(*polys).monic().as_expr()==q**10
qfactor=S.Matrix([S.sympify(c,locals={'q':q,'theta':theta}) for c in entry['quadratic_factor']])
assert all(S.Poly(c,theta).degree()<=2 for c in qfactor)
G=(L*qfactor).applyfunc(S.cancel);assert (N*G).applyfunc(S.cancel)==S.zeros(N.rows,1)
J=S.Matrix([[S.Poly(c,theta).coeff_monomial(theta**i) for i in range(4)] for c in G]);rec=entry['factor_span_minor']
assert S.factor(J.extract(rec['rows'],rec['cols']).det())==256*q**8
exceptions=[]
for value in [S.I,-S.I]:
 NN,LL,_,_=coordinates(relations(S.diag(1,0),[(1-t*t)/value,-t,value,0,t,value]),S.QQ_I)
 GG=(LL*qfactor.subs(q,value)).applyfunc(S.expand)
 assert (NN*GG).applyfunc(S.expand)==S.zeros(NN.rows,1)
 JJ=S.Matrix([[S.Poly(c,theta).coeff_monomial(theta**i) for i in range(4)] for c in GG])
 assert DomainMatrix.from_Matrix(NN).convert_to(S.QQ_I).rank()==8
 assert DomainMatrix.from_Matrix(JJ).convert_to(S.QQ_I).rank()==2
 exceptions.append({'q':str(value),'normal_dimension':2,'factor_image_span':2})
out={'status':'PASS','scope':'symmetric secant, square positive top, positive Pfaffian main z5=q!=0, z3=0, z4=1/2','normal_rank_cover':'two rank8 minors gcd constant*q10; quotient functional poles only q=0 or q2=-1','quadratic_factor_identity':'(x+theta*y)*Q2(q,theta) is normal; six coefficients in exact input, degree<=2 in theta','all_fiber_nonconstant_factor_map':'one coefficient-span 2x2 minor equals 256*q8, so every nonzero q has a nonconstant map into the normal pencil','exceptional_values':exceptions,'geometric_conclusion':'rank8 and image-span2 identify the entire normal pencil; proper projective factor incidence covers it, and domain excludes zero products. Every cut is reducible, no H3 on the entire resonance.','not_claimed':['square plus away from resonance','z5=0 boundary','nondegenerate positive top secant plus','rank2 secant boundary','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_square_resonant_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS full square secant main resonance: rank8 Laurent cover, factor span minor 256*q8 and both Gaussian exceptional points')
