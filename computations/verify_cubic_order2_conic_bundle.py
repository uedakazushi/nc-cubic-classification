#!/usr/bin/env python3
"""Exact global rank-three quadratic bundle and plane-quartic discriminant."""
import json
from pathlib import Path
import sympy as S


def main():
    a,b,c,d,e,f,g,h,la,mu,s,t=S.symbols('a b c d e f g h lambda mu s t')
    P=la*t*t;Y=la*s*s;J=la*s*t;B=mu*s;T=mu*t
    X=(B-d*P-f*Y)/e;A=a*P+b*X+c*Y;H=g*X+h*Y
    M4=S.Matrix([[P,0,J,T/2],[0,X,0,A/2],[J,0,Y,B/2],[T/2,A/2,B/2,H]])
    vectors=[S.Matrix([-J,0,P,0]),S.Matrix([-Y,0,J,0]),S.Matrix([-B,0,T,0])]
    assert all((M4*v).applyfunc(S.cancel)==S.zeros(4,1) for v in vectors)
    Q3=S.Matrix([[la,0,mu/2],[0,X,A/2],[mu/2,A/2,H]])
    quotient=S.Matrix([[t,0,s,0],[0,1,0,0],[0,0,0,1]])
    assert (quotient.T*Q3*quotient-M4).applyfunc(S.cancel)==S.zeros(4)
    assert quotient*S.Matrix([-s,0,t,0])==S.zeros(3,1)
    # Plane coordinates x=lambda*s,y=lambda*t,z=mu after blowing down E.
    xx,yy,zz=S.symbols('x y z')
    Q=xx*zz-d*yy*yy-f*xx*xx
    U=e*a*yy*yy+b*Q+e*c*xx*xx
    V=g*Q+e*h*xx*xx
    F4=S.expand(4*Q*V-U*U-e*Q*zz*zz)
    pull=F4.subs({xx:la*s,yy:la*t,zz:mu},simultaneous=True)
    assert S.cancel(pull-4*e*e*la*Q3.det())==0
    assert F4.subs({xx:0,yy:0,zz:1})==0
    assert S.diff(F4,xx).subs({xx:0,yy:0,zz:1})==-e
    assert Q3.subs({la:0,s:0}).rank()==2
    assert S.cancel(S.diff(Q3.det().subs(la,0),s)+mu**3/(4*e))==0
    # Residual rank-two matrix on the plane: rank-one conic fibres are N=0.
    N=S.Matrix([[Q/e,U/(2*e)],[U/(2*e),V/e-zz*zz/4]])
    assert S.cancel(N.det()-F4/(4*e*e))==0
    # Q is never the square of a line, independently of d,f.
    conic=S.Matrix([[-f,0,S.Rational(1,2)],[0,-d,0],[S.Rational(1,2),0,0]])
    assert conic.extract([0,2],[0,2]).det()==-S.Rational(1,4)
    # Discriminant class 3H-2F = 3E+4F; its intersection with E is one.
    intersection=S.Matrix([[-1,1],[1,0]])
    D=S.Matrix([3,4]);E=S.Matrix([1,0])
    assert (D.T*intersection*E)[0]==1
    data={
      'hypotheses':'eight-coefficient AS4 template, e!=0',
      'scroll_coordinates':['Y=lambda*s²','J=lambda*s*t','P=lambda*t²','B0=mu*s','T=mu*t'],
      'kernel_line':'(-s,0,t,0), with quotient (p,u,w,v)->(t*ell,u,s*ell,v)',
      'vector_bundle':'V=O(F) + O + O on F1, quadratic form valued in L=O(E+2F)',
      'quadratic_matrix':'[[lambda,0,mu/2],[0,X,A/2],[mu/2,A/2,H]]',
      'form_coefficients':['X=(mu*s-lambda*(d*t²+f*s²))/e','A=a*lambda*t²+b*X+c*lambda*s²','H=g*X+h*lambda*s²'],
      'discriminant_class':'3E+4F',
      'plane_blowdown':['x=lambda*s','y=lambda*t','z=mu'],
      'plane_conic':'Q=x*z-d*y²-f*x²',
      'plane_quadrics':['U=e*a*y²+b*Q+e*c*x²','V=g*Q+e*h*x²'],
      'plane_quartic':'F4=4*Q*V-U²-e*Q*z²',
      'marked_point':'[0:0:1] is always smooth, partial_x F4=-e',
      'rank_one_fibres':'Q=U=4V-e*z²=0 away from the marked point',
      'exceptional_curve':'lambda=0 has rank>=2; discriminant meets it in one transverse rank-two point',
      'non_double_conic_witness':'the x,z minor of Q is -1/4',
      'scope':'Global kernel, quotient matrix, determinant and rank identities checked exactly. Clifford-sheaf identification and saturation are proved in the manuscript. Smooth conic-bundle/H3 equivalence is not inferred from these identities alone.'}
    path=Path(__file__).with_name('cubic_order2_conic_bundle_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS global quadratic bundle, quartic discriminant and exceptional-curve identities')


if __name__=='__main__':main()
