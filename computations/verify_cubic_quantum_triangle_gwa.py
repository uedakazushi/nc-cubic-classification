"""Universal q-difference/GWA and Ore determinant identities."""
import sympy as s,json
from pathlib import Path
q,u,D,Q,r=s.symbols('q u D Q r');h=q*q-1;kappa2=q/h**2
b=(q*(u*u+1)*(u*u+q*q)+u*u*h**3*D)/(h*h*(u*u-q*q)*(u*u-1))
rr=u-1/u;a=(u*u+q*q/u**2+1+q*q)/h**2+h*D/q
assert s.cancel(rr*rr.subs(u,u/q)*b-a)==0
assert s.cancel(rr*rr.subs(u,q*u)*b.subs(u,q*u)-a.subs(u,q*u))==0
assert s.cancel(a.subs(u,q/u)-a)==0
assert s.cancel(b.subs(u,1/u)-b.subs(u,q*u))==0
M=s.Matrix([[q*r,-1/q],[1,r/q]])
f=lambda Q:r*r-kappa2*(Q+1/Q)**2
FM=M*M-kappa2*(Q+1/Q)**2*s.eye(2)
assert s.factor(FM.det()-f(q*Q)*f(Q/q))==0
# The right-multiplication matrix has the same characteristic polynomial.
L=s.Matrix([[r/q,-1/q],[1,q*r]])
assert L.charpoly().as_expr()==M.charpoly().as_expr()
v=s.symbols('v');num=v*v+(1+q*q+h**3*D/q)*v+q*q
Dplus=-q/((q-1)*(q+1)**3);Dminus=-q/((q-1)**3*(q+1))
assert s.factor(s.discriminant(num,v)-h**6*(D-Dplus)*(D-Dminus)/q**2)==0
assert s.factor(num.subs(D,Dminus)-(v-q)**2)==0
assert s.factor(num.subs(D,Dplus)-(v+q)**2)==0
cert={'version':'classification-v55','GWA_base':'k[u^+-1,(q^j*u-q^-j*u^-1)^-1 : j in Z]','GWA_a':str(a),'GWA_generators':'A=(u-u^-1)T, B=(u-u^-1)b_D(u)T^-1','involution':'u->u^-1,A->-B,B->-A','Ore_f':'f_j(x)=x²-kappa²(q^j+q^-j)²','Ore_determinant':'det f_j(M(x))=f_(j+1)(x) f_(j-1)(x)','all_universal_identities':True,'ordinary_consequence':'For nonroot q, both D endpoints have infinite gldim U; every other D has finite gldim after this Ore localization. Unlocalized admissibility remains open.','source':'Bavula author overview Theorem3.1: rank1 GWA over a Dedekind ring has infinite global dimension at a repeated zero.'}
Path(__file__).with_name('cubic_quantum_triangle_gwa_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS universal GWA products, reflection, Ore determinant and double-root identities')
