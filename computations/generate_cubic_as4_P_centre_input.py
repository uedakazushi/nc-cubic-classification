#!/usr/bin/env python3
"""Generate the realified primitive P central-cubic module for Singular.
Usage: python computations/generate_cubic_as4_P_centre_input.py work/prefix
Optional final argument -1,0,1 specializes lambda=-1/2+i*index.
Then Singular -q work/prefix.sing > work/prefix.log
Generation alone is not an all-parameter rank assertion.
"""
import sys,json,time,sympy as S
from pathlib import Path
from verify_cubic_pym_generic import words
l,r=S.symbols('l r');G=S.QQ_I.poly_ring(l,r);t=time.time()
prefix=Path(sys.argv[1]);prefix.parent.mkdir(parents=True,exist_ok=True)
root=Path(__file__).parent
free3=json.loads((root/'cubic_as4_P_projection_degree3.json').read_text())['free_columns_zero_based']
z=json.loads((root/'cubic_as4_P_projection_degree4.json').read_text());D=S.sympify(z['common_real_denominator'],locals={'l':l,'r':r});data={}
for key,factor in [('real',S.QQ_I.one),('imag',S.QQ_I(0,1))]:
 for i,j,terms in z[key]:
  poly=G.ring.from_dict({(a,b):S.QQ_I.from_sympy(S.Rational(c))*factor for a,b,c in terms})
  data[i,j]=data.get((i,j),G.zero)+poly
print('PARSED',len(data),time.time()-t,flush=True)
ix={v:j for j,v in enumerate(words(4))};entries={}
for j,k in enumerate(free3):
 v=words(3)[k]
 for g in range(4):
  a,b=ix[v+(g,)],ix[(g,)+v]
  for i in range(35):
   e=data.get((i,a),G.zero)-data.get((i,b),G.zero)
   if e:entries[j,35*g+i]=e
DG=G.from_sympy(D);factors=[G.from_sympy(f) for f in [l,l+1,r-1,l+(1+S.I)/2,l+(1-S.I)/2]];scales={};scaled={}
for c in range(140):
 column={j:e for (j,cc),e in entries.items() if cc==c};h=G.one
 if column:
  for f in factors:
   while not divmod(DG,h*f)[1]:
    quot={};bad=False
    for j,e in column.items():
     q,rem=divmod(e,f)
     if rem:bad=True;break
     quot[j]=q
    if bad:break
    column=quot;h*=f
 scales[c]=str(G.to_sympy(h))
 for j,e in column.items():scaled[j,c]=e
print('PRIMITIVE',time.time()-t,flush=True)
# Optional special index gives lambda=-1/2+i*index before realification.
special=int(sys.argv[2]) if len(sys.argv)>2 else None
if special is not None:
 assert special in [-1,0,1]
 value=S.QQ_I(-S.Rational(1,2),special)
 numeric={}
 for ij,e in scaled.items():
  coeff={}
  for (a,b),c in e.to_dict().items():coeff[0,b]=coeff.get((0,b),S.QQ_I.zero)+c*value**a
  numeric[ij]=G.ring.from_dict(coeff)
 scaled=numeric
cache={}
def rat(x):
 x=S.Rational(x);return '(number('+str(x.p)+')/number('+str(x.q)+'))'
def fmt(e,imag=False):
 key=(str(e),imag)
 if key not in cache:
  ss=[]
  for (a,b),co in e.to_dict().items():
   c=co.y if imag else co.x
   if not c:continue
   s=rat(c)
   if a:s+='*('+'*'.join(['l']*a)+')'
   if b:s+='*('+'*'.join(['r']*b)+')'
   ss.append(s)
  cache[key]='('+'+'.join(ss)+')' if ss else '0'
 return cache[key]
out=[('ring base=(0,l),(r),(c,dp);' if special is None else 'ring base=0,(r),(c,dp);'),'option(redSB);short=0;','matrix A[40][280];']
for (j,c),e in scaled.items():
 ar,ai=fmt(e),fmt(e,True)
 if ar!='0':out.append(f'A[{2*j+1},{2*c+1}]={ar};');out.append(f'A[{2*j+2},{2*c+2}]={ar};')
 if ai!='0':out.append(f'A[{2*j+2},{2*c+1}]={ai};');out.append(f'A[{2*j+1},{2*c+2}]=-({ai});')
out+=['module U=A;matrix X;print("BEGIN_P_CENTRE");module N=liftstd(U,X);matrix B=N;','print("NCOLS="+string(ncols(B)));','if(A*X!=B){print("FAIL_LIFT");quit;}',
'int i,j,p;vector v;','for(j=1;j<=ncols(B);j++){v=lead(N[j]);p=0;for(i=1;i<=40;i++){if(v[i]!=0){p=i;break;}}print("PIV:"+string(j-1)+":"+string(p-1));}',
'for(j=1;j<=ncols(B);j++){for(i=1;i<=40;i++){if(B[i,j]!=0){print("N:"+string(i-1)+":"+string(j-1)+":"+string(B[i,j]));}}}',
'for(j=1;j<=ncols(X);j++){for(i=1;i<=280;i++){if(X[i,j]!=0){print("X:"+string(i-1)+":"+string(j-1)+":"+string(X[i,j]));}}}',
'print("DONE");quit;']
prefix.with_suffix('.scales.json').write_text(json.dumps(scales))
p=prefix.with_suffix('.sing');p.write_text('\n'.join(out)+'\n');print('INPUT_DONE',p.stat().st_size,time.time()-t,flush=True)
