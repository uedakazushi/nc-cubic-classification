#!/usr/bin/env python3
"""All FI2 J families: odd cubic obstruction and h=0 AS4 failure."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple import source_matrix,W2,IX
from verify_cubic_as4_four_simple_second import central_data,check_denominators,check_minor
from verify_cubic_pym_generic import words,relation_rows


def j_matrix(h,eta):
    h,eta=map(S.sympify,(h,eta));i=S.I
    return source_matrix(i,{0:1,1:1,2:1,5:1,10:eta*(1-i)/8,16:eta*(1-i)/8,
      15:eta*(1+i)/8,11:-eta*(1+i)/8,12:h,17:i*h,13:-eta*(1+i)*h/4,
      18:eta*(1-i)*h/4,14:h*h+i/32,19:i*(h*h-S.Rational(1,32)),20:-h*h+i/32})


def main():
    h=S.symbols('h');field=S.QQ_I.frac_field(h);results=[]
    for eta in [1,-1]:
        R,A=j_matrix(h,eta)
        rd=DomainMatrix.from_Matrix(R).convert_to(field);ad=DomainMatrix.from_Matrix(A).convert_to(field)
        top=(rd*ad*rd.transpose()).to_dok()
        assert all(not(top.get((IX[v[:2]],IX[v[2:]]),field.zero)+top.get((IX[v[1:3]],IX[(v[3],v[0])]),field.zero)) for v in words(4))
        M,rows,projections=central_data(R,field);check_denominators(projections,[h])
        expected=S.I*h**9/2048 if eta==1 else (1-S.I)*h**10/128
        check_minor(M,rows,expected)
        print('PASS J eta',eta,'all h!=0 centre3 rank20, denominator h only',flush=True)
        RR,AA=j_matrix(S.Integer(0),eta)
        rels=[{v:S.cancel(RR[k,j]) for k,v in enumerate(W2) if RR[k,j]} for j in range(6)]
        degree5=DomainMatrix.from_Matrix(relation_rows(rels,5)).convert_to(S.QQ_I)
        rank5=degree5.rank();assert 1024-rank5==58
        results.append({'eta':eta,'generic_minor_rows':rows,'generic_minor_determinant':str(expected),
                        'projection_denominator_support':'h','centre3_dimension_h_nonzero':0,
                        'h_zero_degree5_relation_rank':rank5,'h_zero_degree5_dimension':58})
        print('PASS J eta',eta,'h=0 degree5 dimension58 exceeds AS4 value56',flush=True)
    cert={'version':'classification-v81','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source_presentation':'IMAGINARY_BOUNDARY_COMPLETE.tex FI2 explicit coefficients only',
          'both_signs_directly_verified':True,'families':results,'universal_anti_cyclic_top_tensors':True,
          'scope':'Both entire J_h families excluded. h!=0 uses all-value centre3 rank20 conditional AS4; h=0 fails AS4 Hilbert degree5 independently. No full chart/CY coverage, AS4 sufficiency or all-isomorphism theorem imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_boundary_J_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS both full FI2 families and their excluded h=0 endpoints',flush=True)

if __name__=='__main__':main()
