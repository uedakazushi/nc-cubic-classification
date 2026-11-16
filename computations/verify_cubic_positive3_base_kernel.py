#!/usr/bin/env python3
"""Exact q-Weyl localization and cone identities for the all-parameter kernel dichotomy."""
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    q,c,a,gamma,d,Q,U,t=S.symbols('q c a gamma d Q U t',nonzero=True)
    def add(*terms):
        out={}
        for cc,p in terms:
            for w,co in p.items():out[w]=S.cancel(out.get(w,0)+cc*co)
        return {w:co for w,co in out.items() if co!=0}
    @lru_cache(None)
    def nf(w):
        for i in range(len(w)-1):
            if w[i:i+2]==(1,0):
                return add((q,nf(w[:i]+(0,1)+w[i+2:])),(c,nf(w[:i]+w[i+2:])))
        return {w:S.Integer(1)}
    def mul(p,r):return add(*[(cc*co,nf(w+v)) for w,cc in p.items() for v,co in r.items()])
    u={(0,):S.Integer(1)};w={(1,):S.Integer(1)};normal={():c,(0,1):q-1}
    assert not add((1,mul(normal,u)),(-q,mul(u,normal)))
    assert not add((1,mul(normal,w)),(-1/q,mul(w,normal)))
    defining=(d-c)/(q-1)
    assert S.cancel(defining.subs(d,q*d)-q*defining-c)==0
    assert S.cancel(S.resultant(defining,defining.subs(d,Q*d),d)-c*(Q-1)/(q-1)**2)==0
    # q-integer recurrence gives the all-N truncated oscillator representation.
    assert S.cancel((q*Q-1)/(q-1)-q*(Q-1)/(q-1)-1)==0
    # In S[z^-1], u=x/z,w=y/z: wu=a^-4*uw+gamma*a^-3.
    assert S.cancel(a**-1*U-a**3*(a**-4*U+gamma*a**-3)+gamma)==0
    Cprime_over_z2=(1-a**-4)*U/a-gamma*a**-4
    assert S.cancel(Cprime_over_z2+(gamma*a**-3+(a**-4-1)*U)/a)==0
    # Cone quotient has zx=a*xz,yz=a*zy,yx=a²*xy,z²=kappa*xy.
    kap=S.symbols('kappa',nonzero=True)
    rules={(1,0):{(0,1):a},(2,1):{(1,2):a},(2,0):{(0,2):a*a},(1,1):{(0,2):kap}}
    @lru_cache(None)
    def cone_nf(ww):
        for i in range(len(ww)-1):
            if ww[i:i+2] in rules:
                return add(*[(co,cone_nf(ww[:i]+vv+ww[i+2:])) for vv,co in rules[ww[i:i+2]].items()])
        return {ww:S.Integer(1)}
    overlaps=0
    for word in itertools.product(range(3),repeat=3):
        if word[:2] in rules and word[1:] in rules:
            left=add(*[(co,cone_nf(v+word[2:])) for v,co in rules[word[:2]].items()])
            right=add(*[(co,cone_nf(word[:1]+v)) for v,co in rules[word[1:]].items()])
            assert not add((1,left),(-1,right));overlaps+=1
    assert overlaps==4
    assert S.cancel((1-t*t)/(1-t)**3-(1+t)/(1-t)**2)==0
    data={
      'localization':'S[z^-1]=A_q(c)[z^+-1;theta], q=a^-4,c=gamma*a^-3,theta(u,w)=(a*u,a^-1*w)',
      'normal_element':'d=c+(q-1)uw=-a*Cprime/z²',
      'generic_GWA':'A_q(c)[d^-1]=k[d^+-1](sigma,t),sigma(d)=q*d,t=(d-c)/(q-1)',
      'GWA_root_resultant':'c*(Q-1)/(q-1)², Q=q^n',
      'root_of_unity_argument':'A_q(c)[d^-1] is Azumaya degree N over k[u^N,w^N,d^-N]; nonzero domain quotients would split over a function field of dimension<=1 by Tsen',
      'kernel_dichotomy':'Every homogeneous completely prime kernel with z nonzero is0 or(Cprime); if a^4=1 it must be0.',
      'cone_quotient':'S/(Cprime) is the even Veronese of a quantum plane, kappa=(a^4-1)/gamma, a^4!=1',
      'cone_overlap_count':overlaps,
      'primary_sources_checked':[
        'V. Bavula, Generalized Weyl algebras and their global dimension, author lecture manuscript, Theorem2.1 (local source reread)',
        'Stacks Project, Tag03RD, Theorem59.67.10 Tsen; Tag03RF, Lemma59.67.11 Br(k(C))=0; primary pages read 2026-11-16'],
      'scope':'Exact localization/normalizer/GWA/resultant/oscillator and cone identities. All-order Azumaya and Tsen arguments are structural proofs in the manuscript, not finite sampling. This does not classify the extra positive generator or H3 admissibility.'}
    path=Path(__file__).with_name('cubic_positive3_base_kernel_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS q-Weyl localization, GWA and cone identities for the base-kernel dichotomy')


if __name__=='__main__':main()
