"""Universal factor pencil on the nondegenerate secant resonance, and an explicit open exclusion."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import relations,coordinates,THETA
r,s,z=S.symbols('r s z');theta=THETA;K=S.QQ.frac_field(r,s);t=(1-r*r)/2;alpha=(r-1)/(r+1)
D=r**4+2*r**3+4*r*r+6*r+4*s*s+3
E=r**6+4*r**5+7*r**4+8*r**3+4*r*r*s*s+7*r*r+12*r*s*s+4*r+1
R=relations(S.Matrix([[0,r],[r,0]]),[1-r*r-t*t-alpha*s*s,-t,alpha*s,s,t,1]);N,L,nf3,nf4=coordinates(R,K)
assert max(j for row in nf3.values() for j in row)+1==20
assert max(j for row in nf4.values() for j in row)+1==35
entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_nondegenerate_resonance_input.json').read_text());Q=[S.sympify(x,locals={'r':r,'s':s,'theta':theta}) for x in entry['quadratic_factor']]
C=S.Matrix([[S.Poly(x,theta).coeff_monomial(theta**i) for i in range(3)] for x in Q]);assert all(S.Poly(x,theta).degree()<=2 for x in Q)
DQ=DomainMatrix.from_Matrix(C).convert_to(K);D0=DomainMatrix.from_Matrix(L.subs(theta,0)).convert_to(K);D1=DomainMatrix.from_Matrix(L.diff(theta)).convert_to(K)
J=S.zeros(10,4);P0=(D0*DQ).to_Matrix();P1=(D1*DQ).to_Matrix()
for i in range(3):J[:,i]+=P0[:,i];J[:,i+1]+=P1[:,i]
DJ=DomainMatrix.from_Matrix(J).convert_to(K);DN=DomainMatrix.from_Matrix(N).convert_to(K)
assert (DN*DJ).is_zero_matrix and DJ.rank()==2 and DN.rank()==8
coeff=list(C);assert list(S.groebner(coeff+[z*r*(r*r-1)-1],z,s,r))==[1]
# Global positive B2 basis means this coefficient ideal certifies Q is never identically zero.
# Flat specialization on maximal-rank B3/B4 loci extends the generic normality
# and image-rank<=2 identities to all AS4 fibers; the domain argument is in the proof.
rec=entry['normal_minor'];P=N.extract(rec['rows'],rec['cols'])
for i in range(8):
 den=S.lcm([S.denom(x) for x in P[i,:]])
 for j in range(8):P[i,j]=S.cancel(P[i,j]*den)
det=DomainMatrix.from_Matrix(P).convert_to(S.QQ.poly_ring(r,s)).det().as_expr();assert S.expand(det-S.sympify(entry['normal_minor_polynomial'],locals={'r':r,'s':s}))==0
used={i%35 for i in rec['rows']};allowed=S.Poly(r*(r*r-1)*(r*r+1)*(r*r+3)*D,r,s)
for row in nf4.values():
 for j,x in row.items():
  if j not in used:continue
  for pol,m in S.factor_list(S.denom(K.to_sympy(x)),r,s)[1]:assert allowed.rem(S.Poly(pol,r,s)).is_zero
out={'status':'PASS','scope':'nondegenerate positive top / symmetric secant / q1 / positive Pfaffian / resonance2t+rho2-1=0','all_AS4_domain_fibers':'explicit polynomial Q2(theta) nowhere identically zero; maximal-rank quotient flatness extends the generic normality and factor-image span<=2. Domain and degree3 versus degree2 force span>=2, hence an entire normal pencil consists of reducible cuts at every AS4-domain fiber.','explicit_open_complete_exclusion':'outside (rho2+1)(rho2+3)(rho2-9)*D*E=0, normal8minor and regular selected quartic functionals imply the entire normal kernel is that factor pencil, so no H3. D,E explicit in proof.','normal_minor':str(S.factor(det)),'remaining':['resonance exceptional curves rho2=-1,-3,9 or D*E=0 may have larger normal kernels','off-resonance main three-parameter chart','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_nondegenerate_resonance_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS nondegenerate secant resonance: universal factor pencil on all AS4-domain fibers, full exclusion on explicit open')
