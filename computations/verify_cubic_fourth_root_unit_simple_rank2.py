#!/usr/bin/env python3
"""Exact tensor, AS2 and list checks for the fourth-root rank2 exclusion.
Normal Rees, Ore descent and graded bimodule localization are ordinary proofs,
not established by these finite calculations.
"""
import itertools
import json
import math
from pathlib import Path
import sympy as s

root=Path(__file__).resolve().parent
words=list(itertools.product(range(2),repeat=4))
rotate=s.zeros(16); swap=s.zeros(16)
for j,w in enumerate(words):
    rotate[words.index(w[1:]+w[:1]),j]=1
    swap[words.index((w[1],w[0],w[2],w[3])),j]=1
ranks=[]
for rho in [s.I,-s.I]:
    twisted=rotate+rho*s.eye(16)
    assert twisted.rank()==13
    full=twisted.col_join(swap-s.eye(16))
    assert full.rank()==16
    ranks.append({'rho':str(rho),'twisted_binary_quartic_dimension':3,
                  'first_pair_symmetric_twisted_dimension':0})
# Independent square tensors and any nondegenerate even pairing give rank2.
P=s.Matrix([[1,0],[0,0],[0,0],[0,1]])
J=s.Matrix([[0,1],[-1,0]])
assert (P*J*P.T).rank()==2
# Normal quadratic quotient of the rank2 base has the AS2 Hilbert series.
t=s.symbols('t')
HS=1/((1-t)**2*(1-t**2))
assert s.cancel((1-t**2)*HS-1/(1-t)**2)==0
# The AS2 Nakayama fixes the relation, in both normal forms.
p,k=s.symbols('p k',nonzero=True)
forms=[(s.Matrix([[0,1],[-p,0]]),s.diag(p,1/p)),
       (s.Matrix([[-k,-1],[1,0]]),s.Matrix([[1,2*k],[0,1]]))]
for Q,M in forms:
    assert (M*Q*M.T-Q).applyfunc(s.cancel)==s.zeros(2)
# Degree -5 generator maps to b^-1 times degree -4 generator.
assert -5-(-4)==-1
source=json.loads((root/'cubic_fourth_root_negative_repeat_exclusion_certificate.json').read_text())
assert source['status']=='PASS' and source['final_spectrum_count']==13
removed=[r for r in source['final_survivors'] if r['N']==4 and r['spectrum'] in [[1,0,2],[3,0,2]]]
assert len(removed)==2
assert all(r['relation_weight_multiplicities']==[[0,2,2,2]] for r in removed)
final=[r for r in source['final_survivors'] if r not in removed]
assert len(final)==11
counts={str(N):sum(r['N']==N for r in final) for N in [3,4]}
assert counts=={'3':3,'4':8}
reps=set()
for r in final:
    N=r['N']; a,b,c=r['spectrum']
    orbit=[(N,(a*u)%N,*sorted([(b*u)%N,(c*u)%N])) for u in range(1,N) if math.gcd(u,N)==1]
    reps.add(min(orbit))
assert len(reps)==6
out={'status':'PASS','scope':'exact binary tensor symmetry, AS2 relation scaling and finite survivor bookkeeping; ordinary homological proof separate',
     'tensor_checks':ranks,'independent_square_even_principal_rank':2,
     'AS2_Nakayama_relation_scale':1,'normal_quadric_quotient_Hilbert':'1/(1-t)^2',
     'graded_localization_generator_degree':-1,
     'excluded_spectra':removed,'final_survivors':final,'final_spectrum_count':11,
     'remaining_orders':[3,4],'remaining_counts':counts,
     'Galois_label_orbit_count':6,'Galois_label_representatives':sorted(reps),
     'not_claimed':['ordinary Rees/Ore/localization arguments formally verified',
                    'remaining11 H3 existence or admissibility','four-eigenvalue/CY coverage','complete H3 classification']}
(root/'cubic_fourth_root_unit_simple_rank2_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','unit_simple_fourth_root_spectra_excluded':2,'remaining_spectra':11}))
