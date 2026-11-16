#!/usr/bin/env python3
"""Independent polynomial replay of the full order-three 2+2 H3 incidence.
No Singular installation is needed to replay the committed membership witness.
"""
import json,time
from pathlib import Path
from functools import lru_cache
import sympy as S


def build_model():
    w=S.symbols('w');hs=S.symbols('h0:10');ring=S.QQ.poly_ring(*hs);t=time.time()
    def red(e):return S.Poly(S.expand(e),w,domain=ring).rem(S.Poly(w*w+w+1,w,domain=ring)).as_expr().expand()
    mu=[w,w,w*w,w*w];A=[0,1];C=[2,3];ac=[(i,j) for i in A for j in C];ca=[(j,i) for j in C for i in A]
    ra={(0,1):1,(1,0):-w};rc={(2,3):1,(3,2):-w*w};top={}
    def orbit(word,c):
     for j in range(4):
      if word in top:assert red(top[word]-c)==0
      else:top[word]=red(c)
      c=red(-mu[word[0]]*c);word=word[1:]+word[:1]
    for aa,x in ra.items():
     for cc,y in rc.items():orbit(aa+cc,x*y)
    H=S.zeros(4);k=0
    for i in range(4):
     for j in range(i,4):H[i,j]=H[j,i]=hs[k];k+=1
    for i,aa in enumerate(ac):
     for j,bb in enumerate(ac):orbit(aa+bb,H[i,j])
    basis=ac+ca;W=S.Matrix(8,8,lambda i,j:top.get(basis[i]+basis[j],0));HH=W[:4,:4];J=W[:4,4:];KK=W[4:,:4];LL=W[4:,4:]
    def inverse_monomial(M):
     N=S.zeros(4)
     for i in range(4):
      non=[j for j in range(4) if M[i,j]!=0];assert len(non)==1;j=non[0]
      N[j,i]=S.invert(M[i,j],w*w+w+1,w)
     assert all(red(e)==0 for e in M*N-S.eye(4))
     return N
    cross=(HH*inverse_monomial(KK)).applyfunc(lambda e:red(-e));rank_equations=[red(e) for e in KK-LL*inverse_monomial(J)*HH]
    rules={(1,0):{(0,1):w*w},(3,2):{(2,3):w}}
    for j,p in enumerate(ca):rules[p]={v:cross[i,j] for i,v in enumerate(ac) if cross[i,j]!=0}
    def add(out,word,c):
     out[word]=red(out.get(word,0)+c)
     if out[word]==0:del out[word]
    @lru_cache(None)
    def nf(word):
     for k in range(len(word)-1):
      if word[k:k+2] in rules:return at(word,k)
     return {word:S.Integer(1)}
    def at(word,k):
     out={}
     for rep,c in rules[word[k:k+2]].items():
      for v,x in nf(word[:k]+rep+word[k+2:]).items():add(out,v,c*x)
     return out
    def difference(x,y,scale=1):
     out=dict(x)
     for v,c in y.items():add(out,v,-scale*c)
     return list(out.values())
    diamond=[]
    for word in [(2,1,0),(3,1,0),(3,2,0),(3,2,1)]:diamond+=difference(at(word,0),at(word,1))
    normal=[]
    for aa in [0,1]:normal+=difference(nf((2,2,3,aa)),nf((aa,2,2,3)),w*w)
    for cc in [2,3]:normal+=difference(nf((0,0,1,cc)),nf((cc,0,0,1)),w)
    equations=[];seen=set()
    for e in rank_equations+diamond+normal:
     e=red(e)
     if not e:continue
     key=str(e)
     if key not in seen:seen.add(key);equations.append(e)
    return {'w':w,'hs':hs,'red':red,'top':top,'H':H,'cross':cross,'rank':rank_equations,'diamonds':diamond,'normal':normal,'equations':equations,'nf':nf,'ac':ac}


