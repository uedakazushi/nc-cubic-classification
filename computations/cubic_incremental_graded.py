"""Exact recursive graded relation modules and left/right multiplication.
Uses all suffix-ending defining relations after reducing the prefix; no Hilbert
series assumption is used to select or discard relation rows.
"""
import itertools
class GradedAlgebra:
 def __init__(self,K,g,relations,weights):
  self.K=K;self.g=g;self.relations=relations;self.weights=weights;self.basis={0:[()],1:[(j,) for j in range(g)]};self.index={0:{():0},1:{(j,):j for j in range(g)}}
  self.right={1:{(0,j):{j:K.one} for j in range(g)}};self.left={1:{(j,0):{j:K.one} for j in range(g)}}
 def addto(self,A,B,scalar):
  for j,c in B.items():
   A[j]=A.get(j,self.K.zero)+scalar*c
   if not A[j]:A.pop(j,None)
 def echelon(self,rows):
  piv={}
  for row in rows:
   row={j:c for j,c in row.items() if c}
   while row:
    j=min(row)
    if j not in piv:
     co=row[j];piv[j]={k:c/co for k,c in row.items()};break
    self.addto(row,piv[j],-row[j])
  return piv
 def reduce(self,row,P):
  row={j:c for j,c in row.items() if c}
  for j,p in sorted(P.items()):
   if j in row:self.addto(row,p,-row[j])
  return row
 def build(self,n):
  if n in self.basis:return
  self.build(n-1);K=self.K
  candidates=sorted([(i,j) for i in range(len(self.basis[n-1])) for j in range(self.g)],key=lambda ij:((self.basis[n-1][ij[0]]+(ij[1],)).count(0),self.basis[n-1][ij[0]]+(ij[1],)))
  ci={ij:k for k,ij in enumerate(candidates)};rows=[]
  for rel in self.relations:
   rrlen=len(next(iter(rel)))
   if rrlen>n:continue
   for prefix in range(len(self.basis[n-rrlen])):
    row={}
    for w,c in rel.items():
     state={prefix:c};deg=n-rrlen
     for letter in w[:-1]:
      new={}
      for j,co in state.items():self.addto(new,self.right[deg+1][j,letter],co)
      state=new;deg+=1
     for j,co in state.items():row[ci[j,w[-1]]]=row.get(ci[j,w[-1]],K.zero)+co
    rows.append(row)
  piv=self.echelon(rows);free=[j for j in range(len(candidates)) if j not in piv];fi={j:k for k,j in enumerate(free)}
  self.basis[n]=[self.basis[n-1][candidates[j][0]]+(candidates[j][1],) for j in free];self.index[n]={w:j for j,w in enumerate(self.basis[n])}
  self.right[n]={ij:{fi[j]:c for j,c in self.reduce({k:K.one},piv).items()} for k,ij in enumerate(candidates)}
  left={}
  for letter in range(self.g):
   for j,w in enumerate(self.basis[n-1]):
    pre=self.index[n-2][w[:-1]];out={}
    for k,c in self.left[n-1][letter,pre].items():self.addto(out,self.right[n][k,w[-1]],c)
    left[letter,j]=out
  self.left[n]=left
  print('degree',n,'dimension',len(free),flush=True)
 def word(self,w):
  state={0:self.K.one}
  for deg,letter in enumerate(w,1):
   new={}
   for j,c in state.items():self.addto(new,self.right[deg][j,letter],c)
   state=new
  return state
 def normal_matrix(self,n,phases,fixed=True):
  from sympy.polys.matrices import DomainMatrix
  self.build(n+1);selected=[i for i,w in enumerate(self.basis[n]) if not fixed or sum(self.weights[j] for j in w)%3==0];cols=[]
  for i in selected:
   col={}
   for letter,phase in enumerate(phases):
    row=dict(self.right[n+1][i,letter]);self.addto(row,self.left[n+1][letter,i],-phase)
    for j,c in row.items():col[letter*len(self.basis[n+1])+j]=c
   cols.append(col)
  keys=sorted(set().union(*(set(c) for c in cols)))
  M=DomainMatrix.from_dod({r:{j:c[k] for j,c in enumerate(cols) if k in c} for r,k in enumerate(keys)},(len(keys),len(cols)),self.K)
  return M,selected
