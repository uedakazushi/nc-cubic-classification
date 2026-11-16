"""Exact reduction of resonance exceptions to rho^2=-1,-3; structural one-zero boundary exclusion."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import relations,coordinates,normal_free
r,s,t,q,z=S.symbols('r s t q z');alpha=(r-1)/(r+1);h=S.Matrix([[0,r],[r,0]])
# The q-term has strictly smaller auxiliary weight, in each fixed total degree.
Rq=relations(h,[0,-t,alpha*s,s,t,q]);R0=relations(h,[0,-t,alpha*s,s,t,0]);weights=[1,-1,0,0]
for rel,target in zip(Rq,R0):
 degree=max(sum(weights[i] for i in word) for word,c in rel.items() if c)
 top={word:c for word,c in rel.items() if sum(weights[i] for i in word)==degree}
 assert top==target
Tseries=1/((1-z)**2*(1-z*z));assert S.cancel(Tseries*(1+z)/(1-z)-1/(1-z)**4)==0
D=(r+1)**2*(r*r+3)+4*s*s;tt=(1-r*r)/2
assert S.cancel(1-r*r-tt*tt-alpha*s*s+alpha*D/4)==0
# Three normal8minors complement the first minor, without adding new pole curves.
K=S.QQ.frac_field(r,s);N,L,_,nf=coordinates(relations(h,[1-r*r-tt*tt-alpha*s*s,-tt,alpha*s,s,tt,1]),K)
records=json.loads(Path(__file__).with_name('cubic_order2_22_secant_resonance_cover_input.json').read_text());used=set()
for rec in records:
 P=N.extract(rec['rows'],rec['cols'])
 for i in range(8):
  den=S.lcm([S.denom(x) for x in P[i,:]])
  for j in range(8):P[i,j]=S.cancel(P[i,j]*den)
 determinant=DomainMatrix.from_Matrix(P).convert_to(S.QQ.poly_ring(r,s)).det().as_expr()
 assert S.expand(determinant-S.sympify(rec['determinant'],locals={'r':r,'s':s}))==0
 used.update(i%35 for i in rec['rows'])
allowed=S.Poly(r*(r*r-1)*(r*r+1)*(r*r+3)*D,r,s)
for row in nf.values():
 for j,x in row.items():
  if j in used:
   for pol,m in S.factor_list(S.denom(K.to_sympy(x)),r,s)[1]:assert allowed.rem(S.Poly(pol,r,s)).is_zero
E=(r+1)**4*(r*r+1)+4*r*(r+3)*s*s
F=(r+1)**2*(r*r+2*r+3)+6*s*s
J=(r+1)**2*(r*r+1)**2+4*r*r*s*s
assert list(S.groebner([E,F,J],s,r))==[s*s,r*r+2*r+1]
assert S.factor(E.subs(s,0))==(r+1)**4*(r*r+1)
assert S.gcd(S.Poly(F.subs(r,-3),s),S.Poly(J.subs(r,-3),s)).degree()==0
# Only leftover point of the three-minor cover, away from the allowed poles.
# a=1-r^2-t^2=-24 at r=-3,t=-4 (keep this explicit).
NN,_,dim=normal_free(relations(S.Matrix([[0,-3],[-3,0]]),[-24,4,0,0,-4,1]),S.QQ)
assert dim==35 and DomainMatrix.from_Matrix(NN).convert_to(S.QQ).rank()==8
out={'status':'PASS','one_zero_boundary':'auxiliary leading relations for a=0,q arbitrary equal the complete doublezero GWA. Ore base T=k[u,z][v;sigma,delta] with vu=-uv+z has Hilbert 1/((1-h)^2*(1-h2)); GWA PBW gives 1/(1-h)^4. For AS4 candidate the filtered map is an isomorphism. Off traceF1 normal kernel zero; at resonance dimension<=2 and universal factor pencil covers it. Thus entire a*q=0 sector excluded.','resonance_rank_cover':'three additional exact normal8minors; after allowed units their factors are (r+3)*E, s2*F, s2*J. Common zeros away from poles only(-3,0), whose fresh original relation normal rank is8. E,F,J ideal=(s2,(r+1)2).','conclusion':'entire resonance excluded outside r2=-1,-3, since D=0 is the one-zero boundary; only those two quadratic-field one-parameter curves remain on resonance. Off-resonance main a*q!=0 remains.','proof_inputs_not_computer_proofs':['Ore extension and generalized Weyl PBW construction','filtered normal-kernel injection','universal factor pencil from previous proposition'],'not_claimed':['two exceptional curves','off-resonance three-parameter main chart','global classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_resonance_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete one-zero boundary and resonance cover reduced to rho2=-1,-3')
