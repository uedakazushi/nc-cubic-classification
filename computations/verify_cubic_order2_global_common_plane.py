#!/usr/bin/env python3
"""Exact linear-algebra and AS2 identities used in the global common-plane reduction."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    a,b,c,d,m,lam,u,v,q=S.symbols('a b c d m lambda u v q')
    r=S.Matrix([1,0,1,0]);k=S.Matrix([a,b,c,d])
    H=r*k.T+k*r.T
    assert H[:2,:2]-H[2:,2:]==S.Matrix([[2*(a-c),b-d],[b-d,0]])
    H=H.subs({c:a,d:b})
    assert H[:2,2:]==S.Matrix([[2*a,b],[b,0]])
    P=S.Matrix([-lam*u,-lam*v,u,v])
    HH=m*P*P.T
    assert (HH[:2,:2]-HH[2:,2:]-(lam*lam-1)*m*S.Matrix([[u*u,u*v],[u*v,v*v]])).applyfunc(S.expand)==S.zeros(2)
    assert HH[2:,:2]==-lam*m*S.Matrix([[u*u,u*v],[u*v,v*v]])
    # In xy=q*yx, [A*x²+B*xy+C*y²,x+y] has the following two coefficients.
    A,B,C=S.symbols('A B C')
    commute=S.Matrix([[1-q**-2,q**-1-1,0],
                      [0,1-q**-1,q**-2-1]])
    square=S.Matrix([1,1+1/q,1])
    assert (commute*square).applyfunc(S.cancel)==S.zeros(2,1)
    assert S.factor(commute[:,[0,2]].det())==-(q-1)**2*(q+1)**2/q**4
    # At q=-1, the centralizer of ANY nonzero linear form has quadratic
    # part <x²,y²>; the anticommuting part is k*xy.
    assert commute.subs(q,-1)==S.Matrix([[0,-2,0],[0,2,0]])
    # Non-normal linear form: anticommutation forces A=C=0, then B=0
    # unless q=-1.  For a quantum axis, q²=-1 is the only extra case.
    anti_middle=S.Matrix([1/q+1,1+1/q])
    assert all(S.cancel(z.subs(q,-1))==0 for z in anti_middle)
    anti_axis=S.diag(2,1+1/q,1+1/q**2)
    assert S.cancel(anti_axis.det()-2*(q+1)*(q*q+1)/q**3)==0
    # Jordan plane vu=uv+kappa*v², normal axis v.
    kap=S.symbols('kappa',nonzero=True)
    centralizer_u=S.Matrix([[0,kap,0],[0,0,2*kap]])
    centralizer_v=S.Matrix([[-2*kap,0,0],[-2*kap**2,-kap,0]])
    assert centralizer_u.rank()==centralizer_v.rank()==2
    mu=[-1,-1,-1,1] # two W coordinates, v, p
    fixed=[w for w in itertools.product(range(4),repeat=3) if S.prod(mu[j] for j in w)==1]
    assert all(w.count(3)%2==1 for w in fixed)
    # Common commutative plane, zero outer fourth coefficient:
    # normal ell has eigenvalues (1,1,-1,+-i), and G must have eigenvalue -1.
    for phase in [S.I,-S.I]:
        weights=[1,1,-1,phase]
        assert all(S.prod(weights[j] for j in w)!=-1 for w in fixed)
    # Common commutative plane, nonzero outer fourth coefficient:
    # ell² fixes W,v and negates p, whereas G must commute with ell².
    weights=[1,1,1,-1]
    assert all(S.prod(weights[j] for j in w)==-1 for w in fixed)
    # Primitive-fourth quantum exception: normal y² has no fixed mu-fixed cubic.
    for phase in [S.I,-S.I]:
        weights=[-1,1,-1,-phase]
        assert all(S.prod(weights[j] for j in w)!=1 for w in fixed)
    # At q=-1 the positive cross sign would give a normal quadratic
    # that anticommutes with ALL four generators.
    assert all((-1)**len(w)==-1 for w in fixed)
    data={
      'hypotheses':'all H3 envelopes with Nakayama multiplicities(1,3), no normal-coordinate assumption',
      'result':'The canonical common AS2 plane is xy=-yx, and p acts on its axes by opposite signs. The two axis squares and the remaining negative-generator square are central in B.',
      'top_reduction':['if w_vvvv=0, a W-translation makes {v,ell}=0 and v² in T2',
                       'if w_vvvv!=0, a W-translation makes the v³W coefficients zero; cyclic rank-one mixed flattening gives v²=c*ell² and vell-lambda*ellv=q2(W), lambda=+-1',
                       'all lambda=+1 cases and all common planes other than q=-1 are excluded by AS2 centralizers or incompatible normal-quadratic weights'],
      'linear_algebra':'zero-fourth case cross block H=r*k^t+k*r^t; equality of cyclic diagonal blocks forces k_left=k_right, allowing the W-translation',
      'remaining_charts':['zero fourth: {v,ell}=0, v²=h(x²,y²) independent of ell²',
                          'nonzero fourth: v²=c*ell², {v,ell}=q2(x²,y²) independent of ell²'],
      'scope':'Exact block-matrix, binary centralizer and sign/weight identities checked. The rank-four Schur reduction and global case analysis are structural proofs in the manuscript. These constraints do not prove a common axis is normal or complete H3 coverage/admissibility.'}
    path=Path(__file__).with_name('cubic_order2_global_common_plane_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS global common-plane cyclic blocks, AS2 centralizers and normalizer weights')


if __name__=='__main__':main()
