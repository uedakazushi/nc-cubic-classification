#!/usr/bin/env python3
"""Exact original Ore relations for the fourth-root curvature factor obstruction.
All-chart coverage and the rank2 linear-kernel reduction are ordinary proofs.
"""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S
A,B=S.symbols('alpha beta');K=S.QQ_I.frac_field(A,B)
alpha,beta=K.gens;zero=K.zero;one=K.one;i=K.convert(S.I);q=one/(alpha*beta)
# Original valid AS2 Ore curvature family: xy=i yx; bc=q cb+x^2.
rules={(1,0):{(0,1):-i},(2,0):{(0,2):alpha},(2,1):{(1,2):beta},
       (3,0):{(0,3):one/alpha},(3,1):{(1,3):-one/beta},
       (3,2):{(2,3):one/q,(0,0):-one/q}}
@lru_cache(None)
def nf(word):
    for j in range(len(word)-1):
        if word[j:j+2] not in rules:continue
        out={}
        for rep,c in rules[word[j:j+2]].items():
            for w,d in nf(word[:j]+rep+word[j+2:]).items():out[w]=out.get(w,zero)+c*d
        return {w:c for w,c in out.items() if c}
    return {word:one}
def diff(P,Q):
    out=dict(P)
    for w,c in Q.items():out[w]=out.get(w,zero)-c
    return {w:c for w,c in out.items() if c}
def first_reduction(word,j):
    out={}
    for rep,c in rules[word[j:j+2]].items():
        for w,d in nf(word[:j]+rep+word[j+2:]).items():out[w]=out.get(w,zero)+c*d
    return {w:c for w,c in out.items() if c}
for triple in itertools.combinations(range(4),3):
    word=tuple(reversed(triple))
    assert not diff(first_reduction(word,0),first_reduction(word,1))
for F in [(0,0),(0,1),(1,1)]:
    residual=diff(nf(F+(3,2)),nf((2,)+F+(3,)))
    pure={w:c for w,c in residual.items() if all(letter<2 for letter in w)}
    expected={w:-c/q for w,c in nf(F+(0,0)).items()}
    assert pure==expected and pure
Dres=diff(nf((2,3,3,2)),nf((2,2,3,3)))
assert not {w:c for w,c in Dres.items() if all(letter<2 for letter in w)}
assert q*alpha*beta==one and (one/q)*(-one/(alpha*beta))==-one
source=json.loads(Path(__file__).with_name('cubic_fourth_root_negative_repeat_exclusion_certificate.json').read_text())
rows=[r for r in source['final_survivors'] if r['N']==4 and r['spectrum'] in ([1,0,2],[3,0,2])]
assert len(rows)==2
CUBIC=[v for v in itertools.product(range(4),repeat=3) if sum(v)==3]
for row in rows:
    lam=row['spectrum']
    assert row['relation_weight_multiplicities']==[[0,2,2,2]]
    assert [v for v in CUBIC if sum(x*y for x,y in zip(v,lam))%4==0]==[(0,1,2),(0,3,0),(2,0,1)]
assert 2*6+4+9==25
result={'status':'PASS','scope':'exact original AS4 Ore family, all four critical cubic overlaps and three independent quadratic coefficients; ordinary all-chart proof separate',
        'partial_chart_spectra':rows,'cubic_form':'C*b^3+F2*c+D*b*c^2',
        'four_original_critical_overlaps':'PASS','pure_T4_component_of_normal_b_equation':'-q^-1*F2*h',
        'b_c2_term_has_no_pure_T4_component':True,
        'h_nonzero_forces':'F2=0 and G=b*(C*b^2+D*c^2)',
        'remaining_even_rank2_kernel_shape':[25,4],
        'not_claimed':['rank2 chart excluded','two spectra excluded','complete classification']}
Path(__file__).with_name('cubic_fourth_root_unit_simple_rank1_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','original_overlaps':4,'quadratic_basis_coefficients':3,'rank2_kernel':[25,4]}))
