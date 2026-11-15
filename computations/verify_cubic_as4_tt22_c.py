#!/usr/bin/env python3
"""All-parameter PBW/torus identities for the displayed TT22 C_r family.

Centre and reduced-norm arguments are proved in the paper, not sampled.
No all-CY coverage or AS4 existence theorem is imported from as4.
"""
import json
from pathlib import Path
from functools import lru_cache
from itertools import product
import sympy as S


def main():
    q,A,C=S.symbols('q A C');r=(q+1)/(4*(q-1))
    kappa=1/(2*(q*q-1));eta=2*q*(q-1)/(q+1)
    k=2*(q-1)**2/q;L=(q*q+1)/(q+1);s=L*(q-1)/(q*q)
    # Generator indices a,b,c,d; normal order b,d,a,c.
    rules={(3,1):{(1,3):1/q},(0,1):{(1,0):1,(3,3):S.Rational(1,2)},
           (0,3):{(3,0):1/q},(2,1):{(1,2):q},
           (2,3):{(3,2):1,(1,1):-k},(2,0):{(0,2):1/q,(1,3):s}}
    def clean(p):return {w:S.cancel(v) for w,v in p.items() if S.cancel(v)!=0}
    @lru_cache(None)
    def reduce_word(w):
        for i in range(len(w)-1):
            pair=w[i:i+2]
            if pair in rules:
                out={}
                for replacement,coef in rules[pair].items():
                    for word,value in reduce_word(w[:i]+replacement+w[i+2:]).items():out[word]=out.get(word,0)+coef*value
                return clean(out)
        return {w:S.Integer(1)}
    overlaps=[]
    for w in product(range(4),repeat=3):
        if w[:2] not in rules or w[1:] not in rules:continue
        reductions=[]
        for pos in [0,1]:
            out={}
            for repl,coef in rules[w[pos:pos+2]].items():
                for word,value in reduce_word(w[:pos]+repl+w[pos+2:]).items():out[word]=out.get(word,0)+coef*value
            reductions.append(clean(out))
        assert reductions[0]==reductions[1]
        overlaps.append(list(w))
    assert len(overlaps)==4
    # Laurent quantum torus: d*b=q^-1*b*d, A,C polynomial central variables.
    def add(*ps):
        out={}
        for p in ps:
            for e,v in p.items():out[e]=out.get(e,0)+v
        return clean(out)
    def scale(z,p):return clean({e:z*v for e,v in p.items()})
    def mul(p,t):
        out={}
        for (e,f),v in p.items():
            for (g,h),w in t.items():
                exponent=(e+g,f+h);out[exponent]=out.get(exponent,0)+v*w*q**(-f*g)
        return clean(out)
    images=[{(-1,0):A,(-1,2):-kappa*q*q},{(1,0):1},
            {(0,-1):C,(2,-1):-eta},{(0,1):1}]
    for pair,terms in rules.items():
        rhs={}
        for w,v in terms.items():rhs=add(rhs,scale(v,mul(images[w[0]],images[w[1]])))
        assert add(mul(images[pair[0]],images[pair[1]]),scale(-1,rhs))=={}
    assert add(mul(images[0],images[1]),scale(kappa,mul(images[3],images[3])))=={(0,0):A}
    assert add(mul(images[2],images[3]),scale(eta,mul(images[1],images[1])))=={(0,0):C}
    # Source TT1/TT3 potential, without any imported regularity conclusion.
    words=list(product(range(4),repeat=2));ix={w:j for j,w in enumerate(words)}
    def comm(i,j,z):return {(i,j):z,(j,i):-z}
    def nadd(*ps):
        out={}
        for p in ps:
            for w,v in p.items():out[w]=out.get(w,0)+v
        return clean(out)
    rels=[nadd({(1,1):1},comm(2,3,(16*r*r-1)/8)),
          nadd({(3,3):1},comm(0,1,-2)),
          nadd({(0,2):-(4*r-1)/2,(2,0):(4*r+1)/2},comm(1,3,-(16*r*r+1)/(8*r))),
          {(0,3):(4*r+1)/2,(3,0):-(4*r-1)/2},
          {(1,2):(4*r+1)/2,(2,1):-(4*r-1)/2},
          {(1,3):-(4*r-1)/2,(3,1):(4*r+1)/2}]
    R=S.Matrix([[p.get(w,0) for p in rels] for w in words])
    symR=S.Matrix([[S.cancel((R[ix[w],j]+R[ix[w[::-1]],j])/2) for j in range(6)] for w in words])
    U=S.zeros(16,6)
    for j,w in enumerate([(1,1),(3,3),(0,2),(0,3),(1,2),(1,3)]):
        if w[0]==w[1]:U[ix[w],j]=1
        else:U[ix[w],j]=S.Rational(1,2);U[ix[w[::-1]],j]=S.Rational(1,2)
    assert symR==U
    zz=S.symbols('z0:6');quad=-zz[2]*zz[5]+zz[3]*zz[4]-zz[0]*zz[1]+zz[5]**2
    potential_matrix=S.hessian(quad,zz)/2
    assert potential_matrix.det()!=0
    W=R*potential_matrix*R.T
    assert all(S.cancel(W[ix[w[:2]],ix[w[2:]]]+W[ix[w[1:3]],ix[(w[3],w[0])]])==0 for w in product(range(4),repeat=4))
    # Source columns match precisely the six torus/PBW relations.
    for relation in rels:
        out={}
        for w,v in relation.items():out=add(out,scale(v,mul(images[w[0]],images[w[1]])))
        assert out=={}
    # Trace of a quadratic linear combination at q^3=1: central exponent only.
    coeffs=S.symbols('l0:4');ell=add(*[scale(v,p) for v,p in zip(coeffs,images)])
    square=mul(ell,ell);q3=S.Poly(q*q+q+1,q)
    def reduce_q3(expr):
        num,den=S.fraction(S.cancel(expr));domain=S.QQ.frac_field(A,C,*coeffs)
        return (S.Poly(num,q,domain=domain).rem(q3)*S.invert(S.Poly(den,q,domain=domain),q3)).rem(q3).as_expr()
    trace_half=0
    for (e,f),v in square.items():
        if e%3==0 and f%3==0:
            assert (e,f)==(0,0)
            trace_half+=S.Rational(3,2)*v
    assert reduce_q3(trace_half-3*(coeffs[0]*coeffs[1]*A+coeffs[2]*coeffs[3]*C))==0
    assert reduce_q3((48*r*r+1))==0
    for image in images:
        cube=mul(mul(image,image),image)
        assert all(reduce_q3(coef)==0 for (e,f),coef in cube.items() if e%3 or f%3)
    cert={'version':'classification-v70','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'presentation':'CY_ZERO_COMMUTATORS_CURVILINEAR_TWO_TWO_COMPLETE.tex TT1-TT3, C_r',
          'parameter_map':str(r),'PBW_order':'b,d,a,c','four_overlaps':overlaps,
          'six_torus_relations_verified':True,'central_quadrics':[str(kappa),str(eta)],
          'potential_cyclic_equations':256,'potential_pair_matrix_determinant':str(potential_matrix.det()),
          'trace_half_at_primitive_cube_root':str(3*(coeffs[0]*coeffs[1]*A+coeffs[2]*coeffs[3]*C)),
          'scope':'Universal identities. Faithfulness, centre3 classification and surjective reduced norm are ordinary paper proofs. No upstream all-CY coverage or existence theorem imported.'}
    Path(__file__).with_name('cubic_as4_tt22_c_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS all q: four PBW diamonds, six faithful-torus identities, cyclic top tensor and cubic-root trace')


if __name__=='__main__':main()
