#!/usr/bin/env python3
"""Exact original top/minor atlas and last negative-simple fourth-root normal kernels.
All-chart coverage, unipotent rigidity and the cone Ext obstruction are ordinary proofs.
"""
import itertools,json,math
from pathlib import Path
import sympy as s
K=s.QQ_I;one=K.one;zero=K.zero;i=K.convert(s.I)
def echelon(rows):
 piv={}
 for row in rows:
  row={k:v for k,v in row.items() if v}
  while row:
   p=min(row)
   if p not in piv:
    c=row[p];piv[p]={k:v/c for k,v in row.items()};break
   c=row[p]
   for k,v in piv[p].items():
    row[k]=row.get(k,zero)-c*v
    if not row[k]:row.pop(k,None)
 return piv

def reduced(row,piv):
 row=dict(row)
 for p,P in sorted(piv.items()):
  c=row.get(p,zero)
  if not c:continue
  for k,v in P.items():
   row[k]=row.get(k,zero)-c*v
   if not row[k]:row.pop(k,None)
 return row


root=Path(__file__).resolve().parent
a=s.symbols('a:17');Q=s.symbols('q',nonzero=True)
p,r,eta=s.symbols('p r eta');alpha,beta=s.symbols('alpha beta',nonzero=True)
AA,BB,DD=s.symbols('A B D');finite=[];atlas=[]
expected=['xxxy','xxyy','xxcc','xyyy','xycc','xbbc','xbcb','xcxc',
          'xcyc','xcbb','xccy','yycc','ybbc','ybcb','ycyc','ycbb','bbbb']
