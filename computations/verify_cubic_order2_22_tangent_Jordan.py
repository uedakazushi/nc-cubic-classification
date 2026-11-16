"""All five canonical tangent first-assignment positive-Jordan orbits: fixed cubics have a left factor."""
import itertools,json
from pathlib import Path
import sympy as S
# The public tangent verifier supplies exact original-relation quotient functionals.
source=Path(__file__).with_name('verify_cubic_order2_22_tangent_negative.py').read_text()
exec(source[:source.index('R=relations(S.diag(1,0),')])
HH=S.kronecker_product(S.Matrix([[1,1],[0,1]]),S.eye(2))
solution=list(S.linsolve(list(HH*A*HH.T-A),z))[0]
assert solution==(z[0],z[1],z[3],z[3],z[4],S.Integer(0))
records=[]
cases=[('minus',[-S.Rational(1,2),1,0,0,1,0])]+[('plus_'+str((sg,e)),[e,0,sg,sg,0,0]) for sg in [1,-1] for e in [0,1]]
for name,values in cases:
 R=relations(S.diag(1,0),values);words,index,free,nf=quotient(R,3,S.QQ)
 E=[i for i,j in enumerate(free) if sum(t>=2 for t in words[j])%2==0];assert len(E)==10
 ind={k:i for i,k in enumerate(E)};N=-S.eye(10)
 for j,k in enumerate(E):
  word=words[free[k]];options=[[(0,)] if v==0 else ([(0,),(1,)] if v==1 else [(v,)]) for v in word]
  for choices in itertools.product(*options):
   raw=tuple(i for v in choices for i in v)
   for row,c in nf[index[raw]].items():N[ind[row],j]+=S.QQ.to_sympy(c)
 kernel=N.nullspace();fixed=S.Matrix.hstack(*kernel) if kernel else S.zeros(10,0)
 positive2=[v for v in itertools.product(range(4),repeat=2) if sum(i>=2 for i in v)%2==0];L=S.zeros(10,8)
 for j,word in enumerate(positive2):
  for row,c in nf[index[(0,)+word]].items():L[ind[row],j]+=S.QQ.to_sympy(c)
 assert fixed.cols==4 and L.rank()==6 and L.row_join(fixed).rank()==6
 records.append({'orbit':name,'A_coefficients':[str(c) for c in values],'positive_B3_dimension':10,'H_fixed_dimension':4,'left_xB2_dimension':6,'left_xB2_plus_fixed_dimension':6})
out={'status':'PASS','scope':'all positive-only Jordan canonical envelopes in tangent first-assignment','A_invariance':'z5=0,z2=z3','complete_orbits':records,'untwist_argument':'mu(G)=G implies H(G)=G. B=C^(H^-1) has the same vectors and x*B2=x*C2, so the fixed-subspace inclusion gives an actual left factor in B. G is not transported as a normal cut.','conclusion':'combined with semisimple and negative-only/both-Jordan exclusions, the entire first tangent assignment has no H3','not_claimed':['reverse tangent assignment','other nonzero negative rank2 types','global H3 classification','intrinsic relative descent','independent peer review']}
Path(__file__).with_name('cubic_order2_22_tangent_Jordan_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS tangent Jordan: exact A invariants and all 5 fixed-kernel inclusions in left xC2 (dimensions 4,6,6)')
