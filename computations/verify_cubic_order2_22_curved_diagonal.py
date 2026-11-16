"""All-parameter diagonal curved chart: PBW, spectral normal kernel and Weyl limits."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
l,a,b=S.symbols('l a b');rules={(1,0):{(0,1):S.Integer(1),(2,2):-a,(3,3):-b},(3,2):{(2,3):-S.Integer(1)},(2,0):{(0,2):l},(2,1):{(1,2):1/l},(3,0):{(0,3):1/l},(3,1):{(1,3):l}}
@lru_cache(None)
def nf(word):
 for pos in range(len(word)-1):
  if word[pos:pos+2] in rules:
   out={}
   for mid,c in rules[word[pos:pos+2]].items():
    for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+c*d
   return {w:S.cancel(c) for w,c in out.items() if S.cancel(c)}
 return {word:S.Integer(1)}
def plus(out,word,c):
 for w,d in nf(word).items():out[w]=out.get(w,0)+c*d
def iszero(out,sub=None,cyclotomic=False):
 for c in out.values():
  c=S.cancel(c.subs(sub)) if sub else S.cancel(c)
  if cyclotomic:c=S.rem(S.fraction(c)[0],l*l-l+1,l)
  if S.expand(c):return False
 return True
overlaps=0
for word in itertools.product(range(4),repeat=3):
 if word[:2] not in rules or word[1:] not in rules:continue
 out={}
 for pos,sign in [(0,1),(1,-1)]:
  for mid,c in rules[word[pos:pos+2]].items():plus(out,word[:pos]+mid+word[pos+2:],sign*c)
 assert iszero(out);overlaps+=1
assert overlaps==4
words=[w for w in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in w)%2==0];assert len(words)==10
weights=[(-1)**w.count(3)*l**(w.count(0)-w.count(1)) for w in words]
primitive=[]
for c in weights:
 n=S.Poly(S.fraction(S.cancel(c+1))[0],l);primitive.append(n.monic().as_expr())
rootpoly=S.Poly(S.lcm(primitive),l).sqf_part().monic().as_expr()
assert S.expand(rootpoly-(l-1)*(l+1)*(l*l-l+1))==0
indices=[i for i,c in enumerate(weights) if S.rem(S.fraction(S.cancel(c+1))[0],l*l-l+1,l)==0]
assert [words[i] for i in indices]==[(0,0,0),(1,1,1)]
for word in [(0,0,0),(1,1,1)]:
 for g,mu in enumerate([1,1,-1,-1]):
  out={};plus(out,word+(g,),1);plus(out,(g,)+word,-mu)
  assert iszero(out,cyclotomic=True)
# At l=+/-1 the even negative coefficient ring commutes with x,y; replay
# the two exact Weyl derivative identities on every positive cubic monomial.
weyl=0
for value in [1,-1]:
 for word in words:
  for gen,derivative,sgn in [(0,1,1),(1,0,-1)]:
   out={};plus(out,(gen,)+word,1);plus(out,word+(gen,),-1)
   n=word.count(derivative)
   if n:
    i=word.index(derivative);der=word[:i]+word[i+1:]
    plus(out,(2,2)+der,-sgn*n*a);plus(out,(3,3)+der,-sgn*n*b)
   assert iszero(out,{l:value});weyl+=1
out={'status':'PASS','scope':'curved diagonal chart [x,y]=a*u^2+b*v^2, uv=-vu, u acts diag(l,l^-1), v inverse',
 'PBW_overlaps':overlaps,'Weyl_derivative_identities':weyl,
 'normalizer_possible_eigenvalues':'l=1,-1 or l^2-l+1=0',
 'primitive_sixth_root_normal_basis':['x^3','y^3'],
 'all_parameter_claim':'at l primitive6 this normal basis is exact for every a,b; at +/-1 nonzero curvature kills the positive cubic centralizer',
 'not_claimed':['H3 admissibility of primitive6 cuts','domain of the cubic quotient','all nonzero-top rank4 coverage']}
Path(__file__).with_name('cubic_order2_22_curved_diagonal_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS curved diagonal chart: 4 universal PBW overlaps, 40 Weyl identities and exact primitive6 normal kernel')
