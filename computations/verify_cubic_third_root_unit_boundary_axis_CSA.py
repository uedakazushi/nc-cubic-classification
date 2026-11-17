#!/usr/bin/env python3
"""Positive characteristic109 CSA witness on original x=0, Psi=1, Z9=0.
Letter0 is an auxiliary homogenizer. All int64 products are bounded.
"""
import sys,json,sympy as s,numpy as np
from pathlib import Path
from cubic_incremental_graded import GradedAlgebra
p=109;t=next(j for j in range(1,p) if (j**6-j**3+1)%p==0);oo=(t**3-1)%p
print('ROOT',t,oo,flush=True)
K=s.GF(p);d,o=map(K.convert,[t,oo]);one,zero=K.one,K.zero
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o}, {(1,2):d,(3,3):one},{(2,2):one,(3,1):d},{(2,3):d,(1,1):one}]
weights=[0,0,1,2]
RC=[{w:c/o**weights[w[1]] for w,c in r.items()} for r in R]
# Here letter0 is an auxiliary central homogenizer, not the original x.
RC[:3]=[{(0,j):one,(j,0):-one} for j in range(1,4)]
GC={(1,3,2):one,(2,1,3):o**2,(3,2,1):one}
Psi={(1,1,1):one}
data=json.loads(Path(__file__).with_name('cubic_third_root_unit_boundary_axis_center_certificate.json').read_text())
def cm(cs):
 val=0
 for c in cs:
  rr=s.Rational(c);val=(val*t+int(rr.p)*pow(int(rr.q),-1,p))%p
 return K.convert(val)
Z={tuple('xybc'.index(c) for c in w):cm(co.get('(0, 0)',[])) for w,co in data['chosen_center'].items() if 'x' not in w};Z={w:c for w,c in Z.items() if c}
def mod_inv(M):
 n=len(M);aug=np.concatenate([M.copy()%p,np.eye(n,dtype=np.int64)],axis=1)
 for i in range(n):
  hit=np.flatnonzero(aug[i:,i]%p)
  if not len(hit):raise ValueError('singular')
  j=i+int(hit[0]);aug[[i,j]]=aug[[j,i]];aug[i]=aug[i]*pow(int(aug[i,i]),-1,p)%p
  for j in range(n):
   if j!=i and aug[j,i]:aug[j]=(aug[j]-aug[j,i]*aug[i])%p
 return aug[:,n:]
def rank_det(M):
 M=M.copy()%p;rank=0;det=1
 for j in range(M.shape[1]):
  hit=np.flatnonzero(M[rank:,j]%p)
  if not len(hit):continue
  k=rank+int(hit[0])
  if k!=rank:M[[rank,k]]=M[[k,rank]];det=-det
  pivot=int(M[rank,j]);det=det*pivot%p;M[rank]=M[rank]*pow(pivot,-1,p)%p
  for k in range(rank+1,len(M)):
   if M[k,j]:M[k]=(M[k]-M[k,j]*M[rank])%p
  rank+=1
  if rank==len(M):break
 return rank,det%p
assert 81*(p-1)**2<2**63
for aa,bb in [(1,0)]:
 rp=dict(Psi);rp[(0,0,0)]=rp.get((0,0,0),zero)-K.convert(aa)
 rz=dict(Z);rz[(0,)*9]=rz.get((0,)*9,zero)-K.convert(bb)
 A=GradedAlgebra(K,4,RC+[GC,rp,rz],weights);A.build(13)
 if len(A.basis[12])!=81 or len(A.basis[13])!=81:continue
 M,ids=A.normal_matrix(12,[one]*4,fixed=False);cdim=81-M.rank();print('fiber',aa,bb,'center',cdim,flush=True)
 def matrix(j):
  out=np.zeros((81,81),dtype=np.int64)
  for i in range(81):
   for k,c in A.right[13][i,j].items():out[k,i]=int(c)%p
  return out
 xi=mod_inv(matrix(0));generators=[xi@matrix(j)%p for j in range(4)]
 assert np.array_equal(generators[0],np.eye(81,dtype=np.int64))
 assert 81*(p-1)**2<2**63
 cache={():np.eye(81,dtype=np.int64)}
 def operator(w):
  w=tuple(j for j in w if j)
  if w not in cache:cache[w]=generators[w[-1]]@operator(w[:-1])%p
  return cache[w]
 ops=[operator(w) for w in A.basis[12]];traces=np.array([int(np.trace(m))%p for m in ops],dtype=np.int64)
 gram=np.column_stack([traces@m%p for m in ops]);assert np.array_equal(gram%p,gram.T%p)
 rank,det=rank_det(gram)
 print('regular trace rank/det',rank,det,flush=True)
 for rel in RC+[GC,rp,rz]:
  check=sum((int(c)*operator(w) for w,c in rel.items()),np.zeros((81,81),dtype=np.int64))%p
  assert not np.any(check)
 if cdim==1 and rank==81:
  Path(__file__).with_name('cubic_third_root_unit_boundary_axis_CSA_certificate.json').write_text(json.dumps({'status':'PASS','p':p,'root':t,'omega':oo,'Psi':aa,'Z':bb,'center':cdim,'trace_determinant':det,'matrix_size':81,'int64_dot_bound':81*(p-1)**2,'original_x':0,'auxiliary_homogenizer':True,'lift':'positive center80 minor and trace determinant lift over Phi18; original x0 fiber independent of allu,v','not_claimed':['generic division','complete H3 classification']},indent=2));break
else:raise AssertionError('no positive fiber among samples')
