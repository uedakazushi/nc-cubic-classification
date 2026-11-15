#!/usr/bin/env python3
"""Replay a polynomial rank certificate for T central cubics over QQ[l]."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_T_projections import verify
from verify_cubic_pym_generic import words


def main():
    free4,P,Q,D,DI=verify(4);l=S.symbols('l');ii=S.symbols('ii');K=P.domain
    # Use all 64 cubic words, so no degree-three basis choice introduces poles.
    pd,qd=P.to_dok(),Q.to_dok();ix={v:j for j,v in enumerate(words(4))};cr={};ci={}
    for j,v in enumerate(words(3)):
        for g in range(4):
            a,b=ix[v+(g,)],ix[(g,)+v]
            for r in range(35):
                for source,out in [(pd,cr),(qd,ci)]:
                    x=source.get((r,a),K.zero)-source.get((r,b),K.zero)
                    if x:out[j,35*g+r]=x
    CR=DomainMatrix.from_dok(cr,(64,140),K);CI=DomainMatrix.from_dok(ci,(64,140),K)
    data=json.loads(Path(__file__).with_name('cubic_as4_T_centre_lift.json').read_text())
    def load(key,shape):
        re={};im={}
        for r,c,e in data[key]:
            z=S.Poly(S.sympify(e.replace('^','**'),locals={'l':l,'ii':ii}),ii,domain=K)
            assert z.degree()<=1
            a=z.rep.to_dict().get((0,),K.zero);b=z.rep.to_dict().get((1,),K.zero)
            if a:re[r,c]=a
            if b:im[r,c]=b
        return DomainMatrix.from_dok(re,shape,K),DomainMatrix.from_dok(im,shape,K)
    # Strip only column factors dividing the already verified complex D4.
    G=S.QQ_I.poly_ring(l);DG=G.from_sympy(K.to_sympy(D)+S.I*K.to_sympy(DI))
    scales={int(c):G.from_sympy(S.sympify(e,locals={'l':l})) for c,e in data['column_scales'].items()}
    assert set(scales)==set(range(140))
    for h in scales.values():assert h and not divmod(DG,h)[1]
    rr={};ri={}
    for ij in cr.keys()|ci.keys():
        z=G.from_sympy(K.to_sympy(cr.get(ij,K.zero))+S.I*K.to_sympy(ci.get(ij,K.zero))).exquo(scales[ij[1]])
        ar={m:c.x for m,c in z.to_dict().items() if c.x};ai={m:c.y for m,c in z.to_dict().items() if c.y}
        if ar:rr[ij]=K.ring.from_dict(ar)
        if ai:ri[ij]=K.ring.from_dict(ai)
    CR=DomainMatrix.from_dok(rr,(64,140),K);CI=DomainMatrix.from_dok(ri,(64,140),K)
    NR,NI=load('N',(64,20));XR,XI=load('X',(140,20))
    assert (CR*XR-CI*XI-NR).is_zero_matrix
    assert (CR*XI+CI*XR-NI).is_zero_matrix
    piv=dict(data['pivots']);assert set(piv)==set(range(20)) and len(set(piv.values()))==20 and all(0<=p<64 for p in piv.values())
    nr,ni=NR.to_dok(),NI.to_dok();G=S.QQ_I.poly_ring(l)
    allowed=[l,l+1,l+2,l+1-S.I,l+1+S.I,l*l+(-1+3*S.I)*l-2+2*S.I,l*l+(1-3*S.I)*l-4*S.I,l*l+(2-4*S.I)*l-4*S.I]
    supports=set()
    for j,p in piv.items():
        for r in range(p):assert not nr.get((r,j),K.zero) and not ni.get((r,j),K.zero)
        e=G.from_sympy(K.to_sympy(nr.get((p,j),K.zero))+S.I*K.to_sympy(ni.get((p,j),K.zero)));assert e
        for factor in allowed:
            f=G.from_sympy(factor)
            while True:
                quo,rem=divmod(e,f)
                if rem:break
                e=quo;supports.add(str(factor))
        assert e.degree()==0,('unhandled pivot factor',G.to_sympy(e))
    a,b,c=allowed[-3:];H=a*b*c;f=-l/(l+1)
    num=S.fraction(S.cancel(H.subs(l,f)))[0]
    assert S.gcd(S.Poly(H,l,extension=S.I),S.Poly(num,l,extension=S.I)).degree()==0
    print('PASS independent polynomial C*X=N; 20 triangular pivots supported on',sorted(supports),flush=True)
    print('PASS artificial complex pole factors disjoint from their involution transport',flush=True)

if __name__=='__main__':main()
