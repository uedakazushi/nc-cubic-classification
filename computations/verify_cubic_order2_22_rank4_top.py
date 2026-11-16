"""Universal positive-binary top restriction when the odd relation rank is four."""
import itertools,json
from pathlib import Path
import sympy as S
A,B,C,D=S.symbols('A B C D')
P=S.Matrix([[0,A,-A,B],[A,C,-B,D],[-A,-B,-C,-D],[B,D,-D,0]])
minors=[S.expand(P.extract(r,c).det()) for r in itertools.combinations(range(4),3) for c in itertools.combinations(range(4),3)]
G=S.groebner(minors,A,B,C,D)
assert G.reduce(B**3)[1]==0
P0=P.subs(B,0)
assert all(S.expand(m.subs(B,0))==0 for m in minors)
comm=S.Matrix([0,1,-1,0]);quad=S.Matrix([A,C/2,C/2,D])
assert P0==comm*quad.T+quad*comm.T
# A nonzero symmetric quadric cannot be proportional to the commutator.
# Hence the displayed symmetric outer sum has rank2 whenever quad is nonzero.
for values in [{A:1,C:0,D:0},{A:0,C:2,D:0}]:assert P0.subs(values).rank()==2
out={'status':'PASS','scope':'semisimple Nakayama (+,+,-,-), odd relation dimension4',
 'exact_checks':['the 3x3 minor ideal contains B^3','B=0 makes every 3x3 minor zero','P=commutator tensor symmetric_quadric plus its transpose'],
 'structural_conclusion':'positive pure top is zero, commutator times rank1 symmetric quadric, or commutator times rank2 symmetric quadric, up to GL2 and scale',
 'not_claimed':['whole envelope classification','normal cubic exclusion','nonsemisimple sector','H3 admissibility']}
Path(__file__).with_name('cubic_order2_22_rank4_top_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS semisimple (2,2) odd-rank-four positive-top trichotomy')
