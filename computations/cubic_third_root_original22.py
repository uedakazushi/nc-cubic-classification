"""Original22 right-convention twisted-cyclic tops for unit-repeat order3."""
import itertools
from sympy.polys.matrices import DomainMatrix

def top_matrix(K,o,coeff,weights=(0,0,1,2)):
 one,zero=K.one,K.zero;seen=set();tops=[]
 for word in itertools.product(range(4),repeat=4):
  if word in seen:continue
  w=word;c=one;top={}
  while w not in top:
   top[w]=c;seen.add(w);w=(w[-1],)+w[:-1];c=-c/o**weights[w[0]]
  if not(c-one):tops.append(top)
 assert len(tops)==22 and len(coeff)==22
 rows=[[zero]*16 for _ in range(16)]
 for aa,top in zip(coeff,tops):
  for w,c in top.items():rows[4*w[0]+w[1]][4*w[2]+w[3]]+=aa*c
 return DomainMatrix.from_dod({i:{j:c for j,c in enumerate(row) if c} for i,row in enumerate(rows)},(16,16),K)

def relation_vector(K,poly):return {4*w[0]+w[1]:c for w,c in poly.items() if c}
