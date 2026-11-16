#!/usr/bin/env python3
"""Exact quadratic Heisenberg base and its embedded cubic CY down-up subalgebra."""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    a,gamma,t=S.symbols('a gamma t',nonzero=True)
    # Ordered basis x<z<y, z degree1.
    rules={(1,0):{(0,1):a},(2,1):{(1,2):a},
           (2,0):{(0,2):a**-2,(1,1):gamma*a**-2}}
    def add(*terms):
        out={}
        for cc,p in terms:
            for w,c in p.items():out[w]=S.cancel(out.get(w,0)+cc*c)
        return {w:c for w,c in out.items() if c!=0}
    def reducer(rules):
        @lru_cache(None)
        def nf(w):
            for j in range(len(w)-1):
                if w[j:j+2] in rules:
                    return add(*[(cc,nf(w[:j]+v+w[j+2:])) for v,cc in rules[w[j:j+2]].items()])
            return {w:S.Integer(1)}
        return nf
    def overlaps(rules,nf):
        count=0
        for w in itertools.product(range(3),repeat=3):
            if w[:2] in rules and w[1:] in rules:
                left=add(*[(cc,nf(v+w[2:])) for v,cc in rules[w[:2]].items()])
                right=add(*[(cc,nf(w[:1]+v)) for v,cc in rules[w[1:]].items()])
                assert not add((1,left),(-1,right));count+=1
        return count
    nf=reducer(rules);count=overlaps(rules,nf)
    # Quadratic AS3 cubic top in coordinates x,z,y. The cyclic convention
    # uses the inverse of the actual Nakayama, which is (a*x,z,a^-1*y).
    top={(2,1,0):1,(1,2,0):-a,(2,0,1):-a,
         (0,2,1):a**-1,(1,0,2):a**-1,(0,1,2):-1,(1,1,1):gamma/a}
    for pos in [0,1]:
        out={}
        for w,cc in top.items():
            for v,c in nf(w[pos:pos+2]).items():
                ww=w[:pos]+v+w[pos+2:];out[ww]=S.cancel(out.get(ww,0)+cc*c)
        assert not any(out.values())
    inverse_mu=[1/a,1,a]
    rotated={w[1:]+w[:1]:cc for w,cc in top.items()}
    right={w:S.cancel(cc*inverse_mu[w[-1]]) for w,cc in top.items()}
    assert all(S.cancel(rotated.get(w,0)-right.get(w,0))==0 for w in set(rotated)|set(right))
    # C=xy-a²yx=-gamma*z² has degree2. Ordered weighted Ore basis x<C<y.
    weighted_rules={(1,0):{(0,1):a*a},(2,1):{(1,2):a*a},
                    (2,0):{(0,2):a**-2,(1,): -a**-2}}
    nt=reducer(weighted_rules);countT=overlaps(weighted_rules,nt)
    # Elimination gives the two cubic quantum-Serre relations.
    alpha=a*a+a**-2
    cubic1={(0,0,2):1,(0,2,0):-alpha,(2,0,0):1}
    cubic2={(2,2,0):1,(2,0,2):-alpha,(0,2,2):1}
    assert not add(*[(cc,nt(w)) for w,cc in cubic1.items()])
    assert not add(*[(cc,nt(w)) for w,cc in cubic2.items()])
    # Ordinary cyclic quartic top x*r_y+y*r_x=r_y*x+r_x*y.
    topT={(0,2,2,0):1,(0,0,2,2):1,(2,0,0,2):1,(2,2,0,0):1,
          (0,2,0,2):-alpha,(2,0,2,0):-alpha}
    assert {w[1:]+w[:1]:cc for w,cc in topT.items()}==topT
    assert not add((1,topT),(-1,add(*[(cc,{(0,)+w:S.Integer(1)}) for w,cc in cubic2.items()],
                    *[(cc,{(2,)+w:S.Integer(1)}) for w,cc in cubic1.items()])))
    assert not add((1,topT),(-1,add(*[(cc,{w+(0,):S.Integer(1)}) for w,cc in cubic2.items()],
                    *[(cc,{w+(2,):S.Integer(1)}) for w,cc in cubic1.items()])))
    Cprime=add((1,nt((0,2))),(-a**-2,nt((2,0))))
    def mt(p,q):return add(*[(cc*dd,nt(w+v)) for w,cc in p.items() for v,dd in q.items()])
    for gen,weight in [(0,a**-2),(2,a*a)]:
        gg={(gen,):S.Integer(1)}
        assert not add((1,mt(Cprime,gg)),(-weight,mt(gg,Cprime)))
        product=mt({(1,):S.Integer(1)},Cprime)
        assert not add((1,mt(product,gg)),(-1,mt(gg,product)))
    assert S.cancel((1+t)/((1-t)**2*(1-t*t))-(1-t)**-3)==0
    data={
      'hypotheses':'a!=0,gamma!=0; abstract canonical semisimple positive-three common-plane base',
      'quadratic_base':['xy-a²*yx+gamma*z²=0','zx=a*xz','zy=a^-1*yz'],
      'quadratic_PBW':'x^i*z^j*y^k','quadratic_overlap_count':count,
      'quadratic_actual_Nakayama':'(x,z,y)->(a*x,z,a^-1*y)',
      'cubic_subalgebra':'T=<x,y>, C=xy-a²*yx=-gamma*z²; basis x^i*C^j*y^k',
      'cubic_relations':['x²y-(a²+a^-2)xyx+yx²=0','y²x-(a²+a^-2)yxy+xy²=0'],
      'weighted_Ore_relations':['Cx=a²*xC','yC=a²*Cy','yx=a^-2*xy-a^-2*C'],
      'weighted_overlap_count':countT,
      'cubic_regular_structure':'noetherian cubic AS3, resolution type(1,2,2,1), AS index4, actual Nakayama=id',
      'root_extension':'S=T direct_sum T*z, z*t=f(t)*z, f(x,y)=(a*x,a^-1*y), z²=-C/gamma',
      'inverse_normal_quadric':'Cprime=xy-a^-2*yx; Cprime normalizes W by f^-2; C*Cprime is central degree4',
      'scope':'All rewriting overlaps, both cubic relations, quadratic Koszul top and inverse-actual-Nakayama convention, cyclic quartic top and Hilbert identity checked. Embedding of these abstract bases into every H3 envelope has not been proved.'}
    path=Path(__file__).with_name('cubic_positive3_nonzero_gamma_base_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS gamma-nonzero quadratic base, embedded cubic CY base, and rank-two root extension')


if __name__=='__main__':main()
