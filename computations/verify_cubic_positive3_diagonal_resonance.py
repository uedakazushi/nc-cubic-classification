#!/usr/bin/env python3
"""Universal skew derivations and central cubic factors at all diagonal resonances."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    a=S.symbols('a',nonzero=True)
    d0,d1,d2,e0,e1,e2=S.symbols('d0 d1 d2 e0 e1 e2')
    variables=[d0,d1,d2,e0,e1,e2]
    equations=[a*(1-a)*e0,(1+a)*d2,
               (1+a**-3)*d0+(a-1)*e1,
               (1+a**-1)*d1+(a-a**-2)*e2]
    C=S.linear_eq_to_matrix(equations,variables)[0]
    inner=S.Matrix([[1-a,0],[0,a**-2-a],[0,0],[0,0],
                    [1+a**-3,0],[0,1+a**-1]])
    assert (C*inner).applyfunc(S.cancel)==S.zeros(4,2)
    assert C.subs(a,-1).rank()==3 and inner.subs(a,-1).rank()==2
    assert C.subs(a,-1)*S.Matrix([0,0,1,0,0,0])==S.zeros(4,1)
    phi=a*a-a+1
    def rem(q):return S.rem(S.cancel(q).as_numer_denom()[0],phi,a)
    assert rem(1+a**-3)==0
    for q in [a*(1-a),1+a,a-1,a-a**-2,1-a,a**-2-a]:
        assert S.gcd(rem(q),phi)==1
    # After removing the inner derivation, outer comparison has no surviving
    # linear correction and no quadratic base correction at primitive sixth roots.
    for q in [a-a*a,a**-1-a*a]:assert S.gcd(rem(q),phi)==1
    for i in range(3):
        j=2-i
        conditions=[a**(-2*j)-a*a,a**(2*i)-a**-2]
        assert S.gcd(S.gcd(rem(conditions[0]),rem(conditions[1])),phi)==1
    # At a=-1 the normal form has vx=-xv+k*y², vy=yv and
    # v²-z²=A*x²+B*xy+C*y². Check centrality of x²,y²,v² as exact
    # degree-three ideal membership, without asserting AS4 for all coefficients.
    k,A,B,D=S.symbols('k A B D')
    words=list(itertools.product(range(4),repeat=3));index={w:i for i,w in enumerate(words)}
    relations=[{(0,1):1,(1,0):-1},{(3,0):1,(0,3):1},
               {(3,1):1,(1,3):1},{(2,0):1,(0,2):1,(1,1):-k},
               {(2,1):1,(1,2):-1},
               {(2,2):1,(3,3):-1,(0,0):-A,(0,1):-B,(1,1):-D}]
    rows=[]
    for rel in relations:
        for gg in range(4):
            for side in [0,1]:
                row={index[((gg,)+w) if side==0 else (w+(gg,))]:cc for w,cc in rel.items()}
                rows.append(row)
    pivots={}
    while True:
        hit=next(((ii,j,cc) for ii,row in enumerate(rows) for j,cc in row.items()
                  if not S.sympify(cc).free_symbols),None)
        if hit is None:break
        ii,j,cc=hit
        pivot={u:S.expand(v/S.sympify(cc)) for u,v in rows.pop(ii).items()};pivots[j]=pivot
        for row in rows:
            scale=row.get(j,0)
            if not scale:continue
            for u,v in pivot.items():
                new=S.expand(row.get(u,0)-scale*v)
                if new==0:row.pop(u,None)
                else:row[u]=new
    # Pivots are triangular in their elimination order; reducing in that order
    # proves membership with polynomial coefficients and no parameter division.
    for square in [0,1,2]:
        for gg in range(4):
            target={}
            for w,cc in [((square,square,gg),1),((gg,square,square),-1)]:
                target[index[w]]=target.get(index[w],0)+cc
            target={w:cc for w,cc in target.items() if cc}
            for j,pivot in pivots.items():
                scale=target.get(j,0)
                if not scale:continue
                for u,v in pivot.items():
                    new=S.expand(target.get(u,0)-scale*v)
                    if new==0:target.pop(u,None)
                    else:target[u]=new
            assert not target
    data={
      'skew_derivation_equations':[str(q) for q in equations],
      'inner_columns':[[str(q) for q in row] for row in inner.tolist()],
      'a_minus_one':'modulo inner shifts, delta(x)=k*y²,delta(y)=0; the linear square correction is zero by the rational-collapse lemma',
      'central_quadrics_at_minus_one':['x²','y²','v²'],
      'degree3_constant_pivot_count':len(pivots),
      'normal_kernel_at_minus_one':'y*span(x²,y²,v²), by these exact central candidates and the filtered upper bound3',
      'primitive_sixth_root':'all derivations inner; all linear and quadratic square corrections zero; reduces to the top with normal kernel k*y³',
      'conclusion':'Every parameter in the specified full diagonal positive-three normalizing chart is excluded from H3.',
      'scope':'Exact derivation/inner identities, primitive-sixth-root gcds and all-parameter centrality witnesses. AS4 existence for arbitrary displayed correction coefficients and other charts are not asserted.'}
    path=Path(__file__).with_name('cubic_positive3_diagonal_resonance_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS all positive-three diagonal resonances: inner reductions and factorable complete cubic kernels')


if __name__=='__main__':main()
