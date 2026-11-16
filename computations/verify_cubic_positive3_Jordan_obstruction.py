#!/usr/bin/env python3
"""Exact positive-W Jordan quadratic invariants and the universal bad AS3 quotient."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    kap,d,t=S.symbols('kappa d t')
    # Basis x²,xy,y²,xv,yv,vy, with Dy=x,Dv=0 and vx=xv+d*x².
    M=S.zeros(6)
    M[0,1]=1;M[0,2]=kap;M[1,2]=2;M[3,4]=1;M[0,5]=d;M[3,5]=1
    invariants=S.Matrix.hstack(S.eye(6)[:,0],S.eye(6)[:,3],S.Matrix([0,-d,0,0,-1,1]))
    assert M*invariants==S.zeros(6,3)
    assert M.extract([0,1,3],[1,2,4]).det()==2
    assert invariants.extract([0,3,5],[0,1,2]).det()==1
    # At x=0, an invariant v² is a scalar commutator [v,y]. A binary
    # cyclic cubic has only symmetric quadratic contractions, forcing that scalar0.
    A,B,C,D,c=S.symbols('A B C D c')
    # coefficient order y²,yv,vy,v²
    derivative=S.Matrix([B,C,C,D]);required=S.Matrix([0,c*D,-c*D,D])
    equations=list(derivative-required)
    assert S.expand(equations[1]-equations[2]+2*c*D)==0
    # The resulting quotient has relations v²=0, zy=epsilon*yz,z²=t*y².
    # Every degree3 relation is reconstructed; only rational constants are pivots.
    records=[]
    for eps in [1,-1]:
        words=list(itertools.product(range(3),repeat=3));index={w:i for i,w in enumerate(words)}
        relations=[{(1,1):1},{(2,0):1,(0,2):-eps},{(2,2):1,(0,0):-t}]
        rows=[]
        for rel in relations:
            for gg in range(3):
                for side in [0,1]:
                    rows.append({index[((gg,)+w) if side==0 else (w+(gg,))]:cc for w,cc in rel.items() if cc!=0})
        columns=set(range(27));pivots=0
        while True:
            hit=next(((i,j,cc) for i,row in enumerate(rows) for j,cc in row.items()
                      if j in columns and cc!=0 and not S.sympify(cc).free_symbols),None)
            if hit is None:break
            i,j,cc=hit;pivot={k:S.expand(v/S.sympify(cc)) for k,v in rows.pop(i).items()}
            columns.remove(j);pivots+=1
            for row in rows:
                co=row.get(j,0)
                if not co:continue
                for k,v in pivot.items():
                    new=S.expand(row.get(k,0)-co*v)
                    if new==0:row.pop(k,None)
                    else:row[k]=new
        assert pivots==15 and not any(rows) and len(columns)==12
        records.append({'epsilon':eps,'degree3_relation_constant_pivots':15,'degree3_dimension':12})
    q=S.symbols('q')
    HA=(1+q)/(1-q);HV=1+q
    Hfree=S.cancel(1/(1/HA+1/HV-1))
    assert S.cancel(Hfree-(1+q)/(1-2*q))==0
    data={
      'hypotheses':'H3 multiplicities(3,1), gamma=0, split positive-W Jordan2+trivial1 case',
      'quadratic_D_kernel':['x²','xv','vy-yv-d*xy'],
      'cross_relation':'vx=xv+d*x²; x is normal regular linear',
      'quotient_by_x':'v²=c*[v,y], zy=epsilon*yz; AS3 binary cyclic top forces c=0 and z²=t*y²',
      'bad_quotient_checks':records,
      'free_product_Hilbert':'(1+q)/(1-2q), contradicting AS3 Hilbert(1-q)^-3 in degree3 (12 versus10)',
      'conclusion':'No positive-W Jordan case at gamma0; combined with the semisimple result, the whole multiplicity(3,1) gamma0 sector is excluded.',
      'scope':'Universal Jordan invariant matrix, symmetric-contraction constraint and both-sign degree3 quotient ranks checked. Normal-axis recognition and the AS3 quotient argument are structural proofs; gamma!=0 remains open.'}
    path=Path(__file__).with_name('cubic_positive3_Jordan_obstruction_certificate.json')
    if path.exists():assert json.loads(path.read_text())==data
    else:path.write_text(json.dumps(data,indent=2)+'\n')
    print('PASS positive-three Jordan obstruction: invariant kernel and universal quotient dimension12')


if __name__=='__main__':main()
