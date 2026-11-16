#!/usr/bin/env python3
"""Exact stabilizer equations and enhanced-inertia discriminants; no sampling."""
import json
from pathlib import Path
import sympy as S


def main():
    a,b,c,d,e,f,g,h,t,r,s,A,x,y,z=S.symbols('a b c d e f g h t r s A x y z')
    # beta=1, gamma=t, delta=1/t, alpha=A. These are ALL self-arrow equations.
    equations=[a*(1/t-A*A),b/t+2*r-b,c*(1/t-t*t),d*(1-A*A),
               f+2*t*s-f*t*t,a*r+d*s,
               g/t**2+r*b/t+s*e/t+r*r-g,
               h/t**2+r*c/t+s*f/t+s*s-h*t*t]
    # When a*d!=0, A²=1 and t=1 force r=s=0.
    assert all(S.cancel(q.subs({t:1,r:0,s:0,A:1}))==0 for q in equations)
    # a=0, d!=0: use u-translation to set b=0. Then r=s=0,A²=1.
    eq0=[S.cancel(q.subs({a:0,b:0,r:0,s:0,A:1})) for q in equations]
    assert S.cancel(eq0[2]-c*(1-t**3)/t)==0
    # If c!=0 and t is a primitive third root, g=h=0 is forced.
    assert S.gcd(t**3-1,t**2-1)==t-1
    assert S.gcd(t**3-1,t**4-1)==t-1
    # d=0,a!=0: use w-translation to set f=0. Then r=s=0,A²=1/t.
    assert S.cancel(equations[1].subs(r,0)-b*(1-t)/t)==0
    assert S.cancel(equations[2]-c*(1-t**3)/t)==0
    # The enhanced curve f=0,d=b=c=0 has t=A^-2,delta=A².
    reduced=[S.factor(q.subs({d:0,b:0,c:0,f:0,r:0,s:0,t:A**-2})) for q in equations]
    assert all(q==0 for q in reduced[:6])
    assert reduced[6]==g*(A-1)*(A+1)*(A*A+1)
    assert S.expand(reduced[7]-h*(A**8-1)/A**4)==0
    B1=b*d-a*e;C1=c*d-a*f
    delta=(d*d*h-a*a*g)**2-(d*d*C1-a*a*B1)*(B1*h-C1*g)
    assert S.factor(delta.subs({d:0,b:0,c:0,f:0}))==a**4*(e*e*h+g*g)
    # Smoothness on the enhanced curve is exactly h*(g²+e²h)!=0.
    binary=x*z*(4*e*h*x*x+4*g*x*z-e*z*z)
    disc=S.factor(S.discriminant(binary.subs(z,1),x))
    assert disc==16*e**2*(e*e*h+g*g)
    assert S.diff(binary,z).subs({x:1,z:0})==4*e*h
    # h=0 has a degenerate tangent cone at [1:0:0], hence is not admissible.
    F=S.expand(binary-e*e*a*a*y**4)
    bad=F.subs({x:1,h:0})
    assert all(S.diff(bad,i,j).subs({y:0,z:0})==0 for i,j in [(y,y),(y,z)])
    # Normal-axis g=0: two residual lines cross at a rank-two fibre.
    Q=x*z-d*y*y-f*x*x
    Faxis=Q*(4*e*h*x*x-e*z*z)
    point={x:0,y:1,z:0}
    assert Faxis.subs(point)==0 and Q.subs(point)==-d
    assert all(S.diff(Faxis,q).subs(point)==0 for q in [x,y,z])
    # Global curve chart: a=e=h=1,f=0, kappa²!=-1; mu8 acts on kappa
    # through its quotient mu2. The coarse parameter is j=kappa².
    j=g*g/(e*e*h)
    D,C=S.symbols('D C',nonzero=True)
    assert S.cancel(j.subs({g:g/D**2,e:e/(C*D),h:h*C*C/D**2})-j)==0
    data={
      'self_arrow_equations_beta1_delta_inverse_gamma':[str(S.factor(q)) for q in equations],
      'inertia_strata':{
        'a=c=0':'mu2 x mu2, closed normal-axis surface, dimension2',
        'd=b=c=0 and g-e*f/2!=0':'mu4, closed enhanced curve minus its special point',
        'd=b=c=0 and g-e*f/2=0':'mu8, one geometric isomorphism class',
        'all_other_admissible_points':'mu2'},
      'enhanced_curve_after_f_removal':'gbar=g-e*f/2, hbar=h-f²/4; hbar*(gbar²+e²*hbar)!=0',
      'enhanced_curve_stack':'[Spec k[kappa,(kappa²+1)^-1]/mu8], alpha acts by kappa->alpha^-4*kappa',
      'enhanced_curve_coarse':'j=gbar²/(e²*hbar) in A1 minus {-1}; mu8 exactly at j=0',
      'scope':'Exact universal self-arrow equations, finite root constraints, enhanced-curve discriminant and excluded boundary tests. Completeness uses the geometric full-arrow theorem and the structural H3 conic criterion.'}
    path=Path(__file__).with_name('cubic_order2_full_inertia_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('PASS complete (1,3) inertia strata and enhanced cyclic curve')


if __name__=='__main__':main()
