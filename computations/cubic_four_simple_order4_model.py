"""Exact original16 top and full graded normal incidence for order4 simple spectrum."""
import itertools,sympy as s
from cubic_incremental_graded import GradedAlgebra
from sympy.polys.matrices import DomainMatrix
weights=[0,2,1,3]
def top(K,i,co):
 seen=set();tops=[]
 for word in itertools.product(range(4),repeat=4):
  if word in seen:continue
  w=word;c=K.one;ts={}
  while w not in ts:ts[w]=c;seen.add(w);w=(w[-1],)+w[:-1];c=-c/i**weights[w[0]]
  if not(c-K.one):tops.append(ts)
 assert len(tops)==16
 dod={}
 for aa,ts in zip(co,tops):
  for w,c in ts.items():
   if aa*c:dod.setdefault(4*w[0]+w[1],{})[4*w[2]+w[3]]=aa*c
 return DomainMatrix.from_dod(dod,(16,16),K).to_dense()
def rels(H):
 K=H.domain;cols=list(H.transpose().to_list());p=H.rref()[1]
 return [{divmod(j,4):c for j,c in enumerate(cols[k]) if c} for k in p]
def analyze(K,i,rs,finite=False):
 log=[]
 class Alg(GradedAlgebra):
  def echelon(self,rows):
   piv={}
   for row in rows:
    row={j:c for j,c in row.items() if c}
    while row:
     j=min(row)
     if j not in piv:
      cc=row[j];log.append(cc);piv[j]={k:c/cc for k,c in row.items()};break
     self.addto(row,piv[j],-row[j])
   return piv
 B=Alg(K,4,rs,weights);B.build(4);ids=[j for j,w in enumerate(B.basis[3]) if sum(weights[k] for k in w)%4==0];cols=[]
 for j in ids:
  col={}
  for k in range(4):
   row=dict(B.right[4][j,k]);B.addto(row,B.left[4][k,j],-i**(-weights[k]))
   for r,c in row.items():col[k*len(B.basis[4])+r]=c
  cols.append(col)
 keys=sorted(set().union(*(set(c) for c in cols)));M=DomainMatrix.from_dod({r:{j:c[k] for j,c in enumerate(cols) if k in c} for r,k in enumerate(keys)},(len(keys),len(cols)),K)
 rows=list(M.to_dod().values());np=[]
 def complexity(c):
  if finite:return 0
  return (sum(c.numer.degrees())+sum(c.denom.degrees()),len(c.numer.terms())+len(c.denom.terms()))
 while rows:
  ij=[(n,j) for n,row in enumerate(rows) for j in row];n,j=min(ij,key=lambda ij:complexity(rows[ij[0]][ij[1]]));row=rows.pop(n);cc=row[j];np.append(cc);row={k:c/cc for k,c in row.items()}
  for old in rows:
   if j in old:B.addto(old,row,-old[j])
  rows=[rr for rr in rows if rr]
 return {'source_pivots':log,'normal_pivots':np,'normal_shape':M.shape,'dimensions':[len(B.basis[j]) for j in range(5)],'normal_kernel':len(ids)-len(np),'relations':rs,'normal_matrix':M,'algebra':B,'fixed_ids':ids}
