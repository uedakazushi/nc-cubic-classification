#!/usr/bin/env python3
"""All26 original Jordan22 tops, full highest-rank atlas and point obstruction.
No global CY classification input; all computations are characteristic-zero.
"""
from pathlib import Path
import itertools,json,sympy as s
from cubic_diagonal_top import top_basis
from cubic_incremental_graded import GradedAlgebra
ROOT=Path(__file__).resolve().parent
W=list(itertools.product(range(4),repeat=4));ix={w:i for i,w in enumerate(W)};cb=top_basis(s.QQ,[s.QQ.one]*4);C=s.zeros(256,66);DC=s.zeros(256,66);nm={1:0,3:2}
for j,b in enumerate(cb):
 for word,c in b.items():
  C[ix[word],j]=c
  for pos,l in enumerate(word):
   if l in nm:DC[ix[word[:pos]+(nm[l],)+word[pos+1:]],j]+=c
KK=s.Matrix.hstack(*DC.nullspace());B=C*KK;assert B.cols==26;rows=B.T.rref()[1];B=B*B.extract(rows,range(26)).inv();a=s.symbols('a0:26');v=B*s.Matrix(a);H=s.Matrix(16,16,lambda i,j:v[ix[divmod(i,4)+divmod(j,4)]])
U=[0,2];V=[1,3];ur=[4*i+j for i,j in itertools.product(U,repeat=2)];vr=[4*i+j for i,j in itertools.product(V,repeat=2)];mixed=[4*i+j for i,j in itertools.product(range(4),repeat=2) if (i in U)!=(j in U)];Q=H.extract(ur,vr);assert Q==Q.T
q=s.symbols('q0:4');high={a[3]:q[0]**2,a[5]:q[0]*q[1],a[9]:q[0]*q[2],a[11]:q[0]*q[3],a[16]:q[1]**2,a[13]:q[1]*q[2]-q[0]*q[3],a[20]:q[1]*q[3],a[21]:q[2]**2-q[1]**2,a[23]:q[2]*q[3]-q[1]*q[3],a[25]:q[3]**2};assert Q.subs(high,simultaneous=True)==s.Matrix(q)*s.Matrix(q).T
zero={k:0 for k in high};HZ=H.subs(zero);assert HZ.extract(mixed,mixed)==s.zeros(8) and HZ.extract(vr,range(16))==s.zeros(4,16)
p=s.Symbol('p');quantum={k:s.expand(c.subs(dict(zip(q,[0,1,-p,0])))) for k,c in high.items()};jordan={k:s.expand(c.subs(dict(zip(q,[1,1,-1,0])))) for k,c in high.items()};K=H.extract(mixed,mixed).subs(quantum);minor=None
for rr in itertools.combinations(range(8),5):
 for cc in itertools.combinations(range(8),5):
  det=s.factor(K.extract(rr,cc).det())
  if det:minor=(rr,cc,det);break
 if minor:break
