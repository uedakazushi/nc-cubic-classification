#!/usr/bin/env python3
"""Independent original-tensor cover of the principal unipotent H3 sector.
No global CY classification or AS sufficiency is inferred from this cover.
"""
from pathlib import Path
import itertools,json,sympy as s
from cubic_diagonal_top import top_basis
ROOT=Path(__file__).resolve().parent
W=list(itertools.product(range(4),repeat=4));ix={w:i for i,w in enumerate(W)};cb=top_basis(s.QQ,[s.QQ.one]*4);C=s.zeros(256,len(cb));DC=s.zeros(256,len(cb))
for j,basis in enumerate(cb):
 for word,c in basis.items():
  C[ix[word],j]=c
  for pos,letter in enumerate(word):
   if letter:DC[ix[word[:pos]+(letter-1,)+word[pos+1:]],j]+=c
assert len(cb)==66
KK=s.Matrix.hstack(*DC.nullspace());B=C*KK;assert B.cols==12 and DC*KK==s.zeros(256,12)
words=['0001','0011','0021','0031','0020','0111','0202','0211','0113','0213','1112','0033'];ids=[ix[tuple(map(int,w))] for w in words];B=B*B.extract(ids,range(12)).inv();assert B.extract(ids,range(12))==s.eye(12)
a=s.symbols('a0:12');vec=B*s.Matrix(a);H=s.Matrix(16,16,lambda i,j:vec[ix[divmod(i,4)+divmod(j,4)]])
assert [(i,H[i,15]) for i in range(16) if H[i,15]]==[(0,a[11])]
H=H.subs(a[11],0);Hzero=H.subs(a[9],0);pure=[]
for j in range(16):
 entries=[Hzero[i,j] for i in range(16) if Hzero[i,j]]
 if len(entries)==1:pure.append(entries[0])
assert set(pure)=={3*a[10]+5*a[8],-3*a[10]-5*a[8]}
Hzero=Hzero.subs(a[8],-3*a[10]/5);Q=Hzero.extract([10,11,14,15],range(16));assert Q[1:,:]==s.zeros(3,16)
H=H.subs(a[9],1);J=[1,2,3,6,7,11];A=H.extract(J,J);assert A.det()==-1
Schur=H-H.extract(range(16),J)*A.inv()*H.extract(J,range(16));variables=[a[j] for j in [10,8,7,6,3,5,2,4,1,0]];polys=[]
for q in Schur:
 if q:
  q=s.Poly(q,*variables,domain=s.QQ).monic().as_expr()
  if q not in polys:polys.append(q)
assert a[10]*a[8] in polys
u,v,w=s.symbols('u v w');AA={a[11]:0,a[9]:1,a[10]:u,a[8]:0,a[7]:-3*u*u/2,a[6]:0,a[3]:-9*u*u/2,a[2]:v,a[5]:v,a[0]:v*v/u,a[1]:-6*v*u+27*u**4/4,a[4]:w};BB={a[11]:0,a[9]:1,a[10]:0,a[8]:u,a[7]:-5*u*u/2,a[6]:0,a[3]:-35*u*u/2,a[0]:v,a[1]:-3*v/(5*u)-125*u**4/12,a[5]:3*v/(25*u*u)+25*u**3/6,a[2]:50*u**3/3,a[4]:w}
branch_gb={};order=[a[j] for j in [6,7,3,1,5,0,2,4]]
for name,sub in [('A',{a[10]:u,a[8]:0}),('B',{a[10]:0,a[8]:u})]:
 G=s.groebner([q.subs(sub) for q in polys],*order,domain=s.QQ.frac_field(u));branch_gb[name]=list(map(str,G))
 target=[a[6],a[7]+3*u*u/2,a[3]+9*u*u/2,a[1]+6*a[2]*u-27*u**4/4,-a[2]+a[5],a[0]-a[2]**2/u] if name=='A' else [a[6],a[7]+5*u*u/2,a[3]+35*u*u/2,3*a[0]/(5*u)+a[1]+125*u**4/12,-3*a[0]/(25*u*u)+a[5]-25*u**3/6,a[2]-50*u**3/3]
 T=s.groebner(target,*order,domain=s.QQ.frac_field(u));assert G==T
G0=s.groebner([q.subs({a[10]:0,a[8]:0}) for q in polys],a[6],a[3],a[7],a[1],a[5],a[2],a[4],a[0]);assert G0.reduce(a[6]+8*a[7])[1]==0 and G0.reduce(a[3]-3*a[7])[1]==0 and G0.reduce(a[7]**2)[1]==0
G00=s.groebner([q.subs({a[10]:0,a[8]:0,a[6]:0,a[3]:0,a[7]:0}) for q in polys],a[1],a[5],a[2],a[4],a[0]);assert list(G00)==[a[1],2*a[2]**2+a[2]*a[5]]
CC={a[11]:0,a[9]:1,a[10]:0,a[8]:0,a[7]:0,a[6]:0,a[3]:0,a[1]:0,a[0]:u,a[4]:w};C0={**CC,a[2]:0,a[5]:v};C1={**CC,a[2]:v,a[5]:-2*v};subs={'A':AA,'B':BB,'C0':C0,'C1':C1}
for name,sub in subs.items():assert all(not s.cancel(q.subs(sub,simultaneous=True)) for q in polys)
# Full coefficient gauge, not just two selected entries: E commutes with N.
N=s.zeros(4)
for j in range(1,4):N[j-1,j]=1
for name,sub,bb,cc in [('A',AA,-v/(2*u),-w/(6*u)),('B',BB,-3*v/(200*u**3),-w/(12*u))]:
 E=s.eye(4)+bb*N**2+cc*N**3;assert E*N==N*E and E.det()==1
 old=B*s.Matrix([sub.get(q,q) for q in a]);new=s.zeros(256,1)
 for j,word in enumerate(W):
  if not old[j]:continue
  choices=[[(k,E[k,letter]) for k in range(4) if E[k,letter]] for letter in word]
  for terms in itertools.product(*choices):new[ix[tuple(x[0] for x in terms)]]+=old[j]*s.prod(x[1] for x in terms)
 target=B*s.Matrix([s.cancel(s.sympify(sub.get(q,q)).subs({v:0,w:0})) for q in a]);assert all(not s.cancel(x) for x in new-target)
out={'status':'PASS','scope':'principal unipotent H3 necessary CY-untwist top cover, all geometric rank6 points; no AS sufficiency or H3 admissibility claimed','coordinate_words':words,'all12_cyclic_D_invariant_basis':[{''.join(map(str,W[j])):str(c) for j,c in enumerate(B.col(k)) if c} for k in range(12)],'source_unit_minor_det':-1,'Schur_equations':list(map(str,polys)),'two_nonzero_branch_Groebner':branch_gb,'zero_branch_Groebner':list(map(str,G0)),'four_necessary_parameter_families':{n:{str(k):str(x) for k,x in sub.items()} for n,sub in subs.items()},'A_B_gauge':'A: b=-v/(2u),c=-w/(6u); B:b=-3v/(200u^3),c=-w/(12u), E=I+bN^2+cN^3; all256 coefficients verified','not_claimed':['complete principal H3 classification','complete H3 classification','whole CY atlas imported','novelty confirmed']}
(ROOT/'cubic_principal_unipotent_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS original12 top directions, all principal rank6 branches, and complete A/B parameter gauge')
