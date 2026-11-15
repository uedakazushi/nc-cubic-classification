#!/usr/bin/env python3
"""Exact low-degree witness and identities for the proved R13 cut reduction.
No finite rank check here certifies AS regularity, THCR recognition, or smoothness.
"""
from itertools import product
from pathlib import Path
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix


def quotient(relations, degree, generators):
    def words(n): return list(product(range(generators), repeat=n))
    basis=words(degree); index={w:i for i,w in enumerate(basis)}; rows=[]
    for left_length in range(degree-1):
        for left in words(left_length):
            for right in words(degree-2-left_length):
                for rel in relations:
                    rows.append({index[left+w+right]:c for w,c in rel.items()})
    matrix=s.MutableSparseMatrix(len(rows), len(basis),
        {(i,j):c for i,row in enumerate(rows) for j,c in row.items()})
    rr,pivots=DomainMatrix.from_Matrix(matrix).convert_to(s.QQ).rref()
    rr=rr.to_Matrix(); free=[j for j in range(len(basis)) if j not in pivots]
    projection=s.zeros(len(free),len(basis))
    for row,col in enumerate(free): projection[row,col]=1
    for row,col in enumerate(pivots):
        for i,j in enumerate(free): projection[i,col]=-rr[row,j]
    assert projection*matrix.T==s.zeros(len(free),len(rows))
    return basis,free,projection


def center(relations, degree, generators):
    basis,free,_=quotient(relations,degree,generators)
    next_basis,_,pr=quotient(relations,degree+1,generators)
    index={w:i for i,w in enumerate(next_basis)}
    matrix=s.zeros(generators*pr.rows,len(free))
    for j,col in enumerate(free):
        word=basis[col]
        for x in range(generators):
            matrix[pr.rows*x:pr.rows*(x+1),j]=pr[:,index[word+(x,)]]-pr[:,index[(x,)+word]]
    kernel=matrix.nullspace()
    return matrix,kernel,[basis[i] for i in free]


def main():
    # a yz+b zy+c x^2 and its cyclic permutations, (a,b,c)=(1,2,3).
    rels=[{(1,2):1,(2,1):2,(0,0):3},
          {(2,0):1,(0,2):2,(1,1):3},
          {(0,1):1,(1,0):2,(2,2):3}]
    dimensions=[];g=None;g_words=None
    for n in [1,2,3]:
        matrix,kernel,words=center(rels,n,3)
        dimensions.append(len(kernel))
        if n==3:g=kernel[0];g_words=words
    assert dimensions==[0,0,1]
    brels=rels+[{(3,i):1,(i,3):-1} for i in range(3)]
    bm,bk,bwords=center(brels,3,4)
    assert bm.shape==(140,20) and len(bk)==2
    basis,_,pr=quotient(brels,3,4);index={w:i for i,w in enumerate(basis)}
    omega=s.zeros(len(basis),1)
    for word,c in zip(g_words,g):omega[index[word]]=c
    t3=s.zeros(len(basis),1);t3[index[(3,3,3)]]=1
    span=s.Matrix.hstack(pr*omega,pr*t3)
    assert span.rank()==2 and bm*span==s.zeros(140,2)
    x,y,z=s.symbols('x y z')
    # Smooth point-scheme cubic and absence of nonzero characters are separate checks.
    point_cubic=x**3+y**3+z**3-6*x*y*z
    character_equations=[x*x+y*z,y*y+z*x,z*z+x*y]
    for v in (x,y,z):
        gb=s.groebner([*[s.diff(point_cubic,w) for w in (x,y,z)],v-1],x,y,z)
        assert list(gb)==[1]
        assert list(s.groebner([*character_equations,v-1],x,y,z))==[1]
    u=s.symbols('u');cyclotomic=1+u+u*u
    assert s.gcd((1-u)**2,cyclotomic)==1
    assert s.rem((1-u)**2,cyclotomic,u)!=0
    h=(1-u**3)/(1-u)**4
    assert s.simplify(h-(1/(1-u)+3*u/(1-u)**3))==0
    assert s.simplify((1-u)*h-(1-u**3)/(1-u)**3)==0
    a,b,c,A,B,C,lam=s.symbols('a b c A B C lam',nonzero=True)
    action=lambda v,aa,bb,cc:(cc+aa**3*v)/bb
    # phi after psi: t -> Aa t; Omega -> Bb Omega+(B c+C a^3)t^3.
    assert s.simplify(action(action(lam,A,B,C),a,b,c)-action(lam,A*a,B*b,B*c+C*a**3))==0
    cert={'version':'classification-v6','field':'QQ',
          'Sklyanin_witness':{'parameters':[1,2,3],'center_dimensions_degrees_1_2_3':dimensions,
            'central_cubic_representatives':[[list(w),str(v)] for w,v in zip(g_words,g) if v],
            'point_scheme_cubic':str(point_cubic),'smooth_projective_jacobian_charts':3,
            'nonzero_character_charts_empty':3},
          'split_envelope':{'center_matrix_shape':list(bm.shape),'rank':bm.rank(),
                            'kernel_basis':'span(g,t^3)'},
          'identities':['cubic Hilbert series and regular boundary difference',
                        'nonpolynomial inverse Hilbert series at lambda=0',
                        'affine pencil action composition'],
          'proof':'papers/sections/cubic_r13_cut_reduction.tex',
          'limits':'Low-degree linear algebra and identities only. The all-parameter domain/rank, chart criterion, transcendental regularity, split Lambda=C* and groupoids are ordinary proofs using stated external inputs, not finite-rank extrapolations.'}
    Path(__file__).with_name('cubic_r13_cuts_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: exact Sklyanin center dimensions 0,0,1; split envelope center rank18; smooth and character charts; Hilbert and pencil identities')

if __name__=='__main__': main()
