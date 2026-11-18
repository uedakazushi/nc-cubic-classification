"""Exact centre ranks for the square-added disjoint Segre projection."""
import json
from pathlib import Path

import sympy as s

from sympy.polys.matrices import DomainMatrix

from verify_cubic_as4_four_simple import IX
from verify_cubic_pym_generic import words
from verify_cubic_as4_four_simple_second import central_data

Q = s.Rational
h = s.Symbol("h")
basis = s.eye(16)


def word(i, j):
    return basis[:, IX[i, j]]


def comm(i, j):
    return word(i, j) - word(j, i)


def internal(mixed, ell, gamma):
    pairs = [(0, 2), (0, 3), (1, 2), (1, 3)]
    cross = s.Matrix.hstack(*[comm(i, j) for i, j in pairs])
    symmetric = s.Matrix.hstack(*[(word(i, j) + word(j, i))/2 for i, j in pairs])
    marking = s.zeros(4)
    for i, j, sign in [(0, 3, 1), (1, 2, -1)]:
        marking[i, j] = marking[j, i] = Q(sign, 2)
    square = s.kronecker_product(s.Matrix(ell), s.Matrix(ell))
    return s.Matrix.hstack(comm(0, 1), square + gamma * comm(2, 3),
                           symmetric + cross * mixed.T * marking.inv())


def transverse(da, cb, db):
    return s.Matrix.hstack(
        word(1, 0) - word(0, 1) - 8*word(0, 0),
        word(2, 0) + word(0, 2), comm(3, 2),
        word(3, 0) - da, word(2, 1) - cb, word(3, 1) - db,
    )


def cases():
    a, b, plus = (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0)
    entries = [(0, 3), (1, 2)]
    hs = s.zeros(4)
    for i, j in entries:
        hs[i, j] = hs[j, i] = h
    for name, ell in [('S_a', a), ('S_a+b', plus)]:
        yield name, internal(hs, ell, Q(1, 8)-2*h*h), [h, 4*h-1, 4*h+1]
    for name, entries, ells in [
        ('Z', [], [a]), ('R1', [(0, 0)], [a, b]),
        ('RL', [(0, 1), (1, 0)], [a, b]),
        ('RR', [(0, 2), (2, 0)], [a, plus]),
    ]:
        mixed = s.zeros(4)
        for i, j in entries:
            mixed[i, j] = 1
        for index, ell in enumerate(ells):
            yield f'{name}_{index}', internal(mixed, ell, Q(1, 8)), []
    ac, ad, bc, bd = [word(i, j) for i, j in [(0, 2), (0, 3), (1, 2), (1, 3)]]
    yield 'A_h', transverse(-ad, -bc+8*(h-1)*ac, -bd-8*(h+1)*ad), []
    yield 'N', transverse(-ad, -bc-8*ac, -bd-8*ac-8*ad), []
    yield 'B1', transverse(-ad+8*ac, -bc, -bd-16*ad+64*ac-8*bc), []
    yield 'B2', transverse(-ad+8*bc, -bc, -bd-16*ad+64*bc), []


def factors(value):
    return {s.Poly(factor, h).monic().as_expr()
            for factor, _ in s.factor_list(value, h)[1]}


def all_values(name, relations, units):
    """Use generic quotient identities and recompute at every nonunit factor."""
    field = s.QQ.frac_field(h) if h in relations.free_symbols else s.QQ
    matrix, rows, projections = central_data(relations, field)
    assert len(rows) == 20, name
    minor = field.to_sympy(matrix.extract(rows, list(range(20))).det())
    assert minor
    record = {"name": name, "minor": str(s.factor(minor)), "rows": rows}
    if field == s.QQ:
        return record
    denominators = set()
    for projection in projections:
        for entry in projection.to_dok().values():
            denominators.update(factors(field.to_sympy(field(entry.denom))))
    forbidden = set().union(*(factors(unit) for unit in units))
    numerator, denominator = s.fraction(s.cancel(minor))
    exceptional = (denominators | factors(numerator) | factors(denominator)) - forbidden
    roots = []
    for factor in sorted(exceptional, key=str):
        polynomial = s.Poly(factor, h, domain=s.QQ)
        assert polynomial.is_irreducible
        assert polynomial.degree() <= 2
        root = s.solve(polynomial.as_expr(), h)[0]
        assert s.Poly(s.minpoly(root, h), h).monic() == polynomial
        coeff = s.QQ if root.is_Rational else s.QQ.algebraic_field(root)
        specialized = relations.subs(h, root)
        target, special_rows, (projection, _) = central_data(specialized, coeff)
        witness = {"factor": str(factor), "field_degree": polynomial.degree(),
                   "rank": len(special_rows)}
        if name in {"S_a", "S_a+b"} and factor == h*h+Q(1, 48):
            # At the primitive cubic resonance these displayed pure cubes
            # span the whole kernel, not just a subspace of candidate cuts.
            count = 4 if name == "S_a" else 2
            cubic_indices = [words(3).index((i, i, i)) for i in range(count)]
            cubes = projection.extract(list(range(20)), cubic_indices)
            assert isinstance(cubes, DomainMatrix)
            assert cubes.rank() == count and (target*cubes).is_zero_matrix
            assert len(special_rows) == 20-count
            witness["centre_basis"] = ["abcd"[i]*3 for i in range(count)]
        else:
            assert len(special_rows) == 20, (name, factor)
            det = coeff.to_sympy(target.extract(special_rows, list(range(20))).det())
            assert det
            witness.update({"rows": special_rows, "minor": str(det)})
        roots.append(witness)
    record.update({"excluded_factors": sorted(map(str, forbidden)),
                   "quotient_denominator_factors": sorted(map(str, denominators)),
                   "exceptional": roots})
    return record


def main():
    records = []
    for name, relations, units in cases():
        records.append(all_values(name, relations, units))
        print("PASS", name, "centre on every allowed value", flush=True)
    assert len(records) == 13
    Path(__file__).with_name("cubic_CY_one_segre_square_certificate.json").write_text(
        json.dumps(records, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
