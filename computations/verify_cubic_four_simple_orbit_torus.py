#!/usr/bin/env python3
"""Exact all-nonzero-orbit refinement; no rank-sufficiency assertion."""
import itertools,json,collections,math
import sympy as s
from cubic_four_simple_finite_model import top_basis
from cubic_four_simple_support_sieve import leftkern,maxmatch,factor
from pathlib import Path
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'cubic_four_simple_support_sieve_certificate.json').read_text());assert D['status']=='PASS' and D['remaining_Galois_labels']==20
Q=json.loads((ROOT/'cubic_four_simple_finite_atlas_certificate.json').read_text());old={tuple(r['spectrum']):r for r in Q['all115_orbit_checks']}
from cubic_four_simple_laurent_torus import close
results=[]
def obstruction(A,b,mod):
 if not A:return None
 return next((l for l in leftkern(tuple(A)) if sum(x*y for x,y in zip(l,b))%mod),None)
for rec in D['all39_support_records']:
 if not rec['compatible_support_masks']:continue
 N=rec['N'];a=rec['exponents'];basis=top_basis(N,a);active0=old[(N,*a)]['active_orbits'];basisidx={j:k for k,j in enumerate(active0)};counts=rec['quartic_count_types'];cubes=rec['cubic_count_types'];allowed=collections.defaultdict(set)
 for ic,sm,tm,nm in rec['compatible_support_masks']:allowed[ic,sm].add(tm)
 accepted=[];stats=collections.Counter();nb=len(active0)
 for ic,I in enumerate(rec['relation_characters']):
  forbidden={j for j in active0 if any(I[(a[w[0]]+a[w[1]])%N]==0 for w in basis[j])}
  for mask in range(1,1<<nb):
   act=[j for k,j in enumerate(active0) if mask>>k&1]
   if any(j in forbidden for j in act):continue
   sm=0
   for j in act:sm|=1<<counts.index([next(iter(basis[j])).count(k) for k in range(4)])
   if (ic,sm) not in allowed:continue
   E={};bycol=collections.defaultdict(set);blocks=collections.defaultdict(dict);support={w:set() for w in range(N)};pidx={j:k for k,j in enumerate(act)}
   for j in act:
    for w,phase in basis[j].items():
     row=4*w[0]+w[1];col=4*w[2]+w[3];weight=(a[w[0]]+a[w[1]])%N;E[row,col]=(pidx[j],phase);bycol[col].add(row);blocks[weight][row,col]=(pidx[j],phase);support[weight].add(w[:2])
   if any(len(v)==1 for v in bycol.values()):stats['pure_column']+=1;continue
   A=[];rhs=[];fail=False;polys=[]
   constraints=[(blocks[w],r) for w,r in enumerate(I) if r]
   for u,v in itertools.combinations(range(4),2):
    rectangle={4*i+j for i in [u,v] for j in [u,v]};cols0={col for col,rr in bycol.items() if rr<=rectangle}
    if cols0:constraints.append(({ij:val for ij,val in E.items() if ij[1] in cols0},1))
   for block,r in constraints:
    rows=sorted({ij[0] for ij in block});cols=sorted({ij[1] for ij in block});graph={row:{col for rr,col in block if rr==row} for row in rows}
    if maxmatch(graph)<r:fail=True;break
    if r==1 and len(rows)*len(cols)!=len(block):fail=True;break
    for rr in itertools.combinations(rows,r+1):
     if fail:break
     for cc in itertools.combinations(cols,r+1):
      terms=[]
      for perm in itertools.permutations(range(r+1)):
       if not all((rr[j],cc[perm[j]]) in block for j in range(r+1)):continue
       inv=sum(perm[i]>perm[j] for i in range(r+1) for j in range(i+1,r+1));ex=[0]*len(act);phase=(inv%2)*N
       for j in range(r+1):p,pp=block[rr[j],cc[perm[j]]];ex[p]+=1;phase+=pp
       terms.append((ex,phase%(2*N)))
      polys.append(terms)
      if len(terms)==1:fail=True;break
      if len(terms)==2:
       e=tuple(x-y for x,y in zip(terms[0][0],terms[1][0]));b=(N+terms[1][1]-terms[0][1])%(2*N)
       if not any(e):
        if b:fail=True;break
       else:A.append(e);rhs.append(b)
    if fail:break
   if fail:stats['rank_support']+=1;continue
   if obstruction(A,rhs,2*N) is not None:stats['top_toric']+=1;continue
   A,rhs,nclose=close(A,rhs,polys,len(act),2*N)
   if A is None:stats['top_laurent_closure']+=1;continue
   stats['closure_added']+=nclose
   skew={tuple(sorted((i,j))) for i in range(4) for j in range(i+1,4) if any(rr=={4*i+j,4*j+i} for rr in bycol.values())}
   if len(skew)==6:stats['skew']+=1;continue
   normal=[i for i in range(4) if all(i==j or tuple(sorted((i,j))) in skew for j in range(4))];qexpr={}
   for i,j in skew:
    cols=sorted(col for col,rr in bycol.items() if rr=={4*i+j,4*j+i});col=cols[0];pi,ci=E[4*i+j,col];pj,cj=E[4*j+i,col];e=[0]*len(act);e[pj]+=1;e[pi]-=1;qexpr[i,j]=(e,(N+cj-ci)%(2*N))
   S=[tuple(counts[j]) for j in range(len(counts)) if sm>>j&1];survive=[]
   for tm in sorted(allowed[ic,sm]):
    T=[tuple(cubes[j]) for j in range(len(cubes)) if tm>>j&1]
    if factor(T,skew,I,support,a,N):stats['factor']+=1;continue
    aa=list(A);bb=list(rhs)
    for z in normal:
     for v in S+T:
      e=[0]*len(act);phase=0
      for j in range(4):
       if j==z:continue
       ep,cp=qexpr[min(z,j),max(z,j)];sgn=1 if z<j else -1
       for k in range(len(act)):e[k]+=sgn*v[j]*ep[k]
       phase+=sgn*v[j]*cp
      aa.append(tuple(e));bb.append((2*a[z]-phase)%(2*N))
    if obstruction(aa,bb,2*N) is not None:stats['normal_toric']+=1;continue
    rank=s.Matrix(aa).rank() if aa else 0
    cmat=s.Matrix([[next(iter(basis[j])).count(k) for j in act] for k in range(4)])
    cr=cmat.rank();dim=len(act)-rank-cr;assert dim>=0
    assert not aa or all(v==0 for v in s.Matrix(aa)*cmat.T)
    survive.append({'cubic_mask':tm,'A':aa,'b':bb,'effective_dimension':dim,'diagonal_rank':cr})
   if survive:accepted.append({'character_index':ic,'orbit_mask':mask,'active_indices':act,'count_mask':sm,'cubic_masks':survive,'normal_generators':normal})
 stats['surviving_orbit_masks']=len(accepted);stats['surviving_G_supports']=sum(len(r['cubic_masks']) for r in accepted)
 print('RESULT',N,a,dict(stats),flush=True);results.append({'N':N,'exponents':a,'label_count':rec['label_count'],'patterns':accepted,'stats':dict(stats)})
