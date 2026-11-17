#!/usr/bin/env python3
"""Exact original PBW/normal and dehomogenized Casimir/norm identities.
The surface period-index theorem is an external mathematical input, not verified
by this finite calculation. No complete proportional-coupling coverage claimed.
"""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix

def algebra(K,rules,n):
 one,zero=K.one,K.zero
 @lru_cache(None)
 def nf(w):
  for j in range(len(w)-1):
   if w[j:j+2] not in rules:continue
   out={}
   for rep,c in rules[w[j:j+2]].items():
    for v,d in nf(w[:j]+rep+w[j+2:]).items():out[v]=out.get(v,zero)+c*d
   return {v:c for v,c in out.items() if c}
  return {w:one}
 def add(A,B,scale=one):
  out=dict(A)
  for v,c in B.items():out[v]=out.get(v,zero)+scale*c
  return {v:c for v,c in out.items() if c}
 def mul(A,B):
  out={}
  for a,c in A.items():
   for b,d in B.items():
    for v,e in nf(a+b).items():out[v]=out.get(v,zero)+c*d*e
  return {v:c for v,c in out.items() if c}
 def power(A,j):
  out={():one}
  for _ in range(j):out=mul(out,A)
  return out
 for tr in itertools.combinations(range(n),3):
  w=tuple(reversed(tr));branches=[]
  for j in (0,1):
   branches.append({})
   for rep,c in rules[w[j:j+2]].items():
    for v,d in nf(w[:j]+rep+w[j+2:]).items():branches[-1][v]=branches[-1].get(v,zero)+c*d
   branches[-1]={v:c for v,c in branches[-1].items() if c}
  assert branches[0]==branches[1]
 return nf,add,mul,power

def original(K,q,o,h):
 one=K.one
 rules={(1,0):{(0,1):one/q,(3,3):-h/q},(2,0):{(0,2):q,(1,1):-q},
 (2,1):{(1,2):one/q,(0,0):-one/q},(3,0):{(0,3):o**2},
 (3,1):{(1,3):o},(3,2):{(2,3):one}}
 return algebra(K,rules,4)
# All q,h original critical overlaps, not finite parameter sampling.
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z))
qv,hv=s.symbols('q h');L=F.frac_field(qv,hv);lq,lh=L.gens;lo=L.convert(F.to_sympy(F.unit))
original(L,lq,lo,lh)
# Fresh complete primitive9 field, all six embeddings including both omega.
t=s.Symbol('t');phi=s.Poly(t**6+t**3+1,t);assert phi.is_irreducible
K=s.QQ.alg_field_from_poly(phi);q=K.unit;o=q**6;one,zero=K.one,K.zero
nf,add,mul,power=original(K,q,o,one)
basis=[(0,0,0),(1,1,1),(0,1,2),(2,2,2),(0,1,3),(2,2,3),(2,3,3),(3,3,3)]
inv=[o**2,o,one,one];cols=[]
for w in basis:
 out={}
 for j in range(4):
  for v,c in add(nf(w+(j,)),nf((j,)+w),-inv[j]).items():out[j,v]=c
 cols.append(out)
keys=sorted(set().union(*(set(c) for c in cols)))
M=DomainMatrix.from_dod({r:{j:c[k] for j,c in enumerate(cols) if k in c} for r,k in enumerate(keys)},(len(keys),8),K)
assert M.rank()==7
cor=(2+o+(4*o-one)*q-(one+2*o)*q*q)/3
coeff=[q*(2+o)/3,q*q*(1+2*o)/3,q*o**2,one,zero,zero,cor,zero]
for i in range(M.shape[0]):assert sum((M.to_list()[i][j]*coeff[j] for j in range(8)),zero)==zero
# Dehomogenization x^{-1}: capital B,C,Y; exact original six relations
# become the following three, with x acting by (omega^2,omega,1).
Q=q*o;kap=o**2;alpha=o**2*q;beta=o/q
rules={(1,0):{(0,1):one/Q,():-kap/Q},(2,0):{(0,2):Q,(1,1):-alpha},
       (2,1):{(1,2):one/Q,(0,0):-beta}}
nf,add,mul,power=algebra(K,rules,3)
B={(0,):one};C={(1,):one};Y={(2,):one}
z=add(mul(B,C),mul(C,B),-one);S=one+Q+Q**2
H={(1,)*3:alpha*Q**2/S,(0,)*3:-beta/S};Z=add(mul(z,Y),H,-one)
assert not add(mul(z,B),mul(B,z),-one/Q)
assert not add(mul(z,C),mul(C,z),-Q)
for V in [B,C,Y]:assert not add(mul(Z,V),mul(V,Z),-one)
g={(2,)*3:one,(0,1,2):q,(0,)*3:coeff[0],(1,)*3:coeff[1],(2,):cor}
# Inverse generator substitution b=B*x, c=C*x, y=Y*x in D[x^{+-1};rho].
def rho(A,m):
 return {w:c*o**(m*(2*w.count(0)+w.count(1))) for w,c in A.items()}
