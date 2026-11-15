"""Universal even-order half-dimensional family; endpoint identities."""
import sympy as s,json
from pathlib import Path
q,J,b=s.symbols('q J b');h=q*q-1
A=lambda J:J-q/J
lam=lambda J:-(q*J+1/J)/h
C=lambda J:(-(q-1)**2*b*b+q*q*(J*J+J**-2-2)/h**2)/(A(J)*A(q*J))
assert s.factor(C(J)*A(J)-C(q*J)*A(q*q*J)-lam(J))==0
assert s.factor((1-q)*b*b-C(q)*A(q*q)-lam(1))==0
assert s.factor(C(-1/q)*A(-1/q)-(1-q)*b*b-lam(-1/q))==0
# First row Casimir, for M>=2. The last diagonal entry is b.
a=1/(1-q);c1=C(q)
Om=s.factor(a*(b*b+c1/q)+(a*a+(q*q+1)*(b*b+c1))/h)
assert s.factor(Om-(q-1)/(q+1)*b*b-q/((q-1)**3*(q+1)))==0
w=s.factor(-(q+1/q)+h**3*Om/q**2)
assert s.factor(w-2-(q-1)**4*(q+1)**2*b*b/q**2)==0
# vanishing c_j is exactly w=q^(2j)+q^(-2j).
b2=q*q*(J*J+J**-2-2)/(h*h*(q-1)**2)
assert s.factor(w.subs(b*b,b2)-(J*J+J**-2))==0
cert={'version':'classification-v52','base':'q primitive N=2M>=4, q^M=-1','half_dimension':'M','recurrences':'all diagonal recurrences and both endpoint diagonal equations exact','Casimir':str(Om),'w_D':str(w),'reducibility':'c_j=0 iff w_D=q^(2j)+q^(-2j), hence iff k=4','centre_input':'Huang arXiv1509.08719v4 equation5, Section4.3, explicitly normalized; N4 independently PBW checked','ordinary_result':'All finite even-order cuts away from Dplus,Dminus are H3. Dplus always bad; Dminus bad for N<=18 by no-character/rank bound. Dminus at even N>=20 remains unproved.','scope':'Universal rational identities; exponent bounds and McKay rank arguments are ordinary proofs.'}
Path(__file__).with_name('cubic_quantum_triangle_even_representations_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS even-order half-dimension recurrence, Casimir, and all reducibility equations')
