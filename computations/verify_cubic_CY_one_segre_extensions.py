"""Central cubics in selected split and two-square Segre presentations."""
import json
from pathlib import Path

import sympy as s

from verify_cubic_CY_one_segre_square import Q, all_values, comm, h, internal, word
from verify_cubic_pym_generic import words

PAIRS = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]


def ordered_relations(*right):
    return s.Matrix.hstack(*(word(*pair)-rhs for pair, rhs in zip(PAIRS, right)))


def split_cases():
    ab, ac, ad, bc, bd, cd = (word(i, j) for i, j in
                              [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
    k = (1+4*h)/(1-4*h)
    for j, (s0, s4) in enumerate([(0, 0), (1, 0), (1, 1)]):
        relations = ordered_relations(k*ab, -ac, -bc,
                                      -ad/k+8*s4/(1+4*h)*bc,
                                      -k*bd-8*s0/(1-4*h)*ac, cd)
        yield f"T{j}", relations, [h, 4*h-1, 4*h+1]
    yield "C_r", ordered_relations(-ab, h*ac, bc/h, -ad/h, -h*bd, cd+ab), [h, h-1, h+1]
    family_d = ordered_relations(ab/h**2, h*ac, bc/h, h*ad+ac, bd/h-bc/h**2, cd)
    yield "D_r", family_d, [h, h-1, h+1]
    isolated = family_d.subs(h, s.I)
    isolated[:, 5] -= ab
    yield "E", isolated, []


def external_cases():
    for name, values, units in [
        ("A_h_external", {1: h-1}, [h]),
        ("A_delta", {0: 1, 1: -1, 2: h}, [h]),
        ("A0", {1: -1}, []),
        ("Ac", {0: 1, 1: -1}, []),
        ("Ad", {1: -1, 2: 1}, []),
        ("Bc1", {3: 1}, []),
        ("Bc2", {4: 1}, []),
        ("Bdtheta", {1: -2, 2: h, 8: 1}, []),
        ("Bd1", {1: -2, 6: 1}, []),
    ]:
        x = [s.sympify(values.get(i, 0)) for i in range(9)]
        mixed = s.Matrix([[x[0], x[1]+2, x[3], x[5]],
                          [x[1], x[2], x[5], x[6]],
                          [x[3], x[5], x[4], x[7]],
                          [x[5], x[6], x[7], x[8]]])
        relations = internal(mixed, (1, 0, 1, 0), 0)
        relations[:, 0] = comm(2, 3)
        relations[:, 1] = word(0, 0)+word(2, 2)+Q(1, 8)*comm(0, 1)
        yield name, relations, units


def split_internal_cases():
    a2, ab, b2 = word(0, 0), word(0, 1), word(1, 1)
    for name, entries, quadratic, units in [
        ("Z_split", [], ab, []),
        ("R1M", [(0, 0)], ab, []),
        ("R1F", [(0, 0)], a2+b2, []),
        ("LM", [(0, 1), (1, 0)], ab, []),
        ("LF", [(0, 1), (1, 0)], h*a2+b2, [h]),
        ("RF", [(0, 2), (2, 0)], a2+h*ab+b2, [h-2, h+2]),
        ("RE", [(0, 2), (2, 0)], a2+ab, []),
        ("RM", [(0, 2), (2, 0)], ab, []),
    ]:
        mixed = s.zeros(4)
        for i, j in entries:
            mixed[i, j] = 1
        relations = internal(mixed, (1, 0, 0, 0), Q(1, 8))
        relations[:, 1] = quadratic + Q(1, 8)*comm(2, 3)
        yield name, relations, units


def check_exception(name, factor, matrix, projection):
    if name in {"T0", "T1", "T2"}:
        assert factor in {h*h+Q(1, 16), h*h+Q(1, 48)}
        binary = [(2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]
    else:
        assert name == "D_r" and factor == h*h+h+1
        binary = [(2, 2, 2)]
    projected = projection.extract(range(20), [words(3).index(w) for w in binary])
    kernel = matrix.nullspace().transpose()
    assert projected.hstack(kernel).rank() == projected.rank()
    assert kernel.shape == (20, 1)
    return {"centre_contained_in": ["".join("abcd"[i] for i in w) for w in binary]}


def main():
    records = []
    for name, relations, units in [*split_cases(), *split_internal_cases(), *external_cases()]:
        records.append(all_values(name, relations, units, check_exception))
        print("PASS", name, "all parameter values", flush=True)
    Path(__file__).with_name("cubic_CY_one_segre_extensions_certificate.json").write_text(
        json.dumps(records, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
