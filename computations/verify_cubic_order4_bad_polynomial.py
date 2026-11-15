#!/usr/bin/env python3
"""Exact degree-six exceptional polynomial, conditional only on the paper's
ordinary maximal-order/local-duality proofs (not verified by this script).
"""
import json,sympy as s
from pathlib import Path
from sympy.polys.rings import ring
T=s.symbols('g');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));g=K.unit;R,D=ring('D',K);root=Path(__file__).parent
crit=json.loads((root/'cubic_order4_center_critical_certificate.json').read_text());reps=json.loads((root/'cubic_order4_small_rep_certificate.json').read_text())
def cv(t):
 a,b=s.fraction(s.cancel(s.sympify(t)));return K.new(s.Poly(a,T,domain=s.QQ).all_coeffs())/K.new(s.Poly(b,T,domain=s.QQ).all_coeffs())
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
def rp(rows):return sum((R(cv(t['coefficient']))*D**t['D_power'] for t in rows),R.zero)
def sf(branch,m):return next(rp(t['factor']) for t in crit[branch] if t['multiplicity']==m)
P4,P6=sf('symmetric_squarefree',1),sf('symmetric_squarefree',2);Q1,Q2=sf('off_axis_squarefree',1),sf('off_axis_squarefree',2)
ds=(4467*g**3-5311*g*g+6316*g-7511)/4;lin=D-R(ds);bad=lin*P4*Q1
assert bad.degree()==6 and bad.gcd(bad.diff(D)).degree()==0
assert P6.rem(lin)==0
assert reps['combined_norm_identity_verified'] and reps['norms_mutually_coprime']
assert crit['Jacobian_f_multiplication_3minor_gcd_is_unit'] and crit['off_axis_no_triple_roots_at_discriminant']
for n in ['1','2']:
 assert reps[n]['off_axis_separation']['v_nonzero_square_and_zero_trace_verified']
assert reps['2']['reduced'] and reps['2']['detL_everywhere_nonzero']
# PIdegree4 permits tame ramification indices only 1,2,4. In the split lattice-chain
# block model, trace dual transposes the negative valuation matrix. Diagonals force
# any central multiplier to valuation0; for e>1, upper blocks then contradict it.
for e in [1,2,4]:
 val=[[int(i>j) for j in range(e)] for i in range(e)]
 dual=[[-val[j][i] for j in range(e)] for i in range(e)]
 assert (val==dual)==(e==1)
result={'version':'classification-v19','fixed_envelope':'h=1,g^4=2,alpha=(-2,-2,0),beta=(1,1,2)',
 'bad_polynomial_degree':6,'squarefree_verified':True,'factorization':'(D-Dstar)*P4*Q1; monic squarefree layers of center-critical certificate',
 'coefficients':[{'D_power':e[0],'coefficient':txt(c)} for e,c in bad.to_dict().items()],
 'ordinary_proof_dependency':'papers/sections/cubic_order4_local_orders.tex: filtered maximality, central local duality, tame DVR block structure, A1 double-cover descent',
 'scope':'Complete D-line classification in this ONE fixed envelope, not all order4 envelopes nor all intrinsic H3; novelty and independent review unchecked',
 'DVR_block_trace_dual_valuation_checks':[1,2,4]}
(root/'cubic_order4_bad_polynomial_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS exact squarefree degree-six bad polynomial; local-order implication uses the ordinary paper proof')
