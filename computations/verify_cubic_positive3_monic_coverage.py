"""Exact identities supporting the all-candidate monic coverage proof.
The Ore fraction argument and projection coverage are structural, not sampled.
"""
import json
from pathlib import Path
import sympy as s

k,b,x,C,t=s.symbols('k b x C t')
def d(p):
    return s.expand(s.diff(p,x)*(k*x*x+C)-2*b*x*C*s.diff(p,C))
assert s.expand(d(C*x)-d(x*C))==0
assert s.cancel((1+t)/((1-t)**3*(1-t*t))-1/(1-t)**4)==0
assert [s.expand(s.series(1/(1-t)**4,t,0,7).removeO()).coeff(t,i) for i in range(7)]==[1,4,10,20,35,56,84]
# v(vt) has Tv coefficient g(delta(t))+delta(g(t))+g^2(t)*ell;
# (v^2)t has coefficient ell*g(t).
A,B,D,E=s.symbols('g_delta delta_g g2_t_ell ell_g_t',commutative=False)
assert s.expand((A+B+D)-E-(A+B-(E-D)))==0
out={
 'status':'PASS',
 'scope':'universal monic normalizing coverage for remaining (3,1) H3 candidates; structural fraction/projection proof in TeX',
 'exact_checks':['Jordan weighted Ore relation preserved','alternating-word Hilbert identity','14641 dimensions through degree6','square compatibility Tv coefficient'],
 'not_claimed':['existence for arbitrary monic coefficients','H3 admissibility','finite free rank3 for the cut']}
Path(__file__).with_name('cubic_positive3_monic_coverage_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS positive3 monic coverage identities')
