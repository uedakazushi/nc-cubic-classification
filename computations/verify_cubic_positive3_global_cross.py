#!/usr/bin/env python3
"""Exact anti-cyclic Schur block, coordinate translation, and AS2 centralizers."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    a,b,c,d,n,t0,t1,q=S.symbols('a b c d n t0 t1 q',nonzero=True)
    ell=S.Matrix([1,0]);r=ell.col_join(-ell);k=S.Matrix([a,b,c,d])
    H=r*k.T+k*r.T
    assert H[:2,:2]+H[2:,2:]==S.Matrix([[2*(a-c),b-d],[b-d,0]])
    H=H.subs({c:a,d:b});ss=S.Matrix([a,b])
    assert H[:2,2:]==ell*ss.T-ss*ell.T
    # Anti-cyclic orbit vvv*ell has coefficients n,-n,n,-n.
    top={(2,2,2,0):n,(2,2,0,2):-n,(2,0,2,2):n,(0,2,2,2):-n}
    shift={0:{0:S.Integer(1)},1:{1:S.Integer(1)},2:{2:S.Integer(1),0:-t0,1:-t1}}
    transformed={}
    for word,cc in top.items():
        choices=[list(shift[j].items()) for j in word]
        for terms in itertools.product(*choices):
            ww=tuple(i for i,co in terms);co=cc*S.prod(co for i,co in terms)
            transformed[ww]=S.expand(transformed.get(ww,0)+co)
    cross=[(2,0),(2,1),(0,2),(1,2)]
    change=S.Matrix([[transformed.get(w+v,0) for v in cross] for w in cross])
    sub={t0:a/n,t1:b/n}
    assert (H+change.subs(sub)).applyfunc(S.expand)==S.zeros(4)
    Q=-H[:2,2:]
    Qchange=S.Matrix([[transformed.get((2,2,i,j),0) for j in range(2)] for i in range(2)])
    assert (Q+Qchange.subs(sub)).applyfunc(S.expand)==S.zeros(2)
    # Quantum centralizer of ell=x+y in degree2, normal basis x²,xy,y².
    centralizer=S.Matrix([[1-q**-2,q**-1-1,0],[0,1-q**-1,q**-2-1]])
    square=S.Matrix([1,1+1/q,1])
    assert (centralizer*square).applyfunc(S.cancel)==S.zeros(2,1)
    assert S.factor(centralizer[:,[0,2]].det())==-(q-1)**2*(q+1)**2/q**4
    # An axis has only its own square in its quadratic centralizer if q²!=1.
    assert S.factor((1-q**-1)*(1-q**-2))==(q-1)**2*(q+1)/q**3
    kap=S.symbols('kap',nonzero=True)
    assert S.Matrix([[0,kap,0],[0,0,2*kap]]).rank()==2
    assert S.Matrix([[-2*kap,0,0],[-2*kap**2,-kap,0]]).rank()==2
    # In the q=-1 surviving plane, f=diag(i,-i) negates EVERY linear square.
    u,v,X,Y=S.symbols('u v X Y')
    assert S.expand((S.I*u)**2*X+(-S.I*v)**2*Y+(u*u*X+v*v*Y))==0
    data={
      'hypotheses':'H3 multiplicities(3,1), gamma=0, actual Nakayama semisimple',
      'normal_form':'after a W-translation of v, [v,ell]=0 and v² in T2, ell!=0',
      'Schur_block':'r=(ell,-ell); rank2 residual gives Hcross=r*k^t+k*r^t; anti-cyclicity forces kleft=kright',
      'translation':'v_old=v_new-(a*ell+b*m)/n kills the full cross-cross and vvWW blocks',
      'plane_restriction':'T is commutative or the minus-one quantum plane; all other AS2 planes force a commuting square factor',
      'commutative_case':'f=+I or-I, so ell is respectively central or normal with normalizer mu_B',
      'minus_one_case':'f=diag(i,-i); ell² has normalizer mu_B, and v² is independent of ell²; both axis squares commute with all positive generators and anticommute with z',
      'scope':'Block/translation, exact centralizer and square-weight identities checked. Rank/square-quotient and global plane restrictions use the manuscript proofs. Positive-W Jordan and gamma!=0 remain outside this theorem.'}
    path=Path(__file__).with_name('cubic_positive3_global_cross_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS positive-three anti-cyclic cross normal form and surviving-plane constraints')


if __name__=='__main__':main()