assert s.cancel(minor[2]/(p*p*(p-1)**2*(p+1)**2)) in [1,-1]
cases={'commutative':{k:c.subs(p,1) for k,c in quantum.items()},'anticommutative':{k:c.subs(p,-1) for k,c in quantum.items()},'Jordan':jordan};S=[2,7,1,3,6,11];L=[8,4,6,12,14,13];order={k:i for i,k in enumerate([0,2,1,3])};N=s.zeros(4);N[0,1]=N[2,3]=1;HI=s.eye(4)-N;out=[]
for name,sub in cases.items():
 HH=H.subs(sub);assert HH.extract(mixed,mixed).rank()==4;A=HH.extract(S,S);assert A.det()==-1;R=(HH.extract(range(16),S)*A.inv()).applyfunc(s.expand);lead=R.copy()
 for j in range(6):
  wt=max(sum(k in V for k in divmod(i,4)) for i,c in enumerate(R.col(j)) if c)
  for i in range(16):
   if sum(k in V for k in divmod(i,4))<wt:lead[i,j]=0
 low={x:0 for x in a if x not in sub};assert lead.subs(low)==lead
 PP=lead.extract(L,range(6));assert PP.det() in [1,-1];P=(lead*PP.inv()).applyfunc(s.expand)
 for j,inv in enumerate(L):
  assert P[inv,j]==1
  for i,c in enumerate(P.col(j)):
   if c and i!=inv:
    k,l=divmod(i,4);assert order[k]<=order[l]
    if j==0:assert k in U and l in U
    elif j==5:assert k in V and l in V
    else:assert k in U and l in V
 rels=[{divmod(i,4):s.QQ.from_sympy(P[i,j]) for i in range(16) if P[i,j]} for j in range(6)];G=GradedAlgebra(s.QQ,4,rels,[0,1,0,1]);G.build(3);assert len(G.basis[3])==20
 for r in rels:
  reduced={}
  for word,c in r.items():
   for pos,k in enumerate(word):
    if k in nm:G.addto(reduced,G.word(word[:pos]+(nm[k],)+word[pos+1:]),c)
  assert not reduced
 dn=s.zeros(20)
 for j,word in enumerate(G.basis[3]):
  for pos,k in enumerate(word):
   if k in nm:
    for r,c in G.word(word[:pos]+(nm[k],)+word[pos+1:]).items():dn[r,j]+=c
 null=dn.nullspace();assert len(null)==6 and all(sum(k in V for k in G.basis[3][j])<=1 for col in null for j,c in enumerate(col) if c)
 RB=s.zeros(16,6)
 for i,j,k,col in itertools.product(range(4),range(4),range(4),range(6)):RB[4*i+k,col]+=R[4*i+j,col]*HI[k,j]
 RB=RB.applyfunc(s.expand);assert all(not RB[15,col] for col in range(6));others=[0,1,2];AA=s.Matrix([[RB[12+k,col] for k in others] for col in range(6)]);DD=s.Matrix([[-RB[4*k+3,col] for k in others] for col in range(6)]);rp=[1,3,5];A0=AA.extract(rp,range(3));assert A0.det() in [1,-1];M=(A0.inv()*DD.extract(rp,range(3))).applyfunc(s.expand);assert (DD-AA*M).applyfunc(s.expand)==s.zeros(6,3) and M.det()==1
 out.append({'case':name,'highest_normalization':{str(k):str(c) for k,c in sub.items()},'source_unit_minor':-1,'PBW_inversion_pivot_det':str(PP.det()),'highest_PBW_relations':[{''.join(map(str,divmod(i,4))):str(P[i,j]) for i in range(16) if P[i,j]} for j in range(6)],'cubic_N_kernel_dim':6,'degree3_basis':[''.join(map(str,w)) for w in G.basis[3]],'degree3_N_matrix':str(dn),'all6_N_kernel_basis':[{''.join(map(str,G.basis[3][j])):str(c) for j,c in enumerate(col) if c} for col in null],'maximum_invariant_V_weight':1,'point_generator':3,'point_Ext1_dim':3,'full_twisted_point_monodromy':str(M),'shift_determinant':1})
result={'status':'PASS','scope':'entire single-eigenvalue unipotent Jordan(2,2) H3 sector empty, via complete highest-rank atlas and all-parameter point obstruction','coordinate_words':[''.join(map(str,W[j])) for j in rows],'all26_basis':[{''.join(map(str,W[j])):str(c) for j,c in enumerate(B.col(k)) if c} for k in range(26)],'pure_binary_source_block':str(Q),'all_rank1_block_parameterization':{str(k):str(c) for k,c in high.items()},'quantum_5_minor':{'rows':minor[0],'cols':minor[1],'polynomial':str(minor[2])},'all_three_charts':out,'ordinary_dependencies':['domain forces nonzero pure-binary block rank1; its quadratic coefficient matrix nonsingular','full rank6 forces mixed highest block rank<=4; quantum parameter p=+-1, or Jordan','AS2 binary congruence normal forms and simultaneous N-preserving generator changes','PBW spanning of highest algebra and AS4 Hilbert equality give flat associated graded','N-fixed cubic has V weight<=1 hence point ideal square','all tails extensions recurrence and odd Serre determinant lemma'],'not_claimed':['all CY classification','complete H3 classification','ordinary Serre/PBW/cover proofs mechanically formalized','novelty confirmed']}
(ROOT/'cubic_jordan22_unipotent_vertex_certificate.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS all26 tops, all three highest charts, full point recurrences; Jordan22 H3 empty')
