#!/usr/bin/env python3
"""Necessary TT22 cover: fresh exact quotient obstructions, no regularity import."""
from pathlib import Path
import itertools,json,sympy as s
from cubic_incremental_graded import GradedAlgebra
from verify_cubic_as4_tt22_remaining import source_matrix,U,K,A0
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_CY_finite22_input.json').read_text())
assert D['source_commit']=='6f798e0cd3ea36a17685f8d76f1d6d6fe8296ec0'
x=s.symbols('x0:21');g=s.Symbol('g');h,t=s.symbols('h t')
R=source_matrix(dict(enumerate(x)));
# Recover the complete mixed coefficient matrix directly from the relation frame.
B=(A0*((K.T*K).inv()*K.T*(R-U)).T).applyfunc(s.expand)
C=s.zeros(6);C[1,4]=C[4,1]=-s.Rational(1,8);C[2,3]=C[3,2]=s.Rational(1,8);C[4,4]=-s.Rational(1,4)
J=s.zeros(6)
for i,j,v in [(0,5,1),(1,4,-1),(2,3,1)]:J[i,j]=J[j,i]=v
M=(C+g*J-B.T*A0.inv()*B).applyfunc(s.expand)
H=U*A0*U.T+U*B*K.T+K*B.T*U.T+K*(C+g*J)*K.T
ws=list(itertools.product(range(4),repeat=4))
assert all(s.expand(H[4*a+b,4*c+d]+H[4*d+a,4*b+c])==0 for a,b,c,d in ws)
assert s.Matrix(list(B)).jacobian(x).rank()==21
cols=[]
for i,j in itertools.product(range(6),repeat=2):
 HH=U[:,i]*K[:,j].T+K[:,j]*U[:,i].T
 cols.append(s.Matrix([HH[4*a+b,4*c+d]+HH[4*d+a,4*b+c] for a,b,c,d in ws]))
assert s.Matrix.hstack(*cols).rank()==15
# Full connected marked group and swap preserve the relation marking.
p,q,al,v=s.symbols('p q al v',nonzero=True)
lu=(U.T*U).inv()*U.T;lk=(K.T*K).inv()*K.T
N=s.Matrix([[1,0,0,0],[p,1,0,0],[0,0,1,0],[0,0,q,1]])
T=s.diag(1,al,v,v/al);W=s.Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
for P,scale in [(N,1),(T,v*v),(W,1)]:
 PP=s.kronecker_product(P,P);SS=lu*PP*U;KK=lk*PP*K
 for mat in [PP*U-U*SS,SS*A0*SS.T-scale*A0,KK*C*KK.T-scale*C,KK*J*KK.T-scale*J]:assert mat.applyfunc(s.cancel)==s.zeros(*mat.shape)
NN=s.kronecker_product(N,N);BN=(lu*NN*U*B*(lk*NN*K).T).applyfunc(s.expand)
assert BN[3,1]==x[7]+q*x[6] and BN[2,3]==x[12]+p*x[6]
normal={name:{s.Symbol(k):s.sympify(vv) for k,vv in vals.items()} for name,vals in D['normal_forms'].items()}
records=[]
for name,vals in normal.items():
 assert M.subs(vals).applyfunc(s.cancel)==s.zeros(6),name
 RN=R.subs(vals).applyfunc(s.cancel)
 if name not in D['bad_dimensions']:continue
 params=sorted(set().union(*(z.free_symbols for z in RN)),key=str);base=s.QQ_I if any(z.has(s.I) for z in RN) else s.QQ
 F=base.frac_field(*params) if params else base
 for z in RN:
  if params:
   den=s.Poly(s.cancel(z).as_numer_denom()[1],*params,domain=base);assert len(den.terms())==1
   assert all(not e or str(pp)=='h' for pp,e in zip(params,den.monoms()[0]))
 rels=[{divmod(i,4):F.from_sympy(RN[i,j]) for i in range(16) if RN[i,j]} for j in range(6)]
 Q=GradedAlgebra(F,4,rels,[0]*4);expected=D['bad_dimensions'][name];Q.build(len(expected)-1)
 dims=[len(Q.basis[i]) for i in range(len(expected))];assert dims==expected,(name,dims)
 assert dims[-1]>s.binomial(len(expected)+2,3)
 records.append({'name':name,'dimensions':dims,'parameters':list(map(str,params))});print('PASS',name,dims,flush=True)
# Literal match to existing all-parameter exclusion inputs, including both A signs.
Q=s.Rational
old={'I1':{0:1,5:Q(1,8),6:s.I/4,16:-s.I/4,19:s.I/2},'a1':{0:1,5:Q(1,8),7:1,9:-1,17:-1,14:Q(1,16),18:Q(1,16)},'r_zero':{0:1,5:Q(1,16),9:1,17:1,14:-Q(1,16),18:-Q(1,16)},'r_nonzero':{0:1,5:Q(1,16)-h*h,16:h,19:(Q(1,16)-h*h)/h},'disc_nonzero':{9:1,14:-Q(1,16),17:1+t,18:-Q(1,16)-1/(4*t)},'disc_exception':{9:1,14:-Q(1,16),17:-1,18:Q(1,16),19:h}}
for name,vals in old.items():assert (R.subs(normal[name])-source_matrix(vals)).applyfunc(s.cancel)==s.zeros(16,6)
assert (R.subs(normal['I-1'])-source_matrix({k:s.conjugate(vv) for k,vv in old['I1'].items()})).applyfunc(s.cancel)==s.zeros(16,6)
out={'status':'PASS','source_commit':D['source_commit'],'scope':'necessary finite-base22 cover; nine bad representatives/families checked from original relations; six retained presentations literally match old exclusions','bad_quotients':records,'ordinary_dependencies':['TT1-TT14 full branch normalization, pinned upstream control replay separately','all-closed raw relation rank lower bound on explicitly allowed unit domains','existing thm:tt22-C-all-excluded, thm:tt22-EF-all-excluded, prop:tt22-fixed-all-excluded'],'not_claimed':['all branch Groebner controls independently reimplemented','AS sufficiency or full automorphisms imported','relative reduced scheme cover','full H3 classification','novelty confirmed']}
(ROOT/'cubic_CY_finite22_cover_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS necessary22 frame, group, all nine bad quotients and literal six retained presentations')
