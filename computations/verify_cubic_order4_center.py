#!/usr/bin/env python3
"""Exact quartic centers for one fixed order4 envelope, with symbolic central value.
Degreewise quotient construction: AS4 envelope over QQ(g), then its small cubic
quotient over QQ(g)(D). No high-degree free-word enumeration or D sampling.
This checks three independent leading quartics and all central commutators.
The center-generator and relative-base-change consequences require the paper proof;
no complete bad-D classification or computed cubic center relation is asserted.
"""
import sympy as s,json,time
from sympy.polys.matrices import DomainMatrix
from pathlib import Path
T,D=s.symbols('g D');K=s.QQ.alg_field_from_poly(s.Poly(T**4-2,T));F=K;g=K.unit;zero,one=F.zero,F.one
# Degreewise quotients, never enumerate all free words at high degree.
relations=[]
for i,j,k,alpha,beta in [(0,1,2,-2,1),(1,2,0,-2,1),(2,0,1,0,2)]:
 relations.append({(j,k):1+g,(k,j):1-g,(i,i):-one,(3,i):-F.convert(alpha),(3,3):-F.convert(beta)})
 relations.append({(3,i):one,(i,3):-one})
basis=[ [()] ];Ls=[]
def mvec(M,v):
 out={}
 for i,row in enumerate(M):
  z=sum((c*v.get(j,zero) for j,c in row.items()),zero)
  if z:out[i]=z
 return out
def evword(word):
 v={0:one}
 for d,i in enumerate(reversed(word)):v=mvec(Ls[d][i],v)
 return v
def step(n):
 prev=basis[-1];candidates=[(i,j,(i,)+w) for i in range(4) for j,w in enumerate(prev)];candidates.sort(key=lambda v:(-sum(i!=3 for i in v[2]),v[2]));index={(i,j):k for k,(i,j,w) in enumerate(candidates)}
 rows=[]
 for rel in relations:
  deg=len(next(iter(rel)))
  if deg>n:continue
  for bw in basis[n-deg]:
   row={}
   for word,c in rel.items():
    for j,v in evword(word[1:]+bw).items():
     k=index[(word[0],j)];row[k]=row.get(k,zero)+c*v
   rows.append({k:c for k,c in row.items() if c})
 M=DomainMatrix.from_dod({i:r for i,r in enumerate(rows)},(len(rows),len(candidates)),F);rr,piv=M.rref();rr=rr.to_dod();free=[j for j in range(len(candidates)) if j not in piv]
 P=[{j:one} for j in free]
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
 Ls.append(L);basis.append([candidates[j][2] for j in free])
 assert len(free)==(n+1)*(n+2)*(n+3)//6,(n,len(free))
 print('degree',n,'dimension',len(free),'matrix',M.shape,flush=True)
for n in range(1,6):step(n)

# From this point only the small central quotient uses the variable D.
F=K.frac_field(D);zero,one=F.zero,F.one
Ls=[[[{j:F.convert(c,K) for j,c in row.items()} for row in mat] for mat in degree] for degree in Ls]
g=F.convert(K.unit,K)
data=json.load(Path(__file__).with_name('cubic_clifford_integration_certificate.json').open())
subs={'h':1,'z':K.to_sympy(K.unit),'A':1/(2*K.to_sympy(K.unit)),'B':1/(2*K.to_sympy(K.unit)),'C':0,'beta_x':1,'beta_y':1,'beta_z':2}
G={}
for row in data['integrated_cut_coefficients']:
 expr=s.sympify(row['coefficient']).subs(subs,simultaneous=True);G[(3,)*row['t_power']+tuple(row['active_word'])]=F.from_sympy(expr)
# Quotient the constant-coefficient AS4 envelope by the central cubic in a SMALL second step.
Uproj={};Ufree={}
for n in [4,5]:
 rows=[]
 for bw in basis[n-3]:
  row={}
  for word,c in G.items():
   for j,v in evword(word+bw).items():row[j]=row.get(j,zero)+c*v
  rows.append({j:c for j,c in row.items() if c})
 M=DomainMatrix.from_dod({i:r for i,r in enumerate(rows)},(len(rows),len(basis[n])),F)
 rr,piv=M.rref();rr=rr.to_dod();free=[j for j in range(len(basis[n])) if j not in piv];P=[{j:one} for j in free]
 for k,col in enumerate(piv):
  for i,j in enumerate(free):
   c=rr.get(k,{}).get(j,zero)
   if c:P[i][col]=-c
 Uproj[n]=P;Ufree[n]=free
 assert len(free)==1+3*n*(n+1)//2
 print('central quotient',n,'dimension',len(free),'small matrix',M.shape,flush=True)
