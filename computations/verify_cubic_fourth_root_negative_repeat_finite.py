#!/usr/bin/env python3
"""Exact original top atlas and all finite normal kernels for negative-repeat N4.
Atlas coverage, normalization and the absence of unipotent lifts are ordinary proofs.
"""
from pathlib import Path
import itertools,json,math
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
expected=['xxxx','xxxy','xxyy','xxbb','xyxy','xyyy','xybb','xbyb','xbby',
          'xbcc','xcbc','xccb','yyyy','yybb','ybcc','ycbc','yccb']
a=s.symbols('a:17');Q=s.symbols('q',nonzero=True)
atlas_checks=[]
for imaginary in [s.I,-s.I]:
 mu=[-s.S.One,-s.S.One,s.S.One,imaginary];nu=[1/v for v in mu]
 words=list(itertools.product(range(4),repeat=4));seen=set();tensors=[];reps=[]
 for word in words:
  if word in seen:continue
  v=word;co=s.S.One;T={}
  while v not in T:
   T[v]=co;seen.add(v);v=(v[-1],)+v[:-1];co=s.expand(-nu[v[0]]*co)
  if co!=1:continue
  reps.append(''.join('xybc'[j] for j in word));tensors.append(T)
 assert reps==expected
 H=s.zeros(16)
 for coefficient,T in zip(a,tensors):
  for word,co in T.items():
   v=(word[-1],)+word[:-1]
   assert s.expand(T[v]+nu[v[0]]*co)==0
   H[4*word[0]+word[1],4*word[2]+word[3]]+=coefficient*co
 H0=H.extract([0,1,4,5,10],[0,1,4,5,10])
 N=H.extract([2,6,8,9,15],[2,6,8,9,15])
 M=H.extract([3,7,12,13],[11,14])
 assert H0==H0.T and N==-N.T
 assert M==s.Matrix([[a[10],a[11]],[a[15],a[16]],
                     [imaginary*a[9],imaginary*a[10]],[imaginary*a[14],imaginary*a[15]]])
 norm={a[9]:1,a[10]:Q,a[11]:Q**2,a[14]:0,a[15]:0,a[16]:0}
 assert (M[:,1]-Q*M[:,0]).subs(norm)==s.zeros(4,1)
 N=N.subs(norm)
 pf=[s.factor(N[j,k]*N[l,m]-N[j,l]*N[k,m]+N[j,m]*N[k,l])
     for j,k,l,m in itertools.combinations(range(5),4)]
 assert pf==[-a[13]*a[3]+a[6]*a[8]-a[7]**2,a[6]-a[7]*Q**2,
              a[13],-a[7]+a[8]*Q**2,a[13]*Q**2]
 solved={a[13]:0,a[6]:a[8]*Q**4,a[7]:a[8]*Q**2}
 assert all(s.expand(v.subs(solved))==0 for v in pf)
 H0=H0.subs(solved)
 assert H0[:,4]==s.Matrix([a[3],a[8]*Q**4,a[8],0,0])
 # On q^4=1, a2=a3*a5/a8, a4=a2; after the shear a3=0:
 H0=H0.subs({Q**4:1,a[3]:0,a[2]:0,a[4]:0,a[12]:0})
 assert s.factor(H0.extract([0,1,4],[0,1,4]).det())==-a[0]*a[8]**2
 H0=H0.subs(a[0],0)
 r=s.Matrix([0,1,1,0,0]);p=s.Matrix([a[1],0,0,a[5],a[8]])
 assert H0==r*p.T+p*r.T
 # Unipotent y->y+t*x changes the sole pure U relation by 2*t*x^2.
 t=s.symbols('t');X=s.Matrix([[1,t],[0,1]]);relation=s.Matrix([[0,1],[1,0]])
 assert X*relation*X.T-relation==s.Matrix([[2*t,0],[0,0]])
 atlas_checks.append({'imaginary_root':str(imaginary),'top_dimension':17,'Pfaffians_and_normalform':True})
