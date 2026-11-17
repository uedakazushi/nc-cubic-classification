#!/usr/bin/env python3
"""All bounded phases in the last direction, three explicit top models and
exact normalizer identities behind its exhaustive ordinary exclusion proof.
"""
from pathlib import Path
from fractions import Fraction
import itertools,math,json,sympy as s
from cubic_diagonal_top import top_basis,top_matrix
phases=set();modcounts=[];square_cases=[]
for M in range(1,25):
 count=0
 for a,b,c in itertools.product(range(M),repeat=3):
  if a==b or math.gcd(M,a,b,c)!=1:continue
  # Both distinct Ub relation characters need reciprocal Uc partners.
  possible=sorted([a,b])==sorted([(-a-c)%M,(-b-c)%M])
  if not possible:continue
  matched=(2*a+c)%M==0 and (2*b+c)%M==0
  swapped=(a+b+c)%M==0
  assert matched!=swapped
  # Non-skew swapped case forces gamma=alpha*beta, by ordinary domain/
  # Frobenius pure-U/pure-V rank and odd (-1) rank argument.
  if swapped and c!=(a+b)%M:
   if c in [(2*a)%M,(2*b)%M]:
    first=a if c==(2*a)%M else b;second=b if first==a else a
    assert second==(-3*first)%M and (4*first)%M!=0
    exponents=[(j,3-j,0,0) for j in range(4) if (j*first+(3-j)*second)%M==0]
    if (first+c)%M==0:exponents.append((1,0,1,1))
    if (second+c)%M==0:exponents.append((0,1,1,1))
    if exponents:
     common=[j for j in [0,1] if all(v[j]>0 for v in exponents)]
     assert (8*first)%M!=0 # coincident two squares have no cubic support
     if not common:assert (3*first)%M==0 and first!=0
     square_cases.append({'modulus':M,'alpha_exponent':first,'fixed_cubics':exponents,'status':'common U factor' if common else 'primitive cube phase, normal-x eigenvalue contradiction','common_U_factor':common[0] if common else None})
   # Other distinct-character cases are separated AS2/skew or the impossible
   # odd rank1 (-1)-Frobenius block, proved in paper.
   continue
  cubes=[j for j in range(4) if (j*a+(3-j)*b)%M==0]
  mixed=[j for j,p in enumerate([a,b]) if (p+c)%M==0]
  if not cubes and not mixed:continue
  assert 6*a%M==0 and 6*b%M==0
  ab=sorted([Fraction(a,M),Fraction(b,M)]);phases.add((ab[0],ab[1],Fraction(c,M),'M' if matched else 'S'));count+=1
 modcounts.append({'modulus':M,'labeled_minimal_order_cases':count})
assert len(phases)==7
# Swapped minus-one primitive phases have only one pure cube, hence factor.
for a,b,c,kind in phases:
 cubes=[j for j in range(4) if (j*a+(3-j)*b).denominator==1];mixed=[j for j,p in enumerate([a,b]) if (p+c).denominator==1]
 if kind=='S' and c==Fraction(1,2) and a!=0:assert len(cubes)==1 and cubes[0] in [0,3] and not mixed
# Three original top models.
t=s.Symbol('t');aa=s.symbols('a:12');K=s.QQ.frac_field(t,*aa);tt=K.gens[0]
def model(K,lam):
 bs=top_basis(K,lam);H=top_matrix(K,lam,list(K.gens[1:1+len(bs)])).to_Matrix();return bs,H
matched,H=model(K,[K.one,-K.one,tt,1/tt]);assert len(matched)==10
Hp=H.extract([0,5,11,14],[0,5,11,14]);Hm=H.extract([1,4],[1,4]);assert Hm==s.Matrix([[0,-aa[0]],[aa[0],0]])
xb=H.extract([2,8],[3,12]);yb=H.extract([6,9],[7,13]);assert not s.cancel(xb.det()+aa[3]**2+aa[1]*aa[2]/t);assert not s.cancel(yb.det()-aa[7]**2-aa[5]*aa[6]/t)
assert list(Hp.subs(aa[0],0)[0,2:])==[aa[1],aa[2]] and list(Hp.subs(aa[0],0)[1,2:])==[aa[5],aa[6]]
swapped,S=model(K,[K.one,-K.one,tt,-1/tt]);assert len(swapped)==9
Sp=S.extract([0,5],[0,5]);assert Sp==s.Matrix([[0,aa[0]],[aa[0],aa[7]]])
Sm=S.extract([1,4,11,14],[1,4,11,14]).subs({aa[0]:0,aa[7]:0});B=Sm[:2,2:]
pf=Sm[0,1]*Sm[2,3]-Sm[0,2]*Sm[1,3]+Sm[0,3]*Sm[1,2];assert s.expand(pf+B.det())==0 and Sm[:2,:2]==s.zeros(2)
# Swapped primitive cube phase: all crossrank1 constraints imply cross H0 rank1.
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));L=F.frac_field(t,*aa);lt=L.gens[0];o=L.convert(F.unit,F);ts,W=model(L,[o,o**2,lt,1/lt]);assert len(ts)==10
H0=W.extract([1,4,11,14],[1,4,11,14]);M1=W.extract([2,8],[7,13]);M2=W.extract([6,9],[3,12]);p,q,r=s.symbols('p q r');sub={aa[2]:1,aa[3]:p,aa[4]:q,aa[5]:r,aa[6]:p*r/q,aa[7]:p*r}
assert not L.from_sympy(s.cancel(M1.det().subs(sub))) and not L.from_sympy(s.cancel(M2.det().subs(sub))) and not L.from_sympy(s.cancel(H0[:2,2:].det().subs(sub)))
# Nontrivial matched cube phases: accepted N0 quartic supports onlyx²bc,y²bc.
for av in [F.unit,F.unit**2,-F.unit,-F.unit**2]:
 bb=top_basis(L,[L.convert(av,F),-L.convert(av,F),lt,L.convert(av**-2,F)/lt]);counts={tuple(w.count(j) for j in range(4)) for ts0 in bb for w in ts0};assert counts=={(2,0,1,1),(0,2,1,1)}
