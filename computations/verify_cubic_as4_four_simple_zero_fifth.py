#!/usr/bin/env python3
"""All explicit zero-fifth M0/M1 families and fixed N/C cubic obstructions."""
import json
from pathlib import Path
import sympy as S
from verify_cubic_as4_four_simple import source_matrix
from verify_cubic_as4_four_simple_remaining import centre,cyclic


def m_matrix(p,eps):
    p,eps=map(S.sympify,(p,eps))
    return source_matrix(S.Integer(1),{0:1,1:1,2:p,9:eps,14:1/(16*(p-1)),
                                      19:-1/(16*(p-1)),20:p/(16*(p-1))})


def main():
    p=S.symbols('p');families=[]
    for eps in [0,1]:
        R,A=m_matrix(p,eps);cyclic(R,A)
        rows,det,p3,p4=centre(R,S.QQ.frac_field(p))
        expected=(3*p+1)/(2**33*(p-1)**11) if eps==0 else (p+3)*(3*p+1)/(2**23*(p-1)**13)
        assert S.cancel(det-expected)==0
        maxpower=0
        for c in list(p3)+list(p4):
            den=S.Poly(S.fraction(S.cancel(c))[1],p);factor=S.Poly(p-1,p);power=0
            while den.degree()>0:
                quo,rem=den.div(factor);assert rem.is_zero
                den=quo;power+=1
            maxpower=max(maxpower,power)
        special=[]
        for value in [-S.Rational(1,3)]+([S.Integer(-3)] if eps else []):
            RR,AA=m_matrix(value,eps);cyclic(RR,AA);rs,ds,_,_=centre(RR,S.QQ)
            special.append({'p':str(value),'minor_rows':rs,'minor_determinant':str(ds),'rank':20})
        families.append({'epsilon':eps,'generic_minor_rows':rows,'generic_minor_determinant':str(det),
                         'projection_denominator_support':'p-1','denominator_maxpower':maxpower,
                         'all_special_rank20':special})
        print('PASS zero-fifth M',eps,'all p!=1 centre3 zero',flush=True)
    z=S.sqrt(3)*S.I;Q=S.Rational;fixed=[]
    cases=[('N',S.Integer(2),{0:1,1:1,2:-2,8:z/4,10:z/6,11:z/6,16:z/6,15:-z/12,14:Q(1,12),19:Q(1,12),20:Q(1,12)},S.QQ.algebraic_field(z)),
           ('C',S.Integer(1),{0:1,1:1,2:1,10:S.I/8,16:S.I/8,11:-S.I/8,15:-S.I/8,14:Q(1,64),19:Q(1,64),20:Q(1,64)},S.QQ.algebraic_field(S.I))]
    for name,lam,values,field in cases:
        R,A=source_matrix(lam,values);cyclic(R,A);rows,det,_,_=centre(R,field)
        fixed.append({'name':name,'field':str(field),'minor_rows':rows,'minor_determinant':str(det),
                      'centre3_dimension':0,'coefficient_conjugate_also_covered':True})
        print('PASS zero-fifth fixed',name,'centre3 rank20',flush=True)
    cert={'version':'classification-v78','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'presentation_sources':['ZERO_FIFTH_OPEN_COMPLETE FZ2/FZ3','ZERO_FIFTH_BOUNDARY_COMPLETE FB2'],
          'M_families':families,'fixed_presentations':fixed,
          'scope':'Explicit M0/M1/N/C presentations excluded conditional AS4. No full chart/CY coverage or AS4 existence sufficiency imported. The boundary R+/-_1 is not covered by this certificate.'}
    Path(__file__).with_name('cubic_as4_four_simple_zero_fifth_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS both M families and N/C with all-value ranks and cyclic top tensors',flush=True)

if __name__=='__main__':main()
