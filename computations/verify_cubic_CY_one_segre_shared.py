"""Exact centre certificates for seven shared Segre projections."""
from functools import cache
from itertools import combinations_with_replacement
import json
from pathlib import Path

import sympy as s

from verify_cubic_CY_one_segre_cross import Coefficients, PivotAlgebra, factor_set, p
from verify_cubic_CY_one_segre_extensions import ordered_relations
from verify_cubic_CY_one_segre_square import Q, all_values, comm, h, word
from verify_cubic_pym_generic import words

COEFF = Coefficients
PAIRS = words(2)
ORDERED = [i for i, (x, y) in enumerate(PAIRS) if x <= y]
INVERTED = [i for i, (x, y) in enumerate(PAIRS) if x > y]
CUBICS = list(combinations_with_replacement(range(4), 3))
QUARTICS = {w: i for i, w in enumerate(combinations_with_replacement(range(4), 4))}


def add(result, vector, scalar):
    for key, coefficient in vector.items():
        value = result.get(key, COEFF.zero) + coefficient*scalar
        if value:
            result[key] = value
        else:
            result.pop(key, None)


def pbw_check(relations, centre):
    """Check a maximal minor and all stated central candidates in the PBW basis."""
    relations = relations.applyfunc(s.cancel)
    pivot = relations.extract(INVERTED, range(6))
    rewriting = (-relations.extract(ORDERED, range(6))*pivot.inv()).applyfunc(s.cancel)
    rules = {}
    for j, i in enumerate(INVERTED):
        terms = {PAIRS[k]: COEFF.from_sympy(rewriting[n, j])
                 for n, k in enumerate(ORDERED) if rewriting[n, j]}
        assert all(w < PAIRS[i] for w in terms)
        rules[PAIRS[i]] = terms

    @cache
    def reduce(word):
        for i, (x, y) in enumerate(zip(word, word[1:])):
            if x > y:
                result = {}
                for replacement, scalar in rules[x, y].items():
                    add(result, reduce(word[:i]+replacement+word[i+2:]), scalar)
                return result
        return {word: COEFF.one}

    rows = [{} for _ in range(140)]
    for column, cubic in enumerate(CUBICS):
        for gen in range(4):
            result = reduce(cubic+(gen,)).copy()
            add(result, reduce((gen,)+cubic), -COEFF.one)
            for w, value in result.items():
                rows[35*gen+QUARTICS[w]][column] = value
    calculator = PivotAlgebra(COEFF, 4, [], [0]*4)
    calculator.pivot_product = COEFF.one
    rank = len(calculator.echelon(rows))
    assert rank == 20-bool(centre)
    centre_vector = {CUBICS.index(tuple("abcd".index(x) for x in w)): COEFF.from_sympy(q)
                     for w, q in centre.items()}
    assert all(not sum((row.get(i, COEFF.zero)*q for i, q in centre_vector.items()), COEFF.zero)
               for row in rows)
    minor = calculator.pivot_product
    det = COEFF.from_sympy(pivot.det())
    exceptions = set(factor_set([minor.n, minor.d, det.n, det.d,
                                 *[v.d for terms in rules.values() for v in terms.values()]]))
    return {"rank": rank, "minor": str(minor),
            "exception_factors": sorted(map(str, exceptions)), "centre": {word: str(coefficient) for word, coefficient in centre.items()}}, exceptions


