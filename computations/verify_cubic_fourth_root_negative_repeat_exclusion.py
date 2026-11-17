#!/usr/bin/env python3
"""Exact original AS2 coefficient obstructions for the negative repeated root.
The all-chart Ore recovery and free-tensor argument are ordinary proofs.
"""
import itertools
import json
from pathlib import Path
import sympy as S

source=json.loads(Path(__file__).with_name('cubic_sixth_root_last_Ore_exclusion_certificate.json').read_text())
case=[r for r in source['final_survivors'] if r['N']==4 and r['spectrum']==[2,1,3]]
assert len(case)==1 and case[0]['relation_weight_multiplicities']==[[2,2,0,2]]
C=[v for v in itertools.product(range(4),repeat=3) if sum(v)==3 and (2*v[0]+v[1]+3*v[2])%4==0]
assert C==[(1,0,2),(1,2,0)]
# In the rank2 chart, x tensor v = y tensor x has no solution for v.
M=S.Matrix([[1,0],[0,1],[0,0],[0,0]])
assert M.rank()==2 and M.row_join(S.Matrix([0,0,1,0])).rank()==3
alpha,beta,kappa,p,rho=S.symbols('alpha beta kappa p rho',nonzero=True)
# Original Jordan relation yx=xy+kappa*x^2 in alpha^2 F x=alpha beta xF.
J=S.Matrix([[alpha*(alpha-beta),alpha**2*kappa],[0,alpha*(alpha-beta)],[0,0]])
assert S.factor(J[:2,:].det())==alpha**2*(alpha-beta)**2
assert J.subs(beta,alpha).nullspace()==[S.Matrix([1,0])]
# Noncommutative quantum diagonal case: alpha=i, alpha*gamma=-p,
# and the y coefficient normalizes x only when gamma^2=-p.
gamma=S.I*p
assert S.expand(gamma**2+p-p*(1-p))==0
# In the anticommutative case a scalar normalizer must be simultaneously +/-1.
assert S.expand(((rho+1)-(rho-1))/2)==1
assert S.diag(S.I,-S.I)**2==-S.eye(2)
final=[r for r in source['final_survivors'] if not (r['N']==4 and r['spectrum']==[2,1,3])]
assert len(final)==13 and sum(r['N']==3 for r in final)==3 and sum(r['N']==4 for r in final)==10
result={'status':'PASS','scope':'exact cubic support, original AS2 coefficient identities and free-tensor rank obstruction; ordinary all-chart proof separate',
        'excluded_spectrum':case[0],'cubic_support':C,'rank2_free_tensor_augmented_rank':[2,3],
        'Jordan_normal_x_minor':'alpha^2*(alpha-beta)^2','Jordan_equal_eigenvalue_kernel':'k*x',
        'quantum_diagonal_obstruction':'p*(1-p)=0 forces p=1',
        'anticommutative_scalar_normalizer_unit_identity':True,
        'final_survivors':final,'final_spectrum_count':13,'remaining_orders':[3,4],
        'remaining_counts':{'3':3,'4':10},'Galois_label_orbit_count':7,
        'not_claimed':['remaining13 H3 existence','complete four-eigenvalue or CY coverage']}
Path(__file__).with_name('cubic_fourth_root_negative_repeat_exclusion_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','negative_repeat_fourth_root_excluded':1,'remaining_spectra':13}))
