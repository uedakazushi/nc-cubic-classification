#!/usr/bin/env python3
"""Exclude all E2 deformation ratios using two exact polynomial center fibers.
Builds characteristic-zero models first, checks every rational denominator at a
chosen prime, and uses sharp degree bounds before modular interpolation/gcd.
Requires Sympy and NumPy; no floating-point operations or modular zero lifts.
"""
from pathlib import Path
import hashlib,json,sympy as s,numpy as np
from explore_cubic_third_root_boundary_L_parameter_fiber import build_model
from explore_cubic_third_root_boundary_L_parameter_grid import coefficients,evaluate,rankdet
p=1021;t=169;N=81
assert s.isprime(p) and (t**6-9*t**3+57)%p==0 and N*(p-1)**2<2**63
omega_mod=(1-t**3)*pow(7,-1,p)%p
assert omega_mod!=1 and (omega_mod**2+omega_mod+1)%p==0

def scalar(cs):
 ans=0
 for c in cs:
  q=s.Rational(c);ans=(ans*t+int(q.p)*pow(int(q.q),-1,p))%p
 return ans

def trim(a):
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 out=[0]*max(len(a),len(b))
 for i,c in enumerate(a):out[i]=(out[i]+c)%p
 for i,c in enumerate(b):out[i]=(out[i]+c)%p
 return trim(out)
def mul(a,b):
 if not a or not b:return []
 out=[0]*(len(a)+len(b)-1)
 for i,c in enumerate(a):
  for j,d in enumerate(b):out[i+j]=(out[i+j]+c*d)%p
 return trim(out)
def divmod_poly(a,b):
 a=a[:];out=[0]*max(0,len(a)-len(b)+1);inv=pow(b[-1],-1,p)
 while a and len(a)>=len(b):
  j=len(a)-len(b);co=a[-1]*inv%p;out[j]=co
  for i,c in enumerate(b):a[i+j]=(a[i+j]-co*c)%p
  trim(a)
 return trim(out),a
def xgcd(f,g):
 r0,r1=f,g;s0,s1=[1],[];t0,t1=[],[1]
 while r1:
  q,r=divmod_poly(r0,r1);r0,r1=r1,r
  s0,s1=s1,add(s0,[-c%p for c in mul(q,s1)])
  t0,t1=t1,add(t0,[-c%p for c in mul(q,t1)])
 inv=pow(r0[-1],-1,p)
 return [[c*inv%p for c in a] for a in [r0,s0,t0]]
def resultant(f,g):
 result=1
 while len(g)>1:
  m,n=len(f)-1,len(g)-1;_,r=divmod_poly(f,g)
  if not r:return 0
  k=len(r)-1;result=result*((-1)**(m*n))*pow(g[-1],m-k,p)%p
  f,g=g,r
 return result*pow(g[0],len(f)-1,p)%p

def interpolate(values):
 bound=len(values)-1;poly=[0]*(bound+1);basis=[1];diff=values[:]
 for n in range(bound+1):
  for j,c in enumerate(basis):poly[j]=(poly[j]+diff[0]*c)%p
  diff=[(diff[j+1]-diff[j])%p for j in range(len(diff)-1)]
  if n<bound:
   new=[0]*(len(basis)+1)
   for j,c in enumerate(basis):new[j]=(new[j]-n*c)%p;new[j+1]=(new[j+1]+c)%p
   basis=[c*pow(n+1,-1,p)%p for c in new]
 return trim(poly)
def value(poly,a):
 out=0
 for c in reversed(poly):out=(out*a+c)%p
 return out

