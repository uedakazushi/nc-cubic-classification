"""Exact rational chart covering all remaining nonmirror L geometric candidates."""
import json
from pathlib import Path
import sympy as S
r,z,s,t=S.symbols('r z s t');p=r*r-1;c=r*r+1;D=c-p*z*z;Q=c-2*c*z+p*z*z;H=Q+4*z;F=p*z-c;A=Q*Q-2*D*D
T=p*Q/(2*D);V=S.I*(r+1)*c*H/(2*r*D);av=p*p*A/(4*r*r*D*D)
L=2*r*r*(r-1)*s*s+2*(r+1)*c*t*t+(r-1)*(r+1)**2*c;delta=r*r+2*t-1
assert S.rem(L+2*(r-1)*s*s,c,r)==0
for expr in [L.subs({s:V,t:T}),1-r*r-T*T-(r-1)/(r+1)*V*V-av,r*r+2*T-1-2*p*c*(1-z)/D,r*r-2*T-1+2*p*z*F/D]:assert S.cancel(expr)==0
Z=(2*S.I*r*s+(r+1)*c)/((r+1)*delta);assert S.cancel(Z.subs({s:V,t:T})-z)==0
K=S.QQ_I.frac_field(r,t);LP=S.Poly(L,s,domain=K)
for expr in [T.subs(z,Z)-t,V.subs(z,Z)-s]:assert S.Poly(S.together(expr).as_numer_denom()[0],s,domain=K).rem(LP).is_zero
v=(r+1)*(t-1)-S.I*r*s;assert S.cancel(S.rem(L,v,s)-(r+1)*delta**2)==0
expr=D.subs(z,Z)-4*p*c*v/((r+1)*delta**2);assert S.Poly(S.together(expr).as_numer_denom()[0],s,domain=K).rem(LP).is_zero
U=r*p*c*D*z*(z-1)*F*A*Q*H
out={'status':'PASS','chart':'rho=r, s=i(r+1)(r2+1)H/(2rD), t=(r2-1)Q/(2D)','polynomials':{'D':str(D),'Q':str(Q),'H':str(H),'F':str(F),'A':str(A),'localization_unit':str(U)},'inverse':'z=(2i*r*s+(r+1)(r2+1))/((r+1)(2t+r2-1))','coverage':'r2+1=0 on L implies s0, already excluded. On remaining nonmirror L candidates all factors of U are units. The inverse denominator D is a unit because L mod v=(r+1)*delta_plus2, where v=(r+1)(t-1)-i*r*s, and D(inverse)=4(r2-1)(r2+1)*v/((r+1)*delta_plus2). Exact two-sided rational identities verify the open chart.','not_claimed':['normal-module saturation completed','H3 absence on this chart','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_L_parameter_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS complete rational chart of remaining nonmirror L open: identities, inverse, all denominators and excluded special fibers')
