#!/usr/bin/env python3
"""Independent identities for TT22 E_t,F_h and exact fixed A,B,D ranks."""
import json
from pathlib import Path
from itertools import product
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_pym_generic import words,relation_rows

W2=words(2);IX={w:j for j,w in enumerate(W2)}
U=S.zeros(16,6)
for j,w in enumerate([(1,1),(3,3),(0,2),(0,3),(1,2),(1,3)]):
    if w[0]==w[1]:U[IX[w],j]=1
    else:U[IX[w],j]=S.Rational(1,2);U[IX[w[::-1]],j]=S.Rational(1,2)
K=S.zeros(16,6)
for j,(i,l) in enumerate([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):K[IX[(i,l)],j]=1;K[IX[(l,i)],j]=-1
Z=S.symbols('z0:6');QUAD=-Z[2]*Z[5]+Z[3]*Z[4]-Z[0]*Z[1]+Z[5]**2
A0=S.hessian(QUAD,Z)/2


def source_matrix(values):
    x=[S.sympify(values.get(j,0)) for j in range(21)]
    B=S.Matrix([[x[0],x[11]/2,x[15]/2,x[1],x[2],(x[14]-x[18])/2],
                [(x[17]-x[9])/2,-x[10]/2,x[3],-x[20]/2,x[4],x[5]],
                [0,x[6],x[7],x[12],x[16],0],
                [0,x[7],x[8],x[16],x[9],x[10]],
                [x[11],x[12],x[16],x[13],x[14],0],
                [x[15],x[16],x[17],x[18],x[19],x[20]]])
    return U+K*B.T*A0.inv()


def cyclic(R):
    w=R*A0*R.T
    assert all(S.cancel(w[IX[v[:2]],IX[v[2:]]]+w[IX[v[1:3]],IX[(v[3],v[0])]])==0 for v in words(4))


def projection(rels,n,field):
    matrix=relation_rows(rels,n);rr,piv=DomainMatrix.from_Matrix(matrix).convert_to(field).rref();rr=rr.to_Matrix()
    free=[j for j in range(4**n) if j not in piv];p=S.zeros(len(free),4**n)
    for j,k in enumerate(free):p[j,k]=1
    for row,k in enumerate(piv):
        for j,l in enumerate(free):p[j,k]=-rr[row,l]
    assert DomainMatrix.from_Matrix(p*matrix.T).convert_to(field).is_zero_matrix
    return free,p


def main():
    t,h=S.symbols('t h');Q=S.Rational;left_inverse=(U.T*U).inv()*U.T
    families=[('E_t',source_matrix({9:1,14:-Q(1,16),17:1+t,18:-Q(1,16)-1/(4*t)}),t),
              ('F_h',source_matrix({9:1,14:-Q(1,16),17:-1,18:Q(1,16),19:h}),S.Integer(-2))]
    normal=[]
    for name,R,tvalue in families:
        cyclic(R)
        sigma_b=S.Matrix([[1,0,0,0],[-1/tvalue,1,0,0],[0,0,-1,0],[0,0,8,-1]])
        sigma_d=S.Matrix([[-1,0,0,0],[Q(1,2),-1,0,0],[0,0,1,0],[0,0,-4*tvalue,1]])
        certificates=[]
        for generator,sigma in [(1,sigma_b),(3,sigma_d)]:
            for i in range(4):
                target=S.zeros(16,1);target[IX[(generator,i)]]+=1
                for j in range(4):target[IX[(j,generator)]]-=sigma[j,i]
                coefficients=left_inverse*target
                assert all(S.cancel(z)==0 for z in R*coefficients-target)
                certificates.append(list(map(str,coefficients)))
        sigma=sigma_b*sigma_d
        assert (sigma+S.eye(4))**2==S.zeros(4)
        normal.append({'family':name,'normalizer_bd':[[str(v) for v in sigma.row(i)] for i in range(4)],
                       'eight_quadratic_witnesses':certificates,'nilpotent_square_zero':True})
        print('PASS',name,'universal cyclic tensor and bd normalizer with semisimple part -I',flush=True)
    cases=[('A',{0:1,5:Q(1,8),6:S.I/4,16:-S.I/4,19:S.I/2},S.QQ.algebraic_field(S.I)),
           ('B',{0:1,5:Q(1,8),7:1,9:-1,17:-1,14:Q(1,16),18:Q(1,16)},S.QQ),
           ('D',{0:1,5:Q(1,16),9:1,17:1,14:-Q(1,16),18:-Q(1,16)},S.QQ)]
    ranks=[]
    for name,values,field in cases:
        R=source_matrix(values);cyclic(R)
        rels=[{w:R[j,i] for j,w in enumerate(W2) if R[j,i]} for i in range(6)]
        free3,p3=projection(rels,3,field);free4,p4=projection(rels,4,field)
        assert len(free3)==20 and len(free4)==35
        ix={w:j for j,w in enumerate(words(4))};matrix=S.zeros(140,20)
        for j,col in enumerate(free3):
            w=words(3)[col]
            for i in range(4):matrix[35*i:35*(i+1),j]=p4[:,ix[w+(i,)]]-p4[:,ix[(i,)+w]]
        _,rows=DomainMatrix.from_Matrix(matrix.T).convert_to(field).rref();assert len(rows)==20
        det=DomainMatrix.from_Matrix(matrix[list(rows),:]).convert_to(field).det();assert det!=0
        ranks.append({'family':name,'field':str(field),'relations':[{str(w):str(v) for w,v in rr.items()} for rr in rels],
                      'dimensions_3_4':[20,35],'centre3_dimension':0,
                      'minor_rows':list(rows),'minor_determinant':str(field.to_sympy(det))})
        print('PASS fixed',name,'cyclic tensor and centre3 rank20',flush=True)
    cert={'version':'classification-v70','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'presentation_source':'CY_ZERO_COMMUTATORS_CURVILINEAR_TWO_TWO_COMPLETE.tex TT1-TT3',
          'normal_families':normal,'fixed_presentations':ranks,
          'scope':'Independent polynomial/Laurent identities and exact fixed ranks. AS4 existence and full CY coverage are not imported.'}
    Path(__file__).with_name('cubic_as4_tt22_remaining_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')


if __name__=='__main__':main()
