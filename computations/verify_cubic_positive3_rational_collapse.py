#!/usr/bin/env python3
"""Exact AS2 normalizer identities supporting the positive-three collapse exclusion."""
import json
from pathlib import Path
import sympy as S


def main():
    a,b,q,r,s=S.symbols('a b q r s',nonzero=True)
    Q=S.Matrix([[0,1],[-q,0]])
    assert -Q.T*Q.inv()==S.diag(q,1/q)
    F=S.diag(a,1/a)
    assert (F**2-S.diag(q,1/q)).subs(q,a*a)==S.zeros(2)
    anti=S.Matrix([[0,r],[s,0]]);Qminus=S.Matrix([[0,1],[1,0]])
    assert anti*Qminus*anti.T==r*s*Qminus and anti.det()==-r*s
    # Ad_(x^m y^n) has x/y weights q^-n,q^m. The inverse Nakayama
    # implementer xy has degree2, so a degree2 implementer of mu would
    # differ from (xy)^-1 by a central homogeneous element of degree4.
    m,n=S.symbols('m n')
    assert S.solve([-n-1,m+1],[m,n])=={m:-1,n:-1}
    jordan=S.Matrix([[a,0],[b,a]])
    assert jordan.det()==a*a
    assert S.expand((jordan**2)[1,1]-a*a)==0
    # In the localized skew relation zy=a*yz, with a²=1,z²=c*y²,
    # t=zy^-1=a^-1*y^-1*z has t²=a^-3*c=a*c.
    c=S.symbols('c',nonzero=True)
    assert S.rem(S.together((a**-3*c-a*c)*a**3),a*a-1,a)==0
    data={
      'hypotheses':'H3 multiplicities(3,1), common plane gamma=0, embedded AS2 T',
      'excluded_configuration':'complementary positive v in Qgr(T), and negative z² in Qgr(T)',
      'commutative':'inner f²=id, finite fixed-field extension forces GKdim<=2',
      'quantum_nonroot':'f²=mu_T, but h*x*y would be nonzero central homogeneous of degree4; the only homogeneous central elements have degree0',
      'quantum_root':'f finite and Q(T) finite over a trdeg2 fixed central field; finite structure constants force GKdim<=2',
      'Jordan':'f(y)=a*y,a²=1; commuting h with y forces h=c*y²; (z/y)²=a*c is scalar, so algebraic closedness and the domain property force z proportional to y',
      'scope':'Matrix/Nakayama and localized square identities checked exactly. Rational periodicity, homogeneous centers and finite-central growth are structural proofs; no gamma!=0 or full normalizing-chart exclusion asserted.'}
    path=Path(__file__).with_name('cubic_positive3_rational_collapse_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS positive-three quantum/Jordan normalizer and scalar-square identities')


if __name__=='__main__':main()
