#!/usr/bin/env python3
"""Generic central quadrics, three exact sign transports and four disjoint loci."""
import json
from pathlib import Path
from functools import reduce
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_stafford_resonance import graded_projections


def relations(a,b,c):
    fs=[]
    for (i,j,k),v in zip([(1,2,3),(2,3,1),(3,1,2)],[a,b,c]):
        fs += [{(0,i):1,(i,0):-1,(j,k):-v,(k,j):-v},
               {(0,i):1,(i,0):1,(j,k):-1,(k,j):1}]
    return fs


def main():
    a,b=S.symbols('a b');c=-(a+b)/(1+a*b);field=S.QQ.frac_field(a,b)
    fs=relations(a,b,c);degree=lambda w:reduce(int.__xor__,w,0)
    g1={(0,0):-1,(1,1):1,(2,2):1,(3,3):1}
    g2={(1,1):1,(2,2):(1+a)/(1-b),(3,3):(1-a)/(1+c)}
    for omit,signs in [(0,[-1,-1,1,1]),(1,[1,1,-1,-1])]:
        pp,dims=graded_projections(fs[:omit]+fs[omit+1:],field,(3,))
        for q,ss in [(g1,[1]*4),(g2,[1]*4),(fs[omit],signs)]:
            for i in range(4):
                out=S.zeros(len(next(iter(pp[3][degree(next(iter(q)))^i].values()))),1)
                for w,v in q.items():out+=v*(pp[3][degree(w)^i][w+(i,)]-ss[i]*pp[3][degree(w)^i][(i,)+w])
                assert DomainMatrix.from_Matrix(out).convert_to(field).is_zero_matrix
        print('PASS generic five-relation central/normal quadrics',omit+1,flush=True)
    # Exact relation transport including both odd/even positions.
    r,s=S.symbols('r s');u=r*r;v=s*s;third=-(u+v)/(1+u*v)
    cases=[(1,(third,u,v),[1,1,-1,-1],[1,-S.I*r*s,S.I*s,r]),
           (2,(u,third,v),[1,-1,1,-1],[1,s,-S.I*s*r,S.I*r]),
           (3,(u,v,third),[1,-1,-1,1],[1,S.I*s,r,-S.I*r*s])]
    matching=[]
    for h,params,ep,sc in cases:
        old=relations(*params)
        newparams=tuple(x if i==h-1 else 1/x for i,x in enumerate(params))
        tw=[{(i,j):S.cancel(z*ep[j]) for (i,j),z in row.items()} for row in old]
        new=[{(i,j):S.cancel(z*sc[i]*sc[j]) for (i,j),z in row.items()} for row in relations(*newparams)]
        permutation=[]
        for row in new:
            found=[]
            for j,target in enumerate(tw):
                pivot=next(iter(target));ratio=S.cancel(row.get(pivot,0)/target[pivot])
                if ratio and all(S.cancel(row.get(w,0)-ratio*target.get(w,0))==0 for w in set(row)|set(target)):found.append(j)
            assert len(found)==1
            permutation.append(found[0])
        assert len(set(permutation))==6
        assert permutation[:2]==([0,1] if h==1 else [1,0])
        matching.append(permutation)
    d=S.Symbol('d');A=(1+a)/(1-b);C=(1-a)/(1+c)
    params=[(a,1/b,1/c),(1/a,b,1/c),(1/a,1/b,c)]
    ep=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
    sq=[[1,-b*c,-c,b],[1,c,-a*c,-a],[1,-b,a,-a*b]]
    shift=[-1-b*c,-1-c,b-1];slope=[-b*c,-c,b]
    maps=[-(d+1+b*c)/(b*c),-(d+1+c)/c,(d-b+1)/b]
    for h,(aa,bb,cc) in enumerate(params):
        old1=S.Matrix([-1,1,1,1]).multiply_elementwise(S.Matrix(ep[h]))
        old2=S.Matrix([0,1,A,C]).multiply_elementwise(S.Matrix(ep[h]))
        new1=S.Matrix([-1,1,1,1]).multiply_elementwise(S.Matrix(sq[h]))
        new2=S.Matrix([0,1,(1+aa)/(1-bb),(1-aa)/(1+cc)]).multiply_elementwise(S.Matrix(sq[h]))
        assert all(S.cancel(z)==0 for z in new1-old1-shift[h]*old2)
        assert all(S.cancel(z)==0 for z in new2-slope[h]*old2)
        assert S.cancel(shift[h]+slope[h]*maps[h]-d)==0
        for odd in [False,True]:
            oldbad=[0,-1-b*c] if odd else [b-1,-1-c]
            targetodd=odd if h==0 else not odd
            newbad=[0,-1-bb*cc] if targetodd else [bb-1,-1-cc]
            images=[S.cancel(maps[h].subs(d,x)) for x in oldbad]
            assert all(any(S.cancel(y-z)==0 for z in newbad) for y in images)
    loci=[a*b+a-b+3,a*b+a+3*b-1,a*b-3*a-b-1,3*a*b-a+b+1]
    transforms=[params[0],(a,b,c),params[2],params[1]]
    for f,pp in zip(loci,transforms):
        aa,bb,cc=pp;ratio=S.factor(S.cancel((aa*bb+aa+3*bb-1)/f))
        assert ratio in [1,1/b,-1/(a*b),1/a]
    z=S.Symbol('z');unit=a*b*(a*a-1)*(b*b-1)*(a+b)*(1+a*b)
    from itertools import combinations
    for f,g in combinations(loci,2):
        gb=S.groebner([f,g,z*unit-1],z,a,b)
        assert len(gb.polys)==1 and gb.polys[0].as_expr()==1
    cert={'version':'classification-v68','field':'QQ(a,b)',
          'central_normal_quadratic_equations':24,'sign_relation_permutations':matching,
          'pencil_maps':list(map(str,maps)),'cocycle_centre_loci_group_0_1_2_3':list(map(str,loci)),
          'pairwise_disjoint_on_T':True,
          'scope':'Exact identities and forbidden-parameter transport. Paper supplies all-special flatness, W1 transport, factorization and proper elliptic hypotheses.'}
    Path(__file__).with_name('cubic_stafford_transport_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all sign relations, pencils, forbidden values and four pairwise disjoint centre loci')


if __name__=='__main__':main()
