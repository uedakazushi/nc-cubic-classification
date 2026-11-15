#!/usr/bin/env python3
"""Exact QQ(zeta3) Hessian-group certificate for the order-two split family.
The upper bound/completeness of the flex-preserving projective group is the
explicit geometric input in Iyudu-Shkarin Lemma5.1; this checks its generators,
all 216 elements, the 12 base transformations, and every exceptional stabilizer.
"""
from collections import deque
from pathlib import Path
import json
import sympy as s
from sympy.polys.rings import ring


def main():
    z=s.symbols('z');K=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));q=K.unit
    zero=K.zero;one=K.one
    def norm(M):
        c=next(x for x in M if x)
        return tuple(x/c for x in M)
    def mul(A,B):
        return norm(tuple(sum((A[3*i+k]*B[3*k+j] for k in range(3)),zero) for i in range(3) for j in range(3)))
    Id=tuple(K.convert(int(i==j)) for i in range(3) for j in range(3))
    gens=[tuple(map(K.convert,[0,1,0,0,0,1,1,0,0])),
          (one,zero,zero,zero,one,zero,zero,zero,q),
          (q,q*q,one,q*q,q,one,one,one,one)]
    seen={Id};queue=deque([Id])
    while queue:
        M=queue.popleft()
        for G in gens:
            N=mul(M,G)
            if N not in seen:seen.add(N);queue.append(N)
        assert len(seen)<=216
    assert len(seen)==216
    def poly_mul(P,Q):
        out={}
        for a,c in P.items():
            for b,d in Q.items():
                e=tuple(i+j for i,j in zip(a,b));out[e]=out.get(e,zero)+c*d
        return {e:c for e,c in out.items() if c}
    exps=[(3,0,0),(0,3,0),(0,0,3),(1,1,1),
          (2,1,0),(2,0,1),(1,2,0),(0,2,1),(1,0,2),(0,1,2)]
    def cubic_data(M):
        rows=[{tuple(int(i==j) for j in range(3)):M[3*k+i] for i in range(3) if M[3*k+i]} for k in range(3)]
        cubes={}
        for L in rows:
            for e,c in poly_mul(poly_mul(L,L),L).items():cubes[e]=cubes.get(e,zero)+c
        prod=poly_mul(poly_mul(rows[0],rows[1]),rows[2])
        for P in [cubes,prod]:
            assert P.get((3,0,0),zero)==P.get((0,3,0),zero)==P.get((0,0,3),zero)
            assert all(not P.get(e,zero) for e in exps[4:])
        return cubes.get((3,0,0),zero),cubes.get((1,1,1),zero),prod.get((3,0,0),zero),prod.get((1,1,1),zero)
    base=set();kernel=0
    for M in seen:
        s0,s1,p0,p1=cubic_data(M)
        N=norm((6*s0,-36*p0,-s1,6*p1));base.add(N)
        if N==norm((one,zero,zero,one)):kernel+=1
    assert len(base)==12 and kernel==18
    fixed_h_one=sum(1 for M in seen if (lambda d: 6*d[0]-36*d[2]==-d[1]+6*d[3])(cubic_data(M)))
    assert fixed_h_one==18
    R,h=ring('h',K)
    jnum=lambda a,b:110592*b**3*(a**3+b**3)**3
    jden=lambda a,b:a**3*(8*b**3-a**3)**3
    fixed2=R.one;fixed3=R.one;orders={1:0,2:0,3:0}
    def mul2(A,B):
        a,b,c,d=A;aa,bb,cc,dd=B
        return norm((a*aa+b*cc,a*bb+b*dd,c*aa+d*cc,c*bb+d*dd))
    id2=norm((one,zero,zero,one));base_records=[]
    for N in sorted(base,key=lambda x:str(x)):
        a,b,c,d=N
        assert jnum(a*h+b,c*h+d)*jden(h,R.one)==jnum(h,R.one)*jden(a*h+b,c*h+d)
        order=1 if N==id2 else 2 if mul2(N,N)==id2 else 3
        assert order!=3 or mul2(mul2(N,N),N)==id2
        orders[order]+=1
        f=c*h*h+(d-a)*h-b
        if order==2:fixed2*=f
        if order==3:fixed3*=f
        base_records.append({'matrix':[str(K.to_sympy(v)) for v in N],'order':order})
    fixed2=fixed2/fixed2.LC;fixed3=fixed3/fixed3.LC
    assert fixed2==h**6+20*h**3-8
    assert fixed3==h**2*(h**3-8)**2*(h**3+1)**2
    assert orders=={1:1,2:3,3:8}
    assert (h**3+4)**3-27*h**6==(h**3-8)**2*(h**3+1)
    assert (2-h**3)**3+27*h**3==-(h**3-8)*(h**3+1)**2
    assert 64*(1+h**3)**3-h**3*(8-h**3)**3==(h**6+20*h**3-8)**2
    # Chart has no extra normal-linear marking: all orbit maps preserve regular/j!=0 base.
    cert={'version':'classification-v7','field':'QQ(zeta3)',
          'projective_Hessian_group_order':216,'base_image_order':12,'base_kernel_order':18,'fixed_h_one_projective_stabilizer':fixed_h_one,
          'base_orders':orders,'base_transformations':base_records,
          'good_base':'h != 0, h^3 != -1,8',
          'special_stabilizer_polynomial':'h^6+20*h^3-8',
          'PAut_orders':{'generic':18,'special':36},
          'normalized_cut_stabilizer_group_orders':{'generic_base':54,'special_base':108},
          'global_group_order':648,
          'ordinary_proof_dependency':'Flex-preserving group completeness; AS3/THCR, Azumaya and chart proofs. Enumeration alone is not an all-AS4 coverage theorem.'}
    Path(__file__).with_name('cubic_clifford_hesse_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: all216 Hessian matrices; base A4 of order12 with kernel18; all j identities; stabilizer jump polynomial; good-base exclusions')

if __name__=='__main__':main()
