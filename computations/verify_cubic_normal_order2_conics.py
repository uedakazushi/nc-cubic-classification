#!/usr/bin/env python3
"""The four forbidden coefficient directions are three singular conics and coincidence."""
import sympy as s,json
from pathlib import Path
h,b,c,q,r,z=s.symbols('h b c q r z');L1=h*c-2*b;L2=(h**3-2)*b-3*h*c;Q=c*c+h*h*b*c+2*h*b*b
F=L2*q*q-4*(h*h*b-c)*q*r+4*h*b*r*r+L1*z*z
Gamma=-2*(1+h**3)*q*r+3*h*h*r*r+h*(h**3-8)*z*z/4
M=s.hessian(F,(q,r,z))/2;MG=s.hessian(Gamma,(q,r,z))/2
assert s.expand(M.det()+4*L1*Q)==0
assert s.expand(MG.det()+h*(h**3-8)*(1+h**3)**2/4)==0
assert s.cancel(F.subs(c,(h**3-2)*b/(3*h))-4*b*Gamma/(3*h))==0
# Central-coordinate formula A=lC*C+lB*B+lD*D.
C,B,D,T=s.symbols('C B D T');al=(1+h**3)/(2*h);be=(2-h**3)/(4*h);ka=h*b-c/h
Tform=(-2*(1+h**3)*D+3*h*h*C+h*(h**3-8)*B/4)/L2
A=s.cancel((C-be*B-ka*Tform)/al)
expected=(-4*h*b*C-L1*B+4*(h*h*b-c)*D)/L2
assert s.cancel(A-expected)==0
# On the standard scroll C=lambda*r^2,B=lambda*z^2,D=lambda*q*r.
lam=s.symbols('lambda');discr=s.cancel((D*D-A*C).subs({C:lam*r*r,B:lam*z*z,D:lam*q*r}))
assert s.cancel(discr-lam**2*r*r*F/L2)==0
cert={'version':'classification-v41','conic':str(F),'fixed_conic_Gamma':str(Gamma),'conic_determinant':'-4*(hc-2b)*(c^2+h^2bc+2hb^2)','Gamma_determinant':'-h*(h^3-8)*(1+h^3)^2/4','coincidence_member':'L2=0 implies F=4b*Gamma/(3h)','Clifford_discriminant_on_scroll':'D^2-A*C=lambda^2*r^2*F/L2','generic_Brauer_symbol':'(-T/C, (D^2-A*C)/C^2)','scope':'Exact polynomial and rational identities. Four-point transversality and residue ramification follow in the ordinary proof.'}
Path(__file__).with_name('cubic_normal_order2_conics_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS conic pencil, three singular members, coincidence member, Clifford discriminant factorization')
