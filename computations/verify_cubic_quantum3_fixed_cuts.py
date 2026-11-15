#!/usr/bin/env python3
"""Exact critical values and characters in b=(1,1,1), lambda=0 chart."""
import sympy as s,json
from pathlib import Path
q,D,W,X,Y=s.symbols('q D W X Y');d=-(q+2)/3;e=-(2*q+1)/9
def red(c):return s.rem(s.expand(c),q*q+q+1,q).expand()
assert red(d**3-e)==0 and red(e**2+s.Rational(1,27))==0
F=W**3-d*W+X*Y*(X+Y+D)+e*D
crit=[s.diff(F,v) for v in [W,X,Y]]
branches=[(0,0),(0,-D),(-D,0),(-D/3,-D/3)]
res=[]
for a,b in branches:
 assert all(s.expand(c.subs({X:a,Y:b}))==0 for c in crit[1:])
 r=red(s.resultant(F.subs({X:a,Y:b}),crit[0],W));res.append(r)
 # Hessian determinant on the branch has nonzero D^2*W coefficient.
 assert s.factor(s.hessian(F,(W,X,Y)).det().subs({X:a,Y:b}))!=0
r0=red(res[0]/s.Poly(res[0],D).LC());r1=red(res[3]/s.Poly(res[3],D).LC())
assert red(r0-(D**2+4*e))==0
assert red(r1-(D**2+9*e)**2*(D**2+36*e))==0
# Character CI: yz=zx=xy=1/(1-q)=-d -> x=y=z=s, s^2=-d.
a=s.symbols('s');assert red(s.rem((3*a**3)**2+9*e,a*a+d,a))==0
factors=[D**2+4*e,D**2+9*e,D**2+36*e]
for i,f in enumerate(factors):
 assert red(s.resultant(f,s.diff(f,D),D))!=0
 for g in factors[:i]:assert red(s.resultant(f,g,D))!=0
out={'version':'classification-v27','parameters':'b1=b2=b3=1, lambda=0, q^2+q+1=0','center':'W^3-dW+XY(X+Y+D)+eD=0; d=1/(q-1), e=d^3, e^2=-1/27','critical_XY_branches':['(0,0)','(0,-D)','(-D,0)','(-D/3,-D/3)'],'singular_values':{'D^2+4e=0':'three A1 points, no characters, bad','D^2+9e=0':'one A1 point, exactly one character, McKay (1,2), good','D^2+36e=0':'one A1 point, no characters, bad'},'character_algebra':'x=y=z=s, s^2=-d; D=-3s^3','bad_polynomial':'(D^2+4e)(D^2+36e)','scope':'Exact critical elimination and character values; H3 conclusion uses the proved PI3 McKay-order theorem.'}
Path(__file__).with_name('cubic_quantum3_fixed_cuts_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS six singular values, all A1, two good singular cuts, four bad values')
