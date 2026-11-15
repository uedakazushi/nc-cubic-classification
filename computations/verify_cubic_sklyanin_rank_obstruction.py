"""Weighted-centre consistency checks; not a substitute for the Brauer proof."""
import sympy as s,json,hashlib
from pathlib import Path
t=s.symbols('t');HS=1/(1-t)**4
HZ=(1-t**6)**2/((1-t**3)**4*(1-t**2)**2)
HC=s.cancel(HZ*(1-t**3));HR=HS*(1-t**3)
assert s.series(HZ,t,0,4).removeO().coeff(t,3)==4
assert s.limit((1-t)**4*HZ,t,1)==s.Rational(1,9)
assert s.limit(HR/HC,t,1)==9
assert s.limit((1-t)**3*HC,t,1)==s.Rational(1,3)
assert s.cancel(HC.subs(t,1/t)+t*HC)==0
assert 6+6+3-(4*3+2*2)==-1
assert s.Rational(1,3)+4*s.Rational(-3,9)==-1
# Universal traceless 3x3 Cayley--Hamilton norm factorization.
a,b,c,d,e,f,g,h=s.symbols('a b c d e f g h')
M=s.Matrix([[a,b,c],[d,e,f],[g,h,-a-e]])
H=M*M-s.trace(M*M)*s.eye(3)/2
assert all(s.expand(x)==0 for x in M*H-M.det()*s.eye(3))
assert s.expand(s.trace(M**3)-3*M.det())==0
cert={'version':'classification-v58','universal_traceless_3x3_norm_factorization':True,'projective_norm_map_degree':27,'base':'complex proper elliptic four-dimensional Sklyanin, order n not1,2,4 or infinite','order3_centre_weights':[3,3,3,3,2,2],'centre_relations':[6,6],'central_cut_degree':3,'centre_degree3_dimension':4,'generic_rank_S_over_centre':9,'generic_rank_R_over_centre':9,'centre_surface_K2':'1/3','centre_a_invariant':-1,'H3_obstruction':'PI3 with dim Z3=dim B1=4 has base-point-free finite surjective norm map P3->P3; every central cubic is a linear times quadratic product. Hence no domain quotient. General CY PI3 H3 requires dim Z3>=5.','scope':'Only weighted Hilbert/canonical/rank identities are computed. Full exclusion is an ordinary proof using primary WWY centre inputs and the norm-map lemma; no formal proof or independent referee claimed.'}
Path(__file__).with_name('cubic_sklyanin_rank_obstruction_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS weighted Sklyanin PI3 centre, canonical index, degree and rank consistency')
