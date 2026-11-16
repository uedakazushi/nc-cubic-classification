#!/usr/bin/env python3
"""Exact finite arithmetic behind the order-two mixed-relation trace reduction."""
import json
from pathlib import Path
import sympy as S


def main():
    t=S.Symbol('t')
    rows=[]
    for p,q in [(3,1),(1,3),(2,2)]:
        bound=3 if min(p,q)==1 else 5
        candidates=list(range(0,bound+1,2))
        s=p-q
        assert s*s-16<0  # r=0 gives no real t+1/t on the unit circle.
        for r in candidates:
            denominator=1-s*t+(6-2*r)*t*t-s*t**3+t**4
            assert S.expand(t**4*denominator.subs(t,1/t)-denominator)==0
            if r==0:
                continue
            if s==2:
                expected=(1-t)**2*(1+t*t)
            elif s==-2:
                expected=(1+t)**2*(1+t*t)
            elif r==2:
                expected=(1+t*t)**2
            else:
                assert r==4
                expected=(1-t*t)**2
            assert S.expand(denominator-expected)==0
            rows.append({'multiplicities':[p,q],'odd_relation_dimension':r,'trace_denominator':str(expected)})
    assert len(rows)==4
    a,b,c,d=S.symbols('a b c d')
    F=S.Matrix([[a,b],[c,d]])
    J=S.Matrix([[0,1],[-1,0]])
    assert (F*J*F.T-F.det()*J).applyfunc(S.expand)==S.zeros(2)
    data={'rows':rows,'one_dimensional_sector':'Mixed relations preserve a common 2-plane W; z*w=f(w)*z and det(f)=epsilon, the eigenvalue on the three-dimensional block. This includes all Jordan parts.','scope':'Necessary conditions including all Jordan parts. Frobenius parity, domain projection bounds and polynomial-growth exclusion are proved in the manuscript, not by finite sampling.'}
    path=Path(__file__).with_name('cubic_order2_mixed_rank_certificate.json')
    if path.exists():
        assert json.loads(path.read_text())==data
    else:
        path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS four exact trace denominators and excluded rank-zero discriminants')


if __name__=='__main__':
    main()
