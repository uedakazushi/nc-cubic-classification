#!/usr/bin/env python3
"""Positive modular center/trace witness for the characteristic-zero rank81
central module. NumPy is used only with bounded int64 modular arithmetic;
all products are proved below 2^63, with no floating-point operations.
Requires sympy and numpy. Zero modular ranks are not used as generic bounds.
"""
from pathlib import Path
import hashlib
import sympy as s,json,numpy as np
from cubic_incremental_graded import GradedAlgebra
base=str(Path(__file__).resolve().parent)+'/'
data=json.load(open(base+'cubic_third_root_unit_boundary_L_finite_center_certificate.json'))

def scalar_mod(coeff,t,p):
 out=0
 for cc in coeff:
  r=s.Rational(cc);out=(out*t+int(r.p)*pow(int(r.q),-1,p))%p
 return out
p=109;t=15;oo=63
assert s.isprime(p) and (t**6-9*t**3+57)%p==0
assert ((1-t**3)*pow(7,-1,p))%p==oo and (oo**2+oo+1)%p==0 and oo!=1
assert all(v%p for v in [2,7,8+oo,3*8+1+2*oo,3*8+oo-1])
zm={tuple('xybc'.index(c) for c in w):scalar_mod(cs,t,p) for w,cs in data['Z9_original_polynomial_C_coordinates'].items()}
pm={tuple('xybc'.index(c) for c in w):scalar_mod(cs,t,p) for w,cs in data['Psi3_original_polynomial_C_coordinates'].items()}
K=s.GF(p);d,e,o=map(K.convert,[t,2,oo]);one,zero=K.one,K.zero;u=one;v=zero;Y=e**3
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):d,(2,1):e,(3,3):one},{(1,3):e,(3,1):d,(2,2):one},
 {(2,3):d,(3,2):e,(0,0):u,(1,1):one}]
weights=[0,0,1,2];RC=[{w:c/o**weights[w[1]] for w,c in r.items()} for r in R]
C=(-(o+2)*Y**2+(one-o)*Y-o*e**2*d-(o+1)*e*d**2)/(Y-one)
G={(2,2,2):o,(2,3,1):-d*((o+2)*Y+o**2),(3,2,1):e*(2-(o+2)*Y),(3,3,3):one,(1,0,0):C}
GC={w:c/o**sum(j*weights[ww] for j,ww in enumerate(w)) for w,c in G.items()}
Z={w:K.convert(c) for w,c in zm.items() if c};Psi={w:K.convert(c) for w,c in pm.items() if c}

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
for aa,bb in [(0,1)]:
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
  out={'prime':p,'root_t':t,'omega':oo,'central_fiber_Psi':aa,'central_fiber_Z':bb,
       'fiber_dimensions_12_13':[81,81],'fiber_center_dimension':1,'trace_rank':81,'trace_determinant':det,
       'trace_gram_integer_bound':81*(p-1)**2,'matrix_size':81}
  out.update({'status':'PASS','scope':'positive nonzero modular minors and trace determinant lift to the characteristic-zero finite-free central family; no modular zero-rank extrapolation',
       'numpy_version':np.__version__,'integer_arithmetic':'int64 entries reduced mod109 after every product, max dot bound81*108^2<2^63',
       'Gram_sha256':hashlib.sha256(json.dumps(gram.tolist(),separators=(',',':')).encode()).hexdigest(),
       'source_certificate':'cubic_third_root_unit_boundary_L_finite_center_certificate.json',
       'lift_argument':'free rank81 proved in characteristic zero; selected fiber quotient pivots are nonzero mod109, hence same basis lifts; center80-minor and nonzero trace determinant remain nonzero',
       'conclusions':['full center of fixed C/G is K[x,Psi,z9]','center generic algebra is central simple of degree9','fixed affine U is prime, full center k[psi,z], PI degree9'],
       'not_claimed':['generic algebra division','Brauer period9 or3','H3 admissible','same conclusion for all parameters','complete H3 classification']})
  Path(__file__).with_name('cubic_third_root_unit_boundary_L_finite_CSA_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
  print(json.dumps({'status':'PASS','positive_prime':p,'trace_determinant_nonzero':det,'generic_center_CSA_degree':9,'Brauer_period_unresolved':True}))
  break

assert cdim==1 and rank==81
