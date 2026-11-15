"""Universal tridiagonal recurrences, with Q=q^d and J=q^j formal."""
import sympy as s,json
from pathlib import Path
q,Q,J,R=s.symbols('q Q J R');h=q*q-1
relation=R*R+q*q/Q
def zero(f,classic=False):
 n,d=s.cancel(f).as_numer_denom()
 return s.factor(s.rem(n,relation,R) if classic else n)==0
def A(J,R):return R*J/q-q*q/(R*J)
def lam(J,R):return -(R*J+q/(R*J))/h
def cc(J):return q*q*(Q+1/Q-J*J/Q-Q/(J*J))/(h*h*A(J,R)*A(q*J,R))
def cn(J):return q*q*(J*J+J**-2-Q*Q-Q**-2)/(h*h*A(J,q)*A(q*J,q))
assert zero(cc(J)*A(J,R)-cc(q*J)*A(q*q*J,R)-lam(J,R),True)
assert zero(cc(1),True) and zero(cc(Q),True)
assert zero(cn(J)*A(J,q)-cn(q*J)*A(q*q*J,q)-lam(J,q))
assert zero(cn(Q))
d0=(Q-1/Q)/((q-1/q)*(q-1))
assert zero((1-q)*d0*d0-cn(q)*A(q*q,q)-lam(1,q))
# Last-row evaluation, d>=2. For d=1 use the five characters directly.
for label,C,rr,ww,cl in [('classical',cc,R,-Q-1/Q,True),('nonclassical',cn,q,Q*Q+Q**-2,False)]:
 last=Q/q;l=lam(last,rr);c=C(last)
 Om=l*c*rr*last/q+(l*l+(q*q+1)*c)/h
 assert zero(-(q+1/q)+h**3*Om/q**2-ww,cl)
# x eigenvalue differences and off-diagonal entries are proved nonzero by
# odd-order exponent bounds in the paper, rather than numerical samples.
cert={'version':'classification-v50','formal_variables':'Q=q^d, J=q^j; classical R^2=-q^2/Q','universal_checks':['classical all interior diagonal recurrences','classical both boundary coefficients zero','nonclassical all interior diagonal recurrences','nonclassical top boundary and special first-row diagonal term','both last-row Casimir values'],'classical_w':'-(q^d+q^-d)','nonclassical_w':'q^(2d)+q^(-2d)','dimension_range':'1<=d<=(N-1)/2, N odd; irreducibility is an exponent-bound proof','consequence':'All interior singular centres at odd order have a simple of dimension < N. Complete H3 iff (D-Dplus)(D-Dminus)!=0.','scope':'Universal symbolic recurrence identities, not finite parameter sampling; maximal-order, terminal boundary and McKay are ordinary proofs.'}
Path(__file__).with_name('cubic_quantum_triangle_odd_representations_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS universal odd-order tridiagonal recurrence and Casimir identities')
