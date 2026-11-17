"""Exact sparse recursive Hilbert quotients; every inserted relation checked."""
from cubic_incremental_graded import GradedAlgebra

class SparseGradedAlgebra(GradedAlgebra):
 # Prefer sparse source rows before choosing pivots, to control exact coefficient growth.
 def echelon(self,rows):
  active=[dict(row) for row in rows if row];piv={}
  while active:
   row=active.pop(min(range(len(active)),key=lambda i:len(active[i])))
   j=min(row);co=row[j];pivot={k:c/co for k,c in row.items()};piv[j]=pivot
   remaining=[]
   for other in active:
    if j in other:self.addto(other,pivot,-other[j])
    if other:remaining.append(other)
   active=remaining
  return piv


 def build(self,n):
  # Only right multiplication is needed for these Hilbert obstructions.
  if n in self.basis:return
  self.build(n-1);F=self.K;previous=len(self.basis[n-1]);rows=[]
  for prefix in range(len(self.basis[n-2])):
   for rel in self.relations:
    row={}
    for (i,j),co in rel.items():
     for k,value in self.right[n-1][prefix,i].items():row[4*k+j]=row.get(4*k+j,F.zero)+co*value
    row={k:v for k,v in row.items() if v}
    if row:rows.append(row)
  piv=self.echelon(rows);free=[j for j in range(4*previous) if j not in piv];fi={j:k for k,j in enumerate(free)}
  self.basis[n]=[self.basis[n-1][j//4]+(j%4,) for j in free]
  self.right[n]={(i,j):{fi[k]:co for k,co in self.reduce({4*i+j:F.one},piv).items()} for i in range(previous) for j in range(4)}
  # Check every original inserted relation against the full coordinate map.
  for row in rows:
   check={}
   for col,co in row.items():self.addto(check,self.right[n][col//4,col%4],co)
   assert not check
  print('degree',n,'dimension',len(free),flush=True)

