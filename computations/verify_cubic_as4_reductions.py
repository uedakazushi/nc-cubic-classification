#!/usr/bin/env python3
"""Exact finite checks for H3-specific as4 reductions.

The all-parameter quantum exclusion, spectral argument, Weyl localization and
infinite point-Ext assertion are proved in TeX, not inferred from these checks.
All matrices below are over QQ or the characteristic-zero cyclotomic field QQ(zeta3).
"""
from itertools import combinations, product
from pathlib import Path
import json
import sympy as S
from sympy.polys.matrices import DomainMatrix

D3=[a for a in product(range(4),repeat=4) if sum(a)==3]
D4=[a for a in product(range(5),repeat=4) if sum(a)==4]
INDEX4={a:i for i,a in enumerate(D4)}
EDGES=list(combinations(range(4),2))


def qmatrix(values,field):
    q=[[field.one for _ in range(4)] for _ in range(4)]
    for (i,j),value in zip(EDGES,values):
        q[i][j]=field.from_sympy(S.sympify(value));q[j][i]=field.one/q[i][j]
    return q


def polynomial_product(f,g,q,field):
    out={}
    for a,c in f.items():
        for b,d in g.items():
            scalar=c*d
            for j in range(4):
                for i in range(j):scalar*=q[j][i]**(a[j]*b[i])
            exp=tuple(x+y for x,y in zip(a,b))
            out[exp]=out.get(exp,field.zero)+scalar
    return {a:c for a,c in out.items() if c}


def linear_image(matrix,i,field):
    return {tuple(int(r==j) for r in range(4)):field.from_sympy(matrix[j,i])
            for j in range(4) if matrix[j,i]}


def action(matrix,a,q,field):
    out={(0,0,0,0):field.one}
    for i,n in enumerate(a):
        for _ in range(n):out=polynomial_product(out,linear_image(matrix,i,field),q,field)
    return out


def kernel_check(name,values,nilpotent,field):
    q=qmatrix(values,field);N=nilpotent;identity=S.eye(4);G=identity+N
    H=identity+N/4-3*N**2/32+7*N**3/128
    assert N**4==S.zeros(4) and H**4==G
    m=[]
    for row in q:
        value=field.one
        for c in row:value*=c
        m.append(value)
    # as4 right-cyclic nu is inverse to this project's Ext-convention mu.
    normalizer=[[field.from_sympy(G[j,i])/m[j] for i in range(4)] for j in range(4)]
    rows=[[field.zero for _ in D3] for _ in range(140)]
    for col,a in enumerate(D3):
        F={a:field.one};HF=action(H,a,q,field)
        for i in range(4):
            lhs=polynomial_product(F,linear_image(H**3,i,field),q,field)
            rhs_linear={tuple(int(r==j) for r in range(4)):normalizer[j][i]
                        for j in range(4) if normalizer[j][i]}
            rhs=polynomial_product(rhs_linear,HF,q,field)
            for exp,c in lhs.items():rows[35*i+INDEX4[exp]][col]+=c
            for exp,c in rhs.items():rows[35*i+INDEX4[exp]][col]-=c
    dm=DomainMatrix(rows,(140,20),field)
    _,selected=dm.transpose().rref();assert len(selected)==20,name
    minor=DomainMatrix([rows[i] for i in selected],(20,20),field)
    det=minor.det();assert det,name
    return {'name':name,'coefficient_field':str(field),'rank_W1_equations':20,
            'kernel_dimension':0,'nonzero_minor_rows':list(selected),
            'nonzero_minor_determinant':str(field.to_sympy(det)),
            'nilpotent_matrix':[list(map(int,row)) for row in N.tolist()]}


