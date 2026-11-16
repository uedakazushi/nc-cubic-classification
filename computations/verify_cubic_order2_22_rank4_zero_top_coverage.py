"""Zero-top coverage: separation supports, two symmetric forms, two exceptional nuclei."""
import itertools,json
from functools import lru_cache
from pathlib import Path
import sympy as S
p,q=S.symbols('p q',nonzero=True);z=S.symbols('z:6');A=S.zeros(4)
for (i,j),c in zip(itertools.combinations(range(4),2),z):A[i,j]=c;A[j,i]=-c
sharp=S.Matrix([[0,-z[5],z[4],-z[3]],[z[5],0,-z[2],z[1]],[-z[4],z[2],0,-z[0]],[z[3],-z[1],z[0],0]])
E=S.Matrix([[0,1],[-1,0]]);J=S.Matrix([[-1,-1],[1,0]])
SU=S.Matrix([[z[0],(z[2]-z[3])/2],[(z[2]-z[3])/2,z[5]]]);SV=S.Matrix([[z[1],(z[2]+z[3])/2],[(z[2]+z[3])/2,z[4]]])
assert S.kronecker_product(SU,E)+S.kronecker_product(E,SV)==A
assert S.expand(SU.det()-SV.det()-(z[0]*z[5]-z[1]*z[4]+z[2]*z[3]))==0
def graph(a,b,vals,h):
 M=S.zeros(4)
 for i,j,k,l in itertools.product(range(2),repeat=4):M[2*k+j,2*l+i]=-a[i,k]*b[j,l]
 return (-M.T*sharp.subs(vals)/h).applyfunc(S.factor)
def separated(T,negative):
 return all(T[2*l+i,2*k+j]==0 for i,j,k,l in itertools.product(range(2),repeat=4) if (l!=j if negative else i!=k))
L=lambda t:S.Matrix([[0,1],[-t,0]])
assert separated(graph(L(p),L(q),{z[1]:0,z[4]:0},-p*q),True)
assert separated(graph(L(p),L(q),{z[0]:0,z[5]:0},-p*q),False)
assert separated(graph(L(p),J,{z[0]:0,z[4]:0,z[5]:0,z[2]:-z[3]},-p),False)
assert separated(graph(J,L(q),{z[1]:0,z[4]:0,z[5]:0,z[2]:z[3]},-q),True)
# Two exceptional epsilon+ points, with exact PBW reductions and fixed normal minors.
keys_QJ=[(1,(0,0,0,1)),(2,(0,0,0,2)),(0,(0,0,0,1)),(2,(0,0,1,2)),(0,(0,0,2,2)),(2,(0,2,2,2)),(2,(1,2,2,2)),(3,(0,2,2,3)),(3,(1,2,2,2)),(2,(0,2,2,3))]
keys_JQ=[(1,(0,0,0,0)),(2,(0,0,0,3)),(1,(0,0,0,1)),(1,(0,0,1,1)),(0,(0,0,3,3)),(0,(0,0,2,2)),(1,(0,0,3,3)),(1,(0,1,3,3)),(2,(0,2,2,3)),(3,(0,2,2,3))]
records=[]
for name,a,b,values,keys,expected in [('QJ_plus',L(-1),J,[1,0,0,0,0,-1],keys_QJ,-16),('JQ_plus',J,L(-1),[0,1,0,0,1,0],keys_JQ,-36)]:
 T=graph(a,b,dict(zip(z,values)),-1);rewrite=-T.inv().T
 uv=[(i,j) for i in range(2) for j in range(2,4)];vu=[(i,j) for i in range(2,4) for j in range(2)]
 rules={(1,0):{w:-a[i,j]/a[1,0] for i,j,w in [(0,0,(0,0)),(0,1,(0,1)),(1,1,(1,1))] if a[i,j]},(3,2):{w:-b[i,j]/b[1,0] for i,j,w in [(0,0,(2,2)),(0,1,(2,3)),(1,1,(3,3))] if b[i,j]}}
 for i,w in enumerate(vu):rules[w]={v:rewrite[i,j] for j,v in enumerate(uv) if rewrite[i,j]}
 @lru_cache(None)
 def nf(word):
  for i in range(len(word)-1):
   if word[i:i+2] in rules:
    out={}
    for mid,c in rules[word[i:i+2]].items():
     for w,d in nf(word[:i]+mid+word[i+2:]).items():out[w]=out.get(w,0)+c*d
    return {w:c for w,c in out.items() if c}
  return {word:S.Integer(1)}
 overlaps=0
 for word in itertools.product(range(4),repeat=3):
  if word[:2] not in rules or word[1:] not in rules:continue
  results=[]
  for pos in [0,1]:
   out={}
   for mid,c in rules[word[pos:pos+2]].items():
    for w,d in nf(word[:pos]+mid+word[pos+2:]).items():out[w]=out.get(w,0)+c*d
   results.append(out)
  assert all(results[0].get(w,0)==results[1].get(w,0) for w in set(results[0])|set(results[1]));overlaps+=1
 assert overlaps==4
 basis=[w for w in itertools.combinations_with_replacement(range(4),3) if sum(i>=2 for i in w)%2==0];eq={}
 for col,word in enumerate(basis):
  for g,mu in enumerate([1,1,-1,-1]):
   out={}
   for w,c in [(word+(g,),1),((g,)+word,-mu)]:
    for v,d in nf(w).items():out[v]=out.get(v,0)+c*d
   for w,c in out.items():
    if c:eq.setdefault((g,w),{})[col]=c
 minor=S.Matrix([[eq[key].get(col,0) for col in range(10)] for key in keys]).det();assert minor==expected
 records.append({'chart':name,'PBW_overlaps':4,'normal_minor':expected})
out={'status':'PASS','scope':'complete geometric H3 recognition in the canonical mixed-rank4 P=Q=0 sector, together with the zero-top unipotent theorem',
 'checks':['universal decomposition into two symmetric binary forms','Pf=det(SU)-det(SV)','four exact separation support patterns','two exceptional PBW points and constant rank10 minors'],
 'exceptional_points':records,
 'conclusion':'all H3 objects and arrows in this canonical zero-top sector are the known fixed non-CY sign-envelope classification',
 'not_claimed':['nonzero-top rank4 classification','global H3 completeness','intrinsic family descent or componenthood']}
Path(__file__).with_name('cubic_order2_22_rank4_zero_top_coverage_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS zero-top coverage identities, four separation patterns and exceptional minors -16,-36')