def main():
    model=build_model();w,hs,red=model['w'],model['hs'],model['red'];I=model['equations'];nf=model['nf'];H=model['H'];loc={'w':w,**{str(h):h for h in hs}}
    data=json.loads(Path(__file__).with_name('cubic_order3_two_block_incidence_certificate.json').read_text())
    stored=[S.sympify(e,locals=loc) for e in data['input_polynomials']];assert len(I)==len(stored) and all(red(a-b)==0 for a,b in zip(I,stored))
    G=[S.sympify(e.replace('^','**'),locals=loc) for e in data['G']];out=[-e for e in G]
    for i,j,e in data['X']:
        assert 0<=i<len(I) and 0<=j<len(G)
        out[j]+=I[i]*S.sympify(e.replace('^','**'),locals=loc)
    assert all(red(e)==0 for e in out)
    # These are explicit polynomial consequences, not a second trust in a GB.
    F=S.QQ.algebraic_field(S.sqrt(-3));om=(-1+S.sqrt(-3))/2
    def monic(e):return S.Poly(e.subs(w,om),*hs,domain=F).monic()
    gset={monic(e) for e in G};assert monic((hs[5]-w*w)*(3*hs[5]-w-2)) in gset
    assert red(w*w-(w+2)/3)!=0
    for root in [w*w,(w+2)/3]:
        sub={hs[5]:root};branch={monic(e.subs(sub)) for e in G}
        if root==w*w:
            for i in [0,1,2,4,6,7,8,9]:assert monic(hs[i]) in branch
            assert monic(hs[3]+w*w) in branch
        else:
            for e in [hs[3]+(2*w+1)/3,hs[0]*hs[9]-2*w/3,hs[1]*hs[8]+w/3,hs[2]*hs[6]+w/3,6*hs[1]*hs[2]+(w-1)*hs[0],2*hs[1]**2+hs[0]*hs[4],2*hs[2]**2+hs[0]*hs[7]]:assert monic(e) in branch
    p,q=S.symbols('p q',nonzero=True);K=S.QQ.frac_field(p,q)
    def rp(e):return S.Poly(S.cancel(e),w,domain=K).rem(S.Poly(w*w+w+1,w,domain=K)).as_expr()
    param={hs[0]:2*(w+2)*p*q,hs[1]:p,hs[2]:q,hs[3]:-(2*w+1)/3,hs[4]:(w-1)*p/(3*q),hs[5]:(w+2)/3,hs[6]:-w/(3*q),hs[7]:(w-1)*q/(3*p),hs[8]:-w/(3*p),hs[9]:(2*w+1)/(9*p*q)}
    assert all(rp(e.subs(param))==0 for e in I+G)
    known={h:0 for h in hs};known[hs[3]]=-w*w;known[hs[5]]=w*w
    assert all(red(e.subs(known))==0 for e in I+G)
    canonical={h:red(e.subs({p:1,q:1})) for h,e in param.items()}
    for i,first in enumerate(model['ac']):
        for j,second in enumerate(model['ac']):
            word=first+second;weight=p**(1-word.count(0))*q**(1-word.count(2))
            assert rp(H[i,j].subs(param)*weight-H[i,j].subs(canonical))==0
    # Independent noncommutative factorisation at the non-skew representative.
    tau=S.symbols('tau');linear={(0,):1,(2,):tau}
    quadratic={(0,1):tau,(0,2):tau*tau*w*w,(0,3):-tau*tau*(2*w+1)/3,(1,2):-tau*tau*(2*w+1)/3,(1,3):-tau*tau/3,(2,3):1}
    product={}
    for a,c in linear.items():
        for b,d in quadratic.items():
            for word,e in nf(a+b).items():product[word]=product.get(word,0)+c*d*e.subs(canonical)
    for word in set(product)|{(0,0,1),(2,2,3)}:
        value=product.get(word,0)-(tau if word in [(0,0,1),(2,2,3)] else 0)
        value=S.Poly(S.expand(value),tau,domain=S.QQ.poly_ring(w)).rem(S.Poly(tau**3-w,tau,domain=S.QQ.poly_ring(w))).as_expr()
        assert S.Poly(value,w,domain=S.QQ.poly_ring(tau)).rem(S.Poly(w*w+w+1,w,domain=S.QQ.poly_ring(tau))).is_zero
    print('PASS 68 regenerated constraints, 30 polynomial membership identities, two branch normal forms and explicit exotic cubic factorisation')

if __name__=='__main__':main()
