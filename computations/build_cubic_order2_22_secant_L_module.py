"""Build the exact nonmirror-L normal-module experiment; no classification is asserted until the emitted checks pass. Requires python-flint and SymPy."""
import argparse,itertools,sympy as S
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',required=True);parser.add_argument('--method',choices=['direct','presentation'],default='direct');args=parser.parse_args()
from cubic_order2_22_secant_functionals import normal_matrix,RHO,SIGMA,TAU
from cubic_order2_22_secant_tools import relations
from flint import fmpq,fmpq_mpoly_ctx
r,s,t=RHO,SIGMA,TAU;N=normal_matrix(['cubic_order2_22_secant_main_functionals_input.json','cubic_order2_22_secant_additional_functionals_input.json']);P=N.domain;ctx=fmpq_mpoly_ctx.get(('r','s','t'));R,I,Z=ctx.gens();D=R*R+1-(R*R-1)*Z*Z;Q=R*R+1-2*(R*R+1)*Z+(R*R-1)*Z*Z;H=Q+4*Z;F=(R*R-1)*Z-(R*R+1);A=Q*Q-2*D*D;Sn=(R+1)*(R*R+1)*H;Tn=(R*R-1)*Q;unitfactors=[I,R,R-1,R+1,R*R+1,D,Z,Z-1,F,A,Q,H]
alpha=(r-1)/(r+1);rels=relations(S.Matrix([[0,r],[r,0]]),[1-r*r-t*t-alpha*s*s,-t,alpha*s,s,t,1]);words=[w for w in itertools.product(range(4),repeat=3) if sum(i>=2 for i in w)%2==0];index={w:i for i,w in enumerate(words)};rows=[]
for rel in rels:
 for pos in range(2):
  for g in range(4):
   row={}
   for w,c in rel.items():
    word=(g,)+w if pos==0 else w+(g,)
    if word in index:row[index[word]]=P.from_sympy(S.cancel(c*(r-1)*(r+1)**2))
   if row:rows.append(row)
assert len(rows)==24
powercache={};basecache={}
def powc(name,poly,n):
 key=(name,n)
 if key not in powercache:powercache[key]=poly**n
 return powercache[key]
def transform(inputrows):
 out=[];seen=set()
 for count,row in enumerate(inputrows):
  maxD=max(b+c for v in row.values() for a,b,c in v);maxR=max(b for v in row.values() for a,b,c in v);data={}
  for j,v in row.items():
   val=ctx.constant(0)
   for (a,b,c),q in v.items():
    key=(maxD,b,c)
    if key not in basecache:
     phase=[ctx.constant(1),I,ctx.constant(-1),-I][b%4];basecache[key]=powc('Sn',Sn,b)*powc('Tn',Tn,c)*powc('2D',2*D,maxD-b-c)*phase
    val+=fmpq(str(q))*powc('R',R,a+maxR-b)*basecache[key]
   if val:data[j]=val
  if not data:continue
  common=ctx.constant(0)
  for v in data.values():common=common.gcd(v)
  for f in unitfactors:
   h=common.gcd(f)
   while h.total_degree()>0:
    data={j:v//h for j,v in data.items()};common=common//h;h=common.gcd(f)
  lc=data[min(data)].leading_coefficient();data={j:v/lc for j,v in data.items()};key=tuple((j,str(v)) for j,v in sorted(data.items()))
  if key not in seen:seen.add(key);out.append(data)
  if count%10==0:print('transformed',count,len(out),flush=True)
 return out
R3=transform(rows);NN=transform(list(N.to_dod().values()));print('matrices',len(R3),len(NN),flush=True)
def textpoly(p):
 assert all(m[1]<=1 for m in p.to_dict());return str(p).replace('s','i').replace('t','k')
def matrix(name,n,m,data):return f'matrix {name}[{n}][{m}]=\n'+',\n'.join(textpoly(data.get(a,{}).get(b,ctx.constant(0))) for a in range(n) for b in range(m))+';\n'
source='ring R=(0,i),(r,k),dp;\nminpoly=i^2+1;\npoly dd='+textpoly(D)+';\npoly qq='+textpoly(Q)+';\npoly hh=qq+4*k;\npoly ff=(r^2-1)*k-(r^2+1);\npoly aa=qq^2-2*dd^2;\npoly U=r*(r^2-1)*(r^2+1)*dd*k*(k-1)*ff*aa*qq*hh;\n'
source+=matrix('R3',len(R3),32,{j:row for j,row in enumerate(R3)})
source+=matrix('Nall',32,len(NN),{j:{a:row[j] for a,row in enumerate(NN) if j in row} for j in range(32)})
source+='matrix CK=R3*Nall;\nif(size(ideal(CK))!=0){print("FAILED NORMAL ROW CONTAINMENT");quit;}\nprint("NORMAL ROW CONTAINMENT PASS");\nmodule E=syz(R3);\nprint("POLYNOMIAL KERNEL DONE");\nprint(size(E));\n'
if args.method=='direct':
 source+='module NN=Nall;\nmodule GN=std(NN);\nprint("NORMAL MODULE STANDARD BASIS DONE");\nideal Ann=quotient(GN,E);\nmodule TestBasis=E;\nmodule TestModule=GN;\n'
else:
 source+='module ES=syz(E);\nmatrix T=lift(E,Nall);\nmatrix Check=E*T-Nall;\nif(size(ideal(Check))!=0){print("FAILED COORDINATE LIFT");quit;}\nmodule Pres=ES,T;\nmodule GP=std(Pres);\nmodule FF=freemodule(ncols(E));\nideal Ann=quotient(GP,FF);\nmodule TestBasis=FF;\nmodule TestModule=GP;\n'
source+='ideal JJ=std(Ann);\nprint("ANNIHILATOR DONE");\nprint(dim(JJ));\nint step=0;\nideal Next;\nwhile(reduce(1,JJ)!=0)\n{\n Next=std(quotient(JJ,ideal(U)));\n step=step+1;\n print("SATURATION STEP "+string(step));\n if(size(reduce(Next,JJ))==0){break;}\n JJ=Next;\n}\nif(reduce(1,JJ)==0)\n{\n module Test=U^step*TestBasis;\n module Remainder=reduce(Test,TestModule);\n if(size(Remainder)!=0){print("FAILED FINAL MEMBERSHIP");quit;}\n print("LOCALIZED NORMAL MODULE EQUALITY VERIFIED");\n}\nelse{print("UNRESOLVED SUPPORT");print(JJ);}\nquit;\n'
Path(args.output).write_text(source);print('source saved',len(source),'method',args.method,flush=True)
