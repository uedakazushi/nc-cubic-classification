#!/usr/bin/env python3
"""Exact Sklyanin transport and degenerate parity obstruction in FS4."""
import json
from pathlib import Path
from itertools import product
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_pym_generic import words,relation_rows

W2=words(2);IX={w:j for j,w in enumerate(W2)}
U=S.zeros(16,6);K=S.zeros(16,6)
for j,(i,l) in enumerate([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):
    U[IX[(i,l)],j]=S.Rational(1,2);U[IX[(l,i)],j]=S.Rational(1,2)
    K[IX[(i,l)],j]=1;K[IX[(l,i)],j]=-1


def source_matrix(lam,values):
    x=[S.sympify(values.get(j,0)) for j in range(21)]
    B=S.Matrix([[x[0],x[1],x[3],-x[6],-x[10],-x[11]+x[8]],
                [x[1],x[2],x[4],x[7],-x[15]+x[8],-x[16]],
                [x[3],x[4],x[5],x[11]-x[15],x[12],x[17]],
                [x[6],x[7],x[8],x[9],x[13],-x[18]],
                [x[10],x[11],x[12],x[13],x[14],x[19]],
                [x[15],x[16],x[17],x[18],x[19],x[20]]])
    zz=S.symbols('z0:6');quad=zz[0]*zz[5]+lam*zz[1]*zz[4]-(1+lam)*zz[2]*zz[3]
    A=S.hessian(quad,zz)/2
    return U+K*B.T*A.inv(),A


def main():
    lam,t,z=S.symbols('lambda t z');Q=S.Rational
    R,A=source_matrix(lam,{0:1,2:1,5:1,9:(lam+1)*(lam-t)/16,14:lam*(lam+1-t)/16,20:t/16})
    W=R*A*R.T
    assert all(S.cancel(S.expand(W[IX[w[:2]],IX[w[2:]]]+W[IX[w[1:3]],IX[(w[3],w[0])]]))==0 for w in words(4))
    assert all(not W[IX[w[:2]],IX[w[2:]]] or (w[0]^w[1]^w[2]^w[3])==0 for w in words(4))
    alpha=1/t;beta=lam/(t-lam-1);gamma=-(lam+1)/(t-lam)
    assert S.cancel(alpha+beta+gamma+alpha*beta*gamma)==0
    ratios=[-4/t,4/(lam+1-t),4/(lam-t)]
    target=[]
    for (i,j,k),p,ratio in zip([(1,2,3),(2,3,1),(3,1,2)],[alpha,beta,gamma],ratios):
        target += [{(0,i):1,(i,0):-1,(j,k):-p/ratio,(k,j):-p/ratio},
                   {(0,i):1,(i,0):1,(j,k):-1/ratio,(k,j):1/ratio}]
    matches=[]
    for row in target:
        found=[]
        for j in range(6):
            old={w:R[k,j] for k,w in enumerate(W2) if R[k,j]};pivot=next(iter(old));scale=S.cancel(row.get(pivot,0)/old[pivot])
            if scale and all(S.cancel(row.get(w,0)-scale*old.get(w,0))==0 for w in set(row)|set(old)):found.append(j)
        assert len(found)==1;matches.append(found[0])
    assert len(set(matches))==6
    # The only +/-1 parameter boundaries in Omega.
    boundaries=[S.factor(alpha*alpha-1),S.factor(beta*beta-1),S.factor(gamma*gamma-1)]
    # Direct quadratic normal identities for S(1,-1,z).
    params=[S.Integer(1),S.Integer(-1),z];relations=[]
    for (i,j,k),p in zip([(1,2,3),(2,3,1),(3,1,2)],params):
        relations += [{(0,i):1,(i,0):-1,(j,k):-p,(k,j):-p},
                      {(0,i):1,(i,0):1,(j,k):-1,(k,j):1}]
    quads=[{(0,0):1,(3,3):1},{(1,1):1,(2,2):-1}]
    signs=[[1,-1,-1,1],[-1,1,1,-1]]
    M=relation_rows(relations,3);ix3={w:j for j,w in enumerate(words(3))};columns=[]
    for poly,ss in zip(quads,signs):
        for i in range(4):
            v=S.zeros(64,1)
            for w,c in poly.items():v[ix3[w+(i,)]]+=c;v[ix3[(i,)+w]]-=ss[i]*c
            columns.append(v)
    T=S.Matrix.hstack(*columns);field=S.QQ.frac_field(z)
    rr,piv=DomainMatrix.from_Matrix(M.T.row_join(T)).convert_to(field).rref();rr=rr.to_Matrix();assert all(j<M.rows for j in piv)
    certs=S.zeros(M.rows,8)
    for i,j in enumerate(piv):certs[j,:]=rr[i,M.rows:]
    assert DomainMatrix.from_Matrix(M.T*certs-T).convert_to(field).is_zero_matrix
    for c in certs:
        den=S.Poly(S.fraction(S.cancel(c))[1],z)
        for f in [z,z-1,z+1]:
            ff=S.Poly(f,z)
            while not den.rem(ff):den=den.exquo(ff)
        assert den.degree()==0
    assert all(signs[0][i]*signs[1][i]==-1 for i in range(4))
    # The Q family is literally skew: every column involves its own pair only.
    aa,bb,cc=S.symbols('A B C');RQ,AQ=source_matrix(lam,{8:aa,11:bb,15:cc})
    diagonal=[2*cc,2*bb/lam,-2*aa/(lam+1),-2*(bb-cc)/(lam+1),2*(aa-cc)/lam,2*(aa-bb)]
    assert all(S.cancel(x)==0 for x in RQ-U-K*S.diag(*diagonal))
    cert={'version':'classification-v73','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'Sklyanin_parameters':list(map(str,[alpha,beta,gamma])),
          'even_normalization_ratios':list(map(str,ratios)),'six_relation_matching':matches,
          'parameter_boundaries':list(map(str,boundaries)),
          'cyclic_top_tensor':True,'top_Klein_degree_zero':True,
          'S_1_minus1_z_normal_quadrics':[{'terms':{str(w):str(c) for w,c in poly.items()},'signs':ss} for poly,ss in zip(quads,signs)],
          'normality_witnesses':[[{'row':i,'coefficient':str(certs[i,j])} for i in range(M.rows) if certs[i,j]] for j in range(8)],
          'Q_skew_diagonal':list(map(str,diagonal)),
          'scope':'Explicit FS4 S and Q presentation transport and boundary parity identities. No full four-simple or CY coverage theorem imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS FS S-to-Sklyanin transport, all boundary normal parity identities, top degree and Q-skew recognition')


if __name__=='__main__':main()