def main():
    qq=S.QQ;reports=[]
    for partition in [(2,1,1),(2,2),(3,1),(4,)]:
        N=S.zeros(4);offset=0
        for size in partition:
            for i in range(size-1):N[offset+i,offset+i+1]=1
            offset+=size
        reports.append(kernel_check('commutative_'+str(partition),[1]*6,N,qq))
    N=S.zeros(4);N[0,1]=1
    reports.append(kernel_check('nonCY_sign_repeated_row',[1,-1,-1,-1,-1,-1],N,qq))
    N=S.zeros(4);N[0,1]=N[1,2]=1
    reports.append(kernel_check('three_equal_rows',[1,1,2,1,2,2],N,qq))
    N=S.zeros(4);N[0,1]=N[2,3]=1
    reports.append(kernel_check('two_pairs_of_equal_rows',[1,2,2,2,2,1],N,qq))
    zeta=(-1+S.sqrt(-3))/2;cyclotomic=qq.algebraic_field(zeta)
    N=S.zeros(4);N[1,2]=1
    reports.append(kernel_check('quantum_Fermat_repeated_row',[zeta,zeta,zeta,1,zeta,zeta],N,cyclotomic))

    # Two conventions give inverse diagonal Nakayama matrices already in the quantum plane.
    a,b=S.symbols('a b',nonzero=True)
    q=b/a
    assert S.diag(q,1/q)==S.diag(a,b)**-2*(a*b)
    l=S.symbols('l')
    assert S.gcd(l**3-1,l**4-1)==l-1

    # A non-generic S(2,3) Ore example with an actual central cubic, not an empty kernel.
    x,y,z=S.symbols('x y z');variables=(x,y,z)
    f=x**3+y**3+z**3
    delta=(y*y-z*z,z*z-x*x,x*x-y*y)
    assert sum(S.diff(d,v) for d,v in zip(delta,variables))==0
    assert S.expand(sum(S.diff(f,v)*d for v,d in zip(variables,delta)))==0

    # Universal Tate / matrix-factorization identities, over a polynomial ring in independent coefficients.
    g1,g2,g3=S.symbols('g1 g2 g3');F=x*g1+y*g2+z*g3
    d1=S.Matrix([[x,y,z]])
    d2=S.Matrix([[-y,-z,0,g1],[x,0,-z,g2],[0,x,y,g3]])
    d3=S.Matrix([[z,-g2,g1,0],[-y,-g3,0,g1],[x,0,-g3,g2],[0,x,y,z]])
    d4=S.Matrix([[g3,-g2,g1,0],[-y,-z,0,g1],[x,0,-z,g2],[0,x,y,g3]])
    assert (d1*d2-S.Matrix([[0,0,0,F]])).applyfunc(S.expand)==S.zeros(1,4)
    assert (d2*d3-S.Matrix.hstack(S.zeros(3,1),F*S.eye(3))).applyfunc(S.expand)==S.zeros(3,4)
    assert (d3*d4-F*S.eye(4)).applyfunc(S.expand)==S.zeros(4)
    assert (d4*d3-F*S.eye(4)).applyfunc(S.expand)==S.zeros(4)
    t=S.symbols('t')
    betti=[int(S.expand(S.series((1+t)**3/(1-t*t),t,0,13).removeO()).coeff(t,n)) for n in range(13)]
    assert betti==[1,3]+[4]*11
    # Every matrix entry kills the Ore-axis point after xi and the degree-two Gi vanish.
    for differential in [d1,d2,d3,d4]:
        assert differential.subs({x:0,y:0,z:0,g1:0,g2:0,g3:0})==S.zeros(*differential.shape)
    # A shear of a divergence-free base gives delta'=delta-h*Euler; it cannot vanish for h nonzero.
    h1,h2,h3=S.symbols('h1 h2 h3');h=h1*x+h2*y+h3*z
    assert S.expand(sum(S.diff(h*v,v) for v in variables)-4*h)==0

    cert={'date':'2026-11-15','scope':'H3-specific exclusions using pinned as4 graded algebra results',
          'as4_commit':'60eacafa28156a5fc62f74eae004d64a84675f4b',
          'conventions':'as4 nu = inverse of project mu; both right twists u*v=u H^deg(u)(v)',
          'unipotent_W1_witnesses':reports,
          'spectral_scalar_gcd':'gcd(l^3-1,l^4-1)=l-1',
          'Ore_special_center_witness':{'G':str(f),'delta':list(map(str,delta)),
                                         'divergence':0,'delta_G':0},
          'Tate_identities':'d1*d2=(0,0,0,F); d2*d3=(0|F I3); d3*d4=d4*d3=F I4',
          'axis_point_self_Ext_Betti_numbers_degrees0_to12':betti,
          'shear_divergence':'div(h*Euler)=4h',
          'limits':['All-parameter exclusions and infinite Ext are ordinary proofs, not finite-rank extrapolations.',
                    'Not all AS4 coverage, all Z-algebras, relative descent or global H3 classification.',
                    'Existing as4 coverage dependencies retain their explicit audit limitations.']}
    Path(__file__).with_name('cubic_as4_reductions_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: 8 exact unipotent W1 rank20 witnesses over QQ/QQ(zeta3); convention inversion; universal Tate identities; Ore special central cubic; spectral and shear identities')

if __name__=='__main__':main()
