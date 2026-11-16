"""Solve the exported free kernel against the normal rows and verify every polynomial coordinate identity. This does not certify saturation. Requires python-flint. Run after the builder --method free; --prefix is the builder output path."""
import pickle,time
from pathlib import Path
from flint import fmpq_mpoly,fmpq
from cubic_gaussian_rational_function import F,CTX,MOD
import argparse
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--prefix',required=True);args=parser.parse_args()
base=Path(args.prefix).resolve().parent;prefix=Path(args.prefix).resolve()
ep=Path(str(prefix)+'.E.txt').read_text().splitlines();np=Path(str(prefix)+'.Nall.txt').read_text().splitlines();assert len(ep)==320 and len(np)==1408
parse=lambda x:fmpq_mpoly(x.replace('i','s').replace('k','t'),CTX)
EE=[[parse(ep[10*i+j]) for j in range(10)] for i in range(32)];NN=[[parse(np[44*i+j]) for j in range(44)] for i in range(32)];print('parsed',flush=True)
def at(p):
 a=p(3,0,fmpq(1,2));b=p(3,1,fmpq(1,2))-a;return F(CTX.constant(a)+b*CTX.gens()[1])
rankrows={};selected=[]
for i in sorted(range(32),key=lambda i:sum(len(x) for x in EE[i])):
 row={j:at(p) for j,p in enumerate(EE[i]) if p};row={j:v for j,v in row.items() if v}
 while row:
  k=min(row)
  if k not in rankrows:
   a=row[k];rankrows[k]={j:v/a for j,v in row.items()};selected.append(i);break
  a=row[k]
  for j,v in rankrows[k].items():
   vv=row.get(j,F())-a*v
   if vv:row[j]=vv
   else:row.pop(j,None)
 if len(selected)==10:break
assert len(selected)==10;print('selected',selected,flush=True)
A=[[F(x) for x in EE[i]]+[F(x) for x in NN[i]] for i in selected];perm=list(range(10))
def serial(v):return ({m:str(c) for m,c in v.n.to_dict().items()},{m:str(c) for m,c in v.d.to_dict().items()})
for k in range(10):
 choices=[(len(A[i][j].n)+len(A[i][j].d),i,j) for i in range(k,10) for j in range(k,10) if A[i][j]];_,i,j=min(choices)
 if i!=k:A[k],A[i]=A[i],A[k]
 if j!=k:
  for row in A:row[k],row[j]=row[j],row[k]
  perm[k],perm[j]=perm[j],perm[k]
 a=A[k][k];A[k]=[v/a for v in A[k]]
 for i in range(10):
  if i==k or not A[i][k]:continue
  a=A[i][k];A[i]=[v-a*w for v,w in zip(A[i],A[k])]
 print('coordinate pivot',k,flush=True);pickle.dump({'pivot':k,'perm':perm,'A':[[serial(v) for v in row] for row in A]},open(Path(str(prefix)+'.coordinate-checkpoint.pkl'),'wb'))
T=[None]*10
for k in range(10):T[perm[k]]=A[k][10:]
assert all(v.d.is_constant() for row in T for v in row);print('all coordinates polynomial',flush=True)
TP=[[v.n/v.d.leading_coefficient() for v in row] for row in T]
pickle.dump([[{m:str(c) for m,c in v.to_dict().items()} for v in row] for row in TP],open(Path(str(prefix)+'.coordinates.pkl'),'wb'))
for i in range(32):
 for j in range(44):
  val=CTX.constant(0)
  for k in range(10):val+=EE[i][k]*TP[k][j]
  assert not divmod(val-NN[i][j],MOD)[1]
print('FULL POLYNOMIAL COORDINATE IDENTITY PASS',flush=True)
text=lambda p:str(p).replace('s','i').replace('t','k')
source='matrix Tnative[10][44]=\n'+',\n'.join(text(v) for row in TP for v in row)+';\n'
source+='matrix Check=E*Tnative-Nall;\nprint("COORDINATE CHECK");print(size(ideal(Check)));\nmodule NT=Tnative;\nmodule GT=std(NT);\nprint("NATIVE COORDINATE STANDARD BASIS DONE");\nmodule FF=freemodule(10);\nideal Ann=quotient(GT,FF);\nideal JJ=std(Ann);\nprint("NATIVE ANN DONE");print(dim(JJ));\nint step=0;ideal Next;\nwhile(reduce(1,JJ)!=0){Next=std(quotient(JJ,ideal(U)));step=step+1;if(size(reduce(Next,JJ))==0){break;}JJ=Next;}\nif(reduce(1,JJ)==0){print("NATIVE L SATURATION PASS");}else{print(JJ);}\nquit;\n';(Path(str(prefix)+'.coordinates.sing')).write_text(source)
