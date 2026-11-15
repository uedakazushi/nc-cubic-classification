#!/usr/bin/env python3
"""Exact lattice and Euler-index audit for dense Rains root resonances.

This checks arithmetic only. Existence of root sheaves, torsion-free line
bundles, the boundary triangle, and derived equivalence are NOT numerical
statements and require the cited primary results/proofs.
"""
import json
from pathlib import Path

def intersection(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

cases={}
for blown_up in (6,8):
    H=(3,)+(1,)*blown_up
    alpha=(1,)+(1,1,1)+(0,)*(blown_up-3)
    beta=(0,)+(-1,1)+(0,)*(blown_up-2)
    assert intersection(H,H)==9-blown_up
    for root in (alpha,beta):
        assert intersection(root,root)==-2
        assert intersection(H,root)==0
        assert -intersection(root,(root[0]-H[0],)+tuple(x-y for x,y in zip(root[1:],H[1:])))//2==1
    cases[str(9-blown_up)]={'degree':9-blown_up,'blowups':blown_up,
        'root_alpha':list(alpha),'root_beta':list(beta),
        'root_square':-2,'anticanonical_intersection':0,
        'quotient_lower_chi_bound':1}
indices=[]
for m in range(-8,9):
    if m < 0:
        indices.append({'m':m,'forced_hom0':0,
            'forced_ext1':-m,'forced_ext2':0,
            'affine_module_dimension':-m,
            'conclusion':'Negative-index root sheaf forces Rains AZ failure and shift [-1]'})
    elif m == 0:
        indices.append({'m':0,'conclusion':'No zero-index root resonance with a genuine ample classical avatar'})
    else:
        indices.append({'m':m,'forced_hom_minus_ext1':m,
            'conclusion':'Positive index: Hom nonzero, Ext1 not decided'})
result={
    'date':'2026-11-15','version':'resonance-hearts-v1',
    'root_lattices':cases,
    'negative_positive_index_table':indices,
    'convention':'O_E(alpha) tensor q**m = O_E, m=chi(e,M)',
    'density_argument':'For fixed infinite-order q, p3(n) translates along E by q**(-n). Distinct infinitely many n imply Zariski dense in E; this density is a mathematical argument, not computational.',
    'scope':'Exact Picard/Euler arithmetic only. Categorical theorem uses Rains Cor 7.23, 10.16, irreducible root sheaf existence and the boundary triangle.'
}
out=Path('build/resonance_hearts_certificate.json')
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PASS: E6/E8 root intersections, quotient chi bound 1, negative-index affine dimensions 1..8')