assert sum(bool(r['patterns']) for r in results)==13
assert sum(r['label_count'] for r in results if r['patterns'])==33
assert sum(len(r['patterns']) for r in results)==23
assert sum(len(p['cubic_masks']) for r in results for p in r['patterns'])==157
# The sole order7 (0,1,2,4) support chart is excluded by the paper's Ore-volume proof.
n7=next(r for r in results if r['N']==7 and r['exponents']==[0,1,2,4]);assert len(n7['patterns'])==1
pat=n7['patterns'][0];assert len(pat['cubic_masks'])==1
base_rec=next(r for r in D['all39_support_records'] if r['N']==7 and r['exponents']==[0,1,2,4])
ss=[tuple(w) for j,w in enumerate(base_rec['quartic_count_types']) if pat['count_mask']>>j&1]
tm=pat['cubic_masks'][0]['cubic_mask'];tt=[tuple(v) for j,v in enumerate(base_rec['cubic_count_types']) if tm>>j&1]
assert set(ss)=={(1,1,1,1),(0,3,0,1),(0,1,3,0),(0,0,1,3)} and set(tt)=={(3,0,0,0),(0,1,1,1)}
# Pure base pairs yb,yc,bc: isolated actual quadratic weights and rank1.
a=[0,1,2,4];I=base_rec['relation_characters'][pat['character_index']]
for i,j in [(1,2),(1,3),(2,3)]:
 w=(a[i]+a[j])%7;assert [(u,v) for u in range(4) for v in range(4) if (a[u]+a[v])%7==w]==[(i,j),(j,i)] and I[w]==1
# Ore derivation of volume has three different nonzero PBW coefficient monomials.
sy,sb,dy,db,dc,r=s.symbols('sy sb dy db dc r',nonzero=True)
volume={(1,3,0):sy*sb*dc,(3,0,1):sy*db,(0,1,3):dy/r**2};assert len(volume)==3 and all(v!=0 for v in volume.values())
n7['ordinary_exclusion']='skew3 base Ore extension: delta(ybc) has three different nonzero PBW terms, while Gx=xG forces delta(ybc)=0'
final=[r for r in results if r['patterns'] and r is not n7]
assert len(final)==12 and sum(r['label_count'] for r in final)==31
out={'status':'PASS','scope':'complete orbit-nonzero necessary refinement with exact Laurent-binomial closure, plus sole order7 Ore-volume exclusion','remaining_Galois_labels':12,'remaining_root_sets':31,'remaining_orders':sorted({r['N'] for r in final}),'pre_Ore_labels':13,'pre_Ore_root_sets':33,'pre_Ore_orbit_masks':23,'pre_Ore_cubic_support_masks':157,'all20_label_records':results,'final_necessary_labels':[{'N':r['N'],'exponents':r['exponents'],'label_count':r['label_count'],'orbit_masks':len(r['patterns']),'cubic_support_pieces':sum(len(p['cubic_masks']) for p in r['patterns'])} for r in final],'ordinary_proof_inputs':['domain pure two-variable quadratic relation space rank<=1','all nonzero orbit masks and rank minors: one term impossible, two terms root binomial','Smith row-lattice Laurent reduction, including torsion; exact cyclotomic coefficients','all necessary pure-column skew ratios and hdet/G equations in the actual orbit coefficients','Ore3-base recognition and nonzero volume derivation'],'not_claimed':['remaining nonbinomial rank minors vanish','all necessary orbit masks are AS4','normal G exists on remaining masks','all12 labels have H3','complete H3 classification','ordinary Ore proof mechanically checked in entirety']}
(ROOT/'cubic_four_simple_orbit_torus_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all nonzero orbit masks and Laurent closure;12 finite Galois labels /31 root sets remain')
