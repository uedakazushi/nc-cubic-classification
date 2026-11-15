#!/usr/bin/env python3
"""All-parameter extension of the specified transverse central cut through epsilon^3.
Reruns the first-order certificate and verifies every degree4 second-order equation.
No assertion of formal integration or an H3 family beyond the Clifford sector.
"""
import runpy
from pathlib import Path
second_certificate_path=Path(__file__).with_name('cubic_clifford_second_order_certificate.json')
v=runpy.run_path(str(Path(__file__).with_name('verify_cubic_clifford_tangent.py')));globals().update({k:value for k,value in v.items() if not k.startswith('__')})
N1=DM[0]-4*A*DM[1]-4*B*DM[2]-4*C*DM[3]
M1=matrix(4,dr[0])[1]-4*A*matrix(4,dr[1])[1]-4*B*matrix(4,dr[2])[1]-4*C*matrix(4,dr[3])[1]
# Degree4 flatness at second order when no second envelope coefficients are used.
T1=(L*(M1-N1*T)[list(rows),:]).applyfunc(s.cancel)
assert (N*T1+N1*T-M1).applyfunc(s.cancel)==s.zeros(*M.shape)
assert (P*N1*T1).applyfunc(s.cancel)==s.zeros(35,M.cols)
vs=[]
for x in range(3):
 c0=L*cv(g,x)[list(rows),:]
 dif=(cv(explicit,x)-N1*c0).applyfunc(s.cancel)
 c1=(L*dif[list(rows),:]).applyfunc(s.cancel)
 assert (N*c1-dif).applyfunc(s.cancel)==s.zeros(121,1)
 vs.append(-P*N1*c1)
H=s.Matrix.vstack(*vs).applyfunc(s.cancel)
EH=(E*H).applyfunc(s.cancel)
# Envelope alpha_i at order epsilon^2.
kappa=(-(expected[:,1:]).inv()*EH[selected,:]).applyfunc(s.cancel)
print('kappa',[s.factor(q) for q in kappa],flush=True)
res=(H+s.Matrix.hstack(*obs[1:])*kappa).applyfunc(s.cancel)
assert (E*res).applyfunc(s.cancel)==s.zeros(105,1)
G2=(-(ZL*Sel*res)).applyfunc(s.cancel)
assert (ZN*G2+res).applyfunc(s.cancel)==s.zeros(105,1)
assert all(localized(q) for mat in [T1,kappa,G2] for q in mat)
N2=sum((kappa[j]*DM[j+1] for j in range(3)),s.zeros(*DM[0].shape))
M2=sum((kappa[j]*matrix(4,dr[j+1])[1] for j in range(3)),s.zeros(*M.shape))
assert (P*(M2-N1*T1-N2*T)).applyfunc(s.cancel)==s.zeros(35,M.cols)
expected_kappa=s.Matrix([4*A*(h**3+3)/(1+h**3),-4*B*(3*h**3+1)/(1+h**3),-4*C*(h**3-3)/(1+h**3)])
assert (kappa-expected_kappa).applyfunc(s.cancel)==s.zeros(3,1)
import json
certificate={'version':'classification-v10', 'modulus':'epsilon^3=0',
    'ring':certificate['ring'],
    'first_envelope_coefficients':'gamma=1,alpha=-4(A,B,C)',
    'second_alpha_coefficients':list(map(lambda q:str(s.factor(q)),kappa)),
    'second_central_correction':[{'active_word':list(f3[j]),'t_power':3-len(f3[j]),'coefficient':str(s.factor(q))} for j,q in zip(zc,G2) if q],
    'degree4_second_order_all_syzygies_lift':True,
    'denominators':'Only h and 1+h^3 factors; all beta and cut coefficients included',
    'limits':'Existence through epsilon^3 only. No third/higher order integration, genuine H3 family, full ambient tangent space, component or full relative stack claim.'}
second_certificate_path.write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS second-order central lift, all h,beta,a,D; unperturbed-envelope syzygies second order',flush=True)
