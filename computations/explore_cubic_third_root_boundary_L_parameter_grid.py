#!/usr/bin/env python3
"""Evaluate a modular exploratory matrix model at all prime-field values."""
import argparse,json,numpy as np,time
from pathlib import Path
def coefficients(data):
 deg=max((int(deg) for co in data['entries'].values() for deg in co),default=0)
 out=np.zeros((deg+1,*data['shape']),dtype=np.int64)
 for ij,co in data['entries'].items():
  i,j=map(int,ij.split(','))
  for degree,c in co.items():out[int(degree),i,j]=c
 return out
def evaluate(data,a,p):
 out=np.zeros(data.shape[1:],dtype=np.int64)
 for M in reversed(data):out=(a*out+M)%p
 return out
def rankdet(M,p):
 M=M.copy()%p;rank=0;det=1
 for j in range(M.shape[1]):
  hit=np.flatnonzero(M[rank:,j])
  if not len(hit):continue
  k=rank+int(hit[0])
  if k!=rank:M[[k,rank]]=M[[rank,k]];det=-det
  co=int(M[rank,j]);det=det*co%p;M[rank]=M[rank]*pow(co,-1,p)%p
  fac=M[:,j].copy();fac[rank]=0;M=(M-fac[:,None]*M[rank])%p
  rank+=1
  if rank==len(M):break
 return rank,(det%p if rank==len(M)==M.shape[1] else 0)
if __name__=='__main__':
 parser=argparse.ArgumentParser(description='Finite-field observations only, not characteristic-zero coverage')
 parser.add_argument('--model',required=True);parser.add_argument('--output',required=True);args=parser.parse_args()
 D=json.loads(Path(args.model).read_text());p=D['p'];assert p is not None;N=81
 assert N*(p-1)**2<2**63
 G=[coefficients(x) for x in D['generators']];CM=coefficients(D['commutators']);words=[tuple(j for j in w if j) for w in D['basis']]
 rows=[];start=time.monotonic()
 for a in range(p):
  generators=[evaluate(M,a,p) for M in G];cache={():np.eye(N,dtype=np.int64)}
  def op(w):
   if w not in cache:cache[w]=generators[w[-1]]@op(w[:-1])%p
   return cache[w]
  ops=[op(w) for w in words];traces=np.array([int(np.trace(m))%p for m in ops],dtype=np.int64)
  gram=np.column_stack([traces@m%p for m in ops]);assert np.array_equal(gram,gram.T)
  rank,det=rankdet(gram,p);crank,_=rankdet(evaluate(CM,a,p),p);rows.append({'a':a,'center':81-crank,'trace_rank':rank,'trace_det':det})
  if a%10==0 or a==p-1:
   print('checked',a+1,'of',p,'seconds',round(time.monotonic()-start,2),'bad',[r for r in rows if r['center']!=1 or r['trace_rank']!=81],flush=True)
   Path(args.output).write_text(json.dumps({'p':p,'rows':rows,'status':'finite-characteristic observations only; no characteristic-zero coverage claim'},indent=2))
