"""Polynomial quartic annihilators, replayed without any generic quotient elimination."""
import itertools,json
from pathlib import Path
import sympy as S
from sympy.polys.matrices import DomainMatrix
from cubic_order2_22_secant_tools import relations
RHO,SIGMA,TAU=S.symbols('r s t')
def normal_matrix(input_names=None):
 r,s,t=RHO,SIGMA,TAU;P=S.QQ.poly_ring(r,s,t);loc={'r':r,'s':s,'t':t}
 names=input_names or ['cubic_order2_22_secant_main_functionals_input.json'];funcs=[]
 for name in names:
  entry=json.loads(Path(__file__).with_name(name).read_text())
  funcs.extend([{int(i):P.from_sympy(S.sympify(v,locals=loc)) for i,v in row.items()} for row in entry['functionals'].values()])
 words=list(itertools.product(range(4),repeat=4));index={w:i for i,w in enumerate(words)}
 alpha=(r-1)/(r+1);R=relations(S.Matrix([[0,r],[r,0]]),[1-r*r-t*t-alpha*s*s,-t,alpha*s,s,t,1])
 RR=[{w:P.from_sympy(S.cancel(c*(r-1)*(r+1)**2)) for w,c in row.items()} for row in R]
 for lam in funcs:
  for rel in RR:
   for pos in range(3):
    for extra in itertools.product(range(4),repeat=2):
     value=sum((c*lam.get(index[extra[:pos]+w+extra[pos:]],P.zero) for w,c in rel.items()),P.zero)
     assert not value
 E=[w for w in itertools.product(range(4),repeat=3) if sum(v>=2 for v in w)%2==0];data={}
 for a,lam in enumerate(funcs):
  for g in range(4):
   row={j:lam.get(index[w+(g,)],P.zero)+(-1 if g<2 else 1)*lam.get(index[(g,)+w],P.zero) for j,w in enumerate(E)};row={j:c for j,c in row.items() if c}
   if row:data[4*a+g]=row
 return DomainMatrix(data,(4*len(funcs),32),P)
def specialize(matrix,rvalue,tvalue,field):
 s=SIGMA;P=field.poly_ring(s);rr=field.from_sympy(rvalue);tt=field.from_sympy(tvalue);data={};strips={}
 for i,row in matrix.to_dod().items():
  out={}
  for j,v in row.items():
   coeff={}
   for (a,b,c),q in v.items():coeff[(b,)]=coeff.get((b,),field.zero)+field.convert(q,S.QQ)*rr**a*tt**c
   pp=P.ring.from_dict({m:c for m,c in coeff.items() if c})
   if pp:out[j]=pp
  if out:
   m=min(k[0] for v in out.values() for k in v);strips[i]=m
   if m:out={j:v.exquo(P.ring.gens[0]**m) for j,v in out.items()}
   data[i]=out
 return DomainMatrix(data,matrix.shape,P),strips
