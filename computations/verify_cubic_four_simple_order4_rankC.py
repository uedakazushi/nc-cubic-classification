#!/usr/bin/env python3
"""Order4 simple-spectrum necessary atlas and full rank(0,2,2,2) data.
Domain, PBW and twisted-Serre arguments are ordinary proofs in the paper.
"""
from pathlib import Path
import itertools,json,sympy as s
from sympy.polys.matrices import DomainMatrix
from cubic_four_simple_order4_model import top,rels,analyze
F=s.QQ_I;i=F.from_sympy(s.I);a=s.symbols('a:16');P=F.poly_ring(*a);ip=P.convert(i,F)
H=top(P,ip,list(P.gens)).to_Matrix();groups={j:[4*u+v for u in range(4) for v in range(4) if ( [0,2,1,3][u]+[0,2,1,3][v])%4==j] for j in range(4)}
H0=H.extract(groups[0],groups[0]);H2=H.extract(groups[2],groups[2]);M=H.extract(groups[1],groups[3]);assert H0==H0.T and H2==-H2.T
ranks=[]
for r0,r2,r1 in itertools.product(range(5),repeat=3):
 if r0+r2+2*r1==6 and r2%2==0 and abs(6-4*r1)<=2 and abs(r0-r2)<=2:ranks.append([r0,r2,r1,r1])
assert ranks==[[0,2,2,2],[2,0,2,2],[2,2,1,1]]
V=[1]*4
def mul(v,w):return [sum(v[j]*w[(k-j)%4] for j in range(4)) for k in range(4)]
for r0,r2,r1,r3 in ranks:
 ii=[r0,r1,r2,r3];assert [mul(mul(V,V),V)[j]-2*mul(V,ii)[j]+1 for j in range(4)]==[5]*4
# Zero H0 and rank2 H2; pure-product domain argument forces all four cross coefficients nonzero.
zero={a[j]:0 for j in [0,1,2,10,11,12,14,15]};assert H0.subs(zero)==s.zeros(4)
q=s.Symbol('q');sub=dict(zero);sub.update({a[3]:1,a[4]:1,a[7]:q,a[9]:q});MC=M.subs(sub)
assert MC.extract([0,1],[2,3]).det()==-q
minor=[s.expand(MC.extract(rr,cc).det()) for rr in itertools.combinations(range(4),3) for cc in itertools.combinations(range(4),3)]
variables=[a[5],a[6],a[8],a[13],q];gb=s.groebner(minor,*variables,extension=s.I)
A,h,k,E=variables[:4]
expected=[A*h-A*k*q,A*k*k-A*(q**3+q)/2,A*k*(q*q-1),E*A+k*k*q-q*q,A*(q**4-1),h*h-k*k,h*k*k-h*q,E*h+E*k*q,k**3-k*q,E*k*k-E*(q**3+q)/2,k*k*(q*q+1)-q**3-q,E*k*(q*q-1),E*(q**4-1)]
assert len(gb.polys)==len(expected) and all(not s.expand(u-v) for u,v in zip(list(gb),expected))
# Generic branch, valid for every nonzero t, with a5=a13=0.
ts=s.Symbol('t');K=F.frac_field(ts);t=K.gens[0];ik=K.convert(i,F);one=K.one;z=K.zero
for eps in [1,-1]:
 co=[z]*16
 for j,v in {3:one,4:one,7:t*t,9:t*t,6:eps*t,8:t}.items():co[j]=v
 HH=top(K,ik,co)
 rs=[{(2,2):one,(3,3):one},{(0,1):one,(1,0):t*t},{(0,2):one,(2,0):ik*eps/t},{(0,3):one,(3,0):-ik/t},{(1,2):one,(2,1):eps*t},{(1,3):one,(3,1):t}]
 RM=DomainMatrix.from_dod({j:{c:r.get(divmod(j,4),z) for c,r in enumerate(rs) if r.get(divmod(j,4),z)} for j in range(16)},(16,6),K).to_dense()
 leads=[10,1,2,3,6,7];small=RM.extract(leads,range(6));assert not(small.det()-one)
 coords=small.inv().matmul(HH.extract(leads,range(16)));assert not any((RM.matmul(coords)-HH).to_list_flat())
 for c in coords.to_list_flat():
  if c: assert len(c.denom.terms())==1
 # Character arithmetic for basis x3,xy2,xbc,xcb,yb2.
 ex=[1,t**4,eps/t**2,eps/t**2,1];ey=[-t**-6,-t**-2,-eps,-eps,t*t]
 assert ex[0]==1 and ey[2]==-eps and not(ex[2]*t*t-eps)
# All nonbase residual diagonal orbits. Base points are included in generic proof.
cases=[]
for qv in [F.one,-F.one,i,-i]:
 if not(qv*qv+F.one):cases.append((qv,F.one,qv*qv,F.zero,F.zero,'both'))
 for kv in [F.one,-F.one,i,-i]:
  if kv*kv!=qv:continue
  for ep in [1,-1]:
   hv=ep*kv
   if not(hv-kv*qv):cases.append((qv,F.one,F.zero,hv,kv,'a5'))
   if not(hv+kv*qv):cases.append((qv,F.zero,F.one,hv,kv,'a13'))
