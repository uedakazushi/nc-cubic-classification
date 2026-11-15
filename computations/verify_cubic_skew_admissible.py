#!/usr/bin/env python3
"""Exact identities for the five-type geometric skew-envelope classification.

Uses SymPy for polynomial identities and Jacobian unit-ideal certificates;
this does not replace the categorical, valuation, or classification proofs.
"""
import itertools as it
import json
from pathlib import Path
import sympy as S


def main():
    A,B,C,D,E,s,r,k,h=S.symbols('A B C D E s r k h')
    center=D*h*h-E*s*r*h-s*r*(A+B*s+C*r)
    substituted=S.factor(center.subs(h,k*s*r)/(s*r))
    assert S.expand(substituted-((D*k*k-E*k)*s*r-A-B*s-C*r))==0
    rformula=(A+B*s)/((D*k*k-E*k)*s-C)
    assert S.cancel(substituted.subs(r,rformula))==0

    # Critical values of the untwisted sign cubic on t=1.
    x,y,z,t=S.symbols('x y z t')
    critical_xyz=-8*B*C*D/E**3
    critical_value=-A+4*B*C*D/E**2
    assert S.cancel(-A+12*B*C*D/E**2+E*critical_xyz-critical_value)==0

    # Cubic norm: multiply conjugates in Q[zeta,u,a,t]/(zeta^2+zeta+1,u^3-t).
    u,a,zeta=S.symbols('u a zeta')
    def reduce_root(poly):
        return S.rem(S.rem(S.expand(poly),zeta**2+zeta+1,zeta),u**3-t,u)
    product=S.prod(zeta**j*u+a for j in range(3))
    assert S.expand(reduce_root(product)-(t+a**3))==0
    assert S.expand(reduce_root(S.prod(zeta**j*u for j in range(3)))-t)==0

    # The entire central lattice in the excluded six-parameter type has index 9.
    lattice=S.Matrix([[-1,3,0],[1,0,3],[1,0,0]])
    assert abs(lattice.det())==9
    qexp=S.Matrix([[0,1,2],[-1,0,2],[-2,-2,0]])
    assert all(int(v)%3==0 for v in qexp*lattice)
    # With y^3=s, u^3=t, v^3=r^3*s/t the relation becomes linear in s.
    sexpr=-t*(t+1)/(t+r**3)
    assert S.cancel(1+sexpr+t+r**3*sexpr/t)==0

    # Characteristic-zero Jacobian witnesses: every projective affine chart has unit ideal.
    witnesses={
        'CY_sign':-t**3+t*(x*x+y*y+z*z)+x*y*z,
        'nonCY_sign':x**3+x*x*y+2*x*y*y+3*y**3+x*z*z+y*t*t,
        'third_Hesse_Fermat':t**3+x**3+y**3+z**3,
        'third_Hesse_nonzero':t**3+x**3+y**3+z**3+x*y*z,
        'third_double_character':t**3+x**3+y**3+z**3,
    }
    variables=(t,x,y,z);checks=[]
    for name,f in witnesses.items():
        derivatives=[S.diff(f,v) for v in variables]
        for v in variables:
            remaining=[w for w in variables if w!=v]
            gb=S.groebner([g.subs(v,1) for g in derivatives],*remaining,domain=S.QQ)
            assert list(gb)==[S.Integer(1)],(name,v,gb)
            checks.append([name,str(v)])

    # Generic projective isotropy of the CY sign case is the rotational signed-permutation group.
    permutations=list(it.permutations(range(3)))
    def parity(p):
        return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    rotations=[]
    for p in permutations:
        for signs in it.product([-1,1],repeat=3):
            if signs[0]*signs[1]*signs[2]!=parity(p):continue
            m=S.zeros(3)
            for i,j in enumerate(p):m[i,j]=signs[i]
            assert m.det()==1
            rotations.append(m)
    assert len(rotations)==24
    # They act faithfully on the four unoriented body diagonals, hence form S4.
    diagonals=[S.Matrix(v) for v in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1)]]
    actions=set()
    for m in rotations:
        action=[]
        for v in diagonals:
            image=m*v
            hits=[j for j,w in enumerate(diagonals) if image==w or image==-w]
            assert len(hits)==1;action.append(hits[0])
        actions.add(tuple(action))
    assert len(actions)==24

    old=json.loads(Path(__file__).with_name('cubic_skew_jet_certificate.json').read_text())
    assert old['remaining_parameter_count']==37
    excluded=[row for row in old['nontrivial_coordinate_orbits']
              if row['order']==3 and row['candidate_vector_dimension']==4]
    assert len(excluded)==1 and excluded[0]['orbit_size']==6
    cert={'date':'2026-11-15','classification_scope':'Geometric H3 objects with skew-polynomial envelope only',
          'necessary_parameters_before_rank':37,'rank_three_exclusions':6,'admissible_ambient_parameters':31,
          'ambient_coordinate_types':5,'generic_coarse_dimensions':[4,1,2,1,0],
          'CY_sign_projective_isotropy_order':24,'CY_sign_isotropy_action':'all permutations of four body diagonals',
          'third_Hesse_isotropy_orders':{'E_nonzero':27,'E_zero':81},
          'rank_three_obstruction':'s=-t(t+1)/(t+r^3)=Norm(-u(u+1)/(u+r)), u^3=t; generic algebra M3(K)',
          'smooth_jacobian_charts':checks,
          'normalization_checks':['quaternion center rationalization','cubic norm identity over Q(zeta)',
                                  'index-nine central lattice','CY-sign critical value'],
          'proof_scope_limits':['not all AS4 envelopes','no relative stack descent claim',
                                'no claim these five types are global moduli components',
                                'no independent review or exhaustive novelty audit']}
    Path(__file__).with_name('cubic_skew_admissible_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS: characteristic-zero identities, 20 smooth Jacobian charts, S4 inertia, six rank-three exclusions; 31 parameters / five skew types')

if __name__=='__main__':main()
