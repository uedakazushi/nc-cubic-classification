#!/usr/bin/env python3
"""Exact48-dimensional central slice used to recover the order4 cubic center.
A single EXACT evaluation, not by itself an all-parameter claim. Safe degreewise
checkpoints in the supplied workspace; successful sample results are small JSON.
"""
import sympy as s,json,time
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
T,D=s.symbols('g D');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));g=K.unit;zero,one=K.zero,K.one
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--D',type=int,required=True);parser.add_argument('--z1',type=int,required=True);parser.add_argument('--z2',type=int,required=True);parser.add_argument('--work-dir',type=Path,required=True);args=parser.parse_args()
args.work_dir.mkdir(parents=True,exist_ok=True);started=time.monotonic()
sample={'D':args.D,'c1':args.z1,'c2':args.z2};prefix=str(args.work_dir/('sample_'+str(args.D)+'_'+str(args.z1)+'_'+str(args.z2)))
def cv(expr):
 p=s.Poly(s.sympify(expr).subs(D,sample['D']),T,domain=s.QQ);return K.new(p.all_coeffs())
relations=[]
for i,j,k,alpha,beta in [(0,1,2,-2,1),(1,2,0,-2,1),(2,0,1,0,2)]:
 relations.append({(j,k):1+g,(k,j):1-g,(i,i):-one,(3,i):-K.convert(alpha),(3,3):-K.convert(beta)});relations.append({(3,i):one,(i,3):-one})
source=json.load(Path(__file__).with_name('cubic_clifford_integration_certificate.json').open());GG={}
subs={'h':1,'z':K.to_sympy(g),'A':1/(2*K.to_sympy(g)),'B':1/(2*K.to_sympy(g)),'C':0,'beta_x':1,'beta_y':1,'beta_z':2,'D':sample['D']}
for r in source['integrated_cut_coefficients']:GG[(3,)*r['t_power']+tuple(r['active_word'])]=K.from_sympy(s.sympify(r['coefficient']).subs(subs,simultaneous=True))
relations.append(GG)
centers=json.load(Path(__file__).with_name('cubic_order4_center_certificate.json').open())['basis'];zs=[]
for i,zi in enumerate(centers[:3]):
 poly={tuple(row['word']):cv(row['coefficient']) for row in zi};zs.append(poly)
 if i<2:
  rel=poly.copy();rel[(3,3,3,3)]=rel.get((3,3,3,3),zero)-K.convert(sample['c'+str(i+1)]);relations.append(rel)
basis=[[()]];Ls=[]
def mvec(M,v):
 out={}
 for i,row in enumerate(M):
  c=sum((a*v.get(j,zero) for j,a in row.items()),zero)
  if c:out[i]=c
 return out
def evword(word):
 v={0:one}
 for n,i in enumerate(reversed(word)):v=mvec(Ls[n][i],v)
 return v
