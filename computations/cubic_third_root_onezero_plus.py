"""Exact original22 model for the normalized one-zero plus rank-one chart."""
import itertools,sympy as s
from cubic_incremental_graded import GradedAlgebra
from sympy.polys.matrices import DomainMatrix
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z))
def compute(K,av,r,k,finite=False):
 o=K.convert(F.unit,F);one,zero=K.one,K.zero
 # Parameters T=s=1; plus lambda=omega, h=r chart.
 co=[zero]*22
 for i,v in {2:av,17:o*(o+one),15:o**2*(o+one),16:one,6:o*r,12:o*r,7:r+k,11:o*r+k*o,8:(o+one)*av+k*r,3:(o+one)*av,9:r,13:r,10:one,21:one}.items():co[i]=v
 R=[co[2],co[6],-co[11],co[15]];S=[co[3],co[7],-co[13],co[16]];L=[[R[i]*R[j]-o**2*S[i]*S[j] for j in range(4)] for i in range(4)]
 for i,v in {0:L[0][1],1:L[0][3],4:L[1][1],5:L[1][3]}.items():co[i]=v
 # Construct the original22 skew-cyclic top directly over the function field.
 import itertools
 seen=set();tops=[]
 for word in itertools.product(range(4),repeat=4):
  if word in seen:continue
  w=word;c=one;top={}
  while w not in top:
   top[w]=c;seen.add(w);w=(w[-1],)+w[:-1];c=-c/o**[0,0,1,2][w[0]]
  if not(c-one):tops.append(top)
 assert len(tops)==22
 for i,counts in {10:(1,0,3,0),16:(0,2,1,1),17:(0,2,1,1),21:(0,0,2,2)}.items():
  assert all(tuple(w.count(j) for j in range(4))==counts for w in tops[i])
 HH=[[zero]*16 for _ in range(16)]
 for aa,top in zip(co,tops):
  for w,c in top.items():HH[4*w[0]+w[1]][4*w[2]+w[3]]+=aa*c
 DD=DomainMatrix.from_dod({i:{j:c for j,c in enumerate(row) if c} for i,row in enumerate(HH)},(16,16),K)
 ii=[0,1,4,5]
 assert all(not(HH[ii[i]][ii[j]]-L[i][j]) for i in range(4) for j in range(4))
 assert all(not(HH[ii[i]][11]-R[i]) and not(HH[ii[i]][14]-S[i]) for i in range(4))
 rr,pp=DD.transpose().rref();rels=[{divmod(j,4):c for j,c in enumerate(row) if c} for row in rr.to_list() if any(row)]
 assert len(rels)==6
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
 B=Alg(K,4,rels,[0,0,1,2]);B.build(4);dims=[len(B.basis[i]) for i in range(5)]
 if finite and dims[3:]!=[20,35]:return {'dimensions':dims,'nonAS4':True}
 assert dims[:3]==[1,4,10]
 M,ids=B.normal_matrix(3,[one,one,o**2,o],fixed=True)
 rows=[dict(row) for row in M.to_dod().values()];pivs=[]
 def complexity(c):
  if finite:return (0,len(c.to_list()))
  return (sum(c.numer.degrees())+sum(c.denom.degrees()),len(c.numer.terms())+len(c.denom.terms()))
 while rows:
  index,j=min(((i,j) for i,row in enumerate(rows) for j in row),key=lambda ij:complexity(rows[ij[0]][ij[1]]))
  row=rows.pop(index);cc=row[j];pivs.append(cc);row={k:c/cc for k,c in row.items()}
  for old in rows:
   if j in old:B.addto(old,row,-old[j])
  rows=[rr for rr in rows if rr]
 assert len(pivs)==len(ids)==8
 _,cp=DD.rref();minor=DD.extract(pp,cp).det();assert minor
 return {'dimensions':dims,'normal_shape':list(M.shape),'normal_pivots':pivs,'source_pivots':log,'relations':rels,'source_minor':minor,'source_rows':list(pp),'source_columns':list(cp)}
