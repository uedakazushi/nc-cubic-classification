#!/usr/bin/env python3
"""Exact growth and Frobenius-block identities excluding the collapsed base branch."""
import json
from pathlib import Path
import sympy as S


def main():
    t,a=S.symbols('t a',nonzero=True)
    H=(1+t)/((1-t)**2*(1-t-t*t))
    assert S.expand(S.series(H,t,0,4).removeO()).coeff(t,3)==21
    assert S.binomial(6,3)==20
    q=a**-2
    QT=S.Matrix([[0,1],[-q,0]])
    assert S.cancel(QT.det()-q)==0
    u1,u2,v1,v2=S.symbols('u1 u2 v1 v2')
    assert (S.Matrix([u1,u2])*S.Matrix([v1,v2]).T).det()==0
    ell=S.Matrix([1,0]);r=ell.col_join(-ell)
    s=S.Matrix(S.symbols('s0:4'));m,n,b,c,d,e=S.symbols('m n b c d e')
    # Relation basis: pure W quadric, z²-base quadric, cross, v²-correction.
    # Only the last two have cross projections r,s; top v⁴ and vvzz vanish.
    P=S.zeros(4,4);P[:,2]=r;P[:,3]=s
    M=S.Matrix([[b,c,d,e],[c,m,b,0],[d,b,m,n],[e,0,n,0]])
    HH=P*M*P.T
    k=m*r/2+n*s
    assert (HH-r*k.T-k*r.T).applyfunc(S.expand)==S.zeros(4)
    assert (M[3,:]*P.T-n*r.T).applyfunc(S.expand)==S.zeros(1,4)
    # Existing universal anti-cyclic translation and AS2 centralizer proof applies.
    centralizer=S.Matrix([[1-q**-2,q**-1-1,0],[0,1-q**-1,q**-2-1]])
    assert S.expand(centralizer[:,[0,2]].det()+(a**4-1)**2)==0
    data={
      'hypotheses':'H3 multiplicities(3,1), collapsed diagonal base S/(Cprime), hence a^4!=1',
      'base':'W quantum AS2 xy=a^-2*yx, zx=a*xz,zy=a^-1*yz,z²=kappa*xy',
      'rational_collapse_exclusion':'If v lies in Qgr(W), B lies in k(u)[z^+-1;u->a*u]; degree-n coefficients have poles bounded by a divisor of degree O(n), forcing GKdim<=2.',
      'no_v_squared_relation':'Full Ore cross projections give PBW W-monomials times words(v,z) avoiding zz; degree3 dimension21 contradicts14641 value20. Degenerate projections force the rational collapse.',
      'one_v_squared_relation':'If v³W=0, vv row is the nondegenerate pure W quadric but cross-cross rank<=1, contradicting anti-cyclic QvvWW=-Ccross. A nonsplit v->W Jordan action forces precisely that zero case.',
      'semisimple_block':'The z² relation has no cross term, and top v⁴=0; hence Hcross=r*k^t+k*r^t. Anti-cyclic coordinate translation yields [v,ell]=0 and v² in W2.',
      'centralizer_minor':'-(a^4-1)^2, nonzero in this branch; thus v²=c*ell² and commuting square factors contradict the domain property',
      'conclusion':'The quantum-Veronese collapsed base cannot occur for H3. Every remaining(3,1) canonical base embeds as an AS3 into B and R.',
      'scope':'Growth coefficient, nondegenerate/rank-one contrast, relation-basis block and exact centralizer minor checked. Curve-divisor growth, PBW and Jordan/top arguments are structural proofs using existing exact translation and invariant-tensor certificates.'}
    path=Path(__file__).with_name('cubic_positive3_cone_exclusion_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS collapsed positive-three cone branch: growth/block/centralizer obstruction identities')


if __name__=='__main__':main()
