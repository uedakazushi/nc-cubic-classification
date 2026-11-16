#!/usr/bin/env python3
"""Polynomial identities for the exclusion of the split Jordan2+1 sector.

The manuscript proves the global reduction to these identities.  This script
checks them over Q[c,d,kappa], without specializing the parameters.
"""
import json
from functools import lru_cache
from pathlib import Path
import sympy as S


def main():
    c,d,k=S.symbols('c d kappa')
    A,B,C,L,M,N=S.symbols('A B C L M N')
    def add(*terms):
        out={}
        for scalar,poly in terms:
            for word,coeff in poly.items():
                out[word]=S.expand(out.get(word,0)+scalar*coeff)
        return {w:a for w,a in out.items() if a!=0}
    # x=0, y=1, v=2.  The only reductions move x to the left.
    @lru_cache(None)
    def nf(word):
        for i in range(len(word)-1):
            pair=word[i:i+2]
            if pair in [(1,0),(2,0)]:
                image={(0,1):1,(0,0):k} if pair==(1,0) else {(0,2):c,(0,0):d}
                return add(*[(a,nf(word[:i]+w+word[i+2:])) for w,a in image.items()])
        return {word:S.Integer(1)}
    def mul(p,q):
        return add(*[(a*b,nf(u+v)) for u,a in p.items() for v,b in q.items()])
    def deriv(p):
        terms=[]
        for w,a in p.items():
            for i,j in enumerate(w):
                if j==1:terms.append((a,nf(w[:i]+(0,)+w[i+1:])))
        return add(*terms)
    def substitute(p,values):
        return add(*[(a.subs(values),{w:S.Integer(1)}) for w,a in p.items()])
    x={(0,):S.Integer(1)};v={(2,):S.Integer(1)}
    Z={(2,1):S.Integer(1),(1,2):-c,(0,1):-d}
    generic={(1,1):A,(0,1):B,(0,0):C,(1,2):L,(2,1):M,(0,2):N}
    assert deriv(generic)=={(0,1):2*A,(0,0):A*k+B+M*d,(0,2):L+c*M}
    invariant=add((C,{(0,0):S.Integer(1)}),(M,Z),(N,{(0,2):S.Integer(1)}))
    assert not deriv(invariant)
    assert not add((1,mul(Z,x)),(-c,mul(x,Z)),(k*c*d,{(0,0,0):S.Integer(1)}))
    anti=add((1,mul(invariant,x)),(1,mul(x,invariant)))
    rhs=mul(x,add(((1+c)*M,Z),((1+c)*N,{(0,2):S.Integer(1)}),
                  (2*C+N*d-k*c*d*M,{(0,0):S.Integer(1)})))
    assert not add((1,anti),(-1,rhs))
    # After forcing c=-1 and translating v to make d=0, the invariant
    # subspace is <x^2,xv,vy+yv>.  The last two anticommute with x.
    normal= {c:-1,d:0}
    commute=substitute(add((1,mul(invariant,x)),(-1,mul(x,invariant))),normal)
    expected=mul(x,add((-2*M,{(2,1):S.Integer(1),(1,2):S.Integer(1)}),
                       (-2*N,{(0,2):S.Integer(1)})))
    assert not add((1,commute),(-1,expected))
    # The nilpotent linear combination at v^2=C*x^2 is a domain obstruction.
    linear_square=substitute(add((1,mul(v,x)),(1,mul(x,v))),normal)
    assert not linear_square
    data={
      'hypotheses':'H3, Nakayama multiplicities (1,3), split nontrivial Jordan block on W',
      'D_on_generators':{'x':'0','y':'x','p':'0','v':'0'},
      'cross_relation':'vx=c*xv+d*x², c!=0',
      'invariant_even_basis':['x²','xv','Z=vy-c*yv-d*xy'],
      'normalizer_identity':'Zx=c*xZ-kappa*c*d*x³',
      'p_square_constraint':['(1+c)*M=0','(1+c)*N=0','2*C+N*d-kappa*c*d*M=0'],
      'conclusion':'c=-1; a shift makes d=0; v²=Cprime*x² gives a nonzero square-zero linear combination, contradicting the domain hypothesis',
      'scope':'Exact polynomial identities executed; the global reduction, independence and domain argument are proved in the manuscript. This does not classify the remaining semisimple sector.'}
    path=Path(__file__).with_name('cubic_order2_split_jordan_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS split Jordan invariant-space and normalizer identities over Q[c,d,kappa]')


if __name__=='__main__':main()
