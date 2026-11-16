#!/usr/bin/env python3
"""Exact Jordan-Heisenberg PBW and differential localization for base injectivity."""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    kap,beta,gamma,u=S.symbols('kappa beta gamma u')
    records=[]
    for eps in [1,-1]:
        rules={(1,0):{(0,1):eps},
               (2,1):{(1,2):eps,(0,1):-eps*beta},
               (2,0):{(0,2):1,(0,0):kap,(1,1):gamma}}
        def add(*terms):
            out={}
            for cc,p in terms:
                for w,c in p.items():out[w]=S.expand(out.get(w,0)+cc*c)
            return {w:c for w,c in out.items() if c!=0}
        @lru_cache(None)
        def nf(w):
            for i in range(len(w)-1):
                if w[i:i+2] in rules:
                    return add(*[(cc,nf(w[:i]+v+w[i+2:])) for v,cc in rules[w[i:i+2]].items()])
            return {w:S.Integer(1)}
        count=0
        for word in itertools.product(range(3),repeat=3):
            if word[:2] in rules and word[1:] in rules:
                left=add(*[(cc,nf(v+word[2:])) for v,cc in rules[word[:2]].items()])
                right=add(*[(cc,nf(word[:1]+v)) for v,cc in rules[word[1:]].items()])
                assert not add((1,left),(-1,right));count+=1
        assert count==1
        assert nf((2,1,0))=={(0,1,2):S.Integer(1),(0,0,1):eps*kap-beta,(1,1,1):eps*gamma}
        lam=kap+eps*beta;f=lam*u*u+eps*gamma
        # Reverse substitution x=u*z,y=v*z, theta(u,v)=(eps*u,eps*v+beta*u).
        assert S.expand(eps*lam-beta-eps*kap)==0
        assert S.expand(f.subs(u,eps*u)-f)==0
        assert S.expand(S.discriminant(f,u)+4*eps*gamma*lam)==0
        records.append({'epsilon':eps,'overlap_count':count,'delta_of_u':str(f),
                        'quadratic_discriminant':str(S.factor(S.discriminant(f,u)))})
    data={
      'presentation':['yx=xy+kappa*x²+gamma*z²','zx=epsilon*xz','zy=epsilon*yz+beta*xz'],
      'hypotheses':'gamma!=0,epsilon²=1; kappa and beta arbitrary; algebraically closed characteristic-zero field',
      'PBW':'x^i*z^j*y^k; quadratic Koszul noetherian AS3 domain',
      'checks':records,
      'localized_degree_zero':'k[u][v;delta], u=x/z,v=y/z, delta(u)=(kappa+epsilon*beta)*u²+epsilon*gamma',
      'localized_grading_action':'theta(u,v)=(epsilon*u,epsilon*v+beta*u)',
      'domain_kernel_argument':'A[delta(u)^-1] simple by minimal v-degree and differential-simple localized base. A nonzero completely prime quotient forces u=r at a root of delta, hence x=r*z.',
      'conclusion':'Every graded map to a domain with linearly independent images of x,z is injective.',
      'scope':'Exact PBW and localization identities; differential simplicity and all-kernel implication are structural proofs. The additional positive generator and H3 admissibility remain unclassified.'}
    path=Path(__file__).with_name('cubic_positive3_Jordan_base_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS Jordan base PBW, differential localization and the injectivity obstruction identities')


if __name__=='__main__':main()
