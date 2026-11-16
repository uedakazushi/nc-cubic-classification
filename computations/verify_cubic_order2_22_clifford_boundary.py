"""Exact Ore-chart reconstruction and singular dependent-coefficient obstruction."""
import json
from pathlib import Path
import sympy as S
h0,h1,h2,a,b,c,d,aa,bb,cc=S.symbols('h0 h1 h2 a b c d aa bb cc')
# X,Y commute, W anticommutes with both; u anticommutes with X,Y,W.
def add(*ps):
 out={}
 for p in ps:
  for key,v in p.items():out[key]=out.get(key,0)+v
 return {k:S.expand(v) for k,v in out.items() if S.expand(v)}
def scale(p,c):return {k:S.expand(v*c) for k,v in p.items() if S.expand(v*c)}
def mul(p,q):
 out={}
 for (word,i),a0 in p.items():
  for (tail,j),b0 in q.items():
   sign=(-1)**((i*len(tail)+sum(x==2 and y<2 for x in word for y in tail))%2)
   key=(tuple(sorted(word+tail)),i+j);out[key]=out.get(key,0)+sign*a0*b0
 return add(out)
def power(p,n):
 out={((),0):S.Integer(1)}
 for _ in range(n):out=mul(out,p)
 return out
X={((0,),0):S.Integer(1)};Y={((1,),0):S.Integer(1)};W={((2,),0):S.Integer(1)};u={((),1):S.Integer(1)}
h=add(scale(power(X,2),h0),scale(mul(X,Y),2*h1),scale(power(Y,2),h2))
x=mul(X,u);y=mul(Y,u);v=mul(add(W,scale(h,-S.Rational(1,2))),u)
def form(p,q):return add(scale(power(p,2),h0),scale(mul(p,q),2*h1),scale(power(q,2),h2))
assert not add(mul(x,y),scale(mul(y,x),-1))
for p in [x,y]:
 for q in [u,v]:assert not add(mul(p,q),mul(q,p))
assert not add(mul(u,v),mul(v,u),scale(form(x,y),-1))
f=add(scale(power(X,3),a),scale(mul(power(X,2),Y),b),scale(mul(X,power(Y,2)),c),scale(power(Y,3),d))
fg=add(scale(power(x,3),a),scale(mul(power(x,2),y),b),scale(mul(x,power(y,2)),c),scale(power(y,3),d))
G=add(fg,scale(mul(x,power(u,2)),aa),scale(mul(x,power(v,2)),bb))
F=add(f,scale(X,-aa),scale(mul(X,add(power(W,2),scale(power(h,2),-S.Rational(1,4)))),bb))
assert not add(G,mul(F,power(u,3)))
x0,y0,w0=S.symbols('X Y W');hc=h0*x0*x0+2*h1*x0*y0+h2*y0*y0
fc=a*x0**3+b*x0*x0*y0+c*x0*y0*y0+d*y0**3-aa*x0+bb*x0*(w0*w0-hc*hc/4)
assert all(S.expand(e.subs({x0:0,y0:0,w0:cc,aa:bb*cc**2}))==0 for e in [fc,S.diff(fc,x0),S.diff(fc,y0),S.diff(fc,w0)])
out={'status':'PASS','Ore_chart':{'relations':['XY=YX','WX=-XW','WY=-YW'],'reconstruction':['x=Xu','y=Yu','v=(W-h(X,Y)/2)u','u conjugates X,Y,W to their negatives'],'six_envelope_relations':True,'cut_identity':'G=-F*u^3, F=f3-aa*X+bb*X*(W^2-h2^2/4)'},'dependent_boundary_singularity':{'point':'X=Y=0,W=cc','condition':'aa=bb*cc^2','F_and_all_three_derivatives':0,'other_chart':'exchange u,v if bb=0; zero coefficients already factor'},'geometric_conclusion':'all dependent-coefficient cuts are non-H3 by finite-group cocycle comparison with the singular commutative affine surface','not_claimed':['all positive-top envelopes','intrinsic relative descent']}
Path(__file__).with_name('cubic_order2_22_clifford_boundary_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: six Ore-chart relations, exact cubic identity, universal singular dependent boundary')
