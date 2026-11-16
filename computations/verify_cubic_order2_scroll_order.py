#!/usr/bin/env python3
"""Exact center identities and inverse quaternion chart for the cubic quotient."""
import importlib.util
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    spec=importlib.util.spec_from_file_location('central_template',Path(__file__).with_name('verify_cubic_order2_central_template.py'))
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    M=module.Model();P,X,Y,T=M.P,M.X,M.Y,M.T
    a,b,c,d,e,f,g,h=M.parameters
    p,u,v=[(z,{}) for z in M.gens];w=({},M.one);tc=({():T},{})
    G=M.oadd((1,M.omul(tc,w)),(-M.B,p));j=M.omul(p,w)
    assert not any(M.oadd((1,M.omul(j,v)),(-1,M.omul(v,j)),(1,G)))
    assert not any(M.oadd((1,M.omul(tc,w)),(-1,M.omul(w,tc)),(-2,G)))
    assert not any(M.oadd((1,M.omul(j,j)),(-P*Y,(M.one,{}))))
    assert not any(M.oadd((T*Y,(M.one,{})),(-M.B,j),(-1,M.omul(G,w))))
    assert not any(M.oadd((T,j),(-M.B*P,(M.one,{})),(-1,M.omul(G,p))))
    # If d=e=0 the normal cubic factors by w.
    factored=M.omul(M.oadd((1,tc),(-f,j)),w)
    difference=M.oadd((1,G),(-1,factored))
    assert all(S.expand(cc.subs({d:0,e:0}))==0 for poly in difference for cc in poly.values())
    # P-chart: x=u/p and y=v/p-t/2 generate a rank-four Clifford algebra.
    k,t,z=S.symbols('kappa t z');A=a+b*z+c*k*k;H=g*z+h*k*k
    F=t*t/4-H;scroll=k*t-d-e*z-f*k*k
    rules={(0,0):{():-z},(1,1):{():F},(1,0):{(0,1):-1,():-A}}
    def add(*terms):
        out={}
        for scale,poly in terms:
            for word,cc in poly.items():out[word]=S.expand(out.get(word,0)+scale*cc)
        return {word:cc for word,cc in out.items() if cc!=0}
    @lru_cache(None)
    def nf(word):
        for pos in range(len(word)-1):
            if word[pos:pos+2] in rules:
                return add(*[(cc,nf(word[:pos]+ww+word[pos+2:])) for ww,cc in rules[word[pos:pos+2]].items()])
        return {word:S.Integer(1)}
    def mul(poly,qq):return add(*[(cc*dd,nf(word+ww)) for word,cc in poly.items() for ww,dd in qq.items()])
    def eta(poly):return add(*[((-1)**len(word),{word:cc}) for word,cc in poly.items()])
    one={():S.Integer(1)};rr={(0,):S.Integer(1)};bb={(1,):S.Integer(1)}
    pp=one;uu=rr;ww={():k};vv=add((1,bb),(t/2,one))
    def prod1(poly,qq):return mul(poly,eta(qq))
    assert not add((1,prod1(pp,uu)),(1,prod1(uu,pp)))
    assert not add((1,prod1(pp,ww)),(-1,prod1(ww,pp)))
    assert not add((1,prod1(uu,ww)),(1,prod1(ww,uu)))
    assert not add((1,prod1(uu,vv)),(1,prod1(vv,uu)),(-A,one))
    assert not add((1,prod1(ww,vv)),(1,prod1(vv,ww)),(-(d+e*z+f*k*k),one),(-scroll,one))
    assert not add((1,prod1(vv,vv)),(-H,one))
    assert not add((1,prod1(pp,vv)),(1,prod1(vv,pp)),(-t,one))
    determinant=S.expand(-z*F-A*A/4)
    branch=S.expand(4*determinant)
    specialized=S.cancel(branch.subs(z,(k*t-d-f*k*k)/e))
    assert S.cancel(S.Poly(specialized,t).coeff_monomial(t**3)+k/e)==0
    # The two possible scrolls: e!=0 is S(1,2); e=0,d!=0 is S(0,3).
    ss,tt=S.symbols('s t0')
    yc,jc,pc,tc0=ss**3,ss**2*tt,ss*tt**2,tt**3
    assert S.expand(jc*jc-pc*yc)==0
    assert S.expand(yc*tc0-pc*jc)==0
    assert S.expand(jc*tc0-pc*pc)==0
    data={
      'hypotheses':'eight-coefficient AS4 template with nonzero AS resultant; R=B/(G)',
      'central_quotient_elements':['P=p²','X=u²','Y=w²','J=pw','T=pv+vp'],
      'center_relations':['J²=P*Y','Y*T=(dP+eX+fY)*J','J*T=(dP+eX+fY)*P'],
      'exact_before_quotient':['[pw,v]=-G','[T,w]=2G','YT-B0*J=G*w','JT-B0*P=G*p'],
      'factor_obstruction':'d=e=0 gives G=(T-f*pw)*w, so no quotient domain and no H3',
      'P_chart_center':'S=k[kappa,t,z]/(kappa*t-d-e*z-f*kappa²)',
      'P_chart_generators':['r=u*p^-1','b=v*p^-1-t/2'],
      'P_chart_relations':['r²=-z','b²=t²/4-g*z-h*kappa²','rb+br=-(a+b_parameter*z+c*kappa²)'],
      'inverse':'u=r*p,w=kappa*p,v=(b+t/2)*p; conjugation by p negates r,b and fixes kappa,t,z',
      'branch_polynomial':'4*z*(g*z+h*kappa²)-z*t²-(a+b*z+c*kappa²)²',
      'generic_nonzero_check':'For e!=0, after eliminating z the t³ coefficient of the branch polynomial is -kappa/e',
      'global_center_if_R_domain':'The indicated normal scroll ring is exactly Z(R^(2)), generic order rank4. Its Proj is F1 for e!=0 and the cone over a twisted cubic for e=0,d!=0.',
      'scope':'Central identities, inverse Clifford chart, branch polynomial and cone parametrization checked exactly. Finiteness and equality of the global center use the manuscript proof and the quotient domain hypothesis; no all-chart H3 admissibility is asserted.'}
    path=Path(__file__).with_name('cubic_order2_scroll_order_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS central scroll identities, factor obstruction and inverse quaternion chart')


if __name__=='__main__':main()
