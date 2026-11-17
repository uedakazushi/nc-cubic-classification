#!/usr/bin/env python3
"""Original10 top, exact paired rank1 constraints, cross rank1, and the two
normal-base eigenvalue obstructions completing the phase-free rank3 chart.
"""
from pathlib import Path
import sympy as s,json
from cubic_diagonal_top import top_basis,top_matrix
T=s.Symbol('t');aa=s.symbols('a:10');K=s.QQ.frac_field(T,*aa);t=K.gens[0];n=[1,-2,-1,2];lam=[t**j for j in n];basis=top_basis(K,lam)
reps=[''.join('xybc'[j] for j in next(iter(ts))) for ts in basis]
assert reps==['xxbb','xybc','xycb','xbxb','xbyc','xbcy','xcyb','xcby','yycc','ycyc']
H=top_matrix(K,lam,list(K.gens[1:])).to_Matrix();groups={j:[4*u+v for u in range(4) for v in range(4) if n[u]+n[v]==j] for j in [0,1,-1,3,-3]}
H0=H.extract(groups[0],groups[0]);M1=H.extract(groups[1],groups[-1]);M3=H.extract(groups[3],groups[-3]);assert H0==H0.T
assert s.expand(M1.det())==aa[2]*aa[5]-aa[1]*aa[7]
assert not s.cancel(M3.det()-(aa[1]*aa[7]-aa[4]*aa[6])/T**2)
# Domain in both 2x2 pure-pair blocks forces every entry nonzero.
assert set(M1)=={aa[1]/T,-aa[5]*T,aa[2]/T,-aa[7]*T}
assert set(M3)=={aa[6],aa[7],-aa[1]/T**2,-aa[4]/T**2}
p,q,r=s.symbols('p q r');sub={aa[1]:1,aa[2]:p,aa[4]:q,aa[5]:r,aa[7]:p*r,aa[6]:p*r/q};Z=H0.subs(sub).extract([0,2,1,3],[0,2,1,3]);cross=Z[:2,2:]
assert cross==s.Matrix([[q,r],[-p*T,-p*r*T/q]]) and not s.cancel(cross.det())
assert cross==s.Matrix([1,-p*T/q])*s.Matrix([[q,r]])
# Normal-generator eigenvalue comparison: u=x when xb/bx is pure.
a,b,c,l,z=s.symbols('a b c l z');eqU=[l-a*b*c,a-l,b*b*c-l,z*a*b*c*l-1];gb=s.groebner(eqU,z,a,b,c,l)
assert gb.reduce(a*c-1)[1]==0 and gb.reduce(b-l)[1]==0
# Mixed relation yc-tau cy=d xb has eigenvalues1 versusmu_x.
d=s.Symbol('d');gu=s.groebner(eqU[:-1]+[d*(a*c-b),z*a*b*c*l*d-1],z,a,b,c,l,d)
assert gu.reduce(l-1)[1]==0
# Normal-generator v=y when yc/cy is pure: xb side has eigenvaluemu_y,
# while yc has eigenvalue1.
eqV=[l-a*b*c,a*a-l,b*b*c-l,z*a*b*c*l-1];gv=s.groebner(eqV,z,a,b,c,l)
assert gv.reduce(a-b)[1]==0 and gv.reduce(c-1)[1]==0 and gv.reduce(a*b-l)[1]==0
vv=s.groebner(eqV[:-1]+[d*(a*b-c),z*a*b*c*l*d-1],z,a,b,c,l,d);assert vv.reduce(l-1)[1]==0
# Missing reverse-pair coefficient gives an additional independent quadratic.
y,w,m=s.symbols('y w m',commutative=False);kap,sig=s.symbols('kap sig')
assert s.expand((y*w-kap*sig*m)*y-y*(w*y-kap*m)-kap*(y*m-sig*m*y))==0
out={'status':'PASS','scope':'entire phase-free (t,t^-2,t^-1,t²) rank3 support chart excluded by ordinary rank/domain/Ore proof','top_dimension':10,'representatives':reps,'paired_rank1_equations':['a1*a7=a2*a5=a4*a6'],'domain_nonzero_multilinear_coefficients':[1,2,4,5,6,7],'normalized_source':'a1=1,a2=p,a4=q,a5=r,a7=pr,a6=pr/q; pqr nonzero','weight0_cross_block_rank':1,'ordinary_linear_cover':'rank2 symmetric H0 and crossrank1 force pure xb/bx or pure yc/cy relation; each gives two normal base generators','normal_base_Ore_identity':'Nakayama scalar of either normal base generator is product of its three normalizing scalars','pure_U_case':'normal x forces yc eigen1, xb eigenmu_x; nonzero deformation forcesmu_x1','pure_V_case':'normal y forces xb eigenmu_y, yc eigen1; nonzero deformation forcesmu_y1','zero_deformation':'skew, already excluded for four simple eigenvalues','scope_warning':'rank4 finite-order points with extra nonzero-weight support remain in boundedN<=96 locus','remaining_rank3_chart':'(alpha,beta,t,gamma/t), phase common orderM<=24','not_claimed':['last phase chart solved','all bounded finite-order points excluded','full four-simple or CY classification','complete H3 classification','ordinary rank/Ore arguments fully mechanically checked']}
Path(__file__).with_name('cubic_four_simple_last_rank3_curve_certificate.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS original10 source, crossrank1 cover data and both normal-base obstructions')
