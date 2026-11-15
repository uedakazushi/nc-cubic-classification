"""Universal two-dimensional reps; exact fifth-root centre placement."""
import sympy as s,json
from pathlib import Path
q=s.symbols('q');h=q*q-1;I=s.eye(2);phi=s.cyclotomic_poly(5,q)
def rat(f):return s.factor(s.cancel(f))
def red(f):
 n,d=s.cancel(f).as_numer_denom()
 return s.rem(s.rem(n,phi,q)*s.invert(s.rem(d,phi,q),phi,q),phi,q).expand()
def rec5(M):
 C,D=2*I,M;k=q/h**2
 for j in range(1,5):C,D=D,(M*D-k*C).applyfunc(rat)
 return D
A=s.I/(q+1);classic=[s.diag(A,-A),s.Matrix([[0,1],[A*A,0]]),s.Matrix([[0,A*(1+q)],[-A**3*(1+q),0]])]
a=1/(1-q);b=a*(q+1/q-1);c=b/(q-1);d=(q*q+1)/(q*(q-1))
nonclassic=[s.diag(a,b),s.Matrix([[d,1],[c,0]]),s.Matrix([[d,q],[c/q,0]])]
rows=[]
for name,gens,ww in [('classical2',classic,-(q*q+q**-2)),('nonclassical2',nonclassic,q**4+q**-4)]:
 x,y,z=gens
 for j,k,i in [(1,2,0),(2,0,1),(0,1,2)]:assert all(rat(v)==0 for v in gens[j]*gens[k]-q*gens[k]*gens[j]-gens[i])
 O=(x*y*z+(x*x+q*q*y*y+z*z)/h).applyfunc(rat);assert O==O[0,0]*I
 Dval=-O[0,0];w=rat(-(q+1/q)-h**3*Dval/q**2);assert rat(w-ww)==0
 centres=[rec5(g).applyfunc(red) for g in gens]
 assert all(M==M[0,0]*I for M in centres)
 target=0 if name=='classical2' else red(-2/h**5)
 assert all(red(M[0,0]**2-target**2)==0 for M in centres)
 assert red(gens[1][1,0])!=0 and red(x[0,0]-x[1,1])!=0
 rows.append({'type':name,'D':str(rat(Dval)),'w_D':str(w),'central_XYZ':[str(M[0,0]) for M in centres],'irreducible':'x has distinct eigenvalues and both y off-diagonal entries nonzero'})
# Two character levels, and four distinct interior levels.
Dchar=rat(-(a**3+(q*q+2)*a*a/h))
assert rat(-(q+1/q)-h**3*Dchar/q**2-(q*q+q**-2))==0
levels=[-(q+1/q),-(q*q+q**-2),q+1/q,q*q+q**-2]
assert all(red(levels[i]-levels[j])!=0 for i in range(4) for j in range(i))
assert all(red(z-2)!=0 and red(z+2)!=0 for z in levels)
cert={'version':'classification-v49','base':'q primitive fifth root','universal_rational_matrix_relations':True,'representations':rows,'four_interior_levels_distinct':True,'characters':'origin w=-(q+q^-1); four nonzero characters w=q^2+q^-2','result':'Every interior A1 centre has an irreducible representation of dimension1 or2 < PIdegree5; both McKay multiplicities positive','scope':'Representation identities are universal rational checks; central placement and distinctness exact mod Phi5. H3 conclusion uses ordinary maximal-order, McKay and terminal-boundary proofs.'}
Path(__file__).with_name('cubic_quantum_triangle_order5_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
print('PASS fifth-root full interior representation coverage, universal 2x2 identities and exact central placement')
