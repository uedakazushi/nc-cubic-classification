#!/usr/bin/env python3
"""Universal QQ(zeta3)(h) checks for the complete beta-family comparison action.
Unlike the split locus, D can be zero and its transform has an A-beta term.
"""
from pathlib import Path
import json
import sympy as s


def main():
    z,hs=s.symbols('z h');K=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));F=K.frac_field(hs)
    h=F.convert(hs);q=F.convert(K.unit,K);zero=F.zero;one=F.one
    def equal(A,B):return all(not (a-b) for a,b in zip(A,B))
    def matmul(A,B):
        return tuple(sum((A[3*i+k]*B[3*k+j] for k in range(3)),zero) for i in range(3) for j in range(3))
    def transpose(M):return tuple(M[3*j+i] for i in range(3) for j in range(3))
    def det(M):
        a,b,c,d,e,f,g,i,j=M
        return a*(e*j-f*i)-b*(d*j-f*g)+c*(d*i-e*g)
    def plus(A,B):return tuple(a+b for a,b in zip(A,B))
    def scale(c,A):return tuple(c*a for a in A)
    def poly_sub(poly,x):
        return sum((F.convert(c,K)*x**exp[0] for exp,c in poly.items()),zero)
    def sub(v,x):return poly_sub(v.numer,x)/poly_sub(v.denom,x)
    def mat_sub(M,x):return tuple(sub(c,x) for c in M)
    def poly_mul(P,Q):
        out={}
        for a,c in P.items():
            for b,d in Q.items():
                e=tuple(i+j for i,j in zip(a,b));out[e]=out.get(e,zero)+c*d
        return {e:c for e,c in out.items() if c}
    def data(M):
        rows=[{tuple(int(i==j) for j in range(3)):M[3*k+i] for i in range(3) if M[3*k+i]} for k in range(3)]
        cubes={}
        for row in rows:
            for e,c in poly_mul(poly_mul(row,row),row).items():cubes[e]=cubes.get(e,zero)+c
        prod=poly_mul(poly_mul(rows[0],rows[1]),rows[2])
        for P in (cubes,prod):
            assert P.get((3,0,0),zero)==P.get((0,3,0),zero)==P.get((0,0,3),zero)
            assert all(not c for e,c in P.items() if e not in [(3,0,0),(0,3,0),(0,0,3),(1,1,1)])
        sc=cubes.get((3,0,0),zero);sm=cubes.get((1,1,1),zero)
        pc=prod.get((3,0,0),zero);pm=prod.get((1,1,1),zero)
        c=(-h*sm+6*pm)/6;hp=(h*sc-6*pc)/c;dm=det(M)
        beta_matrix=scale(one/c,transpose(M))
        center=[];constant=[]
        for row in [M[3*i:3*i+3] for i in range(3)]:
            a,b,d=row
            center.extend([a*a+hp*b*d,b*b+hp*a*d,d*d+hp*a*b])
            constant.extend([b*d,a*d,a*b])
        U=scale(one/dm,tuple(center));R=scale(one/dm,matmul(tuple(constant),beta_matrix))
        return {'h':hp,'c':c,'B':beta_matrix,'U':U,'R':R,'d':one/dm,'Q':tuple(center),'K':tuple(constant)}
    Id=tuple(F.convert(int(i==j)) for i in range(3) for j in range(3))
    generators=[tuple(map(F.convert,[0,1,0,0,0,1,1,0,0])),
                (one,zero,zero,zero,one,zero,zero,zero,q),
                (q,q*q,one,q*q,q,one,one,one,one)]
    all_compositions=0
    for M in generators:
        dm=data(M)
        for N in generators:
            dn=data(N);mn=data(matmul(M,N));hp=dm['h']
            Bn=mat_sub(dn['B'],hp);Un=mat_sub(dn['U'],hp);Rn=mat_sub(dn['R'],hp)
            assert not(mn['h']-sub(dn['h'],hp))
            assert equal(mn['B'],matmul(Bn,dm['B']))
            assert equal(mn['U'],matmul(dm['U'],Un))
            assert not(mn['d']-dm['d']*dn['d'])
            assert equal(mn['R'],plus(scale(dn['d'],dm['R']),matmul(matmul(dm['U'],Rn),dm['B'])))
            all_compositions+=1
    # For a scalar M=sI and t -> a t the action has weights beta2,A1,D3.
    # Setting a=s gives the identity, justifying quotient by common grading scalars.
    ss=F.convert(2);ds=data(scale(ss,Id))
    assert not(ds['h']-h) and equal(scale(ss**2,ds['B']),Id) and equal(scale(ss,ds['U']),Id)
    assert not(ds['d']*ss**3-one) and equal(ds['R'],tuple([zero]*9))
    # A concrete Fourier transformation really needs the mixed D correction.
    assert any(data(generators[2])['R'])
    cert={'version':'classification-v9','field':'QQ(zeta3)(h)',
      'Hessian_generator_pairs_checked_universally':all_compositions,
      'comparison_formulas':{'beta_new':'a^2/c * M^T beta','A_new':'a/det(M) * A q_hprime(M)',
        'D_new':'(a^3 D+a A k_beta_new(M))/det(M)'},
      'scalar_two_cancellation_control':True,
      'general_scalar_quotient':'The universal grading-scalar cancellation follows from homogeneous degrees in the proof; the additional executable control uses scalar2.',
      'torus_weights':{'beta':2,'A':1,'D':3},
      'mixed_D_correction_required':True,
      'limits':'Checks full rational-function identities on generating substitutions. Completeness of geometric arrows follows from the proved Hesse normal form and unique quadratic-potential translation, not from sample evaluation.'}
    Path(__file__).with_name('cubic_clifford_beta_action_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: all9 universal generator-composition identities; nontrivial mixed D correction; weights2/1/3 and grading-scalar quotient')

if __name__=='__main__':main()
