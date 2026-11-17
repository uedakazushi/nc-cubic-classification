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
result = {'status': 'PASS',
          'scope': 'exhaustive exponent enumeration only; domain and skew reduction are ordinary proofs',
          'quadratic_exponents': quad, 'cubic_resonance_exponents': cubic,
          'nontrivial_quadratic_collisions_for_distinct_eigenvalues': collisions,
          'counts': counts}
Path(__file__).with_name('cubic_spectral_resonance_certificate.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps({'status': 'PASS', 'counts': counts}))
