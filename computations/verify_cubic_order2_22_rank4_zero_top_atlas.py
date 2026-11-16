"""Universal six-linear-equation zero-top atlas; special p,q values retained."""
import itertools,json
from pathlib import Path
import sympy as S
p,q,w=S.symbols('p q w');z=S.symbols('z0:6');A=S.zeros(4)
for (i,j),v in zip(itertools.combinations(range(4),2),z):A[i,j]=v;A[j,i]=-v
pf=z[0]*z[5]-z[1]*z[4]+z[2]*z[3]
sharp=S.Matrix([[0,-z[5],z[4],-z[3]],[z[5],0,-z[2],z[1]],[-z[4],z[2],0,-z[0]],[z[3],-z[1],z[0],0]])
assert (A*sharp-pf*S.eye(4)).applyfunc(S.expand)==S.zeros(4)
tau=S.zeros(4)
for i,j,k,l in itertools.product(range(2),repeat=4):tau[2*j+i,2*l+k]=A[2*i+l,2*k+j]
J=S.Matrix([[-1,-1],[1,0]]);records=[]
for name,a,b,variables,unit in [('QQ',S.Matrix([[0,1],[-p,0]]),S.Matrix([[0,1],[-q,0]]),[p,q],p*q),('QJ',S.Matrix([[0,1],[-p,0]]),J,[p],p),('JQ',J,S.Matrix([[0,1],[-q,0]]),[q],q),('JJ',J,J,[],S.Integer(1))]:
 M=S.zeros(4)
 for i,j,k,l in itertools.product(range(2),repeat=4):M[2*k+j,2*l+i]=-a[i,k]*b[j,l]
 assert S.expand(M.det()+a.det()**2*b.det()**2)==0
 for eps in [1,-1]:
  h=eps*a.det()*b.det();eq=list((h*tau+M.T*sharp*M).applyfunc(S.expand))
  if name=='QQ':
   v=1 if eps==1 else -1
   table=[(p+v)*z[0],(p+v)*z[5],(q+v)*z[1],(q+v)*z[4]]+([z[2],z[3]] if eps==1 else [])
  elif name=='QJ':
   table=([(p+1)*z[0],(p+1)*z[5],z[1],z[2],z[3],z[4]] if eps==1 else [(p-1)*z[0],(p-1)*z[5],z[4],z[2]+z[3]])
  elif name=='JQ':
   table=([(q+1)*z[1],(q+1)*z[4],z[0],z[2],z[3],z[5]] if eps==1 else [(q-1)*z[1],(q-1)*z[4],z[5],z[2]-z[3]])
  else:table=list(z) if eps==1 else [z[2],z[3],z[4],z[5]]
  # Compare localized polynomial ideals, NOT fraction-field row ranks: p=+/-1
  # and q=+/-1 are retained as complete special fibers.
  gens=list(z)+[w]+variables;loc=[1-w*unit]
  G=S.groebner(eq+loc,*gens);H=S.groebner(table+loc,*gens)
  assert list(G)==list(H)
  if name=='JJ':
   Gpf=S.groebner(table+[pf-h],*z);assert list(Gpf)==[1]
  records.append({'type':name,'epsilon':eps,'linear_equations':[str(t) for t in table],'Pfaffian':str(h)})
out={'status':'PASS','scope':'semisimple (2,2), mixed rank4, P=Q=0 necessary top atlas',
 'checks':['universal skew adjugate identity','reshuffled cross determinant','eight localized ideal equalities including special p,q fibers','both Jordan/Jordan branches inconsistent with nonzero Pfaffian'],
 'charts':records,'conclusion':'every such AS4 is a full mixed graph; six alternating coefficients obey the stated linear equations and one nonzero Pfaffian equation',
 'not_claimed':['AS4 sufficiency for every top','H3 classification in nonseparated charts','nonsemisimple zero-top coverage']}
Path(__file__).with_name('cubic_order2_22_rank4_zero_top_atlas_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS zero-top six-linear atlas: eight localized ideals, all special fibers and both JJ exclusions')
