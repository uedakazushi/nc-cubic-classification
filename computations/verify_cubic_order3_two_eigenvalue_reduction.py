#!/usr/bin/env python3
"""Finite identities supporting the global two-eigenvalue order-three reduction."""
import json
from pathlib import Path
import sympy as S


def main():
    m=90;data=[]
    for u,v in [(0,30),(0,60),(30,60)]:
        quadratic=[(k*u+(2-k)*v)%m for k in range(3)];assert len(set(quadratic))==3
        top=[k for k in range(5) if (k*u+(4-k)*v)%m==0]
        mixed=[k for k in top if 0<k<4];assert len(mixed)==1
        cubic=[k for k in range(4) if (k*u+(3-k)*v)%m==0];assert cubic==[0,3]
        data.append({'eigenvalue_exponents_mu90':[u,v],'quadratic_weights':quadratic,'all_top_counts':top,'mixed_top_count':mixed[0],'multiplicities':[mixed[0],4-mixed[0]],'cubic_counts':cubic})
    assert [d['multiplicities'] for d in data]==[[1,3],[1,3],[2,2]]
    z,rho=S.symbols('z rho');leading=[]
    for degree in range(4):
        co=S.symbols('c0:'+str(degree+1));p=sum(co[k]*z**k for k in range(degree+1))
        top=S.Poly(S.expand(p-rho*p.subs(z,z+1)),z).coeff_monomial(z**degree)
        assert S.expand(top-(1-rho)*co[-1])==0
        leading.append(str(top))
    binary=[]
    for qexp in [1,2]:
        for rexp in [1,2]:
            exponents=[u for u in range(4) if qexp*u%3==rexp and qexp*(u-3)%3==rexp]
            assert len(exponents)==1 and exponents[0] in [1,2]
            binary.append({'q_exponent_mu3':qexp,'normalizer_exponent_mu3':rexp,'x_exponent':exponents[0]})
    w=S.symbols('w');A=[0,1];C=[2,3];ac=[(i,j) for i in A for j in C];ca=[(j,i) for j in C for i in A]
    ra={(0,1):1,(1,0):-w};rc={(2,3):1,(3,2):-w*w}
    J=S.zeros(4)
    for (a,b),x in ra.items():
        for (c,d),y in rc.items():J[ac.index((b,c)),ca.index((d,a))]=-w*x*y
    det=S.rem(S.expand(J.det()),w*w+w+1,w);assert det!=0
    assert all(sum(x!=0 for x in J.row(i))==1 for i in range(4))
    cert={'version':'classification-v91','scope':'Necessary structural normal forms for every strong H3 with two eigenvalues and semisimple Nakayama order3. No AS4 existence/admissibility assertion for the remaining mixed relation matrices.','weight_cases':data,'Jordan_binary_leading_comparisons':leading,'quantum_binary_normal_cubic_cases':binary,'mixed_flattening_offdiagonal_matrix':str(J),'mixed_flattening_determinant_mod_w2_w1':str(det),'proof':'papers/sections/cubic_as4_reductions.tex thm:h3-order3-two-blocks','validation_limit':'Bigraded homological arguments, binary automorphism classification, Frobenius pairing and PBW dimension comparison are manuscript proofs; this script checks the finite weight and polynomial identities.'}
    Path(__file__).with_name('cubic_order3_two_eigenvalue_reduction_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS order3 multiplicities 1+3/2+2, binary normal-cubic characters and invertible mixed flattening')

if __name__=='__main__':main()
