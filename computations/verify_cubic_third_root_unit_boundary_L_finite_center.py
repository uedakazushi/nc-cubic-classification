#!/usr/bin/env python3
"""Fresh exact degree6 normal, degree<=9 centers and finite central-module
certificate at E=2,u=1,v=0 over a complete irreducible degree6 field.
No extrapolation to all parameters or full-center assertion is made.
"""
from pathlib import Path
import sympy as s,json
from cubic_incremental_graded import GradedAlgebra
z=s.Symbol('z');K=s.QQ.alg_field_from_poly(s.Poly(z**6-9*z**3+57,z));d=K.unit;e=K.convert(2);o=(1-d**3)/7;one,zero=K.one,K.zero;u=one;v=zero
assert not(o*o+o+one) and s.Poly(z**6-9*z**3+57,z).is_irreducible
assert all([e,e**3-one,e**3+o,e**3+(one+2*o)/3,e**3+(o-one)/3])
R=[{(0,1):one,(1,0):-one},{(0,2):one,(2,0):-o**2},{(0,3):one,(3,0):-o},
 {(1,2):d,(2,1):e,(3,3):one},{(1,3):e,(3,1):d,(2,2):one},
 {(2,3):d,(3,2):e,(0,0):u,(0,1):v,(1,1):one}]
Y=e**3;C=(-(o+2)*Y**2+(1-o)*Y-o*e**2*d-(o+1)*e*d**2)/(Y-one)
G={(2,2,2):o,(2,3,1):-d*((o+2)*Y+o**2),(3,2,1):e*(2-(o+2)*Y),(3,3,3):one,(1,0,0):C}

weights=[0,0,1,2]
RC=[{w:c/o**weights[w[1]] for w,c in rel.items() if c} for rel in R]
GC={w:c/o**sum(j*weights[ww] for j,ww in enumerate(w)) for w,c in G.items() if c}
A=GradedAlgebra(K,4,RC,weights);B=GradedAlgebra(K,4,RC+[GC],weights)
results={}
for name,alg in [('ambient',A),('normal_cut',B)]:
 results[name]={}
 for n in [1,2,3,6,9]:
  M,ids=alg.normal_matrix(n,[one]*4,fixed=(name=='ambient'))
  kernel=len(ids)-M.rank();results[name][str(n)]={'matrix_shape':M.shape,'center_dimension':kernel}
  print(name,'center degree',n,'dimension',kernel,flush=True)

# One additional degree9 central generator modulo k[x,Psi].
Q=(o+2)*(one-Y)
H=(3*(o+1)*Y+(2*o+1)*(e**2*d+e*d**2)-o-2)/(Y-one)
Psi=dict(GC)
for ww,c in { (1,1,1):Q,(1,0,0):H}.items():Psi[ww]=Psi.get(ww,zero)+c

def poly_mul(a,b):
 out={}
 for x,c in a.items():
  for y,dd in b.items():out[x+y]=out.get(x+y,zero)+c*dd
 return {w:c for w,c in out.items() if c}
def poly_pow(a,n):
 out={():one}
 for _ in range(n):out=poly_mul(out,a)
 return out
def vector(alg,p):
 out={}
 for ww,c in p.items():alg.addto(out,alg.word(ww),c)
 return out
M,ids=B.normal_matrix(9,[one]*4,fixed=False);N=M.nullspace().to_list();assert len(N)==5
known=[]
for j in range(4):known.append(vector(B,poly_mul({(0,)*(9-3*j):one},poly_pow(Psi,j))))
from sympy.polys.matrices import DomainMatrix
def rank_vectors(vs,n):return DomainMatrix.from_dod({i:{j:c for j,c in v.items() if c} for i,v in enumerate(vs)},(len(vs),n),K).rank()
assert rank_vectors(known,len(B.basis[9]))==4
for row in N:
 zz={ids[j]:c for j,c in enumerate(row) if c}
 if rank_vectors(known+[zz],len(B.basis[9]))==5:break
