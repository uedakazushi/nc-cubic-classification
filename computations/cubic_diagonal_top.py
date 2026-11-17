"""Exact original twisted-cyclic highest tensors for arbitrary diagonal Nakayama.
No AS or Hilbert condition is inferred from these linear solutions alone.
"""
import itertools
from sympy.polys.matrices import DomainMatrix

def top_basis(K,eigenvalues):
 seen=set();out=[]
 for word in itertools.product(range(4),repeat=4):
  if word in seen:continue
  w=word;c=K.one;ts={}
  while w not in ts:
   ts[w]=c;seen.add(w);w=(w[-1],)+w[:-1];c=-c/eigenvalues[w[0]]
  if not(c-K.one):out.append(ts)
 assert len(seen)==256
 return out

def top_matrix(K,eigenvalues,coefficients):
 basis=top_basis(K,eigenvalues);assert len(basis)==len(coefficients);data={}
 for co,ts in zip(coefficients,basis):
  for w,c in ts.items():
   v=co*c
   if v:data.setdefault(4*w[0]+w[1],{})[4*w[2]+w[3]]=v
 return DomainMatrix.from_dod(data,(16,16),K).to_dense()