records=[];polys=[]
for fiber in [None,'1']:
 D=build_model(fiber_z=fiber)
 degrees=[sum(j!=0 for j in w) for w in D['basis']];bound=sum(degrees);assert bound==486
 def reduce_matrix(M,generator=False):
  entries={}
  for ij,co in M['entries'].items():
   i,j=map(int,ij.split(','))
   if generator:assert 2*max(map(int,co))<=degrees[j]+1-degrees[i]
   # All characteristic-zero rational denominators must be units modulo p.
   new={degree:cc for degree,cs in co.items() if (cc:=scalar(cs))}
   if new:entries[ij]=new
  return {'shape':M['shape'],'entries':entries}
 generators_pol=[coefficients(reduce_matrix(M,True)) for M in D['generators']]
 commutators=coefficients(reduce_matrix(D['commutators']))
 words=[tuple(j for j in w if j) for w in D['basis']]
 samples=[]
 for a in range(bound+9):
  generators=[evaluate(M,a,p) for M in generators_pol]
  assert np.array_equal(generators[0],np.eye(N,dtype=np.int64))
  cache={():np.eye(N,dtype=np.int64)}
  def op(w):
   w=tuple(j for j in w if j)
   if w not in cache:cache[w]=generators[w[-1]]@op(w[:-1])%p
   return cache[w]
  ops=[op(w) for w in words];traces=np.array([int(np.trace(m))%p for m in ops],dtype=np.int64)
  gram=np.column_stack([traces@m%p for m in ops]);assert np.array_equal(gram,gram.T)
  rank,det=rankdet(gram,p);samples.append(det)
  if a==0:
   crank,_=rankdet(evaluate(commutators,a,p),p)
   assert crank==80 and rank==81 and det
   for rel in D['relations']:
    matrix=sum((scalar(co.get('0',[]))*op(tuple('xybc'.index(c) for c in w)) for w,co in rel.items()),np.zeros((N,N),dtype=np.int64))%p
    assert not np.any(matrix)
   origin_det=det
  if a%100==0:print('fiber',fiber,'sample',a,'of',bound+9,flush=True)
 poly=interpolate(samples[:bound+1]);assert len(poly)-1==bound
 assert all(value(poly,a)==det for a,det in enumerate(samples))
 polys.append(poly)
 records.append({'fiber_Z_coefficients':D['fiber_Z_coefficients'],'degree_bound':bound,'modular_degree':len(poly)-1,'leading_coefficient_modp':poly[-1],'origin_center':1,'origin_trace_det':origin_det,'origin_source_relations':'PASS','model_sha256':hashlib.sha256(json.dumps(D,separators=(',',':')).encode()).hexdigest(),'trace_polynomial_low_to_high_modp':poly,'samples':len(samples)})
def product(factors):
 out=[1]
 for factor in factors:out=mul(out,factor)
 return out
h_b=product([[306,228,1],[147,471,1],[1012,573,1],[981,112,317,1]])
h_one=product([[95,1],[110,1],[579,1],[787,740,284,741,322,805,1]])
for f,h in zip(polys,[h_b,h_one]):
 power=[1]
 for _ in range(54):power=mul(power,h)
 assert [340*c%p for c in power]==f
gcd,bezout_f,bezout_g=xgcd(h_b,h_one);assert gcd==[1]
assert add(mul(bezout_f,h_b),mul(bezout_g,h_one))==[1]
res=resultant(*polys);assert res
out={'status':'PASS','scope':'fixed E2 all6 embeddings, every deformation ratio; two center fibers cover all ratios by characteristic-zero coprimality','prime':p,'root_t':t,'matrix_size':81,'integer_dot_bound':N*(p-1)**2,'fibers':records,'trace_power_factor':54,'trace_scalar_modp':340,'trace_degree9_factors_low_to_high':[h_b,h_one],'bezout_f_modp':bezout_f,'bezout_g_modp':bezout_g,'bezout_identity':'bezout_f*h_b+bezout_g*h_one=1','resultant_modp':res,'characteristic_zero_lift':'models first constructed over K[a]; all generator filtered-degree inequalities exact, hence det degree<=486; both modular degrees486 preserve actual degrees; nonzero Sylvester resultant lifts to K','not_claimed':['all E in L curve','actual division or Brauer period separately computed','complete H3 classification']}
Path(__file__).with_name('cubic_third_root_unit_boundary_L_two_fibers_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','resultant_modp':res,'all_E2_deformation_ratios_excluded':True}))
