#!/usr/bin/env python3
"""Exhaust the quadratic collisions of four distinct eigenvalues.
The skew and domain arguments are ordinary proofs, not numerical claims.
"""
import itertools
import json
from pathlib import Path

quad = [a for a in itertools.product(range(3), repeat=4) if sum(a) == 2]
cubic = [a for a in itertools.product(range(4), repeat=4) if sum(a) == 3]
collisions = []
for a, b in itertools.combinations(quad, 2):
    # A common index cancels and forces equality of two eigenvalues.
    if any(min(x, y) for x, y in zip(a, b)):
        continue
    kind = ('opposite' if max(a) == max(b) == 2 else
            'square_pair' if max(a) == 2 or max(b) == 2 else
            'disjoint_pairs')
    collisions.append({'left': a, 'right': b, 'type': kind})
counts = {t: sum(x['type'] == t for x in collisions)
          for t in ['opposite', 'square_pair', 'disjoint_pairs']}
assert len(quad) == 10 and len(cubic) == 20 and len(collisions) == 21
assert counts == {'opposite': 6, 'square_pair': 12, 'disjoint_pairs': 3}
# Substitute all ten three-eigenvalue cubic weights into the four charts.
cubic3 = [v for v in itertools.product(range(4),repeat=3) if sum(v)==3]
charts = {
    'A': ([(1,0),(1,0),(0,1)],[1,-1,1]),
    'B': ([(1,0),(0,1),(0,1)],[1,1,-1]),
    'C': ([(1,0),(1,1),(1,-1)],[1,1,1]),
    'D': ([(1,0),(1,1),(1,2)],[1,1,1])}
chart_results = {}
for name,(exponents,signs) in charts.items():
    weights = set()
    for v in cubic3:
        e = tuple(sum(v[i]*exponents[i][j] for i in range(3)) for j in range(2))
        sign = 1
        for i in range(3): sign *= signs[i]**v[i]
        weights.add((e,sign))
    assert len(weights)==7
    chart_results[name] = sorted(weights)
assert set(chart_results['A']) == {((d,3-d),s) for d in range(1,4) for s in [-1,1]} | {((0,3),1)}
assert set(chart_results['B']) == {((d,3-d),s) for d in range(3) for s in [-1,1]} | {((3,0),1)}
assert set(chart_results['C']) == {((3,k),1) for k in range(-3,4)}
assert set(chart_results['D']) == {((3,k),1) for k in range(7)}
for name,exponent,index in [('C',3,1),('C',-3,2),('D',6,2)]:
    E,_ = charts[name]
    support = [v for v in cubic3 if sum(v[i]*E[i][1] for i in range(3))==exponent]
    pure = tuple(3 if j==index else 0 for j in range(3))
    assert support==[pure]
quartic3 = [v for v in itertools.product(range(5),repeat=3) if sum(v)==4]
quartic_results = {}
for name,(E,signs) in charts.items():
    weights = set()
    for v in quartic3:
        e = tuple(sum(v[i]*E[i][j] for i in range(3)) for j in range(2))
        sign = 1
        for i in range(3): sign *= signs[i]**v[i]
        weights.add((e,sign))
    assert len(weights)==9
    quartic_results[name] = sorted(weights)
A_determinants = sorted({4*i-3*r for i in range(4) for r in range(5)
                         if not (i==0 and r==0) and not (i==3 and r==4)})
assert 0 not in A_determinants and max(2*abs(d) for d in A_determinants)==24
zero = {}
for name,K,L in [('C',range(-3,4),range(-4,5)),('D',range(7),range(9))]:
    pairs = [(k,l) for k in K for l in L]
    zero[name] = [(k,l) for k,l in pairs if 3*l==4*k]
    assert max(abs(3*l-4*k) for k,l in pairs)==24
assert zero['C']==[(-3,-4),(0,0),(3,4)]
assert zero['D']==[(0,0),(3,4),(6,8)]
for name,exponent,index in [('C',-4,2),('C',4,1),('D',0,0),('D',8,2)]:
    E,_ = charts[name]
    support = [v for v in quartic3 if sum(v[i]*E[i][1] for i in range(3))==exponent]
    assert support==[tuple(4 if j==index else 0 for j in range(3))]
result = {'status': 'PASS',
          'scope': 'exhaustive exponent and spectral chart enumeration only; ordinary proofs separate',
          'quadratic_exponents': quad, 'cubic_resonance_exponents': cubic,
          'nontrivial_quadratic_collisions_for_distinct_eigenvalues': collisions,
          'counts': counts, 'three_eigenvalue_chart_cubic_weights':chart_results,
          'isolated_pure_branch_checks':['C:k=3','C:k=-3','D:k=6'],
          'three_eigenvalue_chart_quartic_weights':quartic_results,
          'opposite_pair_chart_nonzero_determinants':A_determinants,
          'cubic_quartic_zero_determinants':zero,
          'common_torsion_order_bound':24,
          'zero_determinant_residual_spectra':['(1,z,z^-1)','(z,1,z^-1)']}
Path(__file__).with_name('cubic_spectral_resonance_certificate.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'counts': counts,'chart_cubic_weight_counts':{k:len(v) for k,v in chart_results.items()},'torsion_bound':24}))
