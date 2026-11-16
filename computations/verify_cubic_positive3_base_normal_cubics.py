#!/usr/bin/env python3
"""Complete sign-normalizing cubic kernel inside the gamma-nonzero diagonal base."""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    a=S.symbols('a',nonzero=True)
    # gamma is scaled to1; over the specified algebraically closed field this
    # covers every nonzero gamma and preserves the sign-normalizer.
    rules={(1,0):{(0,1):a},(2,1):{(1,2):a},
           (2,0):{(0,2):a**-2,(1,1):a**-2}}
    def add(*terms):
        out={}
        for cc,p in terms:
            for w,c in p.items():out[w]=S.cancel(out.get(w,0)+cc*c)
        return {w:c for w,c in out.items() if c!=0}
    @lru_cache(None)
    def nf(w):
        for j in range(len(w)-1):
            if w[j:j+2] in rules:
                return add(*[(cc,nf(w[:j]+v+w[j+2:])) for v,cc in rules[w[j:j+2]].items()])
        return {w:S.Integer(1)}
    fixed=[tuple([0]*i+[1]*j+[2]*k) for i in range(4) for j in [0,2]
           for k in range(4) if i+j+k==3]
    assert len(fixed)==6
    for w in fixed:
        exponent=w.count(0)-w.count(2)
        phase=S.cancel(a**exponent+1).as_numer_denom()[0]
        assert S.rem(a**3+1,phase,a)==0
    # At a=-1 all six parity-fixed cubics are possible phases. The entire
    # commutator system with x,y has rational constant rank6.
    basis4=list(itertools.combinations_with_replacement(range(3),4));index={w:i for i,w in enumerate(basis4)}
    M=S.zeros(2*len(basis4),6)
    for j,w in enumerate(fixed):
        for gi,gg in enumerate([0,2]):
            out=add((1,nf(w+(gg,))),(-1,nf((gg,)+w)))
            for ww,cc in out.items():M[gi*len(basis4)+index[ww],j]=cc.subs(a,-1)
    rows=list(M.T.rref()[1]);minor=M.extract(rows,list(range(6)))
    assert len(rows)==6 and minor.det()!=0
    # At primitive sixth roots only x³,y³ have the required z-weight, and
    # both satisfy every defining normalizer equation modulo Phi6.
    phi=a*a-a+1
    assert S.gcd(a+1,phi)==1
    for w in [(0,0,0),(2,2,2)]:
        for gg,sign in enumerate([1,-1,1]):
            out=add((1,nf(w+(gg,))),(-sign,nf((gg,)+w)))
            assert all(S.rem(S.cancel(cc).as_numer_denom()[0],phi,a)==0 for cc in out.values())
    data={
      'base':'S=(xy-a²*yx+gamma*z²,zx-a*xz,zy-a^-1*yz), gamma!=0',
      'normalizer':'sigma(x,y,z)=(x,y,-z), not the actual Nakayama of S in general',
      'parity_fixed_cubic_dimension':6,
      'kernel':{'a²-a+1!=0':'0','a²-a+1=0':'span(x³,y³)'},
      'a_minus_one_exclusion':{'rank':6,'commutator_minor_rows':rows,'minor_determinant':str(minor.det())},
      'proof':'z-weight forces a³=-1; a=-1 is excluded by the constant full-rank minor; both remaining primitive-sixth-root cubes checked modulo Phi6',
      'scope':'Complete intrinsic sign-normalizer cubic kernel inside the ABSTRACT canonical base. This does not prove that the base embeds into every H3 envelope or that the H3 cubic lies in it, and is not whole (3,1) coverage.'}
    path=Path(__file__).with_name('cubic_positive3_base_normal_cubics_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS complete base sign-normalizing cubic kernel: only the primitive-sixth-root two-plane')


if __name__=='__main__':main()