cols=[]
for j in Ufree[4]:
 word=basis[4][j];v={}
 for x in range(3):
  left=mvec(Uproj[5],evword((x,)+word));right=mvec(Uproj[5],evword(word+(x,)))
  for j in set(left)|set(right):
   c=left.get(j,zero)-right.get(j,zero)
   if c:v[46*x+j]=c
 cols.append(v)
Z=DomainMatrix.from_dod({i:{j:cols[j].get(i,zero) for j in range(len(cols)) if cols[j].get(i,zero)} for i in range(138)},(138,31),F)
print('center matrix constructed',flush=True)

def coefftext(c):
 assert c.denom.degree()==0
 scale=next(iter(c.denom.to_dict().values()));out=0
 for (power,),value in c.numer.to_dict().items():
  coeff=(value/scale).to_list();q=sum(s.Rational(str(v))*T**(len(coeff)-1-i) for i,v in enumerate(coeff));out+=q*D**power
 return str(s.factor(out))

# A filtered-weight ansatz: quartic constants plus D times affine-linear words.
lower=[i for i,j in enumerate(Ufree[4]) if sum(v!=3 for v in basis[4][j])<=1]
print('lower indices',lower,flush=True)
zd=Z.to_dod();coeff={}
for i,row in zd.items():
 for j,c in row.items():
  assert c.denom.degree()==0
  scale=next(iter(c.denom.to_dict().values()))
  for (power,),v in c.numer.to_dict().items():coeff[(i,j,power)]=v/scale
maxdeg=max(k[2] for k in coeff);print('commutator D degree',maxdeg,flush=True)
rows={}
for (i,j,k),c in coeff.items():
 rows.setdefault(138*k+i,{})[j]=c
 if j in lower:rows.setdefault(138*(k+1)+i,{})[31+lower.index(j)]=c
Ans=DomainMatrix.from_dod(rows,(138*(maxdeg+2),31+len(lower)),K)
ker=Ans.nullspace();print('constant-coefficient ansatz kernel',ker.shape,flush=True)
solutions=[]
for row in ker.to_list():
 v=[F.convert(c,K) for c in row[:31]]
 for k,j in enumerate(lower):v[j]+=F.convert(row[31+k],K)*F.gens[0]
 solutions.append(v)
 VF=DomainMatrix.from_list(solutions,F)
assert (Z*VF.transpose()).is_zero_matrix
# Three independent leading quartics plus the constant give the whole center F4.
top=[i for i,j in enumerate(Ufree[4]) if sum(v!=3 for v in basis[4][j])==4]
Lead=DomainMatrix.from_dod({j:{k:row[i] for k,i in enumerate(top) if row[i]} for j,row in enumerate(ker.to_list())},(ker.shape[0],len(top)),K)
_,ind=Lead.transpose().rref();assert len(ind)==3
chosen=[solutions[i] for i in ind]
for row in chosen:
 scale=next(row[i] for i in top if row[i]);row[:]=[c/scale for c in row]
const=[zero]*31;const[next(i for i,j in enumerate(Ufree[4]) if basis[4][j]==(3,3,3,3))]=one
chosen.append(const)
serial=[]
for row in chosen:
 terms=[]
 for j,c in zip(Ufree[4],row):
  if c:terms.append({'word':list(basis[4][j]),'coefficient':coefftext(c)})
 serial.append(terms)
Path(__file__).with_name('cubic_order4_center_certificate.json').write_text(json.dumps({'version':'classification-v14','field':'QQ(g)(D),g^4=2','word_encoding':'0=x,1=y,2=z,3=t; total degree4; t central', 'fixed_envelope':'h1,alpha=(-2,-2,0),beta=(1,1,2)', 'D_degree_of_commutator_matrix':maxdeg,'leading_quartic_rank':3,'center_relation_status':'Cubic relation coefficients not computed; no all-bad-D claim','B_dimensions':[len(b) for b in basis],'U_dimensions':{'4':31,'5':46},'center_F4_dimension':4,'ansatz_kernel_dimension':ker.shape[0],'basis':serial},indent=2)+'\n')
print('CENTER F4:3 independent polynomial-in-D quartics plus constant verified',flush=True)
