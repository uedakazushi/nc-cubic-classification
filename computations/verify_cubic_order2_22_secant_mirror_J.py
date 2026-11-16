"""Entire last mirror curve: exact quartic functionals, all normal-rank exceptions, explicit linear factor."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import relations,quotient,normal_free,QUADRATICS
r=S.symbols('r');E=S.QQ_I;P=E.poly_ring(r);unit=P.from_sympy(r*(r*r-1)*(r*r+1));entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_mirror_J_input.json').read_text());loc={'r':r}
sv=S.I*(r+1)*(r*r+1)/(2*r);tv=(r*r-1)/2;av=-(r*r-1)**2/(4*r*r);alpha=(r-1)/(r+1);assert S.cancel(1-r*r-tv*tv-alpha*sv*sv-av)==0
R=relations(S.Matrix([[0,r],[r,0]]),[av,-tv,alpha*sv,sv,tv,1]);RR=[]
for rel in R:
 den=S.lcm([S.denom(S.cancel(c)) for c in rel.values()]);left=P.from_sympy(den)
 while left.degree()>0:
  g=left.gcd(unit);assert g.degree()>0;left=left.exquo(g)
 RR.append({w:P.from_sympy(S.cancel(c*den)) for w,c in rel.items()})
funcs=[{int(i):P.from_sympy(S.sympify(v,locals=loc)) for i,v in row.items()} for row in entry['functionals'].values()];assert len(funcs)==35
w4=list(itertools.product(range(4),repeat=4));i4={w:i for i,w in enumerate(w4)}
for j,lam in enumerate(funcs):
 for k,index in enumerate(entry['free_quartic_words']):assert bool(lam.get(index,P.zero))==(j==k)
 for rel in RR:
  for pos in range(3):
   for extra in itertools.product(range(4),repeat=2):assert not sum((c*lam.get(i4[extra[:pos]+w+extra[pos:]],P.zero) for w,c in rel.items()),P.zero)
# An exact finite fiber gives the upper semicontinuity bound; the independent
# 35 polynomial functionals give the opposite bound. Thus generic B4dim=35.
R2=[{w:S.cancel(c.subs(r,2) if hasattr(c,'subs') else c) for w,c in rel.items()} for rel in R];_,_,f3,_=quotient(R2,3,E);_,_,f4,_=quotient(R2,4,E);assert len(f3)==20 and len(f4)==35
q=[S.sympify(x,locals=loc) for x in entry['quadratic_factor']];beta=S.sympify(entry['linear_factor_slope'],locals=loc);assert q[0]==1 and S.cancel(beta+2*S.I*r/(r*r-1))==0
G={}
for word,c in zip(QUADRATICS,q):
 for g,b in [(0,1),(1,beta)]:G[(g,)+word]=G.get((g,)+word,0)+b*c
GP={w:P.from_sympy(S.cancel(c*(r*r-1)**3)) for w,c in G.items()}
for lam in funcs:
 for g in range(4):assert not sum((c*(lam.get(i4[w+(g,)],P.zero)+(-1 if g<2 else 1)*lam.get(i4[(g,)+w],P.zero)) for w,c in GP.items()),P.zero)
# Normal rank >=9, uniformly except the quadratic finite remainder.
words=[w for w in itertools.product(range(4),repeat=3) if sum(x>=2 for x in w)%2==0];data={}
for a,lam in enumerate(funcs):
 for g in range(4):
  row={j:lam.get(i4[w+(g,)],P.zero)+(-1 if g<2 else 1)*lam.get(i4[(g,)+w],P.zero) for j,w in enumerate(words)};row={j:c for j,c in row.items() if c}
  if row:data[4*a+g]=row
assert set(map(str,data))==set(entry['normal_row_unit_divisors'])
for i,row in data.items():
 d=P.from_sympy(S.sympify(entry['normal_row_unit_divisors'][str(i)],locals=loc));left=d
 while left.degree()>0:
  g=left.gcd(unit);assert g.degree()>0;left=left.exquo(g)
 assert all(v.rem(d)==0 for v in row.values());data[i]={j:v.exquo(d) for j,v in row.items()}
N=DomainMatrix(data,(140,32),P);common=P.zero
for rec in entry['normal_minors']:
 d=N.extract(rec['rows'],rec['cols']).det();assert d==P.from_sympy(S.sympify(rec['det'],locals=loc));common=common.gcd(d)
left=common;allowed=unit*P.from_sympy(3*r*r+1)
while left.degree()>0:
 g=left.gcd(allowed);assert g.degree()>0;left=left.exquo(g)
# Exact finite point at 3*rho^2+1=0; its number-field embeddings cover both signs.
rv=S.I/S.sqrt(3);s0=(S.sqrt(3)+S.I)/3;t0=-S.Rational(2,3);F=S.QQ.algebraic_field(S.sqrt(3),S.I);a0=S.Rational(4,3);al=S.simplify((rv-1)/(rv+1));RF=relations(S.Matrix([[0,rv],[rv,0]]),[a0,-t0,al*s0,s0,t0,1]);_,_,ff3,_=quotient(RF,3,F);NN,_,dim=normal_free(RF,F);native={}
for i in range(NN.rows):
 row={j:F.from_sympy(S.expand(NN[i,j])) for j in range(NN.cols) if NN[i,j]};row={j:c for j,c in row.items() if c}
 if row:native[i]=row
assert len(ff3)==20 and dim==35 and DomainMatrix(native,NN.shape,F).rank()==9
out={'status':'PASS','scope':'complete Jm=0 mirror curve, rho(rho2-1)(rho2+1)!=0, both signs s=+/-i(rho+1)(rho2+1)/(2rho)','generic_normal_identity':'G=(x-2i*rho/(rho2-1)*y)*Q2, six explicit Q coefficients; Qxx=1. All 35 independent quartic annihilators vanish on every normal commutator. Finite B4dim35 and 35 independent annihilators prove generic B4dim35. Maximal-rank quotient flatness extends normality to every AS4 fiber.','normal_rank_cover':str(P.to_sympy(common)),'finite_remainder':'3rho2+1=0: exact B3dim20/B4dim35/normal rank9 over QQ(sqrt3,i), all embeddings','conclusion':'normal dimension<=1 everywhere; in any AS4 domain G is nonzero and normal, so spans the whole kernel and has an actual linear factor. No H3 on either entire Jm branch. Combined with prior support, entire mirror surface is empty.','remaining':['nonmirror L=0 main surface','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_mirror_J_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete mirror J curve: explicit linear factor, polynomial normal identity, uniform rank9 cover and exact finite conjugates')
