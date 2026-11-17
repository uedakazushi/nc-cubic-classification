"""Exact cyclic orbit support, finite character recursion and necessary factors."""
import itertools,collections

def top_basis(N,a):
 seen=set();basis=[]
 for word in itertools.product(range(4),repeat=4):
  if word in seen:continue
  w=word;c=0;ts={}
  while w not in ts:
   ts[w]=c;seen.add(w);w=(w[-1],)+w[:-1];c=(c+N-2*a[w[0]])%(2*N)
  if c==0:basis.append(ts)
 return basis

def prune(N,a):
 basis=top_basis(N,a);active=set(range(len(basis)));stages=[]
 while True:
  kill={}
  for col in range(16):
   entries={4*w[0]+w[1]:j for j in active for w in basis[j] if 4*w[2]+w[3]==col}
   if len(entries)==1:kill[next(iter(entries.values()))]=col
  if not kill:break
  stages.append(kill);active-=set(kill)
 letters={i for j in active for w in basis[j] for i in w};status='survives'
 if len(letters)<4:status='degenerate or zero top'
 elif all(len(set(w))==4 for j in active for w in basis[j]):status='multilinear skew'
 return basis,active,stages,status

def characters(N,a,max_degree=12):
 dims=collections.Counter((x+y)%N for x in a for y in a);caps={s:max(0,dims[s]-1) for s in range(N)};choices=[]
 for s in range(N//2+1):
  b=(-s)%N
  if s>b:continue
  if s==b:choices.append([(s,b,r,r) for r in range(min(caps[s],6)+1) if s==0 or r%2==0])
  else:choices.append([(s,b,r,2*r) for r in range(min(caps[s],caps[b],3)+1)])
 good=[];bad=[];V=collections.Counter(a);Vd=collections.Counter(-x%N for x in a)
 def conv(A,terms):return [sum(c*A[(s-j)%N] for j,c in terms) for s in range(N)]
 def rec(j,degree,rs):
  if j==len(choices):
   if degree!=6:return
   I=[0]*N
   for s,b,r,d in rs:I[s]=I[b]=r
   B=[[1]+[0]*(N-1),[a.count(j) for j in range(N)]];ii=[(j,c) for j,c in enumerate(I) if c]
   for n in range(2,max_degree+1):
    val=conv(B[n-1],V.items());val=[x-y for x,y in zip(val,conv(B[n-2],ii))]
    if n>=3:val=[x+y for x,y in zip(val,conv(B[n-3],Vd.items()))]
    if n>=4:val=[x-y for x,y in zip(val,B[n-4])]
    if min(val)<0:bad.append({'relation_character':I,'degree':n,'component':val.index(min(val)),'value':min(val)});return
    B.append(val)
   good.append(I);return
  for item in choices[j]:
   if degree+item[3]<=6:rec(j+1,degree+item[3],rs+[item])
 rec(0,0,[]);return good,bad

def factors(N,a,basis,active,chars):
 vs=[v for v in itertools.product(range(4),repeat=4) if sum(v)==3 and sum(x*y for x,y in zip(v,a))%N==0]
 support={s:set() for s in range(N)}
 for j in active:
  for w in basis[j]:support[(a[w[0]]+a[w[1]])%N].add(w[:2])
 good=[];bad=[]
 for I in chars:
  skew={tuple(sorted((i,j))) for i in range(4) for j in range(i+1,4) if support[(a[i]+a[j])%N]=={(i,j),(j,i)} and I[(a[i]+a[j])%N]==1}
  common=[i for i in range(4) if all(v[i] for v in vs) and all(i==j or tuple(sorted((i,j))) in skew for v in vs for j,c in enumerate(v) if c)]
  if common:bad.append({'relation_character':I,'reason':'common skew-normal letter','letter':common[0]});continue
  pure=None
  for S in itertools.combinations(range(4),2):
   if not all(all(v[j]==0 for j in range(4) if j not in S) for v in vs):continue
   weights=[s for s in range(N) if support[s] and all(i in S and j in S for i,j in support[s])]
   if sum(I[s] for s in weights)>0:pure=S;break
  if pure is not None:bad.append({'relation_character':I,'reason':'pure AS2 binary factor','letters':pure});continue
  good.append(I)
 return good,bad,vs
