#!/usr/bin/env python3
"""Replay rational row identities for nonsplit three-dimensional Jordan blocks."""
import itertools
import json
from pathlib import Path
import sympy as S


def main():
    words=list(itertools.product(range(3),repeat=4))
    index={w:i for i,w in enumerate(words)}
    forbidden={w for w in words if w.count(2)>=3}
    assert len(forbidden)==9
    data=json.loads(Path(__file__).with_name('cubic_order2_nonsplit_tensor_certificate.json').read_text())
    total=0
    for name,expected in [('J2_extension',{2:0}),('J3_extension',{2:1,1:0})]:
        entry=data[name]
        dd=dict(entry['D_on_generators'])
        assert dd==expected
        D=S.zeros(81)
        for j,word in enumerate(words):
            for pos,v in enumerate(word):
                if v in dd:
                    target=word[:pos]+(dd[v],)+word[pos+1:]
                    D[index[target],j]+=1
        assert {tuple(r['word']) for r in entry['certificates']}==forbidden
        for record in entry['certificates']:
            covector=S.zeros(81,1)
            for word,c in record['row_multipliers']:
                covector[index[tuple(word)]]+=S.Rational(c)
                total+=1
            rhs=S.zeros(81,1)
            rhs[index[tuple(record['word'])]]=1
            assert D.T*covector==rhs
    assert total==49
    print('PASS 18 exact rational row identities: every invariant quartic has no v³W or v⁴ term')


if __name__=='__main__':main()
