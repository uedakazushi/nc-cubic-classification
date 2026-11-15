#!/usr/bin/env python3
"""Exact symmetric Clifford character branches and four distinct bad directions."""
import sympy as s,json
from pathlib import Path
h,b,c,r=s.symbols('h b c r');u,v,z=s.symbols('u v z')
L1=h*c-2*b;L2=(h**3-2)*b-3*h*c;Q=c*c+h*h*b*c+2*h*b*b
U=4*(h*c-2*b)/(h*(8-h**3));V=4*((h**3-2)*b-3*h*c)/(h*(8-h**3))
assert s.cancel(3*U+V+4*b/h)==0
assert s.cancel((2-h**3)*U-2*V-4*c)==0
assert s.expand(h*(4*b+h*c)**2-h*h*(4*b+h*c)*(h*h*b+2*c)+2*(h*h*b+2*c)**2-(8-h**3)*Q)==0
# Critical branch A: b=s^2(2r-h),c=s^2(2-h*r^2).
crit=h*r*r-h*h*r+2
assert s.rem(s.expand(Q.subs({b:2*r-h,c:2-h*r*r})),crit,r)==0
assert s.expand(s.discriminant(Q,c)-h*(h**3-8)*b*b)==0
assert s.cancel(Q.subs(c,2*b/h)-4*b*b*(h**3+1)/h**2)==0
assert s.cancel(Q.subs(c,(h**3-2)*b/(3*h))-4*b*b*(h**3+1)**2/(9*h*h))==0
assert s.expand(s.resultant(L1,L2,c)-h*b*(h**3-8))==0
cert={'version':'classification-v38','admissibility_polynomial':str(s.factor(L1*L2*Q)),'H3_iff':'polynomial !=0, h!=0,h^3!=-1,8','off_diagonal_branch':{'u_squared':str(U),'v_squared':str(V),'z':'-h*u/2'},'diagonal_branch_critical_polynomial':str(Q),'four_distinct_projective_beta_directions':True,'scope':'Exact all-parameter identities; branch decomposition and reducedness proof in cubic_normal_order2_arrows.tex'}
Path(__file__).with_name('cubic_normal_order2_discriminant_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS explicit quartic admissibility, two character branches, four distinct bad beta directions')
