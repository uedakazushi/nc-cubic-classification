#!/usr/bin/env python3
"""WWY (2.5) at an etale family of E-points: exact order-six locus.

No generic row-reduction chart is used. Nonvanishing of the normalized
third iterate supplies the extension across a removable common factor.
"""
import json
from pathlib import Path
import sympy as S


def main():
    a,b=S.symbols('a b');c=-(a+b)/(1+a*b)
    p=-a*(1+b)/(a+b);q=b*(a-1)/(a+b)
    # E-point (0,r,s,1), r^2=p, s^2=q, both units on T.
    assert S.cancel(p+q+1)==0
    assert S.cancel((1+b)*p+(1-a)*q+1+a*b)==0
    ell=a*b+a+3*b-1;kappa=a*b+a-b+3;m=3*a*b-a+b+1
    vector=[S.Integer(0),S.Integer(1),S.Integer(1),S.Integer(1)]
    commons=[a*b/(1+a*b),a*b*(a-1)**2*(b+1)**2/(1+a*b),a*b*kappa**2/(1+a*b)]
    normalized=[]
    for common in commons:
        u,v,w,z=vector
        u2,v2,w2,z2=u*u*p*q,v*v*p,w*w*q,z*z
        raw=[-2*a*b*c*v*w*z-u*(-u2+b*c*v2+a*c*w2+a*b*z2),
             2*a*u*w*z*q+v*(u2-b*c*v2+a*c*w2+a*b*z2),
             2*b*u*v*z*p+w*(u2+b*c*v2-a*c*w2+a*b*z2),
             2*c*u*v*w*p*q+z*(u2+b*c*v2+a*c*w2-a*b*z2)]
        vector=[S.factor(S.cancel(x/common)) for x in raw]
        assert all(S.denom(x)==1 for x in vector)
        normalized.append(vector)
    assert S.expand(normalized[1][0]+4*(a+1)*(a+b)*(b-1))==0
    zero_condition=2*(a+b)*(a*b-3*a-b-1)*kappa*ell*m
    first_condition=-2*(a-1)*ell**2*m**2
    second_condition=2*a*(b+1)*kappa**2*ell**2
    assert S.expand(vector[0]-zero_condition)==0
    assert S.expand(vector[1]+vector[3]-first_condition)==0
    assert S.expand(vector[2]-vector[3]-second_condition)==0
    assert S.expand((a-1)*m-(3*a+1)*kappa+4*(a+1)**2)==0
    on_curve=S.factor(vector[3].subs(b,(1-a)/(a+3)))
    assert S.cancel(on_curve-1024*(a-1)**2*(a+1)**6/(a+3)**5)==0
    cert={'version':'classification-v67','primary_source':'WWY arXiv:1802.06487v2 Definition-Lemma 2.4, formula (2.5)',
          'point_square_coordinates':[str(p),str(q)],
          'iterate_common_factors':list(map(str,commons)),
          'normalized_iterates':[list(map(str,row)) for row in normalized],
          'conditions':[str(zero_condition),str(first_condition),str(second_condition)],
          'third_coordinate_on_locus':str(on_curve),
          'conclusion':'On T, sigma^3=diag(1,1,-1,-1)|E iff alpha*beta+alpha+3*beta-1=0.',
          'scope':'Exact identities plus the paper nonvanishing/extension argument. Central quadratic elements are not equations of the point curve.'}
    Path(__file__).with_name('cubic_sklyanin_order6_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS global normalized third iterate; exact marked order-six locus; no exceptional chart omitted')


if __name__=='__main__':main()
