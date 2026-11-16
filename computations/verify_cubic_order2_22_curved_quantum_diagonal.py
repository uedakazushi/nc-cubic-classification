"""Full (p,r) curved quantum diagonal chart: exact support ideals and nine norm cases."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
p,r,a,b,z=S.symbols('p r a b z');rules={(1,0):{(0,1):1/p,(2,2):-a/p,(3,3):-b/p},(3,2):{(2,3):-S.Integer(1)},(2,0):{(0,2):r},(2,1):{(1,2):1/r},(3,0):{(0,3):p/r},(3,1):{(1,3):r/p}}
@lru_cache(None)
def nf(word):
 for pos in range(len(word)-1):
  if word[pos:pos+2] in rules:
   out={}
   for mid,c in rules[word[pos:pos+2]].items():
    for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+c*d
   return {w:S.cancel(c) for w,c in out.items() if S.cancel(c)}
 return {word:S.Integer(1)}
overlaps=0
for word in itertools.product(range(4),repeat=3):
 if word[:2] not in rules or word[1:] not in rules:continue
 out={}
 for pos,sign in [(0,1),(1,-1)]:
  for mid,c in rules[word[pos:pos+2]].items():
   for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+sign*c*d
 assert all(S.cancel(c)==0 for c in out.values());overlaps+=1
assert overlaps==4
words=[w for w in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in w)%2==0]
for word in words:
 n=word.count(0)-word.count(1)
 wu=(-1)**word.count(3)*r**n;wv=(-1)**word.count(2)*(p/r)**n
 eq=[S.fraction(S.cancel(wu+1))[0],S.fraction(S.cancel(wv+1))[0],1-z*p*r]
 if abs(n)==3:target=[p**3-1,r**3+1,1-z*p*r]
 elif word.count(2)==word.count(3)==1:target=[p-1,r-1,1-z*p*r]
 else:target=[p-1,r+1,1-z*p*r]
 assert list(S.groebner(eq,p,r,z))==list(S.groebner(target,p,r,z))
# The complete 3x3 roots are contained in Q(lambda), lambda primitive6.
lv=(1+S.sqrt(-3))/2;F=S.QQ.algebraic_field(lv);l=F.from_sympy(lv);records=[]
for pp,rr in itertools.product([F.one,l*l,l**4],[-F.one,l,F.one-l]):
 q0=pp*rr*rr;c=-pp/(rr*rr)
 K=F.frac_field('alpha','beta','C','V','rho');aa,bb,C,V,rho=K.gens
 active_a=q0!=F.one;active_b=rr*rr!=F.one
 A=aa if active_a else K.zero;B=bb if active_b else K.zero
 dl=K(rr)*A/K(q0-F.one) if active_a else K.zero
 den=F.one/(c*c)-q0
 assert (den!=F.zero)==active_b
 gm=K(rr)*B/K(den) if active_b else K.zero
 aval=C-dl-gm*V*V;ring=K.field.ring
 def sigma(x,n=1):
  def tr(poly):return ring.from_dict({m:v*q0**(n*m[2])*c**(-n*m[3]) for m,v in poly.items()})
  return K(tr(x.numer))/K(tr(x.denom))
 P=aval*sigma(aval)*sigma(aval,2)
 assert P and not (sigma(aval,3)-aval) and not (sigma(P)-P)
 assert not (aval*sigma(aval,2)*sigma(aval,4)-P)
 assert not (dl*(K(q0)-1)-K(rr)*A)
 assert not (gm*(K(F.one/(c*c))-K(q0))-K(rr)*B)
 # Exact cubic commutator coefficients: excluded curvature directions are forced0.
 sub={p:F.to_sympy(pp),r:F.to_sympy(rr)}
 comm={}
 for word,sgn in [((1,0,0,0),1),((0,0,0,1),-1)]:
  for w,d in nf(word).items():comm[w]=comm.get(w,0)+sgn*d
 for word,co in comm.items():
  co=S.cancel(co.subs(sub));pa=S.Poly(co,a,b)
  assert all(F.from_sympy(v)==F.zero for m,v in pa.terms() if (m[0] and active_a) or (m[1] and active_b) or not any(m))
 if not active_a:
  coefficient=F.from_sympy(S.diff(S.cancel(comm.get((0,0,2,2),0).subs(sub)),a));assert coefficient
 if not active_b:
  coefficient=F.from_sympy(S.diff(S.cancel(comm.get((0,0,3,3),0).subs(sub)),b));assert coefficient
 # In the monic6 quotient with X^6=rho^3*P, Z^3=1 by sigma^2-norm.
 coefficient=(1/(rho*aval))*sigma(1/(rho*aval),2)*sigma(1/(rho*aval),4)*(rho**3*P)
 assert not (coefficient-K.one)
 records.append({'p':str(F.to_sympy(pp)),'r':str(F.to_sympy(rr)),'alpha_forced_zero':not active_a,'beta_forced_zero':not active_b,'cubic_norm_obstruction':'Z^3=1 in monic6 basis'})
out={'status':'PASS','scope':'all p,r nonzero, all alpha,beta in the curved diagonal quantum chart',
 'universal_PBW_overlaps':4,'localized_support_ideal_equalities':10,'complete_root_cases':records,
 'conclusion':'all possible non-sign cuts either factor immediately or acquire explicit cubic norm zero divisors; the only H3 part is the known fixed sign family at p=1,r=-1,alpha=beta=0',
 'proof':'papers/sections/cubic_order2_22_curved_quantum_diagonal.tex',
 'not_claimed':['all nonzero-top rank4 graphs','non-diagonal normalizing matrices','relative descent']}
Path(__file__).with_name('cubic_order2_22_curved_quantum_diagonal_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS curved quantum diagonal chart: 4 PBW overlaps, 10 support ideals and all nine cubic-norm cases')
