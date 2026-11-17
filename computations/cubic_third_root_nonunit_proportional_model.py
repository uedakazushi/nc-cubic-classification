"""Two-parameter canonical model in coordinates x,Y,b,c, with μ=(ω,ω,1,ω²)."""
from cubic_incremental_graded import GradedAlgebra

def relations(K,o,l,Z):
 one=K.one
 return [{(0,3):one,(3,0):-o**2},{(2,2):one,(1,3):one,(3,1):o**2,(0,3):-2*l},
 {(2,1):one,(1,2):-o**2},{(1,2):one,(0,2):-o**2,(2,0):-one,(3,3):-one},
 {(2,3):one,(0,0):-one,(0,1):o,(1,1):Z},{(3,2):one,(0,0):-o**2,(1,0):one,(1,1):o**2*Z}]

def analyze(K,o,l,Z,finite=False):
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
 B=Alg(K,4,relations(K,o,l,Z),[1,1,0,2]);M,ids=B.normal_matrix(3,[o**2,o**2,K.one,o],fixed=True)
 rows=list(M.to_dod().values());np=[]
 def complexity(c):
  if finite:return (0,len(c.to_list()))
  return (sum(c.numer.degrees())+sum(c.denom.degrees()),len(c.numer.terms())+len(c.denom.terms()))
 while rows:
  i,j=min(((i,j) for i,row in enumerate(rows) for j in row),key=lambda ij:complexity(rows[ij[0]][ij[1]]))
  row=rows.pop(i);cc=row[j];np.append(cc);row={k:c/cc for k,c in row.items()}
  for old in rows:
   if j in old:B.addto(old,row,-old[j])
  rows=[rr for rr in rows if rr]
 assert len(np)==len(ids)
 return {'source_pivots':log,'normal_pivots':np,'normal_shape':list(M.shape),'dimensions':[len(B.basis[j]) for j in range(5)]}
