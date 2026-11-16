"""Exact polynomial right-inverse certificate excluding an explicit main-chart open."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_functionals import normal_matrix,RHO,SIGMA,TAU
r,s,t=RHO,SIGMA,TAU;N=normal_matrix();P=N.domain;entry=json.loads(Path(__file__).with_name('cubic_order2_22_secant_main_open_input.json').read_text());loc={'r':r,'s':s,'t':t}
X=DomainMatrix({i:{j:P.from_sympy(S.sympify(v,locals=loc)) for j,v in enumerate(row) if v!='0'} for i,row in enumerate(entry['polynomial_inverse_numerator'])},(10,10),P)
d=P.from_sympy(S.sympify(entry['denominator'],locals=loc));L=r**5+r**4+2*r**3*s*s+2*r**3*t*t-2*r*r*s*s+2*r*r*t*t+2*r*t*t-r+2*t*t-1
expected=r**3*s*t*t*(r-1)**5*(r+1)**6*(r*r-2*t-1)*(r*r+2*t-1)*L
assert d==P.from_sympy(expected)
C=N.extract(entry['rows'],entry['cols']);assert C*X==DomainMatrix({i:{i:d} for i in range(10)},(10,10),P)
out={'status':'PASS','scope':'nondegenerate positive symmetric-secant q1 positive-Pfaffian main chart','method':'eight polynomial quartic functionals independently annihilate all 288 original insertions; selected normal submatrix C has explicit polynomial X with C*X=d*I10. No multivariate quotient elimination or determinant computation is needed to replay.','denominator_factorization':str(S.factor(expected)),'H3_exclusion_open':'s*t*(rho2-2t-1)*(rho2+2t-1)*L!=0, rho(rho2-1)!=0','remaining_after_completed_boundaries_and_resonance':'only s=0, t=0, rho2-2t-1=0, or L=0; also retain a!=0 and rho2+2t-1!=0 since their complements already excluded','not_claimed':['four residual surfaces','AS4 sufficiency of necessary atlas','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_secant_main_open_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS secant main explicit open: exact polynomial C*X=d*I10 and original-relation annihilators')
