"""Semisimple (2,2), mixed-rank-two pencil reduction: exact tensor identities."""
import itertools,json
from pathlib import Path
import sympy as S
sign=[1,1,-1,-1];seen=set();counts={0:0,2:0,4:0}
for word in itertools.product(range(4),repeat=4):
    if word in seen:continue
    orbit={};w=word;c=1;valid=True
    while w not in orbit:
        orbit[w]=c;c*=-sign[w[0]];w=w[1:]+w[:1]
    valid=(c==orbit[w]);seen.update(orbit)
    if valid:counts[sum(i>=2 for i in word)]+=1
assert counts=={0:4,2:22,4:6}
co=S.symbols('a:6');A=S.zeros(4)
for (i,j),c in zip(itertools.combinations(range(4),2),co):A[i,j]=c;A[j,i]=-c
def transpose_block(A):
    D=S.zeros(4)
    for i,j,k,l in itertools.product(range(2),repeat=4):D[2*j+i,2*l+k]=A[2*i+l,2*k+j]
    return D
def pf(A):return S.expand(A[0,1]*A[2,3]-A[0,2]*A[1,3]+A[0,3]*A[1,2])
assert pf(A)+pf(transpose_block(A))==0
basis=S.eye(4)
charts=[('secant',basis[:,0],basis[:,3],basis[:,1],basis[:,2],-1),
 ('tangent',basis[:,0],basis[:,1]+basis[:,2],basis[:,0],basis[:,1]-basis[:,2],1),
 ('U_ruling',basis[:,0],basis[:,1],basis[:,0],basis[:,2],-1),
 ('V_ruling',basis[:,0],basis[:,2],basis[:,0],basis[:,1],1)]
for name,e0,e1,f0,f1,det in charts:
    AA=e0*e1.T-e1*e0.T
    assert transpose_block(AA)==det*(f0*f1.T-f1*f0.T)
# Pure projected relations give an invertible even off-diagonal block.
p=S.Matrix(2,2,S.symbols('p:4'));q=S.Matrix(2,2,S.symbols('q:4'))
B=S.Matrix(list(p))*S.Matrix(list(q)).T;K=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):K[2*i+k,2*j+l]=-B[2*k+j,2*l+i]
assert S.expand(K.det()+p.det()**2*q.det()**2)==0
out={'status':'PASS','scope':'semisimple Nakayama (+,+,-,-), odd relation dimension2 only',
 'twisted_quartic_dimensions':counts,'pfaffian_partial_transpose':'Pf(D)=-Pf(A)',
 'graph_pencils':[{'type':r[0],'determinant_of_graph':r[-1]} for r in charts],
 'zero_alternating_block':'two pure nondegenerate mixed quadrics; even cross block determinant -(det(p)*det(q))^2',
 'not_claimed':['AS4 existence on necessary charts','normal cubic classification','nonsemisimple (2,2)','mixed dimension4','H3 admissibility']}
Path(__file__).with_name('cubic_order2_22_rank2_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS semisimple (2,2) mixed-rank-two exact pencil and tensor reduction')