lc=zz[min(zz)];zz={i:c/lc for i,c in zz.items()};Z={B.basis[9][i]:c for i,c in zz.items()}
assert rank_vectors(known+[zz],len(B.basis[9]))==5
print('selected central Z9 raw terms',len(Z),flush=True)

def boundary(poly):return {tuple(j-1 for j in ww):c for ww,c in poly.items() if 0 not in ww and c}
SQrels=[rr for r in RC if (rr:=boundary(r))]+[boundary(GC),boundary(Psi)]
SQ=GradedAlgebra(K,3,SQrels,[0,1,2]);SQ.build(9);zbar=vector(SQ,boundary(Z));assert zbar
print('nonzero Z at the 1-dimensional boundary intersection',len(zbar),flush=True)
zrel={SQ.basis[9][i]:c for i,c in zbar.items()}
T=GradedAlgebra(K,3,SQrels+[zrel],[0,1,2]);T.build(13)
t=s.Symbol('t');hilb=s.Poly((1+t+t*t)**2*sum(t**j for j in range(9)),t)
dims=[len(T.basis[j]) for j in range(14)];assert dims==[int(hilb.nth(j)) for j in range(14)] and sum(dims)==81
print('central quotient Artinian dimensions',dims,'sum81',flush=True)

def cc(c):return [str(v) for v in c.to_list()]
def pp(poly):return {''.join('xybc'[j] for j in ww):cc(c) for ww,c in poly.items() if c}
out={'field':'t^6-9t^3+57','omega':'(1-t^3)/7','D':'t','E':2,'u':1,'v':0,
 'Z9_original_polynomial_C_coordinates':pp(Z),'Psi3_original_polynomial_C_coordinates':pp(Psi),
 'center_dimensions':results,'Artinian_dimensions':dims,'rank_over_k_x_Psi_Z':81,
 'not_claimed':['same center basis for all parameters','full center of this example','generic algebra division or H3 admissible']}
out['status']='PASS'
out['scope']='all six characteristic-zero embeddings at E2,u1,v0; exact recursive full relation modules, centers and central regular sequence; ordinary rank81 argument separate'
out['central_base_degrees']=[1,3,9]
# Check all original relation actions from both sides through the computed degree.
def check_actions(alg,top):
 for rel in alg.relations:
  rrlen=len(next(iter(rel)))
  for n in range(rrlen,top+1):
   for i in range(len(alg.basis[n-rrlen])):
    for side in [0,1]:
     total={}
     for ww,c in rel.items():
      state={i:c};degree=n-rrlen
      for letter in (ww if side==0 else tuple(reversed(ww))):
       new={}
       for j,co in state.items():
        action=alg.right[degree+1][j,letter] if side==0 else alg.left[degree+1][letter,j]
        alg.addto(new,action,co)
       state=new;degree+=1
      alg.addto(total,state,one)
     assert not total
for alg,top in [(A,10),(B,10),(T,13)]:check_actions(alg,top)
out['all_original_left_and_right_relation_actions']='PASS through degrees10/10/13'
NM,nids=A.normal_matrix(6,[one,one,o,o**2]);out['inverse_normal6_matrix_shape']=list(NM.shape)
out['inverse_normal6_dimension']=len(nids)-NM.rank();assert out['inverse_normal6_dimension']==2
for alg,n,fixed in [(A,9,True),(B,9,False)]:
 mm,ii=alg.normal_matrix(n,[one]*4,fixed=fixed);nn=mm.nullspace()
 assert not any(nn.matmul(mm.transpose()).to_list_flat())
 assert nn.rank()==nn.shape[0]
Path(__file__).with_name('cubic_third_root_unit_boundary_L_finite_center_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','single_closed_field_degree':6,'central_free_rank':81,'ambient_center9':7,'cut_center9':5,'inverse_normal6':2}))
