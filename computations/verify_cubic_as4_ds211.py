#!/usr/bin/env python3
"""Independent exact DS211 two-parameter and exceptional-family exclusions."""
import json
from pathlib import Path
from functools import lru_cache
from itertools import product
from math import gcd
from verify_cubic_pym_generic import S, words
Q=S.Rational;ww=words(2);ix={w:j for j,w in enumerate(ww)};U=S.zeros(16,6)
for col,pair in enumerate([(1,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):
 if pair[0]==pair[1]:U[ix[pair],col]=1
 else:U[ix[pair],col]=Q(1,2);U[ix[pair[::-1]],col]=Q(1,2)
K=S.zeros(16,6)
for col,(i,j) in enumerate([(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):K[ix[(i,j)],col]=1;K[ix[(j,i)],col]=-1
z=S.symbols('z0:6');quad=-z[1]*z[4]+z[2]*z[3]-z[0]*z[5]+z[3]*z[4];A=S.hessian(quad,z)/2;AI=A.inv()
def source_relations(vals):
 x=[S.sympify(vals.get(j,0)) for j in range(21)];B=S.Matrix([[x[0],x[6]/2,x[10]/2,x[1],x[2],(x[9]-x[13])/2],[0,x[3],x[4],x[7],x[11]-x[15],-x[16]],[0,x[4],x[5],x[11]-x[15],x[12],x[17]],[x[6],x[7],x[11],x[8],x[9],-x[18]],[x[10],x[11],x[12],x[13],x[14],x[19]],[x[15],x[16],x[17],x[18],x[19],x[20]]]);R=U+K*B.T*AI
 return [{w:S.factor(R[j,col]) for j,w in enumerate(ww) if R[j,col]} for col in range(6)]

def source_matrix(vals):
 rr=source_relations(vals)
 return S.Matrix([[row.get(w,0) for row in rr] for w in ww])

def cyclic(R):
 W=R*A*R.T
 assert all(S.cancel(S.expand(W[ix[v[:2]],ix[v[2:]]]+W[ix[v[1:3]],ix[(v[3],v[0])]]))==0 for v in words(4))

def main():
 l,r=S.symbols('l r');q=(4*l+1)/(4*l-1);beta=-1/(4*l)
 u=-(16*l*r+1)/(2*l*(16*l*l-1));v=8*(l+r)/(16*l*l-1)
 delta=l+1/(16*l)
 RA=source_matrix({15:-2*l,11:-l,9:r,13:r+delta});RB=source_matrix({15:-S.I/2,11:-S.I/4,9:r,13:r,20:1})
 cyclic(RA);cyclic(RB)
 rules={(2,1):{(1,2):q},(3,1):{(1,3):1/q},(3,2):{(2,3):q*q},
        (0,1):{(1,0):1,(1,1):beta},(0,2):{(2,0):1/q,(1,2):u},(0,3):{(3,0):q,(1,3):v}}
 def clean(p):return {w:S.cancel(z) for w,z in p.items() if S.cancel(z)!=0}
 @lru_cache(None)
 def red(w):
  for i in range(len(w)-1):
   if w[i:i+2] in rules:
    out={}
    for repl,z in rules[w[i:i+2]].items():
     for word,y in red(w[:i]+repl+w[i+2:]).items():out[word]=out.get(word,0)+z*y
    return clean(out)
  return {w:S.Integer(1)}
 overlaps=[]
 for word in words(3):
  if word[:2] not in rules or word[1:] not in rules:continue
  output=[]
  for i in [0,1]:
   out={}
   for repl,z in rules[word[i:i+2]].items():
    for w,y in red(word[:i]+repl+word[i+2:]).items():out[w]=out.get(w,0)+z*y
   output.append(clean(out))
  assert output[0]==output[1];overlaps.append(list(word))
 assert len(overlaps)==4
 for j in range(6):
  out={}
  for i,w in enumerate(ww):
   for word,z in red(w).items():out[word]=out.get(word,0)+RA[i,j]*z
  assert clean(out)=={}
 left_inverse=(U.T*U).inv()*U.T
 sigma_b=S.diag(1,1,1/q,q);sigma_b[1,0]=-beta
 sigma_c=S.diag(-S.I,-S.I,1,-1);sigma_c[1,0]=1+4*S.I*r
 sigma_d=S.diag(S.I,S.I,-1,1);sigma_d[1,0]=4*S.I*r-1
 for R,g,sigma in [(RA,1,sigma_b),(RB,2,sigma_c),(RB,3,sigma_d)]:
  for i in range(4):
   target=S.zeros(16,1);target[ix[(g,i)]]+=1
   for j in range(4):target[ix[(j,g)]]-=sigma[j,i]
   assert all(S.cancel(z)==0 for z in R*left_inverse*target-target)
 minus=sigma_c**3*sigma_d;assert (minus+S.eye(4))**2==S.zeros(4)
 weights=[]
 for i,j,k in product(range(4),repeat=3):
  if i+j+k!=3:continue
  gg=gcd(abs(j-k),abs(i-2*k));assert gg==(3 if max(i,j,k)==3 else 1)
  weights.append({'exponents':[i,j,k],'weights':[j-k,i-2*k],'gcd':gg})
 # Ore commutators of cubes at q^3=1.
 def mod3(z):
  num,den=S.fraction(S.cancel(z));D=S.QQ.frac_field(r);f=S.Poly(48*l*l+1,l,domain=D)
  return (S.Poly(num,l,domain=D).rem(f)*S.invert(S.Poly(den,l,domain=D),f)).rem(f).as_expr()
 for x,coef in [(1,beta),(2,u),(3,v)]:
  out=red((0,x,x,x)).copy()
  for w,z in red((x,x,x,0)).items():out[w]=out.get(w,0)-z
  for w,z in red((1,x,x,x)).items():out[w]=out.get(w,0)-3*coef*z
  assert all(mod3(z)==0 for z in out.values())
 assert S.cancel(u.subs(r,-1/(16*l)))==0 and S.cancel(v.subs(r,-l))==0
 assert mod3((-1/(16*l))-3*l)==0
 cert={'version':'classification-v71','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
       'presentation_sources':['CY_ZERO_COMMUTATORS_DOUBLE_SIMPLE_NONZERO_COMPLETE.tex DS1-DS2','CY_ZERO_COMMUTATORS_DOUBLE_SIMPLE_SECOND_COMPLETE.tex DT1'],
       'A_parameters':{'q':str(q),'beta':str(beta),'u':str(u),'v':str(v)},
       'four_PBW_overlaps':overlaps,'cyclic_tensor_equations_per_family':256,
       'A_normalizer_b':[[str(z) for z in sigma_b.row(i)] for i in range(4)],
       'B_normalizer_c3d':[[str(z) for z in minus.row(i)] for i in range(4)],
       'base_cubic_weight_table':weights,
       'A_centre3_loci':['48*l^2+1=0, r=3*l: k*c^3','48*l^2+1=0, r=-l: k*d^3'],
       'scope':'Independent all-parameter identities and paper proof; no upstream AS4 existence or full coverage imported.'}
 Path(__file__).with_name('cubic_as4_ds211_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
 print('PASS DS211 A/B cyclic tensors, PBW/Ore identities, normalizers and exact cubic loci')

if __name__=='__main__':main()
