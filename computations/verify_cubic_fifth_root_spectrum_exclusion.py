#!/usr/bin/env python3
"""Exact fifth-root character data and the final original-relation obstruction.
The Ore coverage and AS2 automorphism cases are ordinary proofs in the paper.
"""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S
K=S.QQ.alg_field_from_poly(S.Poly(sum(S.Symbol('Q')**j for j in range(5))))
eta=K.unit;zero=K.zero;one=K.one
assert eta**5==one and eta!=one
p=eta**3;q=eta**4
assert p**3==eta**4 and q**3==eta**2 and q**2==eta**3 and p**2==eta
assert p**-2+p**-1*q**-2==2*eta**4
assert eta**3!=eta**4 and eta**4!=eta**2
# Variables x,c,b, ordered x<c<b. These are the original three relations.
rules={(1,0):{(0,1):q},(2,0):{(0,2):p,(1,1):one},(2,1):{(1,2):q}}
@lru_cache(None)
def nf(word):
    for j in range(len(word)-1):
        pair=word[j:j+2]
        if pair not in rules:continue
        out={}
        for replacement,coefficient in rules[pair].items():
            for w,c in nf(word[:j]+replacement+word[j+2:]).items():
                out[w]=out.get(w,zero)+coefficient*c
        return {w:c for w,c in out.items() if c}
    return {word:one}
def difference(a,b):
    out=dict(a)
    for w,c in b.items():out[w]=out.get(w,zero)-c
    return {w:c for w,c in out.items() if c}
obstruction=difference(nf((1,0,0,2)),nf((2,1,0,0)))
assert obstruction=={(0,1,1,1):-2*eta}
# Independently reduce both choices at the only cubic overlap b c x.
left={};right={}
for rep,coeff in rules[(2,1)].items():
    for w,c in nf(rep+(0,)).items():left[w]=left.get(w,zero)+coeff*c
for rep,coeff in rules[(1,0)].items():
    for w,c in nf((2,)+rep).items():right[w]=right.get(w,zero)+coeff*c
assert difference(left,right)=={}
C3=[v for v in itertools.product(range(4),repeat=3) if sum(v)==3 and (v[0]+3*v[2])%5==0]
assert C3==[(0,3,0),(2,0,1)]
source=json.loads(Path(__file__).with_name('cubic_three_eigenvalue_finite_spectra_certificate.json').read_text())
rows=[r for r in source['final_survivors'] if r['N']==5]
assert len(rows)==4
for row in rows:
    a,b,c=row['spectrum']
    assert b==0 and c==3*a%5
    for R in row['relation_weight_multiplicities']:
        assert [R[j*a%5] for j in range(5)]==[0,2,1,1,2]
result={'status':'PASS','field':'Q(eta), eta primitive fifth root',
        'scope':'exact spectral/Ore character checks and literal original-relation obstruction; ordinary coverage proof separate',
        'fifth_root_spectra_checked':4,'cubic_resonance_exponents':C3,
        'relation_dimensions_in_eta_powers':[0,2,1,1,2],
        'forced_parameters':{'p':'eta^3','q':'eta^4'},
        'original_relations':['c*x=q*x*c','b*x=p*x*b+c^2','b*c=q*c*b'],
        'only_cubic_overlap':'PASS',
        'nonzero_obstruction':'NF(c*x^2*b-b*c*x^2)=-2*eta*x*c^3',
        'ordinary_scope':['all AS2 base types','all commuting f,g types','nonsemisimple Nakayama allowed'],
        'not_claimed':['orders3,4,6 excluded','complete H3 classification']}
Path(__file__).with_name('cubic_fifth_root_spectrum_exclusion_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','spectra_checked':4,'obstruction':'-2*eta*x*c^3 !=0'}))
