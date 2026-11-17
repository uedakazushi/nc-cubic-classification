#!/usr/bin/env python3
"""Exact valid AS2--Ore family: all original overlaps and ordered cubic
normalizer coefficients. The all-AS2-type factor proof is ordinary mathematics.
"""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as s
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1));A,H0,H1,H2=s.symbols('a h0 h1 h2');K=F.frac_field(A,H0,H1,H2)
a,h0,h1,h2=K.gens;o=K.convert(F.to_sympy(F.unit));one=K.one;zero=K.zero
rules={(1,0):{(0,1):one},(2,0):{(0,2):a},(2,1):{(1,2):o},
 (3,0):{(0,3):one/a,(2,2):one},(3,1):{(1,3):o**2},
 (3,2):{(2,3):a,(0,0):-a*h0,(0,1):-a*h1,(1,1):-a*h2}}
@lru_cache(None)
def nf(word):
 for j in range(len(word)-1):
  if word[j:j+2] not in rules:continue
  out={}
  for rep,c in rules[word[j:j+2]].items():
   for v,d in nf(word[:j]+rep+word[j+2:]).items():out[v]=out.get(v,zero)+c*d
  return {v:c for v,c in out.items() if c}
 return {word:one}
def first(word,j):
 out={}
 for rep,c in rules[word[j:j+2]].items():
  for v,d in nf(word[:j]+rep+word[j+2:]).items():out[v]=out.get(v,zero)+c*d
 return {v:c for v,c in out.items() if c}
def diff(P,Q,scale=one):
 out=dict(P)
 for w,c in Q.items():out[w]=out.get(w,zero)-scale*c
 return {w:c for w,c in out.items() if c}
for triple in itertools.combinations(range(4),3):
 w=tuple(reversed(triple));assert not diff(first(w,0),first(w,1))
basis=[(0,0,0),(0,0,1),(0,1,1),(1,1,1),(0,2,3),(1,2,3),(2,2,2),(3,3,3)]
for j,w in enumerate(basis):
 residual=diff(nf(w+(3,)),nf((3,)+w),o)
 assert residual.get((3,3,3,3),zero)==((one-o) if j==7 else zero)
for j,w in enumerate(basis[:-1]):
 residual=diff(nf(w+(2,)),nf((2,)+w),o**2)
 assert residual.get((2,2,2,2),zero)==((one-o**2) if j==6 else zero)
for Fword in [(0,),(1,)]:
 word=Fword+(2,3);residual=diff(nf(word+(0,)),nf((0,)+word))
 pure_b3={w:c for w,c in residual.items() if w.count(2)==3 and 3 not in w}
 assert pure_b3=={Fword+(2,2,2):one}
# Exact root action preserves all original relations, hence Nakayama's simple
# c eigenline cannot acquire an additive x,y,b term.
weights=[0,0,1,2]
for word,terms in rules.items():
 assert all(sum(weights[j] for j in v)%3==sum(weights[j] for j in word)%3 for v in terms)
assert (a**-1)*(a*o)==o and (a**-1*o**2)*a==o**2
out={'status':'PASS','scope':'literal valid Ore family over QQ(omega)(a,h0,h1,h2); every original overlap and ordered normalizer coefficient checked; all-chart Ore recognition not claimed',
 'original_critical_overlaps':4,'normal_c_highest_c4_coefficient':'D*(1-omega)',
 'after_D_zero_normal_b_b4_coefficient':'C*(1-omega^2)',
 'after_C_D_zero_Gx_pure_b3_coefficient':'F*b^3',
 'all_h_coefficients_symbolic':True,'cube_root_action_preserves_every_relation':True,
 'not_claimed':['entire rank1 coupling locus is Ore','degenerate mixed projections covered','even-rank2 or two-curvature cases covered','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_curved_Ore_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','valid_Ore_original_overlaps':4,'ordered_cubic_coefficient_checks':3}))
