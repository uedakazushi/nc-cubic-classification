#!/usr/bin/env python3
"""AZ2 fixed L models: Ore base, scalar-cube normalizer and centre line.

The infinite-self-Ext obstruction is proved in the paper; this verifies its
finite algebraic inputs, not an infinite homological computation.
"""
import json
from pathlib import Path
from itertools import product
import sympy as S
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_four_simple import source_matrix,W2,IX
from verify_cubic_as4_four_simple_second import central_data
from verify_cubic_pym_generic import words


def l_matrix(omega,eta):
    omega,eta=map(S.sympify,(omega,eta))
    return source_matrix(omega,{1:1,4:1,6:eta*(omega+2)/6,17:eta*(omega+2)/6,
      11:eta*(omega+2)/12,8:eta*(omega+1)/4,15:eta/4,13:-S.Rational(1,12),19:omega/12})


def main():
    root=S.sqrt(3)*S.I;omega=(-1+root)/2;field=S.QQ.algebraic_field(root);base=[0,1,3];results=[]
    for eta in [1,-1]:
        R,A=l_matrix(omega,eta);rd=DomainMatrix.from_Matrix(R).convert_to(field)
        ad=DomainMatrix.from_Matrix(A).convert_to(field);top=(rd*ad*rd.transpose()).to_dok()
        assert all(not(top.get((IX[v[:2]],IX[v[2:]]),field.zero)+top.get((IX[v[1:3]],IX[(v[3],v[0])]),field.zero)) for v in words(4))
        cross=[1,3,5];left=rd.extract([IX[(2,i)] for i in base],cross).transpose()
        right=rd.extract([IX[(i,2)] for i in base],cross).transpose()
        sigma=-(left.inv()*right).transpose();assert sigma.det()
        q=field.from_sympy(omega if eta==1 else omega**2)
        assert (sigma**3-DomainMatrix.eye(3,field)*q).is_zero_matrix
        assert q**3==field.one and q!=field.one
        tc={}
        sd=sigma.to_dok()
        for j,i in enumerate(base):
            tc[IX[(2,i)],j]=field.one
            for k,b in enumerate(base):
                if (k,j) in sd:tc[IX[(b,2)],j]=-sd[k,j]
        target=DomainMatrix.from_dok(tc,(16,3),field)
        actual=rd.extract(list(range(16)),cross)
        assert (target*actual.extract([IX[(2,i)] for i in base],list(range(3)))-actual).is_zero_matrix
        # The base has exactly the three pure a,b,d relations; sigma preserves them.
        sr=rd.extract([IX[v] for v in product(base,repeat=2)],[0,2,4])
        U3=S.zeros(9,3);index={v:j for j,v in enumerate(product(range(3),repeat=2))}
        for j,(i,k) in enumerate([(0,1),(0,2),(1,2)]):U3[index[i,k],j]=S.Rational(1,2);U3[index[k,i],j]=S.Rational(1,2)
        li=DomainMatrix.from_Matrix((U3.T*U3).inv()*U3.T).convert_to(field)
        assert (li*sr-DomainMatrix.eye(3,field)).is_zero_matrix
        kd={}
        for i,j,k,l in product(range(3),repeat=4):
            a,b=sd.get((i,k),field.zero),sd.get((j,l),field.zero)
            if a and b:kd[3*i+j,3*k+l]=a*b
        action=DomainMatrix.from_dok(kd,(9,9),field)*sr
        assert (sr*li*action-action).is_zero_matrix
        M,rows,projections=central_data(R,field);assert len(rows)==19
        poly={(0,0,0):24*root,(1,1,1):1,(1,3,1):-omega,(1,3,3):-omega,(3,1,1):1,(3,3,1):1,(3,3,3):1} if eta==1 else {
              (0,0,0):-24*root,(1,1,1):1,(1,3,0):-(3+root),(1,3,3):1,(3,3,0):-(3+root),(3,3,3):1}
        ix3={v:j for j,v in enumerate(words(3))}
        vv=DomainMatrix.from_dok({(ix3[v],0):field.from_sympy(S.sympify(c)) for v,c in poly.items()},(64,1),field)
        coords=projections[0]*vv;assert coords.to_dok() and (M*coords).is_zero_matrix
        results.append({'eta':eta,'normal_c_matrix':[[str(c) for c in row] for row in sigma.to_Matrix().tolist()],
                        'sigma_cube_scalar':str(field.to_sympy(q)),'Ore_relation_transport':True,'base_relation_stability':True,
                        'conditional_AS4_cyclic_top':True,'centre3_dimension':1,
                        'central_generator':{str(v):str(c) for v,c in poly.items()},'factorisation_not_used':True})
        print('PASS adjacent L eta',eta,'Ore sigma^3 nontrivial cube root, CY tensor, centre line',flush=True)
    z=S.symbols('z');assert S.gcd(S.Poly((1-z)**2,z),S.Poly(1+z+z*z,z)).degree()==0
    cert={'version':'classification-v82','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9',
          'source_presentation':'ADJACENT_SHARED_ZERO_CORNER_COMPLETE.tex AZ2 only','models':results,
          'cone_Hilbert_reciprocal':'(1-z)^2/(1+z+z^2), non-polynomial',
          'scope':'Finite exact inputs for both fixed L exclusions. The paper proves all central cubic cuts lie in the Ore base and its vertex has infinite self-Ext. No factorisation/admissibility inference from centre dimension alone, and no AS4 sufficiency/full coverage theorem imported.'}
    Path(__file__).with_name('cubic_as4_four_simple_adjacent_L_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS finite inputs for skew-cone infinite-self-Ext exclusion',flush=True)

if __name__=='__main__':main()
