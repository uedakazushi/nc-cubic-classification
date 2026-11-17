#!/usr/bin/env python3
"""Exact parity filter and original binary twisted-cyclic block at fourth roots.
The nonsemisimple determinant argument and H3 exclusions are ordinary proofs.
"""
import itertools
import json
from math import gcd
from pathlib import Path
import sympy as S
source=json.loads(Path(__file__).with_name('cubic_sixth_root_spectrum_reductions_certificate.json').read_text())
filtered=[];odd=[];unit=[]
for row in source['final_survivors']:
    N=row['N'];lam=tuple(row['spectrum']);keep=[]
    for rel in row['relation_weight_multiplicities']:
        if N%2==0 and rel[N//2]%2:
            odd.append({'N':N,'spectrum':lam,'relation_pattern':rel,'minus_one_multiplicity':rel[N//2]})
        else:keep.append(rel)
    assert keep
    if N==4 and lam==(0,1,3):
        assert keep==[[2,2,0,2]]
        C=[v for v in itertools.product(range(4),repeat=3) if sum(v)==3 and sum(x*y for x,y in zip(v,lam))%4==0]
        assert all(v[1]==v[2] for v in C)
        for w,r in enumerate(keep[0]):
            if r:
                charges={(i==1)-(i==2)+(j==1)-(j==2) for i in range(3) for j in range(3) if (lam[i]+lam[j])%4==w}
                assert len(charges)==1
        unit.append({'N':N,'spectrum':lam,'relation_pattern':keep[0],'cubic_support':C})
    else:filtered.append({**row,'relation_weight_multiplicities':keep})
assert len(odd)==4 and len(unit)==1 and len(filtered)==16
assert all(len(row['relation_weight_multiplicities'])==1 for row in filtered)
# Original right cyclic equation: coefficient of dabc is -mu(d)^-1 times abcd.
i=S.I
mu={0:i,1:-i}
word=(0,0,1,1);coeff=S.Integer(1);orbit={}
for _ in range(4):
    orbit[word]=coeff
    coeff=S.simplify(-coeff/mu[word[-1]])
    word=(word[-1],)+word[:-1]
assert word==(0,0,1,1) and coeff==1
middle=S.Matrix([[0,orbit[(0,0,1,1)]],[orbit[(1,1,0,0)],0]])
assert middle==S.Matrix([[0,1],[-1,0]]) and middle.rank()==2
assert -1/mu[0]!=1 and -1/mu[1]!=1  # pure fourth-power coefficients vanish.
pool={(r['N'],*r['spectrum']) for r in filtered};orbits=[]
while pool:
    N,a,b,c=min(pool)
    orbit={(N,u*a%N,*sorted([u*b%N,u*c%N])) for u in range(1,N) if gcd(u,N)==1}
    assert orbit<=pool
    pool-=orbit;orbits.append(sorted(orbit))
assert len(orbits)==9
result={'status':'PASS','scope':'exact finite parity and auxiliary-grading checks, original fourth-root binary cyclic block; ordinary proofs separate',
        'odd_relation_pattern_exclusions':odd,'unit_repeated_fourth_root_exclusion':unit,
        'binary_minus_one_middle_block':[[0,1],[-1,0]],'final_survivors':filtered,
        'final_spectrum_count':16,'final_relation_pattern_count':16,'counts_by_order':{'3':3,'4':11,'6':2},
        'Galois_label_orbits':orbits,'not_claimed':['remaining16 H3 existence','Galois labels are k-linear equivalences','complete classification']}
Path(__file__).with_name('cubic_fourth_root_spectrum_reductions_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','odd_patterns_excluded':4,'unit_fourth_root_excluded':1,'remaining_spectra':16,'Galois_label_orbits':9}))
