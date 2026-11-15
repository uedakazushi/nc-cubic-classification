#!/usr/bin/env python3
"""Standard Klein cocycles of the shared-zero O/H presentation families."""
import json
from pathlib import Path
import sympy as S
from verify_cubic_as4_four_simple import source_matrix,W2,IX,U
from verify_cubic_as4_four_simple_remaining import centre
from verify_cubic_as4_tt22_remaining import projection
from sympy.polys.matrices import DomainMatrix
from verify_cubic_pym_generic import words


def mu(i,j):return (-1)**((i&1)*((j>>1)&1))
D=S.diag(*[mu(*v) for v in W2])
PAIR_DEGREES=[1,2,3,3,2,1]


def cocycle_tensor(R,A):
    for j,g in enumerate(PAIR_DEGREES):
        assert all(not S.cancel(R[k,j]) or (v[0]^v[1])==g for k,v in enumerate(W2))
    twist_A=A*S.diag(*[mu(g,g) for g in PAIR_DEGREES])
    twisted=D*R;top=twisted*twist_A*twisted.T
    assert all(S.cancel(S.expand(top[IX[v[:2]],IX[v[2:]]]+top[IX[v[1:3]],IX[(v[3],v[0])]]))==0 for v in words(4))
    return twisted


def special_centre(R,value):
    rels=[{v:R[k,j] for k,v in enumerate(W2) if R[k,j]} for j in range(6)]
    f3,p3=projection(rels,3,S.QQ);f4,p4=projection(rels,4,S.QQ)
    assert (len(f3),len(f4))==(20,35)
    ix={v:j for j,v in enumerate(words(4))};matrix=S.zeros(140,20)
    for j,k in enumerate(f3):
        v=words(3)[k]
        for i in range(4):matrix[35*i:35*(i+1),j]=p4[:,ix[v+(i,)]]-p4[:,ix[(i,)+v]]
    dm=DomainMatrix.from_Matrix(matrix).convert_to(S.QQ)
    _,rows=dm.transpose().rref();rank=len(rows)
    if value==-S.Rational(1,2):assert rank==20;poly={}
    else:
        assert rank==19
        poly={(3,3,3):1,(3,2,2):-3} if value==-S.Rational(1,4) else {(3,3,2):1,(2,2,2):-S.Rational(1,3)}
        v=S.zeros(64,1);ix3={w:j for j,w in enumerate(words(3))}
        for w,c in poly.items():v[ix3[w]]=c
        coords=p3*v;assert coords!=S.zeros(20,1) and matrix*coords==S.zeros(140,1)
    return {'lambda':str(value),'rank':rank,'centre3_dimension':20-rank,
            'factored_central_generator':{str(w):str(c) for w,c in poly.items()}}


def main():
    l,a=S.symbols('lambda A');hs=[]
    expected=16384*l**12*(l+1)**9*(2*l+1)**4*(4*l+1)*(4*l+3)
    for eps in [0,1]:
        R,A=source_matrix(l,{2:1,5:1,9:l*(l+1)/16,14:l*(l+1)/16,20:eps})
        twisted=cocycle_tensor(R,A)
        rows,det,p3,p4=centre(twisted,S.QQ.frac_field(l));assert S.cancel(det-expected)==0
        assert all(S.fraction(S.cancel(c))[1]==1 for c in list(p3)+list(p4))
        special=[]
        for lv in [-S.Rational(1,2),-S.Rational(1,4),-S.Rational(3,4)]:
            RR,AA=source_matrix(lv,{2:1,5:1,9:lv*(lv+1)/16,14:lv*(lv+1)/16,20:eps})
            TT=cocycle_tensor(RR,AA);special.append(special_centre(TT,lv))
        hs.append({'epsilon':eps,'generic_minor_rows':rows,'generic_determinant':str(det),
                   'projection_denominators_one':True,'special_centre_and_factor':special})
        print('PASS Klein cocycle H',eps,'all-value centre3 zero or one factored line',flush=True)
    R,A=source_matrix(l,{0:1,8:a,11:l*(l+1)/(16*a)})
    TT=cocycle_tensor(R,A);left=(U.T*U).inv()*U.T*D
    r=-(4*a-l-1)/(4*a+l+1);s=(4*a+l)/(4*a-l)
    q=r*s;k=-32*a/((4*a-l)*(4*a+l+1))
    relations=[{(0,1):1,(1,0):1},{(0,2):1,(2,0):-r},
               {(0,3):1,(3,0):1/r},{(1,2):1,(2,1):-s},
               {(1,3):1,(3,1):1/s},{(2,3):1,(3,2):-q,(0,1):-k}]
    for rel in relations:
        v=S.zeros(16,1)
        for w,c in rel.items():v[IX[w]]=c
        co=left*v;assert all(S.cancel(c)==0 for c in TT*co-v)
    cert={'version':'classification-v76','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'cocycle':'mu((p,q),(r,s))=(-1)^(p*s), degrees a=0,b=1,c=2,d=3',
          'twisted_top_pairing_signs':[mu(g,g) for g in PAIR_DEGREES],
          'all_three_top_tensors_anti_cyclic':True,'H_rank_covers':hs,
          'O_twisted_r_s_q_correction':list(map(str,[r,s,q,k])),
          'O_six_relation_transport':True,
          'O_obstruction':'r,s avoid 0,+-1; the same twenty PBW characters permit only c^3 or d^3 and never both; all possible central cubics factor regardless of r*s=1.',
          'scope':'All standard Klein cocycles of explicit shared-zero O/H families excluded, conditional AS4/domain as required by H3. Arbitrary cocycles/Zhang twists and full CY coverage remain unclaimed.'}
    Path(__file__).with_name('cubic_as4_four_simple_cocycles_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS cocycle O six-relation transport and anti-cyclic top tensor',flush=True)

if __name__=='__main__':main()
