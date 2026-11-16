"""All-coefficient rank constraints excluding both semisimple rank2 ruling pencils."""
import itertools,json
from pathlib import Path
import sympy as S
A,B,C,D=S.symbols('A B C D')
M=S.Matrix([[A,C,-B,D],[-A,-B,-C,-D],[B,D,-D,0]])
def minors(M):
 return [S.expand(M.extract(rr,cc).det()) for rr in itertools.combinations(range(M.rows),2) for cc in itertools.combinations(range(M.cols),2)]
G=S.groebner(minors(M),A,B,C,D)
for p in [B*B,C*C,D*D]:assert G.reduce(p)[1]==0
b,c,d,e,f,t=S.symbols('b c d e f t');N=S.Matrix([[b,d,c,e],[b,c,d,e],[c,e,e,f]])
I=minors(N)
for row in N.tolist():
 det=row[0]*row[3]-row[1]*row[2]
 assert list(S.groebner(I+[1-t*det],b,c,d,e,f,t))==[1]
out={'status':'PASS','scope':'all coefficients in both ruling graph pencils of semisimple (2,2), odd rank2',
 'positive_contractions':'rank<=1 forces B=C=D=0; remaining row A*x0^2 forbidden by domain',
 'negative_contractions':'rank<=1 makes all three quadratic coefficient determinants zero, certified by three unit saturation ideals',
 'structural_conclusion':'each ruling forces a >=3 dimensional pure binary quadratic relation space, contradicting domain',
 'not_claimed':['secant or tangent graph pencils','nonsemisimple or odd rank4']}
Path(__file__).with_name('cubic_order2_22_ruling_exclusion_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS both ruling pencils excluded by universal contraction and domain certificates')
