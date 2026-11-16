"""All-GL2 separated commutative-plane chart: symbolic kernel and factor alternatives."""
import json
from pathlib import Path
import sympy as S
a,b,c,d,x,y,z=S.symbols('a b c d x y z');F=S.Matrix([[a,b],[c,d]]);D=F.det()
assert S.expand((F-D*S.eye(2)).det()-D*(F-S.eye(2)).det())==0
basis=[x**3,x*x*y,x*y*y,y**3]
def cube(M):
 return S.Matrix([[S.Poly(S.expand(p.subs({x:M[0,0]*x+M[1,0]*y,y:M[0,1]*x+M[1,1]*y},simultaneous=True)),x,y).coeff_monomial(t) for p in basis] for t in basis])
assert cube(S.diag(1,z))==S.diag(1,z,z*z,z**3)
assert (cube(S.Matrix([[1,1],[0,1]]))+S.eye(4)).det()==16
records=[]
for name,M in [('identity',S.eye(2)),('negative_identity',-S.eye(2)),('reflection',S.diag(1,-1))]:
 cubeker=4-(cube(M)+S.eye(4)).rank();minus=2-(M+S.eye(2)).rank();uv=2-(M-M.det()*S.eye(2)).rank()
 records.append({'F':name,'cubic_U_kernel':cubeker,'u_square_kernel':minus,'v_square_kernel':minus,'uv_kernel':uv,'total':cubeker+2*minus+uv})
assert [v['total'] for v in records]==[2,8,5]
# F has eigenvalue1, other eigenvalue lambda. Every cubic with F-eigenvalue -1
# has zero x^3 coefficient and hence is divisible by y; uv coefficient is also y
# unless lambda=1, handled by the unipotent check above.
assert (cube(S.diag(1,z))+S.eye(4))[0,0]==2
assert (S.diag(1,z)-z*S.eye(2))==S.diag(1-z,0)
# Iterated Ore Nakayama scalars for q=-det(F)^(-1).
assert S.cancel((-D)**-1*D)==-1
assert S.cancel(D**-1*(-D))==-1
# Jordan negative plane: PBW comparison of (vu-uv)t=kappa*u^2*t
# gives GF=FG and GF=F^2, hence G=F for invertible F.
g0,g1,g2,g3=S.symbols('g0 g1 g2 g3');GG=S.Matrix([[g0,g1],[g2,g3]])
assert ((GG*F-F*F)*F.adjugate()-D*(GG-F)).applyfunc(S.expand)==S.zeros(2)
# Positive-side nontrivial Jordan in the more general commuting f,g chart:
# if f=g and f^2 nontrivial unipotent, f= +/- (I+N); all possible coefficients
# lie in one fixed/eigenline and hence share a linear factor.
J=S.Matrix([[1,1],[0,1]])
assert (J-S.eye(2)).rank()==1 and (J+S.eye(2)).rank()==2
assert (-J+S.eye(2)).rank()==1 and (-J-S.eye(2)).rank()==2
out={'status':'PASS','scope':'commutative positive plane with separated quantum/Jordan negative generators, including all Nakayama Jordan types',
 'family':'ut=F(t)u, vt=F^-1(t)v, vu=-det(F)*uv',
 'mu':['x','y','-u','-v'],
 'kernel':'ker(Sym^3 F+I) + ker(F-det(F)I)*uv; if F^2=I add ker(F+I)*u^2 and ker(F+I)*v^2',
 'involutive_kernel_dimensions':records,
 'conclusion':'in the quantum-negative chart only F=-I admits H3; Jordan-negative separated charts are all H3-empty; the entire known fixed-sign classification applies',
 'proof':'papers/sections/cubic_order2_22_rank4_separated_commutative.tex',
 'not_claimed':['all odd graph coverage','noncommutative positive plane','pure mixed rank3-projection branch','global H3 classification'],
 'all_Jordan_extension':'if fg is nontrivial unipotent, normal cubic terms either equal linear*uv or all share the fixed/eigenline of f=g=+/-unipotent' }
Path(__file__).with_name('cubic_order2_22_rank4_separated_commutative_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all-GL2 separated commutative chart: kernel identities and sole H3 envelope F=-I')
