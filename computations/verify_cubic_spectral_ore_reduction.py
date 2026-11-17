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
# All affine lines through two cubic points; retain lines without a common factor.
affine = {}
for p,q in itertools.combinations(points,2):
    m,n = p[1:]
    u,v = q[1]-m,q[2]-n
    A,B = v,-u
    C = A*m+B*n
    divisor = gcd(gcd(A,B),C)
    A,B,C = A//divisor,B//divisor,C//divisor
    if A < 0 or (A == 0 and B < 0): A,B,C = -A,-B,-C
    affine[A,B,C] = [r for r in points if A*r[1]+B*r[2] == C]
jordan = []
edges = 0
for line,group in sorted(affine.items()):
    if any(min(p[i] for p in group)>0 for i in range(3)): continue
    if any(all(p[i]==0 for p in group) for i in range(3)):
        edges += 1
        continue
    assert len(group)==2
    p,q = group
    determinant = (p[1]-1)*(q[2]-1)-(p[2]-1)*(q[1]-1)
    assert abs(determinant)==1
    jordan.append({'line':line,'support':group,'normal_x_exponent_determinant':determinant})
assert edges==3 and len(jordan)==6
kappa = S.symbols('kappa', nonzero=True)
C = S.Matrix([[-kappa,-1],[1,0]])
mu_T = -(C.inv()*C.T).inv().T
assert mu_T == S.Matrix([[1,2*kappa],[0,1]])
quad3 = [a for a in itertools.product(range(3),repeat=3) if sum(a)==2]
collisions3 = [(a,b) for a,b in itertools.combinations(quad3,2)
               if not any(min(x,y) for x,y in zip(a,b))]
assert len(collisions3)==6
result = {'status':'PASS','scope':'exhaustive cubic lattice, exact shear matrices, Jordan Koszul-dual convention; ordinary proofs separate',
          'lines':certificate,'shear_difference_ranks_degrees_0_to_3':ranks,
          'Ore_action_power_identities':len(points), 'Jordan_support_edge_lines':edges,
          'Jordan_nonfactor_binomial_supports':jordan,
          'Jordan_Nakayama_matrix':str(mu_T),
          'three_distinct_eigenvalue_quadratic_collisions':collisions3}
Path(__file__).with_name('cubic_spectral_ore_reduction_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','center_lines':len(lines),'Jordan_binomials':len(jordan),'three_eigenvalue_collisions':len(collisions3)}))
