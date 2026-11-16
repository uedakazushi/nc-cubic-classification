#!/usr/bin/env python3
"""Exact localized cokernel elimination on the exported polynomial coordinates. Run the L builder --method free and coordinate solver first. Pickle input is generated locally by that solver; do not load untrusted pickle files."""
import argparse,pickle,json
from pathlib import Path
from flint import fmpq
from cubic_gaussian_rational_function import CTX,MOD
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--prefix',required=True);parser.add_argument('--certificate',required=True);args=parser.parse_args();prefix=Path(args.prefix)
data=pickle.load(open(str(prefix)+'.coordinates.pkl','rb'))
T=[[CTX.from_dict({m:fmpq(c) for m,c in p.items()}) for p in row] for row in data]
assert len(T)==10 and all(len(row)==44 for row in T)
r,i,z=CTX.gens();D=r*r+1-(r*r-1)*z*z;Q=r*r+1-2*(r*r+1)*z+(r*r-1)*z*z;H=Q+4*z;F=(r*r-1)*z-(r*r+1);A=Q*Q-2*D*D
units=[r,r-1,r+1,r*r+1,D,z,z-1,F,A,Q,H]
names=['r','r-1','r+1','r^2+1','D','z','z-1','F','A','Q','H']
def red(p):return divmod(p,MOD)[1]
def strip(values):
 vals=sorted([v for v in values if v],key=len)
 if not vals:return CTX.constant(1)
 d=CTX.constant(1)
 for f in units:
  h=vals[0].gcd(f)
  while h.total_degree()>0:
   quot=[divmod(v,h) for v in vals]
   if any(rem for _,rem in quot):break
   vals=[q for q,_ in quot];d*=h;h=vals[0].gcd(f)
 return d

def normalize(T):
 for j in range(len(T[0])):
  d=strip([row[j] for row in T])
  if d!=1:
   for row in T:
    row[j],rem=divmod(row[j],d);assert not rem
 for a,row in enumerate(T):
  d=strip(row);new=[]
  for v in row:
   q,rem=divmod(v,d);assert not rem;new.append(q)
  first=next((v for v in new if v),None)
  if first is not None:new=[v/first.leading_coefficient() for v in new]
  T[a]=new

def unit_witness(v):
 bar=CTX.from_dict({m:(-c if m[1]%2 else c) for m,c in v.to_dict().items()});norm=red(v*bar);assert norm
 g=norm;factors=[]
 for name,f in zip(names,units):
  h=g.gcd(f)
  while h.total_degree()>0:
   factors.append(str(h));g=g//h;h=g.gcd(f)
 if not g.is_constant():return None
 product=g
 for factor in factors:
  from flint import fmpq_mpoly
  product*=fmpq_mpoly(factor,CTX)
 assert product==norm
 return {'norm_factors':factors,'norm_constant':str(g)}
normalize(T);steps=[]
while T:
 choices=sorted((len(v),a,b) for a,row in enumerate(T) for b,v in enumerate(row) if v)
 found=None
 for _,a,b in choices:
  witness=unit_witness(T[a][b])
  if witness is not None:found=(a,b,witness);break
 assert found is not None,'localized unit elimination stalled; no classification claim'
 a,b,witness=found;v=T[a][b]
 steps.append({'rows_before':len(T),'columns_before':len(T[0]),'pivot_row':a,'pivot_column':b,'pivot':str(v),**witness})
 # Scaling by v and clearing its column are invertible after U localization.
 T=[[red(v*x-row[b]*y) for j,(x,y) in enumerate(zip(row,T[a])) if j!=b] for h,row in enumerate(T) if h!=a]
 if T:normalize(T)
 print('unit elimination',len(steps),'remaining rows',len(T),flush=True)
assert len(steps)==10
out={'status':'PASS','coefficient_ring':'QQ(i)[r,z], i^2=-1','localization':'U=r*(r^2-1)*(r^2+1)*D*z*(z-1)*F*A*Q*H','input_shape':[10,44],'serialized_polynomial_variables':{'r':'rho','s':'i, i^2=-1','t':'z'},'all_ten_pivots_are_localized_units':True,'unit_pivots':steps,'remaining_rows':0,'conclusion':'localized normal module equals full polynomial kernel','separate_required_checks':['free rank10 kernel from original cubic relation matrix','full polynomial coordinate identity E*T=N','all original quartic annihilator identities','rational chart covers the entire remaining L open','AS4 cubic-rank base-change recognition'],'not_claimed':['complete global H3 classification','all Nakayama spectra covered']}
Path(args.certificate).write_text(json.dumps(out,indent=2)+'\n');print('LOCALIZED NORMAL MODULE EQUALITY PASS',flush=True)
