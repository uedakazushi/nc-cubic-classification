#!/usr/bin/env python3
"""Exact finite cubic-support and shear checks used in the Ore exclusion.
The ordinary normalizer and noetherian-domain proofs remain in the paper.
"""
import itertools
import json
from collections import defaultdict
from math import gcd
from pathlib import Path
import sympy as S

points = [(3-m-n,m,n) for m in range(4) for n in range(4-m)]
lines = defaultdict(list)
for k,m,n in points:
    u,v = m-1,n-1
    if not (u or v):
        continue
    d = gcd(u,v)
    u,v = u//d,v//d
    if u < 0 or (u == 0 and v < 0):
        u,v = -u,-v
    lines[u,v].append((k,m,n))
certificate = []
for direction, group in sorted(lines.items()):
    group = sorted(group+[(1,1,1)])
    common = [min(p[j] for p in group) for j in range(3)]
    assert any(common)
    certificate.append({'direction':direction,'points':group,'common_factor_exponents':common})
assert len(lines) == 6 and len(points) == 10
x,y = S.symbols('x y')
ranks = []
for degree in range(4):
    basis = [x**(degree-j)*y**j for j in range(degree+1)]
    M = S.Matrix([[S.expand(p.subs(y,y+x)-p).coeff(x,degree-i).coeff(y,i)
                   for p in basis] for i in range(degree+1)])
    assert M.rank() == degree and M*S.eye(degree+1)[:,0] == S.zeros(degree+1,1)
    ranks.append(degree)
alpha,beta,s,t = S.symbols('alpha beta s t', nonzero=True)
f = alpha*S.Matrix([[1,s],[0,1]])
g = beta*S.Matrix([[1,t],[0,1]])
for _,m,n in points:
    assert (f**m*g**n-alpha**m*beta**n*S.Matrix([[1,m*s+n*t],[0,1]])).applyfunc(S.expand) == S.zeros(2)
result = {'status':'PASS','scope':'exhaustive cubic lattice and exact shear matrices; not a substitute for ordinary proofs',
          'lines':certificate,'shear_difference_ranks_degrees_0_to_3':ranks,
          'Ore_action_power_identities':len(points)}
Path(__file__).with_name('cubic_spectral_ore_reduction_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','lines':len(lines),'power_identities':len(points)}))
