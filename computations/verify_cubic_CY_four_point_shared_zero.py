#!/usr/bin/env python3
"""Complete shared-zero four-point necessary equations and skew recognition."""
from pathlib import Path
import json,sympy as s
from verify_cubic_as4_four_simple import source_matrix,U,K,W2,IX
la,g,A,B,C=s.symbols('lambda g A B C');xx=s.symbols('x0:21');diag=[0,2,5,9,14,20]
vals={j:xx[j] for j in diag};vals.update({8:A,11:B,15:C})
R,AA=source_matrix(la,vals);BB=(AA*((K.T*K).inv()*K.T*(R-U)).T).applyfunc(s.cancel)
C0=s.zeros(6);C0[1,4]=C0[4,1]=(la+1)/8;C0[2,3]=C0[3,2]=-la/8
J=s.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v
M=(C0+g*J-BB.T*AA.inv()*BB).applyfunc(s.factor)
products=[xx[0]*C,xx[2]*B,xx[5]*A,xx[9]*(B-C),xx[14]*(A-C),xx[20]*(A-B)]
ratios=[s.cancel(M[j,j]/p) for j,p in enumerate(products)]
for ratio in ratios:
 assert ratio!=0 and ratio.free_symbols<={la}
 for poly in ratio.as_numer_denom():
  pol=s.Poly(poly,la)
  for f in [s.Poly(la,la),s.Poly(la+1,la)]:
   while pol.degree()>0 and pol.rem(f).is_zero:pol=pol.exquo(f)
  assert pol.degree()==0
P0,P1,P2=xx[0]*xx[20],xx[2]*xx[14],xx[5]*xx[9]
e=[g-2*P0-2*C*(A-B),(la+1)/8-g-2*(P1+B*(A-C))/la,-la/8+g+2*(P2+A*(B-C))/(la+1)]
expected=s.diag(*[ratios[j]*products[j] for j in range(6)])
for (i,j),eq in zip([(0,5),(1,4),(2,3)],e):expected[i,j]=expected[j,i]=eq
assert (M-expected).applyfunc(s.cancel)==s.zeros(6)
assert s.cancel((-e[0]+la*e[1]+(la+1)*e[2])/2-P0+P1-P2)==0
# Exact torus weights of the independent normalizations used in the proof.
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
weights=[]
for i,j in pairs:
 w=[-1]*4;w[i]+=2;w[j]+=2;weights.append(w)
assert s.Matrix([weights[j] for j in [0,1,2]]).rank()==3
assert s.Matrix([weights[j] for j in [1,2,5]]).rank()==3
# Quantum presentation: exactly one relation for each unordered pair.
RQ,_=source_matrix(la,{8:A,11:B,15:C});q={};coefficient_product=1
for j,(i,k) in enumerate(pairs):
 assert all(not RQ[r,j] for r in range(16) if r not in [4*i+k,4*k+i])
 left,right=RQ[4*i+k,j],RQ[4*k+i,j];assert s.cancel(left+right)==1
 coefficient_product*=left*right;q[i,k]=s.cancel(-left/right);q[k,i]=1/q[i,k]
 assert s.cancel(q[i,k]-1)!=0
Theta=(1-16*C*C)*(la*la-16*B*B)*((la+1)**2-16*A*A)*((la+1)**2-16*(B-C)**2)*(la*la-16*(A-C)**2)*(1-16*(A-B)**2)
ratio=s.cancel(coefficient_product/Theta);assert ratio!=0 and ratio.free_symbols<={la}
F=A*B+la*A*C-(la+1)*B*C-la*(la+1)/16
for i in range(4):
 num=s.cancel(s.prod(q[i,j] for j in range(4) if i!=j)-1).as_numer_denom()[0]
 assert s.rem(num,F,A,B,C,domain=s.QQ.frac_field(la))==0
# The excluded O-boundaries have an actual product relation, uniformly in lambda.
critical=[]
for av in [la/4,-la/4,(la+1)/4,-(la+1)/4]:
 RO,_=source_matrix(la,{0:1,8:av,11:la*(la+1)/(16*av)});RO=RO.applyfunc(s.cancel)
 witnesses=[]
 for j in range(6):
  nonzero=[r for r in range(16) if RO[r,j]!=0]
  if len(nonzero)==1 and RO[nonzero[0],j]==1:witnesses.append({'column':j,'word':W2[nonzero[0]]})
 assert witnesses;critical.append({'A':str(av),'unit_product_relations':witnesses})
# Retained normalized presentations are precisely the old source matrices.
t=s.Symbol('t')
Svals={0:1,2:1,5:1,9:(la+1)*(la-t)/16,14:la*(la+1-t)/16,20:t/16}
assert M.subs({**dict.fromkeys([*xx,A,B,C],0),**{xx[j]:v for j,v in Svals.items()},g:t/8}).applyfunc(s.cancel)==s.zeros(6)
for eps in [0,1]:
 Hvals={2:1,5:1,9:la*(la+1)/16,14:la*(la+1)/16,20:eps}
 assert M.subs({**dict.fromkeys([*xx,A,B,C,g],0),**{xx[j]:v for j,v in Hvals.items()}}).applyfunc(s.cancel)==s.zeros(6)
Osub={**dict.fromkeys([*xx,C,g],0),xx[0]:1,B:la*(la+1)/(16*A)}
assert M.subs(Osub).applyfunc(s.cancel)==s.zeros(6)
out={'status':'PASS','scope':'whole shared-zero four-point necessary cover S/Q/O/H; entire shared-zero H3 stratum empty by old S/Q/O/H exclusions','diagonal_equation_units':list(map(str,ratios)),'three_residual_equations':list(map(str,e)),'quantum_coefficient_product_over_Theta':str(ratio),'quantum_CY_row_products':'all four identities modulo F','O_bad_boundary_product_relations':critical,'ordinary_dependencies':['all24 monomial support/marking actions from four-point support lemma','algebraically closed torus normalization using three independent integer weights','existing prop:cubic-fs-sklyanin and all-value O/H H3 exclusions','existing lem:cubic-cy-skew-zero-commutator for Q with every q_ij !=1'],'not_claimed':['nonzero shared supports classified','all Q central cubics admissible','relative torus quotient or descent','complete CY/H3 classification','novelty confirmed']}
Path(__file__).with_name('cubic_CY_four_point_shared_zero_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS whole shared-zero necessary equations, all gauges, Q skew/CY identities, O product boundaries and retained S/O/H frames')