def expected(n):return (1+3*n*(n+1)//2 if n>=0 else 0)-2*(1+3*(n-4)*(n-3)//2 if n>=4 else 0)+(1+3*(n-8)*(n-7)//2 if n>=8 else 0)
def save():
 def en(c):return [str(v) for v in c.to_list()]
 obj={'sample':sample,'basis':basis,'Ls':[[[{str(j):en(c) for j,c in row.items()} for row in mat] for mat in degree] for degree in Ls]}
 Path(prefix+'_cache.json').write_text(json.dumps(obj))
def step(n):
 prev=basis[-1];cand=[(i,j,(i,)+w) for i in range(4) for j,w in enumerate(prev)];cand.sort(key=lambda v:(-sum(c!=3 for c in v[2]),v[2]));index={(i,j):k for k,(i,j,w) in enumerate(cand)};rows=[]
 for rel in relations:
  deg=len(next(iter(rel)))
  if deg>n:continue
  for bw in basis[n-deg]:
   row={}
   for word,c in rel.items():
    for j,v in evword(word[1:]+bw).items():
     k=index[(word[0],j)];row[k]=row.get(k,zero)+c*v
   rows.append({k:c for k,c in row.items() if c})
 M=DomainMatrix.from_dod({i:r for i,r in enumerate(rows)},(len(rows),len(cand)),K);rr,piv=M.rref();rr=rr.to_dod();free=[j for j in range(len(cand)) if j not in piv];P=[{j:one} for j in free]
 for k,col in enumerate(piv):
  for i,j in enumerate(free):
   c=rr.get(k,{}).get(j,zero)
   if c:P[i][col]=-c
 L=[[{} for _ in free] for i in range(4)]
 for i in range(4):
  for j in range(len(prev)):
   col=index[(i,j)]
   for k,row in enumerate(P):
    c=row.get(col,zero)
    if c:L[i][k][j]=c
 Ls.append(L);basis.append([cand[j][2] for j in free]);assert len(free)==expected(n),(n,len(free),expected(n));save();print('sample',sample,'degree',n,'dimension',len(free),'matrix',M.shape,flush=True)
cache=Path(prefix+'_cache.json')
if cache.exists():
 c=json.loads(cache.read_text());assert c['sample']==sample;basis=[[tuple(w) for w in ws] for ws in c['basis']];Ls=[[[{int(j):K.new([s.QQ(v) for v in coeff]) for j,coeff in row.items()} for row in mat] for mat in degree] for degree in c['Ls']];print('resumed degree',len(basis)-1,flush=True)
for n in range(len(basis),10):step(n)
def dm(rows):return DomainMatrix.from_dod({i:r for i,r in enumerate(rows)},(48,48),K)
tinv=dm(Ls[8][3]).inv();X=[tinv*dm(Ls[8][i]) for i in range(3)];Xrows=[m.to_dod() for m in X]
def xv(i,v):
 out={}
 for row,cols in Xrows[i].items():
  c=sum((a*v.get(j,zero) for j,a in cols.items()),zero)
  if c:out[row]=c
 return out
def act(word,v):
 for i in reversed(word):
  if i!=3:v=xv(i,v)
 return v
unit={basis[8].index((3,)*8):one};vZ={}
for w,c in zs[2].items():
 for i,d in act(w,unit).items():vZ[i]=vZ.get(i,zero)+c*d
cols=[act(w,vZ) for w in basis[8]];Z=DomainMatrix.from_dod({i:{j:col[i] for j,col in enumerate(cols) if col.get(i,zero)} for i in range(48)},(48,48),K)
print('Z3 regular-representation matrix built',flush=True)
Z2=Z*Z;Z3=Z2*Z
tr=lambda M:sum((M[i,i].element for i in range(48)),zero)
s1,s2,s3=[tr(M)/16 for M in [Z,Z2,Z3]];c2=-s1;c1=(s1*s1-s2)/2;c0=-(s3+c2*s2+c1*s1)/3
I=DomainMatrix.eye(48,K);assert (Z3+Z2.scalarmul(c2)+Z.scalarmul(c1)+I.scalarmul(c0)).is_zero_matrix
flat=DomainMatrix.from_dod({i*48+j:{0:I.to_dod().get(i,{}).get(j,zero),1:Z.to_dod().get(i,{}).get(j,zero),2:Z2.to_dod().get(i,{}).get(j,zero)} for i in range(48) for j in range(48)},(2304,3),K);assert flat.rank()==3
def txt(c):
 v=c.to_list();return str(s.factor(sum(s.Rational(str(a))*T**(len(v)-1-i) for i,a in enumerate(v))))
Path(prefix+'_result.json').write_text(json.dumps({'sample':sample,'finite_dimension':48,'minimum_polynomial_coefficients':list(map(txt,[one,c2,c1,c0])),'degrees':[len(b) for b in basis],'elapsed_seconds':time.monotonic()-started,'minimum_polynomial_identity_verified':True,'power_rank':3},indent=2)+'\n');print('CUBIC MINIMUM POLYNOMIAL VERIFIED',[txt(c) for c in [one,c2,c1,c0]],flush=True)
