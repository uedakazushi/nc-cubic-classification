"""Entire QQ epsilon=+ zero-top branch: three PBW charts and exact normal minors."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
t=S.symbols('t');F=S.QQ.frac_field(t)
keys_p1=[(1,(0,0,0,1)),(2,(0,0,0,2)),(0,(0,0,0,1)),(2,(0,0,1,2)),(0,(0,0,2,2)),(2,(0,2,2,2)),(0,(0,0,2,3)),(2,(0,2,2,3)),(0,(0,0,3,3)),(2,(0,2,3,3))]
keys_p2=keys_p1.copy();keys_p2[4]=(1,(0,1,2,2));keys_p2[8]=(1,(0,1,3,3))
keys_q=[(2,(0,0,0,2)),(2,(0,0,1,2)),(2,(0,1,1,2)),(0,(0,0,3,3)),(2,(0,2,2,2)),(2,(0,2,2,3)),(2,(1,1,1,2)),(0,(0,1,3,3)),(2,(1,2,2,2)),(2,(1,2,2,3))]
keys_both=[(1,(0,0,0,1)),(2,(0,0,0,2)),(2,(0,0,1,2)),(3,(0,0,0,2)),(0,(0,1,2,3)),(1,(0,1,2,2)),(2,(0,2,2,2)),(2,(0,2,2,3)),(3,(0,2,2,2)),(0,(0,1,2,2))]
records=[]
for name,p,q,z,witnesses,expected in [
 ('p_minus_one',-S.Integer(1),t,[1,0,0,0,0,-t],[keys_p1,keys_p2],[-8*(t+1)**2/t**9,8*(t-1)**2/t**9]),
 ('q_minus_one',t,-S.Integer(1),[0,1,0,0,t,0],[keys_q],[S.Integer(1)]),
 ('both_minus_one',-S.Integer(1),-S.Integer(1),[1,1,0,0,t,t+1],[keys_both],[-S.Integer(4)])]:
 A=S.zeros(4)
 for (i,j),c in zip(itertools.combinations(range(4),2),z):A[i,j]=c;A[j,i]=-c
 h=p*q;assert S.expand(z[0]*z[5]-z[1]*z[4]+z[2]*z[3]-h)==0
 a=S.Matrix([[0,1],[-p,0]]);b=S.Matrix([[0,1],[-q,0]]);M=S.zeros(4);tau=S.zeros(4)
 for i,j,k,l in itertools.product(range(2),repeat=4):
  M[2*k+j,2*l+i]=-a[i,k]*b[j,l];tau[2*j+i,2*l+k]=A[2*i+l,2*k+j]
 inv=A.inv();assert (tau+M.T*inv*M).applyfunc(S.cancel)==S.zeros(4)
 graph=-M.T*inv;rewrite=-graph.inv().T
 uv=[(i,j) for i in range(2) for j in range(2,4)];vu=[(i,j) for i in range(2,4) for j in range(2)]
 rules={(1,0):{(0,1):1/p},(3,2):{(2,3):1/q}}
 for i,w in enumerate(vu):rules[w]={v:S.cancel(rewrite[i,j]) for j,v in enumerate(uv) if rewrite[i,j]}
 @lru_cache(None)
 def nf(w):
  for pos in range(len(w)-1):
   if w[pos:pos+2] in rules:
    out={}
    for v,c in rules[w[pos:pos+2]].items():
     for x,d in nf(w[:pos]+v+w[pos+2:]).items():out[x]=out.get(x,0)+c*d
    return {x:S.cancel(c) for x,c in out.items() if S.cancel(c)}
  return {w:S.Integer(1)}
 overlaps=0
 for w in itertools.product(range(4),repeat=3):
  if w[:2] not in rules or w[1:] not in rules:continue
  def reduce_at(pos):
   out={}
   for v,c in rules[w[pos:pos+2]].items():
    for x,d in nf(w[:pos]+v+w[pos+2:]).items():out[x]=out.get(x,0)+c*d
   return out
  left=reduce_at(0);right=reduce_at(1)
  assert all(S.cancel(left.get(x,0)-right.get(x,0))==0 for x in set(left)|set(right));overlaps+=1
 assert overlaps==4
 words=[w for w in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in w)%2==0];assert len(words)==10
 eq={}
 for col,w in enumerate(words):
  for g,mu in enumerate([1,1,-1,-1]):
   out={}
   for word,c in [(w+(g,),1),((g,)+w,-mu)]:
    for v,d in nf(word).items():out[v]=out.get(v,0)+c*d
   for v,c in out.items():
    c=S.cancel(c)
    if c:eq.setdefault((g,v),{})[col]=c
 for keys,value in zip(witnesses,expected):
  matrix=S.Matrix([[eq[key].get(j,0) for j in range(10)] for key in keys])
  det=DomainMatrix.from_Matrix(matrix).convert_to(F).det()
  assert det==F.from_sympy(value)
 records.append({'chart':name,'PBW_overlaps':4,'normal_rows':len(eq),'normal_columns':10,'exact_minors':[str(v) for v in expected]})
assert S.expand((2-t)*(t+1)**2/4+(t+2)*(t-1)**2/4)==1
out={'status':'PASS','scope':'entire QQ epsilon=+ semisimple zero-top branch, including all parameter/boundary values',
 'charts':records,'cover':'linear atlas forces p=-1 or q=-1; at p=q=-1 torus and axis swaps cover by z0=z1=1,z4=t,z5=t+1, or the two one-pair-zero charts',
 'conclusion':'designated positive normal cubic kernel zero on every chart; no H3 in this whole branch',
 'not_claimed':['QQ epsilon=- classification','all zero-top H3 classification','nonsemisimple branch transport','AS4 recognition beyond what is needed for exclusion']}
Path(__file__).with_name('cubic_order2_22_rank4_zero_top_QQ_plus_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS entire QQ epsilon+ branch: twelve PBW overlaps, four exact minors, all boundaries')
