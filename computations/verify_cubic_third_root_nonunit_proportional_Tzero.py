#!/usr/bin/env python3
"""Exact necessary equations, all cyclotomic normal-x spectra and source skew-cone
image for the entire v1,n=T=0 nonunit proportional boundary. Ordinary H3 proof
uses the existing skew-cone vertex lemma, not a sampled global-dimension claim.
"""
from pathlib import Path
import itertools,json,sympy as s
from sympy.polys.matrices import DomainMatrix
from cubic_third_root_original22 import top_matrix
z=s.Symbol('z');F=s.QQ.alg_field_from_poly(s.Poly(z*z+z+1,z));os=F.to_sympy(F.unit);O=s.Symbol('omega');a=s.symbols('a:22')
def red(e):
 e=s.expand(e).replace(lambda v:v.is_Pow and v.base==O and v.exp.is_Integer,lambda v:O**(int(v.exp)%3))
 return s.rem(s.expand(e),O*O+O+1,O)
P=F.poly_ring(*a);oo=P.convert(F.unit,F)
H=top_matrix(P,oo,list(P.gens),[1,1,0,2]).to_Matrix().xreplace({os:O}).applyfunc(red)
M=H.extract([2,6,8,9,15],[0,1,4,5,11,14]);m=s.Symbol('m');alpha=-O*m*m
sub={a[13]:1,a[20]:0,a[9]:-alpha*O**2,a[17]:0,a[11]:0,a[19]:0,a[12]:1,a[3]:0,a[14]:-O/alpha,a[7]:-O**2*alpha,a[16]:0,a[10]:m,a[18]:0,a[21]:0}
N=M.subs(sub).applyfunc(red);Q=N[4,:4];R0=N[1,:4];R1=N[3,:4];R2=(N[0,:4]+m*N[2,:4]).applyfunc(red)
assert red(R0[0]-O**2*a[1])==0 and red(R0[3]-O**2*a[15])==0 and red(R1[0]-O**2*a[2])==0
assert red(R2[0]-(O**2-m)*a[0])==0 and red(R2[3]-(a[8]-m*a[5]))==0
cross=lambda row:red(row[1]*Q[2]-row[2]*Q[1])
assert red(cross(R0)+O**2*alpha*(a[6]-O**2/alpha**2*a[5]))==0
assert red(cross(R1).subs({a[6]:O**2/alpha**2*a[5],a[8]:m*a[5]})-(1-m**9)/alpha**3*a[5])==0
assert red(cross(R2).subs({a[1]:0,a[2]:0})+(m**5-O)/alpha*a[4])==0
Pm=F.poly_ring(m);omega=Pm.convert(F.unit,F);mm=Pm.gens[0]
assert (mm**5-omega).gcd(mm**9-Pm.one).monic()==mm-omega**2
assert (mm**5-omega).diff(0).gcd(mm**5-omega).degree()==0
assert (mm**9-Pm.one).diff(0).gcd(mm**9-Pm.one).degree()==0
# No remaining cubic coupling makes a pure c² source column.
Nz=N.subs({a[j]:0 for j in [0,1,2,4,5,6,8,15]});assert all(not Nz[i,1] for i in range(4)) and Nz[4,1]
# Normal x: phi=(1,omega²*m^-4,m^-1,omega*m²).
G9=s.QQ.alg_field_from_poly(s.Poly(z**6+z**3+1,z));q=G9.unit
G15=s.QQ.alg_field_from_poly(s.Poly(z**8-z**7+z**5-z**4+z**3-z+1,z));r=G15.unit
cases=[('m1',F,F.one,F.unit,'x factor'),('momega',F,F.unit,F.unit,'x factor'),('momega2',F,F.unit**2,F.unit,'zero'),('primitive9_cube_omega',G9,q,q**3,'zero'),('primitive9_cube_omega2',G9,q,q**6,'pure base'),('primitive15',G15,r,r**5,'zero')]
spectra=[]
for name,L,mm,o,expected in cases:
 phases=[L.one,o**2/mm**4,L.one/mm,o*mm**2];allowed=[]
 for w in itertools.product(range(4),repeat=3):
  if sum([1,1,0,2][j] for j in w)%3:continue
  co=L.one
  for j in w:co*=phases[j]
  if co==o:allowed.append(w)
 if expected=='zero':assert not allowed
 if expected=='x factor':assert allowed and all(0 in w for w in allowed)
 if expected=='pure base':assert allowed and all(0 not in w for w in allowed) and all(co==L.one/mm for co in phases[1:])
 spectra.append({'case':name,'conclusion':expected,'allowed_words':[''.join('xybc'[j] for j in w) for w in allowed]})
# At primitive9 m³=omega², the source image is literally a skew cone on y,b,c.
C=s.Symbol('C');K=G9.frac_field(C);C0=K.gens[0];mm=K.convert(q,G9);o=mm**6;one,zero=K.one,K.zero;alph=-o*mm**2
co=[zero]*22
for j,c in {13:one,9:-alph*o**2,12:one,14:-o/alph,7:-o**2*alph,10:mm,5:C0,6:o**2/alph**2*C0,8:mm*C0}.items():co[j]=c
D=top_matrix(K,o,co,[1,1,0,2]);f=one/mm
rels=[{(2,2):one,(1,3):one,(3,1):one/mm**2},{(2,3):mm,(3,2):one,(1,1):C0},{(1,2):o**2*C0,(2,1):o/alph**2*C0,(3,3):-o*alph},
 {(0,1):one,(1,0):-f},{(0,2):one,(2,0):-f},{(0,3):one,(3,0):-f}]
R=DomainMatrix.from_dod({i:{j:rel.get(divmod(i,4),zero) for j,rel in enumerate(rels) if rel.get(divmod(i,4),zero)} for i in range(16)},(16,6),K)
lead=[10,14,15,1,2,3];small=R.extract(lead,range(6));det=small.det();assert det and det.numer.is_ground and det.denom.is_ground
coords=small.inv().matmul(D.extract(lead,range(16)));assert not any((R.matmul(coords)-D).to_list_flat())
assert all(c.denom.is_ground for c in coords.to_list_flat())
assert D.rank()==R.rank()==6
out={'status':'PASS','scope':'all v1,n=T0 proportional nonunit coupling; proof uses domain and normalizer eigenconditions','necessary_cube_equations':['a1=a2=a15=0','a6=omega²/alpha²*a5','a8=m*a5','(m-omega²)*a0=0','(m5-omega)*a4=0','(m9-1)*a5=0'],'finite_m_values_at_fixed_omega':13,'normal_x_spectra':spectra,'actual_skew_cone':'originalH=displayedR*coords, unit6minor, coefficient-field denominators only; x has uniform scalar m^-1 on y,b,c','external_to_program':'ordinary skew-cone vertex lemma in existing paper; not independently computer-proved','not_claimed':['v1 Tnonzero isolated phase excluded','v0 or zero couplings covered','wholeH3 complete']}
Path(__file__).with_name('cubic_third_root_nonunit_proportional_Tzero_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all v1,n=T0 nonunit proportional boundary identities')