finite=[]
for imaginary in [i,-i]:
 for q in [one,-one,i,-i]:
  for A in [0,1]:
   R=[{(1,0):one,(0,1):one},{(2,2):one,(0,0):K.convert(A),(1,1):one},
      {(2,0):one,(0,2):-q*q},{(2,1):one,(1,2):q*q,(3,3):one},
      {(3,0):one,(0,3):-imaginary*q},{(3,2):one,(2,3):one/q}]
   WS={n:list(itertools.product(range(4),repeat=n)) for n in [3,4]}; IS={n:{w:j for j,w in enumerate(WS[n])} for n in [3,4]};Ps={}
   for n in [3,4]:
    rows=[]
    for r in R:
     for l in range(n-1):
      for pre in itertools.product(range(4),repeat=l):
       for post in itertools.product(range(4),repeat=n-l-2):
        rows.append({IS[n][pre+w+post]:c for w,c in r.items() if c})
    Ps[n]=echelon(rows)
   dims=[len(WS[n])-len(Ps[n]) for n in [3,4]]
   free=[w for j,w in enumerate(WS[3]) if j not in Ps[3] and sum([2,2,0,1][k] for k in w)%4==0]
   columns=[]
   muinv=[-one,-one,one,one/imaginary]
   for w in free:
    out={}
    for v in range(4):
     row={IS[4][w+(v,)]:one}
     k=IS[4][(v,)+w];row[k]=row.get(k,zero)-muinv[v]
     row=reduced(row,Ps[4])
     for k,c in row.items():out[v*256+k]=c
    columns.append(out)
   keys=sorted(set().union(*(set(c) for c in columns)))
   M=s.Matrix([[K.to_sympy(c.get(k,zero)) for c in columns] for k in keys])
   ker=M.nullspace()
   assert dims==[20,35] and len(free)==6
   expected_kernel=1 if q==one else 0
   assert len(ker)==expected_kernel
   if ker:
    assert free.index((3,3,0))>=0
    assert list(ker[0])==[s.S.One if w==(3,3,0) else s.S.Zero for w in free]
   finite.append({'imaginary_root':str(imaginary),'q':str(q),'A':A,'B3_B4_dimensions':dims,
                  'invariant_cubic_basis':[''.join('xybc'[j] for j in w) for w in free],
                  'normal_matrix_rank':M.rank(),'W1_basis':['ccx'] if ker else []})

assert len(finite)==16
source=json.loads((root/'cubic_fourth_root_unit_repeat_resonance_certificate.json').read_text())
assert source['final_spectrum_count']==9
removed=[r for r in source['final_survivors'] if r['N']==4 and r['spectrum'] in [[2,0,1],[2,0,3]]]
assert len(removed)==2
final=[r for r in source['final_survivors'] if r not in removed]
assert len(final)==7
reps=set()
for r in final:
 N=r['N'];A,b,c=r['spectrum']
 reps.add(min((N,A*u%N,*sorted([b*u%N,c*u%N])) for u in range(1,N) if math.gcd(u,N)==1))
assert len(reps)==4
out={'status':'PASS','scope':'original twisted top blocks and finite exact normal kernels for both signs; ordinary atlas coverage and unipotent-rigidity proof separate',
 'orbit_representatives':expected,'atlas_checks':atlas_checks,'finite_kernel_cases':finite,
 'excluded_spectra':removed,'final_survivors':final,'final_spectrum_count':7,'remaining_orders':[3,4],
 'remaining_counts':{'3':3,'4':4},'Galois_label_orbit_count':4,'Galois_label_representatives':sorted(reps),
 'not_claimed':['all eight candidate presentations AS4 sufficient','remaining7 H3 existence/admissibility','four-eigenvalue/CY completeness','complete H3 classification']}
(root/'cubic_fourth_root_negative_repeat_finite_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','finite_normal_kernel_cases':16,'remaining_spectra':7}))
