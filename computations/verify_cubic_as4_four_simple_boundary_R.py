#!/usr/bin/env python3
"""All FG2 R-boundary values: twist transport and opposite central weights."""
import json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple import source_matrix,W2,IX
from verify_cubic_pym_generic import words,relation_rows


def r_matrix(lam,eta=1):
    lam,eta=map(S.sympify,(lam,eta))
    return source_matrix(lam,{0:1,1:1,2:1,5:1,9:(lam*lam-1)/16,
      10:-eta*S.I*lam*lam/(4*(lam+1)),16:-eta*S.I/(4*(lam+1)),
      11:eta*S.I*lam/(4*(lam+1)),15:eta*S.I*lam/(4*(lam+1)),
      14:lam**4/(16*(lam+1)**2),19:lam*lam/(16*(lam+1)**2),20:1/(16*(lam+1)**2)})


def target_relations(t):
    return [{(0,0):1,(1,1):1,(2,3):t/16,(3,2):t/16},
            {(0,1):1,(1,0):1,(2,2):-S.Rational(1,16),(3,3):-S.Rational(1,16)},
            {(0,2):1,(2,0):1},{(0,3):1,(3,0):-1},
            {(1,2):1,(2,1):1,(3,0):-2*t},{(1,3):1,(3,1):1}]


def matrix_of(relations):
    T=S.zeros(16,6)
    for j,poly in enumerate(relations):
        for v,c in poly.items():T[IX[v],j]=c
    return T


def main():
    l,t=S.symbols('lambda t');k=l/(4*(l+1));tt=(l-1)/(l+1);F=S.QQ_I.frac_field(l)
    R,A=r_matrix(l)
    phi=S.Matrix([[0,0,0,1],[0,0,l*k,0],[0,k/l,0,0],[-k*k,0,0,0]])
    C=S.Matrix([[1,1,0,0],[0,0,l,-l],[0,0,1,1],[S.I*k,-S.I*k,0,0]])
    sigma=S.diag(S.I,-S.I,1,-1)
    assert all(S.cancel(c)==0 for c in C.inv()*phi*C-k*sigma)
    assert S.cancel(C.det()+4*S.I*k*l)==0
    T=matrix_of(target_relations(tt));piv=[IX[v] for v in [(0,0),(0,1),(0,2),(0,3),(1,2),(1,3)]]
    assert T[piv,:]==S.eye(6)
    rd=DomainMatrix.from_Matrix(R).convert_to(F);ad=DomainMatrix.from_Matrix(A).convert_to(F)
    transform=S.kronecker_product(C.inv(),C.inv())*S.kronecker_product(S.eye(4),phi)
    new=DomainMatrix.from_Matrix(transform).convert_to(F)*rd
    td=DomainMatrix.from_Matrix(T).convert_to(F);co=new.extract(piv,list(range(6)))
    assert (td*co-new).is_zero_matrix
    action=DomainMatrix.from_Matrix(S.kronecker_product(sigma,sigma)).convert_to(F)*td
    assert (td*action.extract(piv,list(range(6)))-action).is_zero_matrix
    top=(rd*ad*rd.transpose()).to_dok()
    assert all(not(top.get((IX[v[:2]],IX[v[2:]]),F.zero)+top.get((IX[v[1:3]],IX[(v[3],v[0])]),F.zero)) for v in words(4))
    print('PASS all-lambda FG2 six-relation twist transport, eigenbasis and CY top tensor',flush=True)
    # Polynomial free-algebra witnesses: q0=a^2 and q1=d^2 are central for all t.
    rels=target_relations(t);source=relation_rows(rels,3);coeff=S.zeros(source.rows,8)
    def add(col,rel,c,left=None,right=None):
        assert (left is None)!=(right is None)
        row=24+left*6+rel if left is not None else right*6+rel
        coeff[row,col]+=c
    add(1,1,1,left=0);add(1,1,-1,right=0)
    add(1,2,S.Rational(1,16),right=2);add(1,2,-S.Rational(1,16),left=2)
    add(1,3,S.Rational(1,16),right=3);add(1,3,S.Rational(1,16),left=3)
    add(2,2,1,left=0);add(2,2,-1,right=0)
    add(3,3,1,left=0);add(3,3,1,right=0)
    add(4,3,-1,right=3);add(4,3,-1,left=3)
    add(5,5,1,left=3);add(5,5,-1,right=3)
    for rel,c,left,right in [(2,-16,None,1),(2,16,1,None),(4,16,0,None),(4,-16,None,0),
                              (3,32*t,None,0),(1,-16,None,2),(1,16,2,None)]:add(6,rel,c,left,right)
    ix3={v:j for j,v in enumerate(words(3))};target=S.zeros(64,8)
    for q,gen in enumerate([0,3]):
        for i in range(4):
            target[ix3[(gen,gen,i)],4*q+i]+=1;target[ix3[(i,gen,gen)],4*q+i]-=1
    assert all(S.expand(c)==0 for c in source.T*coeff-target)
    T0=matrix_of(rels)
    dual_a=S.zeros(1,16);dual_a[0,IX[(0,0)]]=1;dual_a[0,IX[(1,1)]]=-1
    dual_d=S.zeros(1,16);dual_d[0,IX[(2,2)]]=1;dual_d[0,IX[(3,3)]]=-1
    assert dual_a*T0==S.zeros(1,6) and dual_d*T0==S.zeros(1,6)
    cert={'version':'classification-v80','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source_presentation':'GENERAL_BOUNDARY_COMPLETE.tex FG2/FG6 only',
          'domain':'lambda!=0,-1; both eta signs by formal coefficient conjugation',
          'six_relation_transport':True,'basis_determinant':str(S.factor(C.det())),
          'target_t':'(lambda-1)/(lambda+1)','sigma_weights':['i','-i','1','-1'],
          'right_Zhang_twist_convention':'A_t=(R in C basis)^(sigma^-1)',
          'central_quadrics':['a^2','d^2'],'sigma_inverse_quadratic_weights':[-1,1],
          'centrality_polynomial_witnesses':[[{'row':i,'coefficient':str(coeff[i,j])} for i in range(source.rows) if coeff[i,j]] for j in range(8)],
          'nonzero_quadrics_dual_witnesses':['aa-bb','cc-dd'],
          'universal_CY_top_tensor':True,
          'scope':'All explicit R_lambda+/- excluded: every domain realization has zero odd centre by opposite central quadratic weights after Zhang twist. No AS4 existence/coverage/isomorphism theorem imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_boundary_R_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS polynomial all-t central quadric witnesses and opposite-weight odd-centre obstruction')

if __name__=='__main__':main()