def skewmul(A,m,B,n):return mul(A,rho(B,m)),m+n
orig=[B,C,Y,{():one}]
original_relations=[(0,1,q,{():one}),(2,0,q,{(1,1):-q*o}),(2,1,one/q,{(0,0):-o**2/q}),
 (3,0,o**2,{}),(3,1,o,{}),(3,2,one,{})]
for i,j,phase,tail in original_relations:
 left,_=skewmul(orig[i],1,orig[j],1);right,_=skewmul(orig[j],1,orig[i],1)
 assert not add(add(left,right,-phase),tail,-one)
# b^3*x^-3=B^3, c^3*x^-3=C^3, b*c*y*x^-3=omega*B*C*Y.
assert rho(C,1)=={(1,):o}
assert power(B,3)=={(0,)*3:one} and power(C,3)=={(1,)*3:one}
for V,phase in [(B,o**2),(C,o),(Y,one)]:assert not add(mul(g,V),mul(V,g),-phase)
for V in [B,C,Y]:
 for w in [(0,)*9,(1,)*9]:assert not add(mul(nf(w),V),mul(V,nf(w)),-one)
assert power(z,9)=={():kap**9,(0,)*9+(1,)*9:(Q-one)**9}
diff=add(mul(power(z,3),g),power(Z,3),-one)
a=diff[(2,)]/Z[(2,)];rest=add(diff,Z,-a)
assert set(rest)=={(0,)*9,(1,)*9};b=rest[(1,)*9];c=rest[(0,)*9]
assert a==(-q**5+2*q**4-q**3-2*q**2+q-2)/3
assert b==(-q**5+q**4+q**3-2*q**2-q+1)/3
assert c==(-2*q**5-q**4+q**3-q**2-2*q)/3
assert a and b and c
assert a**3*(Q-one)**9==27*kap**9*b*c
# Algebraic norm identity after the constant rescaling in the ordinary proof.
u,T,v=s.symbols('u T v')
assert s.expand(s.resultant(v**3-u,v*v-T*v+1,v))==s.expand(1-u*(T**3-3*T)+u**2)
# a=-3*rho^2; nu=(Q-1)^9*rho^3/(b*kap^9).
# The preceding Chebyshev equality is exactly -((Q-1)^9*c/(b*kap^9))=nu^2.
coeff_record={name:[str(x) for x in val.to_list()] for name,val in [('a',a),('b',b),('c',c)]}
out={'status':'PASS','scope':'all-q,h original PBW; fresh primitive9 normal kernel; dehomogenized Casimir, center relation, quantum-Weyl power and norm identities',
 'all_parameter_cubic_overlaps':4,'primitive9_field':'QQ[t]/(t^6+t^3+1), omega=t^6',
 'primitive9_h1_normal_matrix_shape':list(M.shape),'primitive9_h1_normal_rank':7,
 'central_identity':'z^3*g = Z^3+a*Z+b*C^9+c*B^9',
 'a_b_c_descending_t_coefficients':coeff_record,
 'quantum_Weyl_identity':'z^9=kappa^9+(Q-1)^9*B^9*C^9',
 'Chebyshev_identity':'a^3*(Q-1)^9=27*kappa^9*b*c',
 'norm_identity':'Norm_{s^3=u}(s^2-T*s+1)=1-u*(T^3-3*T)+u^2',
 'external_input':{'author':'Max Lieblich','title':'Twisted sheaves and the period-index problem',
 'arxiv':'math/0511244v4','theorem':'4.2.2.3, p23','url':'https://arxiv.org/pdf/math/0511244',
 'pdf_sha256':'8de9324c08bf75289887df7cb01ba684e52fa174872c1222d7a71beb9fd7d10f',
 'hypotheses':'function field of transcendence degree2 over algebraically closed field',
 'conclusion':'period=index for every Brauer class','read_status':'statement, surrounding definitions and printed proof read; full deep proof not independently audited',
 'journal':'Compositio Mathematica 144(1) (2008), 1-31','doi':'10.1112/S0010437X07003144'},
 'not_claimed':['program verifies Brauer period-index theorem','exact Goldie rank3','all rank1 cube couplings covered','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_deformed_double_Ore_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','primitive9_normal_dimension':1,'Casimir_and_norm_identities':True}))
