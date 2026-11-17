#!/usr/bin/env python3
"""Exact original top/minor atlas and all last fourth-root normal kernels.
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
a=s.symbols('a:16');Q=s.symbols('q',nonzero=True)
expected=['xxxy','xxyy','xxcc','xyyy','xycc','xbbc','xbcb','xcxc',
          'xcyc','xcbb','xccy','yycc','ybbc','ybcb','ycyc','ycbb']
atlas=[];finite=[]
for imaginary in [s.I,-s.I]:
 for epsilon in [1]:
  mu=[imaginary,imaginary,s.Integer(epsilon),-imaginary];nu=[1/v for v in mu]
  words=list(itertools.product(range(4),repeat=4));seen=set();reps=[];tensors=[]
  for word in words:
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
  H0=H.extract([3,7,10,12,13],[3,7,10,12,13]);H2=H.extract([0,1,4,5,15],[0,1,4,5,15])
  M=H.extract([2,6,8,9],[11,14])
  assert M==s.Matrix([[a[5],a[6]],[a[12],a[13]],[-epsilon*a[6],-epsilon*a[9]],[-epsilon*a[13],-epsilon*a[15]]])
  norm={a[9]:1,a[15]:0,a[12]:0,a[13]:0,a[5]:Q**-2,a[6]:Q**-1}
  assert (M[:,1]-Q*M[:,0]).subs(norm)==s.zeros(4,1)
  H0=H0.subs(norm);H2=H2.subs(norm)
  # For the conjugate sign, use conjugation of the exact QQ(i) identities.
  I=imaginary
  sol={a[11]:0,a[14]:0,a[10]:a[8]*Q**2,a[4]:a[8]/Q**2,
       a[2]:a[7]*(1+I*Q**4)/(2*Q**2)}
  minors=[s.factor(H0.extract(J,L).det()) for J in itertools.combinations(range(5),3) for L in itertools.combinations(range(5),3)]
  for target in [a[11],a[14],a[10]-a[8]*Q**2,a[4]-a[8]/Q**2,
                 2*I*a[2]*Q**2+a[7]*Q**4-I*a[7]]:
   assert any(s.cancel(m/target).is_number and m!=0 for m in minors) or any(s.cancel(m/target).free_symbols<={Q} and m!=0 for m in minors)
  assert all(s.expand(m.subs(sol))==0 for m in minors)
  pf=[s.factor(H2[j,k]*H2[l,m]-H2[j,l]*H2[k,m]+H2[j,m]*H2[k,l]) for j,k,l,m in itertools.combinations(range(5),4)]
  # After a3=0, pure U rank and Pfaffians force q^4=-1 or a0=0.
  assert any(s.cancel(p.subs(sol).subs({a[3]:0,a[1]:0})/(a[0]*a[8]*(1+Q**4))).free_symbols<={Q} and p.subs(sol).subs({a[3]:0,a[1]:0})!=0 for p in pf)
  final={a[0]:0,a[1]:0,a[2]:0,a[7]:0,a[11]:0,a[14]:0,
         a[10]:a[8]*Q**2,a[4]:a[8]*Q**2}
  assert all(s.rem(s.together(p.subs(final)).as_numer_denom()[0],Q**4-1,Q)==0 for p in pf)
  t=s.symbols('t');X=s.Matrix([[1,t],[0,1]]);r=s.Matrix([[0,1],[I,0]])
  assert (X*r*X.T-r-s.Matrix([[(1+I)*t,0],[0,0]])).applyfunc(s.expand)==s.zeros(2)
  atlas.append({'rho':str(I),'epsilon':epsilon,'top_dimension':16,'minor_atlas_and_unipotent_coefficient':True})
  rho=K.convert(I);eps=K.convert(epsilon)
  for q in [one,-one,i,-i]:
   R=[{(1,0):one,(0,1):-rho},{(3,3):one,(1,1):one},
      {(3,0):one,(0,3):rho*q*q},{(1,3):one,(3,1):q*q,(2,2):one},
      {(2,0):one,(0,2):-eps/q},{(3,2):one,(2,3):one/q}]
   WS={n:list(itertools.product(range(4),repeat=n)) for n in [3,4]};IS={n:{w:j for j,w in enumerate(WS[n])} for n in [3,4]};Ps={}
   for n in [3,4]:
    rows=[]
    for r in R:
     for l in range(n-1):
      for pre in itertools.product(range(4),repeat=l):
       for post in itertools.product(range(4),repeat=n-l-2):rows.append({IS[n][pre+w+post]:c for w,c in r.items() if c})
    Ps[n]=echelon(rows)
   assert [len(WS[n])-len(Ps[n]) for n in [3,4]]==[20,35]
   mult=[rho,rho,eps,-rho];inv=[one/v for v in mult]
   free=[w for j,w in enumerate(WS[3]) if j not in Ps[3] and mult[w[0]]*mult[w[1]]*mult[w[2]]==one]
   columns=[]
   for w in free:
    out={}
    for v in range(4):
     row={IS[4][w+(v,)]:one};k=IS[4][(v,)+w];row[k]=row.get(k,zero)-inv[v]
     for k,c in reduced(row,Ps[4]).items():out[v*256+k]=c
    columns.append(out)
   keys=sorted(set().union(*(set(c) for c in columns)))
   mat=s.Matrix([[K.to_sympy(c.get(k,zero)) for c in columns] for k in keys]);kernel=mat.nullspace()
   target={}
   if eps==-one and q==one:target={(1,2,0):one,(2,1,0):one}
   if eps==one and q==-rho:target={(2,2,2):rho,(3,1,2):-rho,(3,2,1):one}
   assert len(kernel)==int(bool(target))
   if target:
    assert list(kernel[0])==[K.to_sympy(target.get(w,zero)) for w in free]
   finite.append({'rho':str(rho),'epsilon':epsilon,'q':str(q),'B3_B4_dimensions':[20,35],
                  'normal_rank':mat.rank(),'invariant_cubic_dimension':len(free),
                  'W1_basis':[{''.join('xybc'[j] for j in w):str(c) for w,c in target.items()}] if target else [],
                  'exclusion':'right x factor' if eps==-one and q==one else 'Ore cone vertex' if target else 'W1 zero'})
assert len(finite)==8
source=json.loads((root/'cubic_fourth_root_negative_repeat_finite_certificate.json').read_text())
assert source['final_spectrum_count']==7
removed=[r for r in source['final_survivors'] if r['N']==4 and r['spectrum'] in [[1,0,3],[3,0,1]]];final=[r for r in source['final_survivors'] if r not in removed]
assert len(removed)==2 and len(final)==5
out={'status':'PASS','scope':'exact original tensor blocks/minors and all8 finite normal kernels; ordinary all-chart, unipotent rigidity and cone Ext proofs separate',
 'orbit_representatives':expected,'atlas_checks':atlas,'finite_kernel_cases':finite,'excluded_spectra':removed,
 'final_survivors':final,'final_spectrum_count':5,'remaining_orders':[3,4],'remaining_counts':{'3':3,'4':2},'Galois_label_orbit_count':3,
 'not_claimed':['all candidate presentations AS4 sufficient','five remaining H3 existence/admissibility','four-eigenvalue/CY coverage','complete H3 classification']}
(root/'cubic_fourth_root_last_finite_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','finite_kernel_cases':8,'remaining_spectra':5,'remaining_orders':[3,4]}))
