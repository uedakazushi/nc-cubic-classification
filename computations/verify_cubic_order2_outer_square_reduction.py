#!/usr/bin/env python3
"""Exact matrix identities and positive-family calibration for the outer-square reduction."""
import json
from pathlib import Path
import sympy as S


def main():
 a,r,s,h,t=S.symbols('a r s h t')
 F=S.diag(a,-1/a);q=-a*a;mu=S.diag(q,1/q)
 assert (F**2+mu).applyfunc(S.cancel)==S.zeros(2)
 anti=S.Matrix([[0,r],[s,0]]);Q=S.Matrix([[0,1],[1,0]])
 assert anti*Q*anti.T==r*s*Q
 assert anti.det()==-r*s
 def mul(u,v):
  out={}
  for i,x in u.items():
   for j,y in v.items():out[i,j]=out.get((i,j),0)+x*y
  return out
 def add(*terms):
  out={}
  for c,p in terms:
   for w,d in p.items():out[w]=S.expand(out.get(w,0)+c*d)
  return {w:c for w,c in out.items() if c!=0}
 # Clifford swap quotient by W=<t,z+h(x+y)/2>.
 x={0:S.Rational(1,2),1:S.Rational(1,2)}
 y={0:-S.Rational(1,2),1:S.Rational(1,2)}
 z={1:-h/2}
 r1=add((1,mul(y,z)),(1,mul(z,x)),(-h,mul(x,y)))
 r2=add((1,mul(z,y)),(1,mul(x,z)),(-h,mul(y,x)))
 r3=add((1,mul(x,x)),(1,mul(y,y)),(-h,mul(z,z)))
 assert not add((1,r1),(-1,r2))
 rsum=add((1,r1),(1,r2))
 assert rsum=={(0,0):h/2,(1,1):-3*h/2}
 assert r3=={(0,0):S.Rational(1,2),(1,1):S.Rational(1,2)-h**3/4}
 M=S.Matrix([[rsum.get(w,0) for w in [(0,0),(1,1)]],[r3.get(w,0) for w in [(0,0),(1,1)]]])
 assert S.expand(M.det()-h*(8-h**3)/8)==0
 data={'global_result':'Every H3 envelope with multiplicities(1,3) has B/(W)=k<p,v>/(p²,v²); the negative unipotent extension of W splits.',
       'remaining_Jordan_types':['semisimple negative block','split Jordan2+1 with W carrying Jordan2'],
       'quantum_identity':'f²=-mu_T for f=diag(a,-a^-1), q=-a²',
       'anti_identity':'At q=-1, det(anti)=-hdet(anti), so both cannot equal-1',
       'Clifford_swap_square_minor':'h*(8-h³)/8',
       'scope':'Rational-normalizer impossibility, finite-central division growth and global rank reduction are proved in the manuscript. This verifier checks matrix identities and a known admissible-family calibration, not arbitrary rational functions by sampling.'}
 path=Path(__file__).with_name('cubic_order2_outer_square_reduction_certificate.json')
 if path.exists():assert json.loads(path.read_text())==data
 else:path.write_text(json.dumps(data,indent=2)+'\n')
 print('PASS quantum/anti identities and Clifford-swap rank-two square calibration')


if __name__=='__main__':main()
