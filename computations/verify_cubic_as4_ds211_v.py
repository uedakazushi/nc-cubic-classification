#!/usr/bin/env python3
"""Universal square-root-cover PBW/torus/norm identities for DS211 V_h."""
import json
from pathlib import Path
from functools import lru_cache
import sympy as S
from verify_cubic_as4_ds211 import source_matrix,cyclic,ww
from verify_cubic_pym_generic import words


def main():
    p,Z1,Z2=S.symbols('p Z1 Z2');r=(p+1)/(4*(1-p));h=-r*r
    theta=p-1/p;alpha=p*p/(2*(p+1)**2);beta=1/(2*(p+1)**2);gamma=p/(p+1)**2
    t0=(p-1)/(2*(p+1));s0=theta*(1+p*p)/(2*(p+1)**2)
    # Generator indices a',b,x,y; PBW order b,x,y,a'.
    rules={(2,1):{(1,2):1/p},(3,1):{(1,3):p},(3,2):{(2,3):1,(1,1):-theta},
           (0,1):{(1,0):1,(2,2):t0,(3,3):-t0},
           (0,2):{(2,0):1/p,(1,3):s0},(0,3):{(3,0):p,(1,2):-s0}}
    def clean(poly):return {w:S.cancel(z) for w,z in poly.items() if S.cancel(z)!=0}
    @lru_cache(None)
    def red(word):
        for i in range(len(word)-1):
            if word[i:i+2] in rules:
                out={}
                for repl,z in rules[word[i:i+2]].items():
                    for w,v in red(word[:i]+repl+word[i+2:]).items():out[w]=out.get(w,0)+z*v
                return clean(out)
        return {word:S.Integer(1)}
    overlaps=[]
    for word in words(3):
        if word[:2] not in rules or word[1:] not in rules:continue
        results=[]
        for i in [0,1]:
            out={}
            for repl,z in rules[word[i:i+2]].items():
                for w,v in red(word[:i]+repl+word[i+2:]).items():out[w]=out.get(w,0)+z*v
            results.append(clean(out))
        assert results[0]==results[1];overlaps.append(list(word))
    assert len(overlaps)==4
    def add(*polys):
        out={}
        for poly in polys:
            for e,z in poly.items():out[e]=out.get(e,0)+z
        return clean(out)
    def scale(z,poly):return clean({e:z*v for e,v in poly.items()})
    def mul(poly,other):
        out={}
        for (e,f),z in poly.items():
            for (g,j),v in other.items():out[(e+g,f+j)]=out.get((e+g,f+j),0)+z*v*p**(-f*g)
        return clean(out)
    b={(1,0):1};x={(0,1):1};y={(0,-1):Z2,(2,-1):-p}
    ap=mul({(-1,0):1},add({(0,0):Z1},scale(-alpha,mul(x,x)),scale(-beta,mul(y,y))))
    images=[ap,b,x,y]
    for pair,replacements in rules.items():
        rhs={}
        for word,z in replacements.items():rhs=add(rhs,scale(z,mul(images[word[0]],images[word[1]])))
        assert add(mul(images[pair[0]],images[pair[1]]),scale(-1,rhs))=={}
    assert add(mul(x,y),scale(1/p,mul(b,b)))=={(0,0):Z2}
    assert add(mul(b,ap),scale(alpha,mul(x,x)),scale(beta,mul(y,y)))=={(0,0):Z1}
    original=[add(ap,scale(-gamma,b)),b,scale(S.Rational(1,2),add(x,y)),scale(1/(2*r),add(y,scale(-1,x)))]
    R=source_matrix({0:1,7:1,12:h,14:h+S.Rational(1,16),20:h+S.Rational(1,16)});cyclic(R)
    for j in range(6):
        out={}
        for i,word in enumerate(ww):out=add(out,scale(R[i,j],mul(original[word[0]],original[word[1]])))
        assert out=={}
    lam=S.symbols('l0:4');ell=add(*[scale(z,v) for z,v in zip(lam,images)]);square=mul(ell,ell)
    def mod3(z):
        n,d=S.fraction(S.cancel(z));D=S.QQ.frac_field(Z1,Z2,*lam);f=S.Poly(p*p+p+1,p,domain=D)
        return (S.Poly(n,p,domain=D).rem(f)*S.invert(S.Poly(d,p,domain=D),f)).rem(f).as_expr()
    assert S.cancel(h-S.Rational(1,48)+(p*p+p+1)/(12*(p-1)**2))==0
    for image in images:
        assert all(mod3(z)==0 for (e,f),z in image.items() if e%3==0 and f%3==0)
    central_square=0
    for (e,f),z in square.items():
        if e%3==0 and f%3==0:
            if (e,f)==(0,0):central_square+=S.Rational(3,2)*z
            else:assert mod3(z)==0
    expected=3*(lam[0]*lam[1]*Z1+(lam[2]*lam[3]+lam[0]**2/4)*Z2)
    assert mod3(central_square-expected)==0
    for image in [b,x,y]:
        cube=mul(mul(image,image),image)
        assert all(mod3(z)==0 for (e,f),z in cube.items() if e%3 or f%3)
    na=add(mul(mul(ap,ap),ap),scale(-S.Rational(3,4)*Z2,ap))
    assert all(mod3(z)==0 for (e,f),z in na.items() if e%3 or f%3)
    cert={'version':'classification-v72','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source':'CY_ZERO_COMMUTATORS_DOUBLE_SIMPLE_NONZERO_COMPLETE.tex DS1-DS3, V_h',
          'cover':{'r':str(r),'h':str(h)},'linear_change':{'a_prime':'a+gamma*b','x':'c-r*d','y':'c+r*d','gamma':str(gamma)},
          'alpha':str(alpha),'beta':str(beta),'four_PBW_overlaps':overlaps,
          'six_source_relations_verified':True,'cyclic_top_tensor':True,
          'trace_half_at_cube_root':str(expected),'a_prime_norm':'a_prime^3-(3/4)*Z2*a_prime',
          'centre3_locus':'h=1/48, dimension4; boundary h=0 checked separately',
          'scope':'Exact all-cover identities; injectivity, centre and norm surjectivity are proved in the paper. No upstream AS4 existence/coverage imported.'}
    Path(__file__).with_name('cubic_as4_ds211_v_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS V_h: four PBW diamonds, all source relations, faithful torus, cubic-root trace and monic norm')


if __name__=='__main__':main()
