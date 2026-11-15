#!/usr/bin/env python3
"""Generate a primitive polynomial T commutator module for optional Singular.
Usage: python computations/generate_cubic_as4_T_centre_input.py work/prefix
Then Singular -q work/prefix.sing > work/prefix.log
No full-rank or all-parameter conclusion is asserted by generation.
"""
import json,sys,time
from pathlib import Path
import sympy as S
from verify_cubic_pym_generic import words
l=S.symbols('l');K=S.QQ_I.poly_ring(l);t=time.time()
prefix=Path(sys.argv[1]);prefix.parent.mkdir(parents=True,exist_ok=True)
z=json.loads(Path(__file__).with_name('cubic_as4_T_projection_degree4.json').read_text())
D=S.sympify(z['common_denominator_real'],locals={'l':l})+S.I*S.sympify(z['common_denominator_imag'],locals={'l':l})
data={}
for key,factor in [('real',1),('imag',S.I)]:
 for i,j,e in z[key]:
  data[i,j]=data.get((i,j),K.zero)+K.from_sympy(factor*S.sympify(e,locals={'l':l}))
print('PARSED',len(data),time.time()-t,flush=True)
def rat(x):
 x=S.Rational(x);return '(number('+str(x.p)+')/number('+str(x.q)+'))'
def fmt(e):
 parts=[]
 for (n,),c in e.to_dict().items():
  a,b=c.x,c.y;co='('+rat(a)+'+ii*'+rat(b)+')'
  if n:co+='*('+'*'.join(['l']*n)+')'
  parts.append(co)
 return '('+'+'.join(parts)+')'
ix={v:j for j,v in enumerate(words(4))};out=['ring r=(0,ii),(l),(c,dp);','minpoly=ii*ii+1;','option(redSB);short=0;','matrix A[64][140];']
entries={}
for j,v in enumerate(words(3)):
 for g in range(4):
  a,b=ix[v+(g,)],ix[(g,)+v]
  for i in range(35):
   e=data.get((i,a),K.zero)-data.get((i,b),K.zero)
   if e:entries[j,35*g+i]=e
den=K.from_sympy(D);scales={};scaled={}
for c in range(140):
 column={r:e for (r,cc),e in entries.items() if cc==c};h=den
 for e in column.values():
  h=h.gcd(e)
  if h.degree()==0:break
 if not column:h=K.one
 scales[c]=str(K.to_sympy(h))
 for r,e in column.items():scaled[r,c]=e.exquo(h)
import json
prefix.with_suffix('.scales.json').write_text(json.dumps(scales))
print('PRIMITIVE',max(e.degree() for e in scaled.values()),time.time()-t,flush=True)
for (j,c),e in scaled.items():out.append(f'A[{j+1},{c+1}]={fmt(e)};')
out+=['module U=A;matrix X;print("BEGIN_CENTRE");module N=liftstd(U,X);matrix B=N;','print("NCOLS="+string(ncols(B)));','if(A*X!=B){print("FAIL_LIFT");quit;}',
'int i,j,p;vector v;','for(j=1;j<=ncols(B);j++){v=lead(N[j]);p=0;for(i=1;i<=64;i++){if(v[i]!=0){p=i;break;}}print("PIV:"+string(j-1)+":"+string(p-1));}',
'for(j=1;j<=ncols(B);j++){for(i=1;i<=64;i++){if(B[i,j]!=0){print("N:"+string(i-1)+":"+string(j-1)+":"+string(B[i,j]));}}}',
'for(j=1;j<=ncols(X);j++){for(i=1;i<=140;i++){if(X[i,j]!=0){print("X:"+string(i-1)+":"+string(j-1)+":"+string(X[i,j]));}}}',
'print("DONE");quit;']
p=prefix.with_suffix('.sing');p.write_text('\n'.join(out)+'\n');print('DONE_GENERATION',p.stat().st_size,time.time()-t,flush=True)