def presentations():
    aa, bb, cc = (word(i, i) for i in range(3))
    ab, ac, ad, bc, bd, cd = (word(i, j) for i, j in
                             [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    ab_c, ac_c, ad_c, bc_c, bd_c, cd_c = (comm(i, j) for i, j in
                                         [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])

    def sym(i, j):
        return word(i, j)+word(j, i)

    for epsilon in range(2):
        yield f"SC{epsilon}", ordered_relations(ab+ad, ac+ab, bc-cd-bd-epsilon*ad,
                                                ad, bd+word(3, 3), cd+bd)
    yield "SOS", ordered_relations(ab+aa/8, ac, bc+ac/4, ad-aa/8-2*ab,
                                   bd+aa/64-bb, cd+ac/2+4*bc)
    yield "TWS", ordered_relations(ab, ac+aa/8, bc-ab/4, ad+aa/8+2*ac,
                                   bd+ab/2-4*bc, cd-aa/64+bb+cc)
    yield "P", s.Matrix.hstack(ab_c, aa+bc_c, sym(0, 1)+2*ac_c, sym(0, 2)+4*bd_c,
                               sym(1, 2)+4*ad_c, sym(1, 3)+ac_c/4-2*h*bc_c+2*cd_c)
    yield "A", s.Matrix.hstack(ab_c, aa+ac_c, sym(0, 1)-2*bc_c, sym(0, 2)+4*ad_c,
                               sym(1, 2)-4*bd_c, sym(0, 3)+2*bb+ac_c/4+2*h*bc_c+2*cd_c)

    def parabola(t, u, v, extra):
        return s.Matrix.hstack(
            ac_c, aa+8*t/(t+1)*ab_c, sym(0, 1)-4*t*ad_c,
            sym(0, 2)-16*u/(t+1)*ab_c+8*(t-1)/(t+1)*bc_c,
            sym(1, 2)+4*u*ad_c+2*(t-1)*cd_c,
            sym(0, 3)+2*bb+extra*cc+(Q(1, 4)-16*t*v/(t+1))*ab_c-8*t*(t-1)/(t+1)*bd_c,
        )

    for extra in (0, 2):
        yield f"T_{extra}", parabola(h, 0, 0, extra)
        yield f"V_{extra}", parabola(s.Integer(3), 0, h, extra)
        yield f"U_{extra}", parabola(Q(1, 3), h if extra else 1, 0, extra)
    yield "STS", ordered_relations(
        ab, ac+ab-h*aa/2, bc-(h*h/2+h/8)*aa+h*ab,
        ad+(h/2+Q(1, 4))*aa-ab+2*ac-4*bc/h,
        bd+(h*h/2+h/8)*aa+(Q(1, 4)-h)*ab+(2*h+Q(1, 2))*ac-4*bc,
        cd+cc+bd+(h+Q(1, 4))*ac-h*ab/2-2*bc+(h*h/4+h/8+p)*aa,
    )


def main():
    records = []
    for name, relations in presentations():
        if name in {"SC0", "SC1"}:
            records.append(all_values(name, relations, []))
        else:
            centre = {"SOS": {"aac": 1}, "TWS": {"aab": 1}}.get(name, {})
            primary, exceptions = pbw_check(relations, centre)
            primary["name"] = name
            forbidden = set()
            if name in {"T_0", "T_2"}:
                forbidden = {h, h-1, h+1}
                special, factors = pbw_check(relations.subs(h, -Q(1, 3)), {"acc": 1})
                assert not factors
                assert exceptions-forbidden == {h+Q(1, 3)}
                primary["recomputed_at_h_minus_1_over_3"] = special
            if name == "STS":
                forbidden = {h}
                assert exceptions-forbidden == {h+Q(1, 2), h+Q(1, 4)}
                special, factors = pbw_check(relations.subs(h, -Q(1, 2)), {})
                assert not factors
                primary["recomputed_at_h_minus_1_over_2"] = special
                centre = {"bbb": 1, "abb": Q(3, 4), "aab": Q(9, 64)}
                specialized = relations.subs(h, -Q(1, 4))
                special, factors = pbw_check(specialized, centre)
                assert factors == {p-Q(1, 64)}
                primary["recomputed_at_h_minus_1_over_4"] = special
                last, factors = pbw_check(specialized.subs(p, Q(1, 64)), centre)
                assert not factors
                primary["recomputed_at_h_minus_1_over_4_p_1_over_64"] = last
            if name not in {"T_0", "T_2", "STS"}:
                assert not exceptions
            records.append(primary)
        print("PASS", name, "central cubic exclusion", flush=True)
    Path(__file__).with_name("cubic_CY_one_segre_shared_certificate.json").write_text(
        json.dumps(records, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
