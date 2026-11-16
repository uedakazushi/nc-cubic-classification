#!/usr/bin/env python3
"""Exact matrix identities and calibration of the involution common-plane reduction."""
import json
from pathlib import Path
import sympy as S


def main():
    a,b,c,d,be=S.symbols('a b c d beta')
    F=S.Matrix([[a,b],[c,d]])
    J=S.Matrix([[0,1],[-1,0]])
    Q=J*F.T
    assert (F*J*F.T-F.det()*J).applyfunc(S.expand)==S.zeros(2)
    mu=-Q.T*Q.inv()
    assert (mu*F.det()-F**2).applyfunc(S.cancel)==S.zeros(2)
    M=S.Matrix([[1,1],[-1,0]])
    checks=[]
    for alpha in [S.Integer(1),S.Integer(-1),S.I,-S.I]:
        epsilon=alpha**2
        F=S.Matrix([[alpha,be],[0,alpha]])
        T=-epsilon*M.T*M.inv()
        Q=M*F.T
        assert T==epsilon*S.Matrix([[1,2],[0,1]])
        assert S.simplify(F*M*F.T-epsilon*M)==S.zeros(2)
        assert S.simplify(F*Q*F.T-epsilon*Q)==S.zeros(2)
        assert S.simplify(T*F-F*T)==S.zeros(2)
        assert S.simplify(-Q.T*Q.inv()-T*F**2)==S.zeros(2)
        checks.append({'alpha':str(alpha),'epsilon':str(epsilon),'Q':[[str(x) for x in row] for row in Q.tolist()]})
    # General trace(-1,-1) condition equals degeneracy of the symmetric part.
    M0=S.Matrix([[a,b],[c,d]])
    defect=S.cancel((S.trace(M0.T*M0.inv())+2)*M0.det())
    assert S.expand(defect-4*((M0+M0.T)/2).det())==0
    # Clifford swap: u=x-y, w=z+h(x+y)/2, s=t.
    h,bb,cc=S.symbols('h b c')
    def mul(u,v):
        out={}
        for i,x in u.items():
            for j,y in v.items():out[i,j]=out.get((i,j),0)+x*y
        return out
    def combine(*terms):
        out={}
        for scale,p in terms:
            for word,x in p.items():out[word]=S.expand(out.get(word,0)+scale*x)
        return {word:x for word,x in out.items() if x!=0}
    x={0:1};y={1:1};z={2:1};s={3:1}
    u={0:1,1:-1};w={2:1,0:h/2,1:h/2}
    r1={(1,2):1,(2,0):1,(0,1):-h,(3,3):-bb}
    r2={(2,1):1,(0,2):1,(1,0):-h,(3,3):-bb}
    tx={(3,0):1,(0,3):1};ty={(3,1):1,(1,3):1};tz={(3,2):1,(2,3):1}
    assert not combine((1,mul(u,w)),(-1,mul(w,u)),(1,r1),(-1,r2))
    assert not combine((1,mul(u,s)),(1,mul(s,u)),(-1,tx),(1,ty))
    assert not combine((1,mul(s,w)),(1,mul(w,s)),(-1,tz),(-h/2,tx),(-h/2,ty))
    data={'alternating_form':'M=J; T=epsilon*I; det(F)=epsilon; Q=J*F^t',
          'nonalternating_forms':checks,
          'general_identity':'(trace(M^t*M^-1)+2)*det(M)=4*det((M+M^t)/2)',
          'Clifford_swap_calibration':'u=x-y, w=z+h(x+y)/2, s=t; W=<s,w>; u*s=-s*u, u*w=w*u, s*w=-w*s; F=diag(-1,1), epsilon=-1',
          'scope':'Necessary common-plane forms, not complete ambient relations or H3 classification.'}
    path=Path(__file__).with_name('cubic_order2_plane_matrices_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS two matrix normal forms, four Jordan parameters and known Clifford-swap calibration')


if __name__=='__main__':main()
