#!/usr/bin/env python3
"""All-value FN3 F0/F1 rank covers and three fixed first-shared presentations."""
import json
from pathlib import Path
import sympy as S
from verify_cubic_as4_four_simple_first import fn_matrix
from verify_cubic_as4_four_simple_remaining import centre,cyclic


def main():
    l=S.symbols('lambda');root=S.sqrt(3)*S.I;omega=(-1+root)/2
    families=[]
    for eps in [0,1]:
        R,A=fn_matrix(l,0,eps,1,(l*l-1)/16);cyclic(R,A)
        rows,det,p3,p4=centre(R,S.QQ.frac_field(l))
        expected=l**6*(l-1)**(4+eps)*(l+1)**(6+eps)*(l*l+1)**(2-eps)*(l*l-l+1)*(l*l+l+1)/2**(40+2*eps)
        assert S.cancel(det-expected)==0
        for c in list(p3)+list(p4):
            den=S.Poly(S.fraction(S.cancel(c))[1],l)
            for factor in [l,l-1,l+1,l*l+1]:
                ff=S.Poly(factor,l)
                while not den.rem(ff):den=den.exquo(ff)
            assert den.degree()==0
        special=[]
        for lv,field,label in [(S.Integer(1),S.QQ,'lambda=1'),(S.I,S.QQ.algebraic_field(S.I),'lambda^2+1=0'),
                               (omega,S.QQ.algebraic_field(root),'lambda^2+lambda+1=0'),
                               (-omega,S.QQ.algebraic_field(root),'lambda^2-lambda+1=0')]:
            RR,AA=fn_matrix(lv,0,eps,1,(lv*lv-1)/16);RR=RR.applyfunc(S.expand)
            rs,ds,_,_=centre(RR,field)
            special.append({'condition':label,'representative':str(lv),'field':str(field),
                            'minor_rows':rs,'minor_determinant':str(ds),'rank':20,'conjugate_roots_covered':True})
            print('PASS F',eps,label,'centre3 rank20',flush=True)
        families.append({'epsilon':eps,'generic_minor_rows':rows,'generic_minor_determinant':str(det),
                         'projection_denominator_support':['lambda','lambda-1','lambda+1','lambda^2+1'],
                         'special_rank_cover':special})
    fixed=[]
    for name,e,f,r in [('G0',0,0,1),('G1',1,0,1),('K',1,0,0)]:
        R,A=fn_matrix(S.Integer(1),0,e,f,r);cyclic(R,A)
        rows,det,_,_=centre(R,S.QQ)
        fixed.append({'name':name,'minor_rows':rows,'minor_determinant':str(det),'centre3_dimension':0})
        print('PASS fixed',name,'centre3 rank20',flush=True)
    cert={'version':'classification-v77','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source':'CY_ZERO_COMMUTATORS_FOUR_SIMPLE_FIRST_SHARED_COMPLETE.tex FN2-FN3',
          'F_families':families,'fixed_families':fixed,
          'scope':'All explicit F0/F1/G0/G1/K excluded conditional AS4. Together with independent L/M Ore proof covers all seven FN3 rows. Full chart/CY coverage and AS4 existence not imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_first_remaining_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all FN3 F and fixed rows with denominator and all-special rank control',flush=True)

if __name__=='__main__':main()
