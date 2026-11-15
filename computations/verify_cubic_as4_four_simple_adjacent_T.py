#!/usr/bin/env python3
"""T presentation: exact nonempty exclusion open and parameter involution.
No all-parameter T classification is asserted by this validator.
"""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple_adjacent_S import t_matrix
from verify_cubic_as4_four_simple import U,IX
from verify_cubic_as4_four_simple_second import central_data
from verify_cubic_pym_generic import words


def main():
    l=S.symbols('lambda');F=S.QQ_I.frac_field(l);q=l+1;f=-l/q
    R,A=t_matrix(l);RR,_=t_matrix(f)
    rd=DomainMatrix.from_Matrix(R).convert_to(F)
    ad=DomainMatrix.from_Matrix(A).convert_to(F)
    w=(rd*ad*rd.transpose()).to_dok()
    assert any(w.values())
    assert all(not(w.get((IX[v[:2]],IX[v[2:]]),F.zero)+w.get((IX[v[1:3]],IX[(v[3],v[0])]),F.zero)) for v in words(4))
    swap=S.eye(4);swap.row_swap(1,3)
    P=S.diag(1,-1/q,-1/q**2,-1/q)*swap
    trans=DomainMatrix.from_Matrix(S.kronecker_product(P,P)).convert_to(F)*rd
    target=DomainMatrix.from_Matrix(RR).convert_to(F)
    left=DomainMatrix.from_Matrix((U.T*U).inv()*U.T).convert_to(F)
    assert (target*left*trans-trans).is_zero_matrix
    assert all(S.cancel(x)==0 for x in P.subs(l,f)*P-S.eye(4))
    assert S.cancel(P.det()-q**-4)==0
    assert S.cancel(f.subs(l,f)-l)==0
    E=l**4+2*l**3+10*l*l+24*l+16
    num=S.fraction(S.cancel(E.subs(l,f)))[0]
    assert S.gcd(S.Poly(E,l),S.Poly(num,l)).degree()==0
    R1,_=t_matrix(S.Integer(1));M,rows,projections=central_data(R1,S.QQ_I)
    assert len(rows)==20
    minor=M.extract(rows,list(range(20))).det();assert minor
    special=[]
    for eta in [1,-1]:
        for ll in [-1+S.I,-1-S.I]:
            Rs,_=t_matrix(ll,eta);Ms,rs,_=central_data(Rs,S.QQ_I);assert len(rs)==20
            special.append({'lambda':str(ll),'eta':eta,'centre3_rank':20,'minor_rows':rs})
    cert={'version':'classification-v85','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
      'source_scope':'AB2 coefficients and AB14 candidate map; relation identities independently checked',
      'conditional_AS4_nakayama':'identity via nonzero anti-cyclic top tensor',
      'special_parameters':special,
      'T_1':{'degree3_dimension':20,'degree4_dimension':35,'centre3_rank':20,'minor_rows':rows,'minor':str(S.QQ_I.to_sympy(minor))},
      'involution':{'parameter':str(f),'matrix':str(P),'determinant':str(q**-4),'inverse':'P(f(lambda))'},
      'quartic':str(E),'quartic_and_transport_coprime':True,
      'mathematical_consequence':'Only finitely many parameters in this T line can be H3 envelopes; finite set not enumerated. Proof uses presentation-rank dichotomy and kernel semicontinuity on the constant-rank open, not assumed all-fibre AS4 existence.',
      'scope':'Not all-parameter T exclusion or all-H3 coverage; polynomial-module generic calculations are separate until independently replayed.'}
    Path(__file__).with_name('cubic_as4_four_simple_adjacent_T_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS universal T CY tensor, exact T_1 centre3 rank20, involution and coprime quartic transport')

if __name__=='__main__':main()
