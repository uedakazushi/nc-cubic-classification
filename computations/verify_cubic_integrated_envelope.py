#!/usr/bin/env python3
"""Universal tensor identities for the integrated CY AS4 envelope theorem.
All-parameter identities support ordinary proofs via EG7.3.1 and LBS2.6/2.7.
No finite tensor or point-rank test alone certifies AS-regularity or H3 openness.
"""
import json
from pathlib import Path
from collections import defaultdict
from itertools import product
import sympy as s
p,q,h=s.symbols('p q h');alpha=s.symbols('alpha_x alpha_y alpha_z');beta=s.symbols('beta_x beta_y beta_z')
r=[]
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
    r.append({(j,k):p,(k,j):q,(i,i):-h,(3,i):-alpha[i]/2,(i,3):-alpha[i]/2,(3,3):-beta[i]})
left=defaultdict(lambda:s.Integer(0));right=defaultdict(lambda:s.Integer(0));w4=defaultdict(lambda:s.Integer(0))
for i,ri in enumerate(r):
    ki={(3,i):1,(i,3):-1}
    for a,c in ri.items():left[(i,)+a]+=c;right[a+(i,)]+=c
    for a,c in ki.items():
        left[(i,)+a]-=alpha[i]*c/2;left[(3,)+a]-=beta[i]*c
        right[a+(i,)]+=alpha[i]*c/2;right[a+(3,)]+=beta[i]*c
    for a,c in ri.items():
        for b,v in ki.items():w4[a+b]+=c*v;w4[b+a]+=v*c
for word in product(range(4),repeat=3):assert s.expand(left[word]-right[word])==0
for word in product(range(4),repeat=4):assert s.expand(w4[word]+w4[word[-1:]+word[:-1]])==0
selected=[(1,2),(2,0),(0,1),(3,0),(3,1),(3,2)]
minor=s.factor(s.Matrix([[w4[a+b] for b in selected] for a in selected]).det());assert minor==-p**6
x,y,z=s.symbols('x y z');M=s.Matrix([[-h*x,p*z,q*y],[q*z,-h*y,p*x],[p*y,q*x,-h*z]])
curve=h*p*q*(x**3+y**3+z**3)+(p**3+q**3-h**3)*x*y*z
assert s.expand(M.det()-curve)==0
origin=s.Matrix([1,-1,0]);P=s.Matrix([q,p,-h]);P2=s.Matrix([-p*(h**3+q**3),q*(h**3+p**3),h*(p**3-q**3)])
assert M.subs({x:1,y:-1,z:0})*P==s.zeros(3,1)
assert (M.subs({x:q,y:p,z:-h})*P2).applyfunc(s.expand)==s.zeros(3,1)
gamma=s.symbols('gamma');sub={p:1+gamma,q:1-gamma}
assert s.expand((P2[0]-P2[1]).subs(sub)-2*(gamma**4-1-h**3))==0
Delta=(p**3+q**3-h**3)**3+27*h**3*p**3*q**3
assert s.expand(Delta.subs({p:1,q:1})+(h**3-8)*(h**3+1)**2)==0
# Exact good order-four witness h=1,gamma^4=2; no interpolation.
a=s.symbols('a');minpoly=a**4-2
assert s.rem(Delta.subs({h:1,p:1+a,q:1-a}),minpoly,a)!=0
assert s.gcd(Delta.subs({h:1,p:1+a,q:1-a}),minpoly,a)==1
# The homogeneous Rains central cubic cannot vanish as a relation class:
# in the cyclic quotient, the pure-cube/three-distinct-word block has basis U,V.
qr,tau,U,V=s.symbols('q_R tau U V')
top_trace=(tau**2*(qr+1)*(tau**3+1)*(U-qr*V)/tau
 +tau*(qr+1)*(qr**3-tau**3)*U-qr*tau*(qr+1)*(tau**3+1)*V
 +tau**2*(qr+1)*(qr**3-tau**3)*(U-qr*V)/tau)
trace_expected=tau*(qr+1)*((1+2*qr**3-tau**3)*U-qr*(qr**3+tau**3+2)*V)
assert s.expand(top_trace-trace_expected)==0
cu=1+2*qr**3-tau**3;cv=qr**3+tau**3+2
assert s.expand((cu+cv)/3-(qr**3+1))==0
assert s.expand(cv-(cu+cv)/3-(tau**3+1))==0
certificate={'version':'classification-v12','ring':'QQ[p,q,h,alpha_x,alpha_y,alpha_z,beta_x,beta_y,beta_z]',
    'W3_lift_tensor_identities':64,'W4_signed_cyclic_tensor_identities':256,
    'W4_rank6_minor':str(minor),
    'W3_lift':'sum xi*r_i - sum (alpha_i*xi/2+beta_i*t)*k_i = sum r_i*xi + sum k_i*(alpha_i*xi/2+beta_i*t)',
    'point_curve':str(curve),'smooth_discriminant':str(Delta),
    'gamma0_discriminant':'-(h^3-8)*(h^3+1)^2',
    'translation_origin_image':['q','p','-h'],
    'translation_twice_origin':list(map(str,P2)),
    'order4_equation_on_smooth_nonzero_parameter_locus':'gamma^4=1+h^3',
    'order4_exact_witness':'h=1,gamma^4=2; discriminant coprime to gamma^4-2',
    'ordinary_proof_inputs':'IS Theorem1.1/Corollary6.1; EG Proposition7.3.1(i), Lemma7.2.1 and graded argument; LBS Theorem2.6 and Corollary2.7 with actual 1-regularity and W3 surjectivity',
    'top_central_class_nonvanishing':'Cyclic U,V coefficients vanish simultaneously only if q_R^3=tau^3=-1, excluded by the smooth discriminant',
    'scope':'All-degree flat AS4-envelope and central-quotient recognition on explicit smooth leading locus, using IS Theorem1.1/Cor6.1 and LBS. H3 iff finite affine global dimension; transcendental central values good; order4 branch has finitely many bad values. No full relative H3 openness, bad-value list or complete H3 classification certificate.'}
Path(__file__).with_name('cubic_integrated_envelope_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('PASS:64 W3 identities;256 signed-cyclic W4 identities; minor -p^6; elliptic graph and exact order4 witness; ordinary formal-flatness/AS4 proof hypotheses recorded')
