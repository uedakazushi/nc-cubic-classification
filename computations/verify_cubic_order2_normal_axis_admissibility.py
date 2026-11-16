#!/usr/bin/env python3
"""Exact Clifford-swap covering map and character discriminant of the axis chart."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    h,r,R,b,c=S.symbols('h r R b c')
    k=h**3;den=h*(k-8)
    shift=2*(k-2)/den
    vscale=4*r/den
    pscale2=16*r**3/den**2
    a=(k*k+20*k-8)/(4*r**3)
    d=h*(k-8)*(b*(k-2)-3*c*h)/(4*r**3)
    i=h*(k-8)*(2*b-c*h)/(4*r**2)
    def zero(expr):
        expr=S.cancel(expr)
        num=expr.as_numer_denom()[0]
        expr=S.rem(num,R*R-pscale2,R)
        num=S.cancel(expr).as_numer_denom()[0]
        return S.expand(S.rem(num,r*r-k-1,r))==0
    assert zero(a*a-4-k*(k-8)**3/(16*(k+1)**3))
    # Quadratic normal form, generators (x,p,y,v).
    rules={(1,0):{(0,1):-1},(2,0):{(0,2):-1},(3,0):{(0,3):-1},
           (2,1):{(1,2):1},(1,1):{(2,2):a,(2,3):1,(3,2):1,(0,0):d},
           (3,3):{(2,2):1,(0,0):i}}
    def add(*terms):
        out={}
        for scalar,poly in terms:
            for word,coeff in poly.items():out[word]=S.expand(out.get(word,0)+scalar*coeff)
        return {w:v for w,v in out.items() if v!=0}
    def mul(u,v):
        return add(*[(a*b,rules.get(w+q,{w+q:1})) for w,a in u.items() for q,b in v.items()])
    x={(0,):1};p={(1,):R};y={(2,):1}
    U={(3,):vscale,(2,):shift}
    X=add((S.Rational(1,2),U),(S.Rational(1,2),p))
    Z=add((1,y),(-h/2,U))
    YY=add((S.Rational(1,2),U),(-S.Rational(1,2),p))
    source=[add((1,mul(x,w)),(1,mul(w,x))) for w in [X,YY,Z]]
    source += [add((1,mul(YY,Z)),(1,mul(Z,X)),(-h,mul(X,YY)),(-b,mul(x,x))),
               add((1,mul(Z,YY)),(1,mul(X,Z)),(-h,mul(YY,X)),(-b,mul(x,x))),
               add((1,mul(X,X)),(1,mul(YY,YY)),(-h,mul(Z,Z)),(-c,mul(x,x)))]
    assert all(zero(coeff) for rel in source for coeff in rel.values())
    matrix=S.Matrix([[S.diff(d,b),S.diff(d,c)],[S.diff(i,b),S.diff(i,c)]])
    expected=(h*(k-8)/(4*r**3))**2*h*r*(8-k)
    assert S.cancel(matrix.det()-expected)==0
    source_Q=c*c+h*h*b*c+2*h*b*b
    assert zero(r**8*(d*d-a*d*i+i*i)-h**4*(k-8)**4*source_Q/64)
    source_Delta=(h*c-2*b)*(b*(k-2)-3*h*c)*source_Q
    assert zero(d*i*(d*d-a*d*i+i*i)+h**6*(k-8)**6*source_Delta/(1024*r**13))
    # Every a²!=4 has a lift: the quartic in k avoids k=0,8,-1.
    aa,q=S.symbols('a q')
    cover=(q*q+20*q-8)**2-16*aa*aa*(q+1)**3
    assert S.expand(cover.subs(q,0)-16*(4-aa*aa))==0
    assert S.expand(cover.subs(q,8)-16*9**3*(4-aa*aa))==0
    assert cover.subs(q,-1)==729
    etale_cover=r**4-4*aa*r**3+18*r*r-27
    assert S.expand(S.discriminant(etale_cover,r)+5038848*(aa*aa-4)**2)==0
    # Character complete intersection, p*y=0, splits into two disjoint branches.
    dd,ii,v=S.symbols('d i v')
    Q=dd*v*v+2*ii*v+aa*ii-dd
    Delta=S.factor(S.discriminant(Q,v))
    assert S.expand(Delta-4*(dd*dd-aa*dd*ii+ii*ii))==0
    assert S.expand(Q.subs(v,-aa/2)-dd*(aa*aa-4)/4)==0
    xx=S.symbols('x')
    jac=S.Matrix([[2*dd*xx,2],[-2*ii*xx,2*v]])
    assert S.expand(jac.det()-4*xx*(dd*v+ii))==0
    # Parameter action from diagonal graded isomorphisms modulo degree scalars.
    lam,eps=S.symbols('lambda epsilon')
    obstruction=dd*dd-aa*dd*ii+ii*ii
    transformed=obstruction.subs({aa:eps*aa,dd:eps*lam**2*dd,ii:lam**2*ii},simultaneous=True)
    assert S.rem(S.expand(transformed-lam**4*obstruction),eps**2-1,eps)==0
    rho=aa*ii/dd;sigma=dd*dd/(ii*ii)
    assert S.cancel(rho*rho*sigma-aa*aa)==0
    assert S.cancel(1+(1-rho)*sigma-obstruction/(ii*ii))==0
    data={
      'source':'known Clifford swap h,b,c; h!=0,h³!=-1,8',
      'cover':['k=h³,r²=k+1','a=(k²+20k-8)/(4r³)',
               'd=h(k-8)(b(k-2)-3ch)/(4r³)','i=h(k-8)(2b-ch)/(4r²)'],
      'coordinate_change':['p_old=R*p, R²=16r³/[h²(k-8)²]',
                           'U_old=4r*v/[h(k-8)]+2(k-2)y/[h(k-8)]',
                           'X_old=(U_old+p_old)/2,Y_old=(U_old-p_old)/2,Z_old=y-h*U_old/2,t=x'],
      'six_source_relations_checked':6,
      'discriminant_identity':'a²-4=k(k-8)³/[16(k+1)³]',
      'cover_surjectivity':'The quartic in k has no roots k=0,8,-1 when a²!=4; the (b,c)->(d,i) matrix is invertible on this cover.',
      'relative_cover':'r^4-4*a*r^3+18*r²-27=0 has discriminant -5038848*(a²-4)², a finite etale cover on the stated open; h³=r²-1 and R² are then unit-root etale covers.',
      'character_CI':['p*y=0','p²+a*y²+2*y*v+d*x²=0','v²-y²-i*x²=0'],
      'character_reduced_criterion':'d*i*(a²-4)*(d²-a*d*i+i²)!=0',
      'old_new_bad_discriminants':'d*i*(d²-a*d*i+i²)=-h^6*(k-8)^6*Delta_h(b,c)/(1024*r^13)',
      'H3_criterion':'(a²-4)*d*i*(d²-a*d*i+i²)!=0, using the nodal obstruction and the known Clifford-swap H3 criterion',
      'geometric_arrow_action':'(lambda,zeta) in Gm x mu4: (a,d,i)->(zeta²*a,zeta²*lambda²*d,lambda²*i)',
      'scope':'Six defining relations, covering identities, character discriminants and action covariance checked exactly. Geometric surjectivity, H3 recognition and completeness of arrows are structural proofs in the manuscript.'}
    path=Path(__file__).with_name('cubic_order2_normal_axis_admissibility_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS six-relation Clifford cover, character discriminant and arrow covariance')


if __name__=='__main__':main()
