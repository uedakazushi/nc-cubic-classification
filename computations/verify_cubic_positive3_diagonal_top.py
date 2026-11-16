#!/usr/bin/env python3
"""Exact Ore model and universal cubic-weight gcds for the (3,1) diagonal chart."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    a=S.symbols('a',nonzero=True)
    def add(*terms):
        out={}
        for scalar,poly in terms:
            for w,c in poly.items():out[w]=S.cancel(out.get(w,0)+scalar*c)
        return {w:c for w,c in out.items() if c!=0}
    def mono(w,v):
        i,j,k,l=w;I,J,K,L=v
        cc=(-a)**(l*(I+J))*a**(-2*l*K)*(-1)**(I*J*(l%2))
        if l%2:I,J=J,I
        cc*=a**(-k*(I+J))*(-1)**(j*I)
        return S.cancel(cc),(i+I,j+J,k+K,l+L)
    def mul(u,v):
        return add(*[(c*d*mono(w,z)[0],{mono(w,z)[1]:S.Integer(1)}) for w,c in u.items() for z,d in v.items()])
    r,s,x,y=[{tuple(int(i==j) for i in range(4)):S.Integer(1)} for j in range(4)]
    v=add((S.Rational(1,2),r),(S.Rational(1,2),s))
    z=add((S.Rational(1,2),r),(-S.Rational(1,2),s))
    assert not add((1,mul(r,s)),(1,mul(s,r)))
    assert not add((1,mul(x,y)),(-a*a,mul(y,x)))
    for gg,hh,cc in [(z,x,a),(z,y,1/a),(v,x,a),(v,y,-1/a)]:
        assert not add((1,mul(gg,hh)),(-cc,mul(hh,gg)))
    assert mul(v,v)==mul(z,z)
    # Associativity of the explicit iterated-Ore monomial product, on all
    # triples of generator monomials, verifies the swap and scalar conventions.
    generators=list(r)+list(s)+list(x)+list(y)
    for ww,uu,tt in itertools.product(generators,repeat=3):
        c1,w1=mono(ww,uu);c2,w2=mono(w1,tt)
        d1,v1=mono(uu,tt);d2,v2=mono(ww,v1)
        assert w2==v2 and S.cancel(c1*c2-d1*d2)==0
    # mu(v)=v, mu(z)=-z, mu(x)=x, mu(y)=y.
    # In each outer degree n, its fixed subspace has dimensions1,1,1,2.
    fixed=[]
    for n in range(4):
        basis=[(i,n-i) for i in range(n+1)]
        M=S.zeros(n+1)
        for j,(i,k) in enumerate(basis):M[basis.index((k,i)),j]=(-1)**(i*k)
        fixed.append(len((M-S.eye(n+1)).nullspace()))
    assert fixed==[1,1,1,2]
    assert sum(fixed[n]*(4-n) for n in range(4))==11
    def gcd_laurent(polys):
        numerators=[S.Poly(S.cancel(p).as_numer_denom()[0],a) for p in polys if S.cancel(p)!=0]
        if not numerators:return S.Integer(0)
        gg=numerators[0]
        for qq in numerators[1:]:gg=S.gcd(gg,qq)
        # a is a unit, so remove its factors.
        expr=gg.monic().as_expr()
        while expr.subs(a,0)==0:expr=S.cancel(expr/a)
        return S.factor(expr)
    # For n=1 or3, x/y commutation alone kills every fixed cubic.
    eliminated=[]
    for n in [1,3]:
        for i in range(4-n):
            j=3-n-i
            polynomials=[a**(n-2*j)-1,(-1)**n*a**(2*i-n)-1]
            assert gcd_laurent(polynomials)==1
            eliminated.append([i,j,n])
    # For n=0 or2, fixed cubics are x^i*y^j*v^n. All four normality
    # equations are scalar on each such word, so no cross-cancellation.
    survivors={}
    for n in [0,2]:
        for i in range(4-n):
            j=3-n-i
            conditions=[a**(n-2*j)-1,a**(2*i-n)-1,
                        (-1)**j*a**(i-j)-1,a**(i-j)+1]
            gg=gcd_laurent(conditions)
            survivors[f'x^{i} y^{j} v^{n}']=str(gg)
    assert survivors=={'x^0 y^3 v^0':'(a + 1)*(a**2 - a + 1)',
                        'x^1 y^2 v^0':'1','x^2 y^1 v^0':'a + 1','x^3 y^0 v^0':'1',
                        'x^0 y^1 v^2':'a + 1','x^1 y^0 v^2':'1'}
    # Direct normality of the universal resonant candidate y³ modulo a³+1.
    for gg,sign in [(x,1),(y,1),(v,1),(z,-1)]:
        cubic=mul(mul(y,y),y)
        out=add((1,mul(cubic,gg)),(-sign,mul(gg,cubic)))
        assert all(S.rem(S.cancel(cc).as_numer_denom()[0],a**3+1,a)==0 for cc in out.values())
    data={
      'top_algebra':['xy=a²*yx','zx=a*xz','zy=a^-1*yz','vx=a*xv','vy=-a^-1*yv','v²=z²'],
      'Ore_PBW':'r=v+z,s=v-z; basis r^i*s^j*x^k*y^l; rs=-sr, x scales r/s by a^-1, y swaps r/s with factor -a',
      'actual_Nakayama':'(x,y,v,z)->(x,y,v,-z)',
      'fixed_cubic_dimension':11,'outer_fixed_dimensions':fixed,
      'normality_gcd_by_remaining_monomial':survivors,
      'normal_kernel':{'a³!=-1':'0','a³=-1 and a!=-1':'k*y³','a=-1':'y*span(x²,y²,v²)'},
      'filtered_consequence':'Any 14641 presentation with these weighted leading relations has W1=0 if a³!=-1, including all lower-weight base/cross/square corrections preserving the specified Nakayama action.',
      'scope':'Exact Ore identities, all scalar-weight gcds and candidate normality. Resonant leading factors do not prove factorization of deformed cubics; full (3,1) coverage is not asserted.'}
    path=Path(__file__).with_name('cubic_positive3_diagonal_top_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS (3,1) diagonal Ore top: complete cubic kernel and nonresonant filtered exclusion')


if __name__=='__main__':main()
