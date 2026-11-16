#!/usr/bin/env python3
"""Exact CY skew cubic-centre obstruction and its literal FZ2 Q application."""
import json
from itertools import product
from pathlib import Path
import sympy as S
from verify_cubic_as4_four_simple import source_matrix,U,K
from verify_cubic_pym_generic import words


def main():
    pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
    def weight(exponents,i):return [exponents[j] if i==k else (-exponents[k] if i==j else 0) for k,j in pairs]
    ones=[1]*4;mixed=[];cubes=[]
    for e in product(range(4),repeat=4):
        if sum(e)!=3:continue
        nz=[i for i,x in enumerate(e) if x]
        if len(nz)==1:cubes.append(e);continue
        if len(nz)==2:
            i=next(i for i in nz if e[i]==2);forced=weight(e,i)
        else:
            i=nz[0];forced=[x-y for x,y in zip(weight(e,i),weight(ones,i))]
        assert sum(abs(x) for x in forced)==1
        mixed.append({'monomial_exponents':e,'forced_unit_commutator_edge':pairs[next(k for k,x in enumerate(forced) if x)]})
    assert len(mixed)==16 and len(cubes)==4
    # Two distinct central cubes force all six q_ij to be third roots:
    # five incident edges directly, the last by one CY row identity.
    count=0
    for signs in product([1,2],repeat=6):
        row=[sum(signs[k]*weight(ones,i)[k] for k in range(6))%3 for i in range(4)]
        if row==[0]*4:count+=1
    assert count==0
    l,A,B,C=S.symbols('lambda A B C');rho=[2*C,2*B/l,-2*A/(l+1),-2*(B-C)/(l+1),2*(A-C)/l,2*(A-B)]
    R,_=source_matrix(l,{8:A,11:B,15:C})
    assert all(S.cancel(x)==0 for x in R-U-K*S.diag(*rho))
    qq={}
    for (i,j),x in zip(pairs,rho):
        qq[i,j]=(2*x-1)/(2*x+1);qq[j,i]=1/qq[i,j]
        assert S.cancel((qq[i,j]-1)*(2*x+1)+2)==0
    constraint=A*B+l*A*C-(l+1)*B*C-l*(l+1)/16
    for i in range(4):
        numerator=S.fraction(S.cancel(S.prod(qq[i,j] for j in range(4) if j!=i)-1))[0]
        _,rem=S.div(numerator,constraint,l,A,B,C);assert rem==0
    cert={'version':'classification-v89','statement':'CY quantum affine four-space with no pure commutator has centre in degree3 of dimension at most1, spanned if nonzero by one pure cube. Every nonzero central cubic cut is a non-domain; no H3 envelope.','mixed_cubic_types':mixed,'pure_cube_types':cubes,'nontrivial_third_root_assignments_checked':64,'assignments_satisfying_all_CY_rows':count,'Q_source_commit':'a45f834f51a00c47443b51caf66abaf4629546b9','Q_constraint':str(constraint),'Q_skew_rho':list(map(str,rho)),'Q_CY_row_products_verified_mod_constraint':True,'scope':'All literal FZ2 Q excluded conditional H3 domain/AS4. No full zero-commutator CY atlas coverage imported; arbitrary twists/cocycles are not treated by c=0 invariance.'}
    Path(__file__).with_name('cubic_as4_Q_centre_bound_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all 20 cubic types, no two central cubes, and literal Q CY identities')

if __name__=='__main__':main()
