#!/usr/bin/env python3
"""Exact faithful matrix model of the canonical two-cycle quotient."""
import json
from pathlib import Path
import sympy as S


def main():
    s=S.symbols('s',nonzero=True)
    I=S.eye(2);zero=S.zeros(2)
    p=S.Matrix([[0,s],[0,0]]);v=S.Matrix([[0,0],[s,0]])
    z=p*v+v*p
    assert p*p==v*v==zero and z==s**2*I
    assert z*p==p*z and z*v==v*z
    # A=k[p,v]/(p^2,v^2) is free over k[z] on these four elements.
    basis=[I,p,v,p*v]
    matrix=S.Matrix.hstack(*[S.Matrix(list(a)) for a in basis])
    assert S.factor(matrix.det())==-s**4
    assert p*v*p==z*p and v*p*v==z*v
    u=p+v;w=p-v
    assert u*u==z and w*w==-z and u*w==-w*u
    a=w*u.inv()
    assert a==S.diag(1,-1) and a*a==I
    e0=(I+a)/2;e1=(I-a)/2
    assert e0*e0==e0 and e1*e1==e1 and e0*e1==zero
    assert u*e0*u.inv()==e1 and u*e1*u.inv()==e0
    # The mu-fixed cubic quotient is k*vpv; it cannot commute with p.
    comm=v*p*v*p-p*v*p*v
    assert comm==S.diag(-s**4,s**4)
    # mu(p)=p, mu(v)=-v fixes the degree-zero involution a.
    assert (p+v)*(p-v).inv()==a
    data={
      'quotient':'A=k<p,v>/(p²,v²)',
      'central_parameter':'z=pv+vp, degree 2, regular',
      'free_central_basis':['1','p','v','pv'],
      'matrix_model':'p=s*E12, v=s*E21, z=s²*I',
      'basis_determinant':'-s^4',
      'degree_zero_localization':'(A[(p+v)^-1])_0=k[e0] x k[e1], e0,e1 orthogonal primitive idempotents',
      'shift':'conjugation by u=p+v exchanges e0,e1',
      'normal_cubic_restriction':'mu-fixed cubics are k*vpv; [vpv,p] has matrix diag(-s^4,s^4), so every H3 normal cubic restricts to zero',
      'scope':'Polynomial identities and the faithful central basis checked exactly. The qgr equivalence, canonical-point interpretation and normal-cubic reduction are proved in the manuscript.'}
    path=Path(__file__).with_name('cubic_order2_boundary_cycle_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS faithful two-cycle matrix model, primitive idempotents, shift and cubic restriction')


if __name__=='__main__':main()
