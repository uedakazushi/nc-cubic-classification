#!/usr/bin/env python3
"""Original22 top-image and exhaustive Schur identities for proportional
nonzero cube couplings, S=0. Actual AS4/Ore and domain proof is in the paper.
"""
import itertools,json
from pathlib import Path
import sympy as s
from sympy.polys.matrices import DomainMatrix
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));O=s.Symbol('omega');a=s.symbols('a:22')
def red(e):
 e=s.expand(e).replace(lambda n:n.is_Pow and n.base==O and n.exp.is_Integer,lambda n:O**(int(n.exp)%3))
 return s.rem(s.expand(e),O**2+O+1,O)
def expr(c):
 return sum(s.Rational(v.numerator,v.denominator)*O**(len(c.to_list())-j-1) for j,v in enumerate(c.to_list()))
tops=[];seen=set()
for word in itertools.product(range(4),repeat=4):
 if word in seen:continue
 w=word;c=F.one;T={}
 while w not in T:
  T[w]=c;seen.add(w);w=(w[-1],)+w[:-1];c=-c/F.unit**[0,0,1,2][w[0]]
 if c==F.one:tops.append(T)
assert len(tops)==22
H=s.zeros(16)
for aa,T in zip(a,tops):
 for w,c in T.items():H[4*w[0]+w[1],4*w[2]+w[3]]+=aa*expr(c)
base={a[10]:1,a[14]:1,a[18]:0,a[19]:0,a[20]:0}
M=H.extract([2,6,8,9,15],[3,7,10,12,13]).subs(base).applyfunc(red)
res=[]
for j in [1,2,3]:
 row=M[j,:]-M[j,2]*M[0,:]
 row=(row-row[0]/O**2*M[4,:]).applyfunc(red);res.extend(list(row))
A,D,E,Z,T=s.symbols('A D E Z T')
mp={a[2]:A,a[3]:-O**2*A,a[6]:D,a[7]:E,a[8]:Z,a[9]:E,a[11]:D,a[12]:D,a[13]:E,a[15]:0,a[16]:0,a[17]:0}
assert all(red(v.subs(mp))==0 for v in res)
# The pivot residuals have exactly the nine displayed linear constraints.
constraints=[a[17],a[12]-a[6],a[15],a[16],a[13]-a[9],a[9]-a[7],a[3]+O**2*a[2],a[11]-a[12]]
assert len([v for v in res if v])==9
assert s.Matrix([red(v) for v in res]).jacobian(a).rank()==8
H0=H.extract([0,1,4,5,11,14],[0,1,4,5,11,14]).subs(base).subs(mp).applyfunc(red)
K=s.diag(T,-O*T);P=H0[:4,4:].subs(a[21],T)
Schur=(H0[:4,:4]-P*K.inv()*P.T).applyfunc(red)
for eps in [1,-1]:
 dd=eps*O*E
 sub={D:dd,a[0]:A*(dd+O*E)/T,a[1]:0,a[4]:0,a[5]:0}
 assert Schur.subs(sub).applyfunc(red)==s.zeros(4)
# T0,A0 with (D,E)!=0: exact rank2 factorization of the full even block.
R=s.Matrix([0,1,-1,0]);V=s.Matrix([a[0],a[4]/2,a[4]/2,a[5]])
assert (H0[:4,:4].subs({A:0,a[1]:0})-R*V.T-V*R.T).applyfunc(red)==s.zeros(4)

def image_check(K,coeff,rels):
 HH=[[K.zero]*16 for _ in range(16)]
 for aa,top in zip(coeff,tops):
  for w,c in top.items():
   cc=K.zero
   for v in c.to_list():cc=cc*K.convert(F.to_sympy(F.unit))+K.convert(v)
   HH[4*w[0]+w[1]][4*w[2]+w[3]]+=aa*cc
 RR=[[rel.get(divmod(i,4),K.zero) for rel in rels] for i in range(16)]
 def dm(rows):return DomainMatrix.from_list(rows,K)
 h,r=dm(HH),dm(RR)
 assert h.rank()==r.rank()==6 and h.hstack(r).rank()==6
 return HH

def mixed(K,o,A,D,E,Z):
 one=K.one
 return [{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):D,(2,1):E,(3,3):one,(0,2):A+o*Z},
 {(1,3):E,(3,1):D,(2,2):one,(0,3):Z-o**2*A}]