for imaginary in [s.I,-s.I]:
 I=imaginary;mu=[I,I,-s.S.One,-I];nu=[1/v for v in mu]
 seen=set();tensors=[];reps=[]
 for word in itertools.product(range(4),repeat=4):
  if word in seen:continue
  v=word;c=s.S.One;T={}
  while v not in T:
   T[v]=c;seen.add(v);v=(v[-1],)+v[:-1];c=s.expand(-nu[v[0]]*c)
  if c!=1:continue
  reps.append(''.join('xybc'[j] for j in word));tensors.append(T)
 assert reps==expected
 H=s.zeros(16)
 for coefficient,T in zip(a,tensors):
  for word,c in T.items():
   v=(word[-1],)+word[:-1];assert s.expand(T[v]+nu[v[0]]*c)==0
   H[4*word[0]+word[1],4*word[2]+word[3]]+=coefficient*c
 H0=H.extract([3,7,10,12,13],[3,7,10,12,13]);H2=H.extract([0,1,4,5,15],[0,1,4,5,15]);M=H.extract([2,6,8,9],[11,14])
 assert H0[2,2]==a[16]
 assert M==s.Matrix([[a[5],a[6]],[a[12],a[13]],[a[6],a[9]],[a[13],a[15]]])
 norm={a[9]:1,a[15]:0,a[12]:0,a[13]:0,a[5]:Q**-2,a[6]:Q**-1}
 assert (M[:,1]-Q*M[:,0]).subs(norm)==s.zeros(4,1)
 H0=H0.subs(norm).subs(a[16],1)
 J=[0,1,3,4];T=H0.extract(J,J)-H0.extract(J,[2])*H0.extract([2],J)
 assert T==s.Matrix([[a[7]-1,a[8],-I*a[2]+I/Q**2,a[10]],
                     [a[8],a[14],-I*a[4],-I*a[11]],
                     [-I*a[2]+I/Q**2,-I*a[4],-I*a[7]+Q**-4,-I*a[8]],
                     [a[10],-I*a[11],-I*a[8],-I*a[14]]])
 sub={a[7]:1+p**2,a[8]:p*r,a[14]:r**2,a[10]:eta*p*r,
      a[11]:I*eta*r**2,a[4]:I*eta*p*r,a[2]:Q**-2+I*eta*p**2}
 v=s.Matrix([p,r,eta*p,eta*r]);diff=(T.subs(sub)-v*v.T).applyfunc(s.expand)
 # Every coefficient vanishes under eta^2=-I and q^4=-I.
 for e in diff:
  num=s.together(e).as_numer_denom()[0]
  num=s.rem(s.Poly(num,eta).as_expr(),eta**2+I,eta)
  assert s.rem(s.expand(num),Q**4+I,Q)==0
 quad=s.Matrix([[Q**-2+I*eta*p**2,I*eta*p*r],[I*eta*p*r,I*eta*r**2]])
 assert s.expand(quad.det())==I*eta*r**2/Q**2
 # Rank2 Pfaffians with a nondegenerate symmetric pure U relation.
 Kmid=s.Matrix([[0,AA,-I*AA,BB,alpha],[-AA,0,-I*BB,DD,0],
                 [I*AA,I*BB,0,I*DD,0],[-BB,-DD,-I*DD,0,beta],[-alpha,0,0,-beta,0]])
 pf=[s.expand(Kmid[j,k]*Kmid[l,m]-Kmid[j,l]*Kmid[k,m]+Kmid[j,m]*Kmid[k,l]) for j,k,l,m in itertools.combinations(range(5),4)]
 assert all(s.expand(target) in pf for target in [-I*alpha*BB,beta*AA+alpha*DD,I*(-beta*AA+alpha*DD)])
 assert s.solve(pf,[AA,BB,DD],dict=True)==[{AA:0,BB:0,DD:0}]
 atlas.append({'rho':str(I),'top_dimension':17,'extra_orbit':'bbbb','Schur_and_symmetric_quadric_obstruction':True})
 rho=K.convert(I)
 for q in [one,-one,i,-i]:
  R=[{(1,0):one,(0,1):-rho},{(3,3):one,(1,1):one},
     {(3,0):one,(0,3):rho*q*q},{(1,3):one,(3,1):q*q,(2,2):one},
     {(2,0):one,(0,2):one/q},{(3,2):one,(2,3):one/q}]
  WS={n:list(itertools.product(range(4),repeat=n)) for n in [3,4]};IS={n:{w:j for j,w in enumerate(WS[n])} for n in [3,4]};Ps={}
  for n in [3,4]:
   rows=[]
   for rel in R:
    for l in range(n-1):
     for pre in itertools.product(range(4),repeat=l):
      for post in itertools.product(range(4),repeat=n-l-2):rows.append({IS[n][pre+w+post]:c for w,c in rel.items() if c})
   Ps[n]=echelon(rows)
  assert [len(WS[n])-len(Ps[n]) for n in [3,4]]==[20,35]
  mult=[rho,rho,-one,-rho];inv=[one/x for x in mult]
  free=[w for j,w in enumerate(WS[3]) if j not in Ps[3] and mult[w[0]]*mult[w[1]]*mult[w[2]]==one]
  cols=[]
  for w in free:
   out={}
   for j in range(4):
    row={IS[4][w+(j,)]:one};k=IS[4][(j,)+w];row[k]=row.get(k,zero)-inv[j]
    for k,c in reduced(row,Ps[4]).items():out[j*256+k]=c
   cols.append(out)
  keys=sorted(set().union(*(set(c) for c in cols)))
  mat=s.Matrix([[K.to_sympy(c.get(k,zero)) for c in cols] for k in keys]);ker=mat.nullspace()
  assert len(ker)==int(q==one)
  if ker:assert list(ker[0])==[s.S.One if w in [(1,2,0),(2,1,0)] else s.S.Zero for w in free]
  finite.append({'rho':str(rho),'q':str(q),'B3_B4_dimensions':[20,35],'normal_rank':mat.rank(),
                 'W1_basis':['(yb+by)x'] if ker else [],'exclusion':'right x factor' if ker else 'W1 zero'})
source=json.loads((root/'cubic_fourth_root_last_finite_certificate.json').read_text());assert source['final_spectrum_count']==5
removed=[r for r in source['final_survivors'] if r['N']==4];final=[r for r in source['final_survivors'] if r['N']==3]
assert len(removed)==2 and len(final)==3 and len(finite)==8
out={'status':'PASS','scope':'all17 original tensor orbits, Schur identity, binary symmetric-quadric Pfaffians and eight finite kernels; ordinary coverage/unipotent arguments separate',
 'orbit_representatives':expected,'atlas_checks':atlas,'finite_kernel_cases':finite,'excluded_spectra':removed,
 'final_survivors':final,'final_spectrum_count':3,'remaining_orders':[3],'remaining_counts':{'3':3},'Galois_label_orbit_count':2,
 'not_claimed':['remaining3 H3 existence/admissibility','four-eigenvalue or CY completeness','complete H3 classification']}
(root/'cubic_fourth_root_last_negative_simple_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','remaining_spectra':3,'remaining_orders':[3]}))
