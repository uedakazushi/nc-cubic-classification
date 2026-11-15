#!/usr/bin/env python3
"""Exact central quadratic space and cubic-scroll relations in a non-CY H3 witness."""
import sympy as sy,json
from sympy.polys.matrices import DomainMatrix
from itertools import product,combinations_with_replacement
from pathlib import Path
qrels=[]
for i in [1,2,3]:qrels.append({(0,i):sy.Integer(1),(i,0):sy.Integer(1)})
qrels +=[{(2,3):1,(3,1):1,(1,2):-1,(0,0):-1},{(3,2):1,(1,3):1,(2,1):-1,(0,0):-1},{(1,1):1,(2,2):1,(3,3):-1,(0,0):-1}]
G={(1,1,3):1,(1,3,2):-1,(2,3,1):1,(2,2,3):-1,(3,2,2):1,(3,1,1):-1}
def add(f,g,c=1):
 out=dict(f)
 for w,a in g.items():out[w]=sy.expand(out.get(w,0)+c*a)
 return {w:a for w,a in out.items() if a!=0}
def mul(f,g):
 out={}
 for u,a in f.items():
  for v,b in g.items():out[u+v]=sy.expand(out.get(u+v,0)+a*b)
 return {w:a for w,a in out.items() if a!=0}
def scale(f,c):return {w:a*c for w,a in f.items()}
def quotient(n,cut=True):
 ws=list(product(range(4),repeat=n));ix={w:i for i,w in enumerate(ws)};rows=[]
 for degree,rs in ([(2,qrels),(3,[G])] if cut else [(2,qrels)]):
  for dl in range(n-degree+1):
   for left in product(range(4),repeat=dl):
    for right in product(range(4),repeat=n-degree-dl):
     for r in rs:rows.append({ix[left+w+right]:a for w,a in r.items()})
 M=sy.MutableSparseMatrix(len(rows),len(ws),{(i,j):a for i,row in enumerate(rows) for j,a in row.items()});rr,piv=DomainMatrix.from_Matrix(M).convert_to(sy.QQ).rref();rr=rr.to_Matrix();free=[j for j in range(len(ws)) if j not in piv]
 P=sy.zeros(len(free),len(ws))
 for i,j in enumerate(free):P[i,j]=1
 for i,j in enumerate(piv):
  for k,l in enumerate(free):P[k,j]=-rr[i,l]
 def reduce(f):return P*sy.Matrix([f.get(w,0) for w in ws])
 return free,ws,reduce
free2,w2,red2=quotient(2);free3,w3,red3=quotient(3);free4,w4,red4=quotient(4)
u={(1,):sy.Integer(1),(2,):sy.Integer(1)};v={(1,):sy.Integer(1),(2,):sy.Integer(-1)};w=add({(3,):sy.Integer(1)},scale(u,sy.Rational(1,2)))
_,_,red3B=quotient(3,False)
identity=add(scale(G,sy.Rational(2,3)),add(mul(mul(v,w),u),mul(u,mul(v,w)),-1))
assert red3B(identity)==sy.zeros(20,1)
B=mul(v,v);C=mul(w,w);D=scale(add(mul(u,w),mul(w,u)),sy.Rational(1,2));a=mul(v,w);ss=add(mul(u,v),mul(v,u));cent=[B,C,D,a,ss]
for f in cent:
 for i in range(4):assert red3(add(mul(f,{(i,):1}),mul({(i,):1},f),-1))==sy.zeros(19,1)
comm=sy.Matrix.hstack(*[sy.Matrix.vstack(*[red3(add(mul({word:1},{(i,):1}),mul({(i,):1},{word:1}),-1)) for i in range(4)]) for word in [w2[j] for j in free2]])
assert len(free2)-comm.rank()==5
assert sy.Matrix.hstack(*[red2(f) for f in cent]).rank()==5
pairs=list(combinations_with_replacement(range(5),2));sym=sy.Matrix.hstack(*[red4(mul(cent[i],cent[j])) for i,j in pairs]);assert sym.rank()==12
relations=[add(mul(B,C),mul(a,a),-1),add(mul(C,ss),scale(mul(D,a),2),-1),add(mul(a,ss),scale(mul(D,B),2),-1)]
for f in relations:assert red4(f)==sy.zeros(31,1)
# Exact conversion of central coordinates, all coefficients.
h,b,c,A,BB,CC,DD,TT=sy.symbols('h b c A B C D T');al=(1+h**3)/(2*h);be=(2-h**3)/(4*h);ka=h*b-c/h
Dconverted=sy.cancel(3*h*(CC-be*BB-ka*TT)/(4*al)-h*BB/4+b*TT)
D0=sy.factor(sy.diff(Dconverted,TT));assert sy.cancel(D0+((h**3-2)*b-3*h*c)/(2*(1+h**3)))==0
s=sy.symbols('s');HR=(1-s**3)/(1-s)**4;HC=(1+2*s*s)/(1-s*s)**3;assert sy.limit(HR/HC,s,1)==8
assert sy.limit((1+7*s+4*s*s)/(1+2*s),s,1)==4
cert={'version':'classification-v40','example':'h=b=c=1','volume_commutator_identity':'Gstar=-[vw,u]/4','central_quadrics_dimension':5,'quadrics':['B=v^2','C=w^2','D=(uw+wu)/2','a=vw','s=uv+vu'],'u_v_w':['x+y','x-y','z+h*(x+y)/2'],'degree4_symmetric_products_rank':12,'all_three_scroll_minors_zero':True,'scroll_matrix':'[[C,a,2D],[a,B,s]]','conversion_T_coefficient_in_D':str(D0),'Hilbert_generic_rank_R_over_scroll':8,'Hilbert_generic_rank_even_over_scroll':4,'scope':'Exact witness central-space and relation ranks; all-parameter centre exhaustion, normal scroll and quaternion claims are ordinary proofs.'}
Path(__file__).with_name('cubic_normal_order2_scroll_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS five central quadrics, three scroll minors, product rank12, generic rank8/even rank4')