def relations(K,o,A,D,E,Z,q,h,T):
 one=K.one
 return mixed(K,o,A,D,E,Z)+[{(2,3):one,(3,2):-q,(0,0):-h},
 {(1,0):one,(0,1):-one,(0,0):-A/D,(2,3):-T/D}]
params=s.symbols('A E Z T');L=F.frac_field(*params);A0,E0,Z0,T0=L.gens;o=L.convert(F.to_sympy(F.unit));one,zero=L.one,L.zero
records=[]
for eps in [1,-1]:
 DD=eps*o*E0;coeff=[zero]*22
 for i,v in {0:A0*(DD+o*E0)/T0,2:A0,3:-o**2*A0,6:DD,7:E0,8:Z0,9:E0,10:one,11:DD,12:DD,13:E0,14:one,21:T0}.items():coeff[i]=v
 qq=-eps*o**2;hh=-(1+eps)*A0/T0
 image_check(L,coeff,relations(L,o,A0,DD,E0,Z0,qq,hh,T0));records.append({'T_nonzero_branch_sign':eps,'q':str(L.to_sympy(qq))})
# T0,A nonzero and D nonzero, after all even binary coefficients vanish.
params=s.symbols('A D Z');L=F.frac_field(*params);A0,DD,Z0=L.gens;o=L.convert(F.to_sympy(F.unit));one,zero=L.one,L.zero;EE=-o**2*DD
coeff=[zero]*22
for i,v in {2:A0,3:-o**2*A0,6:DD,7:EE,8:Z0,9:EE,10:one,11:DD,12:DD,13:EE,14:one}.items():coeff[i]=v
image_check(L,coeff,relations(L,o,A0,DD,EE,Z0,o**2,zero,zero))
# Remaining normal-linear boundary, including both degenerate mixed directions.
params=s.symbols('D E Z u v w');L=F.frac_field(*params);DD,EE,Z0,u,v,w=L.gens;o=L.convert(F.to_sympy(F.unit));one,zero=L.one,L.zero
for de in [None,(zero,one),(one,zero)]:
 d,e=(DD,EE) if de is None else de
 coeff=[zero]*22
 for i,val in {0:u,4:v,5:w,6:d,7:e,8:Z0,9:e,10:one,11:d,12:d,13:e,14:one}.items():coeff[i]=val
 rels=mixed(L,o,zero,d,e,Z0)
 rels+=[{(0,1):one,(1,0):-one},{(2,3):d,(3,2):e,(0,0):u,(0,1):v/2,(1,0):v/2,(1,1):w}]
 image_check(L,coeff,rels)
# T nonzero,D=E=0: exact quotient (x,c) has only b^2 relation.
coeff=[F.zero]*22
for i,val in {2:F.one,3:-F.unit**2,8:F.one,10:F.one,14:F.one,21:F.one}.items():coeff[i]=val
# Pure U binary coefficients are zero here; all surviving top-image entries
# in span(y,b)^2 are supported only on b^2, independently of A,Z,T.
assert all(not H[i,j].subs(base).subs(mp).subs({D:0,E:0,a[0]:0,a[1]:0,a[4]:0,a[5]:0}) for i in [5,6,9] for j in range(16))
counts=[1,2]
for j in range(2,16):counts.append(counts[-1]+counts[-2])
assert counts[15]==1597 and s.binomial(18,3)==816
out={'status':'PASS','scope':'all original22 mixed pivot constants, even Schur/factorization, exact generic and both boundary top-image equalities; ordinary exhaustive rank/Ore/domain proof separate',
 'mixed_pivot_residual_rank':8,'T_nonzero_branches':records,
 'T0_A_nonzero_Ore_branch_q':'omega^2',
 'remaining_both_nonzero_proportional_sector':'S=T=a2=0, a1=0, (a6,a7)!=(0,0); normal x and xy=yx',
 'remaining_six_relation_parameters':['D','E','Z','u','v','w'],
 'exponential_quotient_degree15':1597,'AS4_degree15':816,
 'not_claimed':['remaining six-parameter normal-linear chart admissible','one-zero cube coupling covered','nonunit semisimple atlas classified','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_proportional_Szero_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','both_nonzero_proportional_T_and_a2_zero_required':True,'remaining_normal_linear_chart_parameters':6}))
