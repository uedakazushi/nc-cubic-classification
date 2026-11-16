#!/usr/bin/env python3
"""Finite arithmetic of the global two-eigenvalue H3 spectral filter.
The tensor/non-free-product argument is proved in the manuscript.
"""
import json,math
import sympy as S
from pathlib import Path


def main():
    determinants=sorted({abs(4*a-3*c) for a in range(4) for c in range(1,4)})
    assert determinants==[1,2,3,5,6,9]
    modulus=90;records=[];counts={}
    for u in range(modulus):
        for v in range(u+1,modulus):
            matches=[{'cubic_alpha_count':a,'top_alpha_count':c,'determinant':4*a-3*c} for a in range(4) for c in range(1,4) if (a*u+(3-a)*v)%modulus==0 and (c*u+(4-c)*v)%modulus==0]
            if not matches:continue
            order=modulus//math.gcd(modulus,u,v);assert order in [2,3,5,6,9]
            assert all(order==abs(x['determinant']) or abs(x['determinant'])%order==0 for x in matches)
            counts[order]=counts.get(order,0)+1
            records.append({'eigenvalue_exponents_in_mu90':[u,v],'joint_semisimple_order':order,'weight_witnesses':matches})
    assert counts=={3:3,2:1,9:6,6:2,5:4} and len(records)==16
    eliminated=[];remaining=[]
    for record in records:
        order=record['joint_semisimple_order']
        if order in [2,3]:remaining.append(record);continue
        u,v=record['eigenvalue_exponents_in_mu90'];assert modulus//math.gcd(modulus,u-v)>4
        assert len(record['weight_witnesses'])==1
        w=record['weight_witnesses'][0];a,c=w['cubic_alpha_count'],w['top_alpha_count']
        if order==5:assert (a,c) in [(1,3),(2,1)];reason='normal one-generator block; cubic has a repeated linear factor'
        elif order==9:assert (a,c) in [(0,3),(3,1)];reason='pure cube in the one-dimensional block'
        else:assert order==6 and c==2 and a in [0,3];reason='homogeneous cubic in a binary one-quadric domain factors'
        eliminated.append({'eigenvalue_exponents_in_mu90':[u,v],'reason':reason})
    assert len(eliminated)==12 and len(remaining)==4
    z,q,k=S.symbols('z q k');roots=S.symbols('a0:3')
    for degree in range(4):
        lhs=S.Integer(1)
        for j in range(degree):
            shift=k*sum(q**i for i in range(j));b=q**j*roots[j]+shift
            lhs*=q**j*z+shift-b
        assert S.expand(lhs-q**(degree*(degree-1)//2)*S.prod(z-roots[j] for j in range(degree)))==0
    cert={'version' :'classification-v90','scope':'Necessary spectrum filter for all strong H3 envelopes with exactly two distinct eigenvalues, including nonsemisimple Jordan parts. The preliminary 16 spectra reduce to four unordered eigenvalue sets by factorisation. This is not an existence, Jordan-type or admissibility classification.','proof':'papers/sections/cubic_as4_reductions.tex thm:h3-two-eigenvalue-refined','input':'mu_B(G)=G in degree3; hdet(mu_B)=1 on the degree4 Koszul top; the top cannot split over a nontrivial generator decomposition in a finite-GK AS4 domain.','arithmetic_determinants':determinants,'preliminary_semisimple_orders':[2,3,5,6,9],'possible_semisimple_orders':[2,3],'eliminated_by_factorisation':eliminated,'remaining_spectra':remaining,'binary_factorisation_formula_verified_through_degree':3,'root_coordinate':'Choose one primitive 90th root zeta; exponent pair [u,v] means unordered {zeta^u,zeta^v}.','preliminary_counts_by_order':counts,'preliminary_spectra':records,'validation_limit':'Exact residue arithmetic only. Frobenius flattening, free-product exponential growth, the multigraded Hilbert argument and binary-domain factorisation are manuscript proofs, not asserted to be proved by this enumeration.'}
    Path(__file__).with_name('cubic_two_eigenvalue_filter_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS preliminary 16 spectra, 12 factorisation exclusions, and four remaining spectra; orders 2 or 3')

if __name__=='__main__':main()
