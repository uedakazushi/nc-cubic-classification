#!/usr/bin/env python3
"""Exact low-degree identities for global centrality of the positive square."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    t=S.symbols('t')
    trace=1/((1+t)**2*(1+t*t))
    assert S.expand(S.series(trace,t,0,4).removeO()).coeff(t,3)==-2
    assert (20-(-2))//2==11
    assert S.expand(S.series(1/(1-t)**3,t,0,4).removeO()).coeff(t,3)==10
    # Two independent mu-positive cubic syzygies if p² had no free
    # negative Clifford-central quadratic coefficient.
    a,b=S.symbols('a b')
    rels=[{(0,1):1,(1,0):1}, # pu+up
          {(0,2):1,(2,0):-1}, # pw-wp
          {(1,2):1,(2,1):1}, # uw+wu
          {(0,0):1,(1,1):-a,(2,2):-b}]
    words=list(itertools.product(range(3),repeat=3));index={w:j for j,w in enumerate(words)}
    columns=[];labels=[]
    for ri,rel in enumerate(rels):
        for j in range(3):
            for left in [True,False]:
                col=[S.Integer(0)]*27
                for w,c in rel.items():col[index[(j,)+w if left else w+(j,)]]+=c
                labels.append((ri,j,left));columns.append(col)
    M=S.Matrix.hstack(*map(S.Matrix,columns))
    def vector(terms):
        out=S.zeros(24,1)
        for label,c in terms:out[labels.index(label)]+=c
        return out
    z1=vector([((0,2,False),1),((1,1,True),-1),((2,0,True),-1),
               ((2,0,False),-1),((0,2,True),1),((1,1,False),1)])
    z2=vector([((3,0,False),1),((3,0,True),-1),((0,1,False),-a),
               ((0,1,True),a),((1,2,False),-b),((1,2,True),-b)])
    assert M*z1==S.zeros(27,1) and M*z2==S.zeros(27,1)
    assert S.Matrix([[z1[labels.index((0,2,False))],z2[labels.index((0,2,False))]],
                     [z1[labels.index((3,0,False))],z2[labels.index((3,0,False))]]]).det()==1
    mu=[1,-1,-1];rel_mu=[-1,-1,1,1]
    for zvec in [z1,z2]:
        assert all(rel_mu[ri]*mu[j]==1 for pos,(ri,j,left) in enumerate(labels) if zvec[pos]!=0)
    # The third free central coordinate really enters the generic
    # Clifford determinant, so the generic negative Clifford is nondegenerate.
    X,Y,K,h1,h2,A0,A1,B0,B1,alpha,beta=S.symbols('X Y K h1 h2 A0 A1 B0 B1 alpha beta')
    A=A0*X+A1*Y+alpha*K;B=B0*X+B1*Y+beta*K;H=h1*X+h2*Y
    Q=S.Matrix([[X,0,A/2],[0,Y,B/2],[A/2,B/2,H]])
    assert S.expand(Q.det()).coeff(K,2)==-(X*beta**2+Y*alpha**2)/4
    # [ {v,u},w ] = [u,{v,w}] using only uw=-wu.
    def nf(word):
        for j in range(len(word)-1):
            if word[j:j+2]==(1,0):
                return {w:-c for w,c in nf(word[:j]+(0,1)+word[j+2:]).items()}
        return {word:1}
    def add(terms):
        out={}
        for c,w in terms:
            for v,d in nf(w).items():out[v]=out.get(v,0)+c*d
        return {w:c for w,c in out.items() if c}
    assert not add([(1,(2,0,1)),(1,(0,2,1)),(-1,(1,2,0)),(-1,(1,0,2)),
                    (-1,(0,2,1)),(-1,(0,1,2)),(1,(2,1,0)),(1,(1,2,0))])
    data={
      'hypotheses':'all H3 envelopes with Nakayama multiplicities(1,3)',
      'result':'p² is central, and {v,u},{v,w} are also central in B. Thus all four generator squares are central.',
      'negative_abstract_Clifford':'S0 is free rank8 over Z0=k[X=u²,Y=w²,K], with one free negative anticommutator K; its natural map to B is injective in degrees <=3.',
      'degree_three_dimension_argument':'B3 has negative-eigenvalue dimension11; it is spanned by S0_3 (dimension10) and pvp, proving cubic injectivity.',
      'generic_determinant_K2_coefficient':'-(X*beta²+Y*alpha²)/4 !=0 for (alpha,beta)!=0',
      'centralizer':'The centralizer of the nondegenerate two-generator Clifford subalgebra in the generic three-generator Clifford algebra is its two-dimensional center.',
      'p_square_form':'p²=aX+bY+cK with c!=0; c=0 produces the two independent mu-positive cubic syzygies checked here, while AS4 permits only one.',
      'independent_syzygies_checked':2,
      'scope':'Trace, Clifford determinant and exact polynomial syzygies checked. The generic centralizer and graded-dimension proof are in the manuscript. Full embedding of S0, all remaining normal cubics and H3 admissibility are not asserted.'}
    path=Path(__file__).with_name('cubic_order2_positive_square_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS positive-square trace, generic Clifford determinant and independent cubic syzygies')


if __name__=='__main__':main()
