#!/usr/bin/env python3
"""Exact weight elimination for a normal quantum coordinate in the (1,3) sector."""
import json
import itertools
from pathlib import Path
import sympy as S


def main():
    q,c,r,lam=S.symbols('q c r lambda')
    # Since p^2 cannot lie in T_2 for q!=-1, its nonzero v-component
    # forces c=-q or c=-q^2.  These and the v^2 weights eliminate c.
    P=(q+c)*(q*q+c)
    V=(c*c-1)*(q*c*c-1)*(q*q*c*c-1)*(c-1)*(q*c-1)
    result=S.factor(S.resultant(P,V,c))
    expected=(q-1)**6*(q+1)**6*(q*q+1)**4*(q*q-q+1)**2*(q*q+q+1)**2*(q**4+q**3+q*q+q+1)
    assert S.expand(result-expected)==0
    names=['x²','xy','y²','xv','yv','vy']
    expected_masks={
      (3,1):[[3],[1]],(3,2):[[4,5],[2]],
      (4,1):[[1,3],[2,4,5]],(4,2):[[1,4,5],[0,3]],
      (5,1):[[3],[]],(5,2):[[4,5],[1]],
      (6,1):[[2,3],[]],(6,2):[[2,4,5],[2,4,5]]}
    cases=[]
    for n in [3,4,5,6]:
        phi=S.cyclotomic_poly(n,q)
        for power in [1,2]:
            cv=-q**power
            weights=[1,1/q,1/q**2,cv,cv/q,cv/q]
            masks=[]
            for target in [-q,cv**2]:
                masks.append([i for i,w in enumerate(weights)
                              if S.rem(S.cancel(target-w).as_numer_denom()[0],phi,q)==0])
            assert masks==expected_masks[n,power]
            cases.append({'q_order':n,'c':str(cv),
                          'p_square_support':[names[i] for i in masks[0]],
                          'v_square_support':[names[i] for i in masks[1]]})
    # Binary AS2 normalizer lemma: for a non-normal linear y, hy=lambda*yh
    # with h quadratic forces lambda=+-1 (if h!=0).
    A,B,C=S.symbols('A B C')
    quantum=[A*(1-lam),A*(1-lam/r**2)+B*(1/r-lam),
             B*(1-lam/r)+C*(1/r**2-lam),C*(1-lam)]
    e1=quantum[1].subs({A:0,C:0});e2=quantum[2].subs({A:0,C:0})
    assert S.expand(e2+lam*e1-B*(1-lam**2))==0
    k=S.symbols('kappa')
    jordan=S.Matrix([[1-lam,0,0],[0,1-lam,0],[0,k,1-lam]])
    assert S.expand(jordan.det()-(1-lam)**3)==0
    # The two binary-obstruction cases have lambda=-q^-1 != +-1.
    for n in [3,6]:
        phi=S.cyclotomic_poly(n,q)
        assert S.rem(1-q*q,phi,q)!=0
    # At q=-1 the remaining c=1 case would give B/(x) with three
    # relations py=epsilon*yp, p²=A*y², v²=C*y².  Its cubic dimension
    # is at least 11 at EVERY A,C, whereas regularity requires dimension 10.
    quotient_ranks=[]
    words=list(itertools.product(range(3),repeat=3));index={w:i for i,w in enumerate(words)}
    for epsilon in [1,-1]:
        rels=[{(0,1):1,(1,0):-epsilon},{(0,0):1,(1,1):-A},
              {(2,2):1,(1,1):-C}]
        columns=[]
        for rel in rels:
            for j in range(3):
                for left in [True,False]:
                    column=[S.Integer(0)]*27
                    for w,coeff in rel.items():
                        word=(j,)+w if left else w+(j,)
                        column[index[word]]+=coeff
                    columns.append(column)
        matrix=S.Matrix.hstack(*[S.Matrix(col) for col in columns])
        syz1=S.zeros(18,1);syz2=S.zeros(18,1)
        # columns: relation, then generator, then left/right.
        syz1[6]=1;syz1[7]=-1;syz1[3]=A;syz1[2]=epsilon*A
        syz2[9]=1;syz2[8]=-1;syz2[0]=-1;syz2[1]=-epsilon
        assert matrix*syz1==S.zeros(27,1) and matrix*syz2==S.zeros(27,1)
        assert S.Matrix([[syz1[6],syz2[6]],[syz1[9],syz2[9]]]).det()==1
        rows=[{j:columns[j][i] for j in range(18) if columns[j][i]!=0} for i in range(27)]
        rank=0
        while True:
            hit=next(((i,j,a) for i,row in enumerate(rows) for j,a in row.items()
                      if a!=0 and not S.sympify(a).free_symbols),None)
            if hit is None:break
            i,j,a=hit;pivot={k:S.expand(S.sympify(b)/a) for k,b in rows.pop(i).items()}
            rank+=1
            for row in rows:
                if j not in row:continue
                coeff=row[j]
                for k,b in pivot.items():
                    value=S.expand(row.get(k,0)-coeff*b)
                    if value==0:row.pop(k,None)
                    else:row[k]=value
        residual_columns={j for row in rows for j in row}
        assert rank==15 and len(residual_columns)==1
        quotient_ranks.append({'epsilon':epsilon,'constant_pivots':rank,
                               'residual_rank_bound':1,'cubic_dimension_lower_bound':11})
    # If a=1 then mu*theta flips x alone.  Every possible cubic G is
    # consequently divisible by the normal x; this is a structural obstruction.
    mu=[-1,-1,-1,1];theta_plus=[1,-1,-1,1]
    possible=[]
    for word in itertools.product(range(4),repeat=3):
        if S.prod(mu[i] for i in word)==1 and S.prod(theta_plus[i] for i in word)==-1:
            possible.append(word)
            assert word.count(0)%2==1
    assert possible
    data={
      'hypotheses':'H3 multiplicities(1,3); common plane xy=q*yx with q!=1; a quantum coordinate x is normal in all B',
      'result':'q=-1; after translating v by W, x anticommutes with p,y,v and x² is central. Both the p-action on W and x-normalizer are involutions.',
      'normalizer_reduction':'The unipotent part of theta_x would have Dv=ell!=0 and D²(v²)=2ell², while the solved square relation has D²=0. Thus theta_x is semisimple and vx=c*xv after translating v by W.',
      'even_basis':names,
      'weights':['1','q^-1','q^-2','c','c*q^-1','c*q^-1'],
      'resultant':str(expected),
      'root_cases':cases,
      'binary_lemma':'A non-normal linear y in a genuine quantum/Jordan AS2 plane has no nonzero quadratic normalizer hy=lambda*yh with lambda not in {1,-1}.',
      'q_minus_one_c_plus_one_obstruction':quotient_ranks,
      'a_plus_one_obstruction':'mu*theta flips x alone and acts by -1 on G, forcing G=x*H and violating the quotient domain hypothesis',
      'scope':'Resultant, all cyclotomic supports and binary-normalizer coefficient identities checked exactly; the global normal-axis reduction and domain exclusions are proved in the manuscript. Normality of a common-plane coordinate is an additional hypothesis, not a full coverage theorem.'}
    path=Path(__file__).with_name('cubic_order2_normal_axis_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS normal-axis resultant, eight exact cyclotomic supports and binary normalizers')


if __name__=='__main__':main()
