#!/usr/bin/env python3
"""Exact full-arrow coefficient equations and generic four-coordinate normalization."""
import importlib.util
import json
from pathlib import Path
import sympy as S


def main():
    spec=importlib.util.spec_from_file_location('template',Path(__file__).with_name('verify_cubic_order2_central_template.py'))
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    M=mod.Model();a,b,c,d,e,f,g,h=M.parameters
    A,B,C,D=S.symbols('alpha beta gamma delta',nonzero=True)
    r,s=S.symbols('r s')
    P,X,Y,T=M.P,M.X,M.Y,M.T
    p,u,v=[(q,{}) for q in M.gens];w=({},M.one)
    pp=M.oadd((A,p));uu=M.oadd((B,u));ww=M.oadd((C,w))
    vv=M.oadd((D,v),(r,u),(s,w))
    # Source parameters expressed in terms of target parameters and the arrow.
    source=[B*D*a/A**2,(B*D*b+2*B*r)/B**2,B*D*c/C**2,
            C*D*d/A**2,C*D*e/B**2,(C*D*f+2*C*s)/C**2,
            (D**2*g+D*r*b+D*s*e+r*r)/B**2,
            (D**2*h+D*r*c+D*s*f+s*s)/C**2]
    aa,bb,cc,dd,ee,ff,gg,hh=source
    def zero(poly):return all(S.cancel(z)==0 for part in poly for z in part.values())
    assert zero(M.oadd((1,M.omul(pp,uu)),(1,M.omul(uu,pp))))
    assert zero(M.oadd((1,M.omul(pp,ww)),(-1,M.omul(ww,pp))))
    assert zero(M.oadd((1,M.omul(uu,ww)),(1,M.omul(ww,uu))))
    imA=M.oadd((aa,M.omul(pp,pp)),(bb,M.omul(uu,uu)),(cc,M.omul(ww,ww)))
    imB=M.oadd((dd,M.omul(pp,pp)),(ee,M.omul(uu,uu)),(ff,M.omul(ww,ww)))
    assert zero(M.oadd((1,M.omul(uu,vv)),(1,M.omul(vv,uu)),(-1,imA)))
    assert zero(M.oadd((1,M.omul(ww,vv)),(1,M.omul(vv,ww)),(-1,imB)))
    square=M.oadd((1,M.omul(vv,vv)),(-gg,M.omul(uu,uu)),(-hh,M.omul(ww,ww)))
    assert zero(M.oadd((1,square),(-D*(r*a+s*d)*P,(M.one,{}))))
    Timage=M.oadd((1,M.omul(pp,vv)),(1,M.omul(vv,pp)))
    Gimage=M.oadd((1,M.omul(Timage,ww)),(-1,M.omul(imB,pp)))
    G=M.oadd((T,w),(-M.B,p))
    assert zero(M.oadd((1,Gimage),(-A*C*D,G)))
    # Generic a*d*e!=0 chart has the unique normal form a=d=e=1,b=0.
    delta=a*e/d;gamma=d/a;rr=b/2;ss=-b/2
    cp=S.cancel(c*gamma**2/delta)
    fp=S.cancel((f*gamma**2-2*gamma*ss)/(gamma*delta))
    gp=S.cancel((g-delta*rr*0-delta*ss-rr**2)/delta**2)
    hp=S.cancel((h*gamma**2-delta*rr*cp-delta*ss*fp-ss**2)/delta**2)
    # Alpha only occurs squared, with alpha²=e/d.
    equations=[delta-a*e/d,delta*0+2*rr-b,delta*cp-c*gamma**2,
               gamma*delta-d*e/d,gamma*delta-e,
               gamma*delta*fp+2*gamma*ss-f*gamma**2,
               rr+ss,delta**2*gp+delta*ss+rr**2-g,
               delta**2*hp+delta*rr*cp+delta*ss*fp+ss**2-h*gamma**2]
    assert all(S.cancel(q)==0 for q in equations)
    # Potential nonzero stabilizer tangent directions force AS resultant zero.
    B1=b*d-a*e;C1=c*d-a*f
    resultant=(d*d*h-a*a*g)**2-(d*d*C1-a*a*B1)*(B1*h-C1*g)
    assert S.expand(resultant.subs({a:0,c:0,f:0,h:0}))==0
    assert S.expand(resultant.subs({d:0,b:0,c:0,g:e*f/2,h:f*f/4}))==0
    data={
      'arrow_generators':['p->alpha*pprime','u->beta*uprime','w->gamma*wprime','v->delta*vprime+r*uprime+s*wprime'],
      'coefficient_equations':['beta*delta*aprime=a*alpha²','beta*delta*bprime+2beta*r=b*beta²','beta*delta*cprime=c*gamma²',
                               'gamma*delta*dprime=d*alpha²','gamma*delta*eprime=e*beta²','gamma*delta*fprime+2gamma*s=f*gamma²',
                               'r*aprime+s*dprime=0','delta²*gprime+delta*r*bprime+delta*s*eprime+r²=g*beta²',
                               'delta²*hprime+delta*r*cprime+delta*s*fprime+s²=h*gamma²'],
      'common_grading_scalar':'multiply alpha,beta,gamma,delta,r,s by one common unit; use beta=1 to rigidify',
      'cubic_covariance':'G maps to alpha*gamma*delta*Gprime',
      'generic_normal_form':'a=d=e=1,b=0, remaining coordinates c,f,g,h',
      'generic_normalization':{'alpha_squared':'e/d','beta':'1','gamma':'d/a','delta':'a*e/d','r':'b/2','s':'-b/2',
                               'cprime':str(cp),'fprime':str(fp),'gprime':str(gp),'hprime':str(hp)},
      'generic_stack':'the admissible open in A4_(c,f,g,h) times Bmu2',
      'global_presentation':'smooth irreducible four-dimensional Deligne-Mumford stack of the specified graded presentation families, modulo degree scalars',
      'scope':'All defining-relation and cubic arrow equations, generic normalization and the resultant contradictions in the infinitesimal-stabilizer proof checked exactly. Full intrinsic category-family recognition and global componenthood are not asserted.'}
    path=Path(__file__).with_name('cubic_order2_full_arrows_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS full arrow equations, cubic covariance and generic four-coordinate normalization')


if __name__=='__main__':main()
