"""Exact original-relation linear algebra for the symmetric-secant necessary atlas."""
import itertools
import sympy as S
from sympy.polys.matrices import DomainMatrix
THETA=S.symbols('theta')
QUADRATICS=[(0,0),(0,1),(1,0),(1,1),(2,3),(3,2)]
def relations(h,values):
 A=S.zeros(4)
 for (i,j),c in zip(itertools.combinations(range(4),2),values):A[i,j]=c;A[j,i]=-c
 cU=S.Matrix([[0,1],[-1,0]]);b1=S.diag(1,1);b2=S.diag(1,-1);flip=S.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
 M=-(S.kronecker_product(cU.T,b2)+S.kronecker_product(h.T,b1))*flip
 rewrite=-M.inv()*A
 R=[{(0,1):S.Integer(1),(1,0):-S.Integer(1),(2,2):S.Integer(1),(3,3):S.Integer(1)},{**{(i,j):h[i,j] for i,j in itertools.product(range(2),repeat=2) if h[i,j]},(2,2):S.Integer(1),(3,3):-S.Integer(1)}]
 uv=[(i,j) for i in range(2) for j in range(2,4)];vu=[(i,j) for i in range(2,4) for j in range(2)]
 for i,w in enumerate(vu):R.append({w:S.Integer(1),**{v:S.cancel(-rewrite[i,j]) for j,v in enumerate(uv) if rewrite[i,j]}})
 return R

def quotient(R,n,K):
 words=list(itertools.product(range(4),repeat=n));index={w:i for i,w in enumerate(words)};rows=[]
 for rel in R:
  for pos in range(n-1):
   for extra in itertools.product(range(4),repeat=n-2):
    row={index[extra[:pos]+w+extra[pos:]]:K.from_sympy(S.sympify(c)) for w,c in rel.items() if c}
    rows.append({j:c for j,c in row.items() if c})
 dm=DomainMatrix({i:row for i,row in enumerate(rows) if row},(len(rows),len(words)),K);rr,piv=dm.rref();data=rr.to_dod();free=[i for i in range(len(words)) if i not in piv];outindex={v:j for j,v in enumerate(free)}
 nf={i:{outindex[j]:-c for j,c in data[k].items() if j in outindex and c} for k,i in enumerate(piv)}
 nf.update({i:{outindex[i]:K.one} for i in free})
 for row in rows:
  value={}
  for j,c in row.items():
   for v,d in nf[j].items():value[v]=value.get(v,K.zero)+c*d
  assert not any(value.values())
 return words,index,free,nf

def coordinates(R,K):
 w3,i3,f3,nf3=quotient(R,3,K);w4,i4,f4,nf4=quotient(R,4,K)
 E=[i for i in f3 if sum(v>=2 for v in w3[i])%2==0];assert len(E)==10
 ei={v:i for i,v in enumerate(E)};N=S.zeros(4*len(f4),10);L=S.zeros(10,6)
 for j,v in enumerate(E):
  for g in range(4):
   for raw,c in [(w3[v]+(g,),1),((g,)+w3[v],-1 if g<2 else 1)]:
    for row,d in nf4[i4[raw]].items():N[g*len(f4)+row,j]+=c*K.to_sympy(d)
 for j,word in enumerate(QUADRATICS):
  for v,c in [(0,S.Integer(1)),(1,THETA)]:
   for row,d in nf3[i3[(v,)+word]].items():L[ei[f3[row]],j]+=c*K.to_sympy(d)
 return N.applyfunc(S.cancel),L.applyfunc(S.cancel),nf3,nf4

def polynomial_rows(N,variable):
 rows=[]
 for i in range(N.rows):
  row=[S.cancel(c) for c in N[i,:]];den=S.lcm([S.denom(c) for c in row]);row=[S.cancel(c*den) for c in row]
  if any(row):rows.append(row)
 return S.Matrix(rows)