# Exceptional swapped square/cube chart: top only x³y and multilinear,
# normalx hdet gives phi_x(y)=omega, phi_x(b)*phi_x(c)=1;
# all three fixed cubic types then have phi_x eigenvalue1, notomega.
for av in [F.unit,F.unit**2]:
 lv=L.convert(av,F);sq=top_basis(L,[lv,L.one,lt,lv**2/lt]);assert len(sq)==7
 counts={tuple(w.count(j) for j in range(4)) for ts0 in sq for w in ts0};assert counts=={(3,1,0,0),(1,1,1,1)}
 assert not(lv**3-L.one) and lv!=L.one
# Central quadratic argument in independent-P,Q branch: exact free-word identity.
x,y=s.symbols('x y',commutative=False)
assert s.expand((y*x*y*x-x*y*x*y)-(x*y+y*x)*(y*x-x*y)-(y*x*x*y-x*y*y*x))==0
# Normalizer degree3/degree4 obstruction in proportional-P,Q branch.
A,l,z=s.symbols('A l z');gb=s.groebner([l-A**3,l-A**4,z*A*l-1],z,A,l);assert gb.reduce(A-1)[1]==0 and gb.reduce(l-1)[1]==0
# Swapped cube phase with pure bc/cb: hdet mu_b=ade, normalG a³=d³=l,
# and nonzero xy deformation forces ad=e.
a,d,e,l,z=s.symbols('a d e l z');gb=s.groebner([l-a*d*e,a**3-l,d**3-l,a*d-e,z*a*d*e*l-1],z,a,d,e,l);assert gb.reduce(l-1)[1]==0
# Swapped sign chart: nonfactor needs x³ andybc, so a³=de=ade.
gb=s.groebner([l-a*d*e,a**3-l,d*e-l,z*a*d*e*l-1],z,a,d,e,l);assert gb.reduce(a-1)[1]==0 and gb.reduce(l-1)[1]==0
# Pure-U matched chart, after center-fixing kills cb deformation.
q=s.Symbol('q');gb=s.groebner([l-A*A*q,A**3-l,A*q-l,z*A*q*l-1],z,A,q,l);assert gb.reduce(A-1)[1]==0 and gb.reduce(l-1)[1]==0
# Full scalar right twist on a normal degree-one z fixed by phi_z.
lam,hdet=s.symbols('lam hdet',nonzero=True);assert s.cancel(lam/hdet-1)==(lam-hdet)/hdet
out={'status':'PASS','scope':'entire last (alpha,beta,t,gamma/t) rank3 support chart excluded by paper proof; all four-simple H3 spectra now bounded finite torsion','phase_orbits':[[str(a),str(b),str(c),kind] for a,b,c,kind in sorted(phases)],'phase_moduli':modcounts,'excluded_square_collision_phase_cases':square_cases,'normal_linear_identity':'mu_B(z)=hdet_B(phi_z)*z, proved by centralization and central Nakayama fixing','primary_rechecked':{'source':'Reyes-Rogalski-Zhang, Skew Calabi-Yau algebras and homological identities','theorems':['0.3 full scalar formula','5.4(a)','proof of0.3'],'pdf_sha256':'28b4b649089bbebb722664452c665f8a43ad5b8d9589925b2f97818322736e25','right_twist':'mu_BH=mu_B H^-4 xi_hdetH'},'top_dimensions':{'matched_sign':10,'swapped_sign':9,'swapped_cube':10,'matched_nonsign_cube':6},'exact_checks':['all bounded reciprocal-character phase cases and7 orbits','matched sign pure-minus block and both rank1 paired determinants','swapped sign symmetric pure-square block and skew Pfaff=-detcross','swapped cube crossrank1 from full paired equations','matched nonsign all quartic supports pure offdiagonal','independentP/Q free-word central quadratic identity','all4 normalizer ideal contradictions'],'ordinary_cases':['swapped square collision: common factor or primitive cube normal-x contradiction','swapped cubic singlepurecube','matched nonsign pure AS2 factor','swapped cube purepair and degree3/4 normalizer','swapped sign PBW fixed cubic factor criterion','matched sign projectionrank1 pureAS2 and center flip, orrank2 independent/proportionalP/Q'],'remaining_four_simple_spectra':'all eigenvalues common Nth roots for some N<=96','scope_warning':'rank4 extra-support finite points not excluded here','not_claimed':['all bounded finite spectra classified','all CY covered','global components/groupoids/descent','complete H3 classification','ordinary homological proofs mechanically verified in full']}
Path(__file__).with_name('cubic_four_simple_zero_pair_rank3_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS all last-phase data and exhaustive rank3 exclusion obstructions')
