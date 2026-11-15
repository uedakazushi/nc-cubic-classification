#!/usr/bin/env python3
"""Exact identities behind the complete beta-family local criterion.
Local homological equivalences are proved in TeX; no finite-dimensional check
here is used to infer finite global dimension or AS regularity by extrapolation.
"""
from pathlib import Path
from itertools import product
import json
import sympy as s


def main():
    h,u,v,w,bx,by,bz,A,B,C,D=s.symbols('h u v w beta_x beta_y beta_z A B C D')
    Q=s.Matrix([[u,(h*w+bz)/2,(h*v+by)/2],
                [(h*w+bz)/2,v,(h*u+bx)/2],
                [(h*v+by)/2,(h*u+bx)/2,w]])
    T=s.factor(Q.det());L=A*u+B*v+C*w+D
    def left(i):
        matrix=s.zeros(8)
        for mask in range(8):
            bits=[j for j in range(3) if mask>>j&1]
            if i not in bits:matrix[mask|(1<<i),mask]+=(-1)**sum(j<i for j in bits)
            for k,j in enumerate(bits):matrix[mask^(1<<j),mask]+=(-1)**k*Q[i,j]
        return matrix
    X,Y,Z=[left(i) for i in range(3)]
    volume=X*Y*Z-Q[0,1]*Z+Q[0,2]*Y-Q[1,2]*X
    assert all((volume*M-M*volume).applyfunc(s.expand)==s.zeros(8) for M in (X,Y,Z))
    assert (volume**2+T*s.eye(8)).applyfunc(s.expand)==s.zeros(8)
    a=v-Q[0,1]**2/u;b=w-Q[0,2]**2/u;c=Q[1,2]-Q[0,1]*Q[0,2]/u
    assert s.cancel(T-u*(a*b-c*c))==0
    # Formal coordinate change to the character point, on u=r^2 !=0.
    r=s.symbols('r',nonzero=True)
    px=r;py=(h*w+bz)/(2*r);pz=(h*v+by)/(2*r)
    chars=[2*py*pz-h*px**2-bx,2*pz*px-h*py**2-by,2*px*py-h*pz**2-bz]
    assert all(s.cancel(x)==0 for x in [chars[0]+2*c.subs(u,r*r),
                                      chars[1]-h*a.subs(u,r*r),chars[2]-h*b.subs(u,r*r)])
    jac=s.Matrix([[s.diff(p,x)/(2*r) if x==r else s.diff(p,x) for x in (r,v,w)] for p in (px,py,pz)])
    assert s.factor(jac.det())==-h*h/(8*r**3)
    # Cauchy-Binet identity: Hessian on an image hyperplane equals8*det(K).
    es=s.symbols('e0:12');E=s.Matrix(4,3,es)
    ell=s.Matrix([(-1)**i*E[[j for j in range(4) if j!=i],:].det() for i in range(4)])
    assert (E.T*ell).applyfunc(s.expand)==s.zeros(3,1)
    H=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,-2,0],[0,0,0,2]])
    pair=s.Matrix([[ell[0],(ell[2]-ell[3])/2],[(ell[2]+ell[3])/2,ell[1]]])
    assert s.expand((E.T*H*E).det()-8*pair.det())==0
    # Every nonzero character has Jacobian rank >=2: point cubic is smooth.
    x,y,z=s.symbols('x y z');M=s.Matrix([[-h*x,z,y],[z,-h*y,x],[y,x,-h*z]])
    assert s.expand(M.det()-(h*(x**3+y**3+z**3)+(2-h**3)*x*y*z))==0
    # A fully explicit nonsplit H3 witness with a singular (four-node) center.
    witness={h:1,bx:-1,by:0,bz:0}
    Tw=s.factor(T.subs(witness));Qw=Q.subs(witness)
    assert s.expand(4*Tw-((5*u-1)*v*w-u*(u-1)**2-v**3-w**3))==0
    grads=[s.diff(Tw,q) for q in (u,v,w)]
    gb=s.groebner([Tw,*grads],u,v,w)
    assert gb.is_zero_dimensional
    std=[];leaders=[p.LM(order=gb.order).exponents for p in gb.polys]
    for exp in product(range(5),repeat=3):
        if not any(all(i>=j for i,j in zip(exp,l)) for l in leaders):std.append(exp)
    assert len(std)==4
    for rr in [(0,1),(0,2),(1,2)]:
        for cc in [(0,1),(0,2),(1,2)]:
            assert gb.reduce(s.expand(Qw.extract(rr,cc).det()))[1]==0
    Hess=s.hessian(Tw,(u,v,w));detH=s.factor(Hess.det())
    assert list(s.groebner([Tw,*grads,detH],u,v,w))==[1]
    assert Tw.subs({u:1,v:0,w:0})==0 and detH.subs({u:1,v:0,w:0})==s.Rational(1,2)
    assert all(g.subs({u:-s.Rational(1,7),v:-s.Rational(4,7),w:-s.Rational(4,7)})==0 for g in [Tw,*grads])
    reps=[2*y*z-x*x+1,2*z*x-y*y,2*x*y-z*z]
    char_gb=s.groebner(reps,x,y,z);char_lead=[p.LM(order=char_gb.order).exponents for p in char_gb.polys]
    assert char_gb.is_zero_dimensional
    standard=[exp for exp in product(range(9),repeat=3) if not any(all(i>=j for i,j in zip(exp,l)) for l in char_lead)]
    assert len(standard)==8
    assert list(s.groebner([*reps,M.subs(h,1).det()],x,y,z))==[1]
    # Base-point-free net guarantees all determinant singularities are rank-one.
    # This is the exact characteristic-zero factor used in the ordinary proof.
    cert={'version':'classification-v9','field':'QQ / rational-function identities',
      'Schur_determinant':'T=u*(a*b-c^2)',
      'universal_beta_volume_8x8':'central and volume^2=-det(Q), all h,beta',
      'character_coordinate_Jacobian':'-h^2/(8*r^3)',
      'quadratic_Ext_pairing_Hessian_identity':'det(E^T H E)=8 det(K), for universal4x3 E',
      'nonsplit_witness':{'h':1,'beta':[-1,0,0],'cut':'g_beta=0',
        'affine_center':str(Tw),'center_singular_scheme_length':4,
        'all_singular_points_rank_at_most_one':True,'all_singular_points_ordinary_double':True,
        'character_scheme_length':8,'character_scheme_reduced':True,
        'Hessian_determinant_at_axis_node':'1/2'},
      'limits':'Universal algebraic identities and exact geometric witness only. A1-endomorphism, Serre/Yoneda necessity and completion-local global-dimension descent are ordinary proofs in cubic_clifford_beta_classification.tex.'}
    Path(__file__).with_name('cubic_clifford_beta_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: universal Schur/character/Hessian-Ext identities; exact nonsplit four-node center with reduced8-point character scheme')

if __name__=='__main__':main()