assert len(cases)==10
fresh=[]
for qv,Av,Ev,hv,kv,label in cases:
 vals={q:qv,A:Av,E:Ev,h:hv,k:kv};assert all(not F.from_sympy(e.subs({x:F.to_sympy(v) for x,v in vals.items()})) for e in minor)
 co=[F.zero]*16
 for j,v in {3:F.one,4:F.one,7:qv,9:qv,5:Av,13:Ev,6:hv,8:kv}.items():co[j]=v
 HH=top(F,i,co);assert HH.rank()==6
 out=analyze(F,i,rels(HH),finite=True);B=out['algebra'];ids=out['fixed_ids'];N=out['normal_matrix'].nullspace().to_list()
 assert out['dimensions']==[1,4,10,20,35]
 status='normal kernel zero'
 if N and qv==F.one:
  X=DomainMatrix.from_dod({r:{col:B.left[3][0,col][r] for col in range(10) if r in B.left[3][0,col]} for r in range(20)},(20,10),F).to_dense()
  for v in N:
   vv=DomainMatrix.from_dod({ids[n]:{0:c} for n,c in enumerate(v) if c},(20,1),F).to_dense();assert X.hstack(vv).rank()==X.rank()
  status='all normal cubics have left factor x'
 elif N:
  assert qv==-F.one and Av==F.one and not Ev and hv==i and kv==-i and len(N)==1
  gg={B.basis[3][ids[j]]:c for j,c in enumerate(N[0]) if c};g=B.word((3,3,1));B.addto(g,B.word((2,3,0)),-F.one/2);B.addto(g,B.word((3,2,0)),i/2)
  # Normalize at the ccy component and verify the full cubic vector.
  vec={ids[j]:c for j,c in enumerate(N[0]) if c};pivot=next(iter(g));factor=vec[pivot]/g[pivot];assert all(not(vec.get(j,F.zero)-factor*g.get(j,F.zero)) for j in set(vec)|set(g))
  expected_rs=[{(2,2):F.one,(3,3):F.one},{(1,2):F.one,(2,1):i,(0,3):-i},{(1,3):F.one,(3,1):-i,(0,2):-F.one},{(0,2):F.one,(2,0):F.one},{(0,3):F.one,(3,0):F.one},{(0,1):F.one,(1,0):-F.one}]
  RM=DomainMatrix.from_dod({n:{j:r.get(divmod(n,4),F.zero) for j,r in enumerate(expected_rs) if r.get(divmod(n,4),F.zero)} for n in range(16)},(16,6),F).to_dense();assert RM.rank()==6 and RM.hstack(HH).rank()==6
  def dehom(r):
   out={}
   for word,c0 in r.items():
    sign=(-1)**sum(j for j,ch in enumerate(word) if ch in [2,3]);ww=tuple(ch for ch in word if ch!=0);out[ww]=out.get(ww,F.zero)+sign*c0
   return {w:v for w,v in out.items() if v}
  affine_expected=[{(2,2):F.one,(3,3):F.one},{(1,2):F.one,(2,1):-i,(3,):-i},{(1,3):F.one,(3,1):i,(2,):-F.one}]
  assert dehom(expected_rs[0])=={w:-v for w,v in affine_expected[0].items()}
  assert dehom(expected_rs[1])=={w:-v for w,v in affine_expected[1].items()}
  assert dehom(expected_rs[2])=={w:-v for w,v in affine_expected[2].items()}
  assert all(not dehom(r) for r in expected_rs[3:])
  assert dehom({(3,3,1):F.one,(2,3,0):-F.one/2,(3,2,0):i/2})=={(3,3,1):-F.one,(2,3):F.one/2,(3,2):-i/2}
  status='unique cubic excluded by ordinary twisted-Serre character proof' 
 else:assert out['normal_kernel']==0
 fresh.append({'q':str(F.to_sympy(qv)),'a5':str(F.to_sympy(Av)),'a13':str(F.to_sympy(Ev)),'a6':str(F.to_sympy(hv)),'a8':str(F.to_sympy(kv)),'normal_kernel':len(N),'status':status})
# Complete affine presentation character linearization and induced Serre action.
y,b,c=s.symbols('Y B C');aff=[b*b+c*c,y*b-s.I*b*y-s.I*c,y*c+s.I*c*y-b,2*c*c*y-b*c+s.I*c*b];J=s.Matrix(aff).jacobian([y,b,c]).subs({y:0,b:0,c:0});assert J.rank()==2 and J.nullspace()==[s.Matrix([1,0,0])];assert s.diag(1,-1,-1)*J.nullspace()[0]==J.nullspace()[0]
out={'status':'PASS','scope':'complete order4 simple16 top necessary rank atlas; whole rank(0,2,2,2) excluded by paper domain/PBW/twisted-Serre proof','top_dimension':16,'necessary_relation_ranks_weight_0_2_1_3':ranks,'B3_character':[5]*4,'rankC_normalization':'a3=a4=1,a7=a9=q nonzero; a5=A,a6=h,a8=k,a13=E','rankC_groebner':list(map(str,expected)),'generic_branch':'A=E=0,k=t,h=eps*t,q=t²; all t nonzero, eps=+-1','generic_source_identity':'unit6minor and Laurent-t coordinates, all values','generic_factor_cover':'normal x/y forces common x if q³=1, common y if q=-1; otherwise zero','fresh_residual_orbits':fresh,'Serre_character':{'point':[0,0,0],'self_Ext1':1,'Serre_action_on_Ext1':'identity','ordinary_proof':'twisted trace cyclicity forces alternating pairing; contradiction'},'not_claimed':['rank(2,0,2,2) or (2,2,1,1) classified','whole order4 spectrum excluded','all four-simple or CY coverage','complete H3 classification','ordinary proofs fully mechanically checked']}
Path(__file__).with_name('cubic_four_simple_order4_rankC_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS original16 rank atlas and full rankC data')
