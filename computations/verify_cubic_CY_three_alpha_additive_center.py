"""Central cubic pencils, point obstructions and weight filtrations in three alpha types."""
from collections import defaultdict
from itertools import combinations_with_replacement

import sympy as s

from verify_cubic_CY_three_alpha_repeated_lines import check_lift, check_tangent, ordered_reducer

A, B, C, D, E, F = s.symbols("A B C D E F")
Q = s.Rational


def check_boundary_center(rules, order):
    boundary_rules = {pair: [(word, coeff) for word, coeff in terms if "a" not in word]
                      for pair, terms in rules.items()}
    reduce = ordered_reducer(boundary_rules, order)
    for degree, expected in ((1, 0), (2, 0), (3, 1)):
        basis = ["".join(word) for word in combinations_with_replacement(order[1:], degree)]
        output = defaultdict(lambda: [0]*len(basis))
        for index, word in enumerate(basis):
            for variable in order[1:]:
                for term, coeff in reduce(variable+word).items():
                    output[variable, term][index] += coeff
                for term, coeff in reduce(word+variable).items():
                    output[variable, term][index] -= coeff
        assert len(basis)-s.Matrix(list(output.values())).rank() == expected


def check(name, rules, lift, leading, order, weights, leading_weight, leading_symbol):
    check_lift(rules, lift, leading, order)
    check_boundary_center(rules, order)
    weight = dict(zip("abcd", weights))
    word_weight = lambda word: sum(weight[letter] for letter in word)
    for (x, y), terms in rules.items():
        assert all(word_weight(word) < weight[x]+weight[y] for word, _ in terms)
    assert all(word_weight(word) <= leading_weight for word, _ in lift)
    assert [(word, coeff) for word, coeff in lift if word_weight(word) == leading_weight] == leading_symbol
    print("PASS", name, "central pencil, boundary centre, and weight filtration")


def check_boundary_curve(order, leading, point_matrix, equation, charts):
    b, c, d, t = s.symbols("b c d t")
    variables = (b, c, d)
    assert s.expand(point_matrix.det()-equation) == 0
    degree_two = list(combinations_with_replacement(order[1:], 2))
    pair_coordinates = []
    for point_at in charts:
        p, q, r = [point_at(t+shift) for shift in range(3)]
        assert point_matrix.subs(dict(zip(variables, p)), simultaneous=True).multiply(s.Matrix(q)).applyfunc(s.expand) == s.zeros(3, 1)
        triples = [dict(zip("bcd", coords)) for coords in (p, q, r)]
        assert s.expand(sum(coeff*s.prod(coordinates[letter] for coordinates, letter in zip(triples, word))
                            for word, coeff in leading)) == 0
        products = [s.Poly(triples[0][x]*triples[1][y], t) for x, y in degree_two]
        pair_coordinates.extend([poly.nth(i) for poly in products]
                                for i in range(1+max(poly.degree() for poly in products if poly)))
    assert s.Matrix(pair_coordinates).rank() == 6


def check_axis_symbols(rules, lift, a_weight, brackets, initial_cut):
    weights = {"a": a_weight, "b": 1, "c": 1, "d": 0}
    weight = lambda word: sum(weights[letter] for letter in word)
    for (x, y), terms in rules.items():
        least = weights[x]+weights[y]
        assert all(weight(word) >= least for word, _ in terms)
        assert [(word, value) for word, value in terms if weight(word) == least] == brackets.get(x+y, [])
    least = min(weight(word) for word, _ in initial_cut)
    assert all(weight(word) >= least for word, _ in lift)
    assert [(word, value) for word, value in lift if weight(word) == least] == initial_cut


def check_singular_axis(rules, lift, shift):
    def specialize(terms):
        return [(word, s.sympify(coefficient).subs(C, 0)) for word, coefficient in terms]

    check_tangent({pair: specialize(terms) for pair, terms in rules.items()},
                  specialize(lift), dict(a=0, b=0, c=0, d=1), "d", shift)


def cusp():
    rules = {
        ("b", "c"): [("cc", 1), ("ab", B), ("ad", 2*C), ("aa", F)],
        ("d", "c"): [("bb", -3), ("ac", -A), ("ad", -B), ("aa", -D)],
        ("d", "b"): [("cd", 2), ("bb", -3), ("ab", A), ("ac", -A), ("ad", -B), ("aa", E-D)],
    }
    leading = [("ccd", 1), ("cbb", -3), ("bbb", 1)]
    lift = [
        ("aac", -A*B/2+3*A*C-D+E),
        ("aab", A*B-3*A*C-B**2/2+D-2*F),
        ("aad", A*C+3*B*C+F),
        ("acc", -A/2), ("acb", A), ("acd", -6*C), ("abb", -5*B/2+12*C),
        ("abd", B-6*C), ("add", C),
        *leading,
    ]
    check("cusp", rules, lift, leading, "acbd", (0, 4, 3, 6), 12,
          [("add", C), ("ccd", 1), ("bbb", 1)])
    check_singular_axis(rules, lift, s.Matrix([[1, 0, 0], [-B, 1, 2], [-B, 0, 1]]))
    b, c, d = s.symbols("b c d")
    point_matrix = s.Matrix([[-c, b-c, 0], [-3*b, -d, c], [d, -d, -b-c]])
    check_boundary_curve("acbd", leading, point_matrix, -3*(b**3-b*c**2+c**2*d),
                         [lambda t: (-t, 1, -t+t**3)])
    check_axis_symbols(rules, lift, 2, {"bc": [("cc", 1), ("ad", 2*C)], "db": [("cd", 2)]},
                       [("add", C), ("ccd", 1)])


def tangent():
    rules = {
        ("c", "b"): [("bb", -1), ("ab", -A), ("ac", -B), ("ad", -2*C), ("aa", -F)],
        ("d", "b"): [("bc", 2), ("bb", -1), ("ab", -A), ("ac", -B), ("ad", B-2*C), ("aa", E-F)],
        ("d", "c"): [("bd", -2), ("bc", -2), ("bb", 1), ("cc", -1),
                     ("ab", A), ("ac", B), ("ad", -A-B+2*C), ("aa", F-D)],
    }
    leading = [("bbb", -Q(1, 3)), ("bbc", 1), ("bbd", 1), ("bcc", 1)]
    lift = [
        ("aab", A*B/2-A*C-B**2/6+D-F),
        ("aac", -A*B/2+B**2/2-B*C+E-F),
        ("aad", A*C+2*B*C-2*C**2+F),
        ("abb", -A/2+B/2-2*C/3), ("abc", -2*B+2*C), ("abd", A),
        ("acc", -3*B/2+2*C), ("acd", B-2*C), ("add", C),
        *leading,
    ]
    check("tangent", rules, lift, leading, "abcd", (0, 2, 3, 4), 8,
          [("add", C), ("bbd", 1), ("bcc", 1)])
    check_singular_axis(rules, lift, s.Matrix([[1, 0, 0], [B, 1, 0], [-A-B, -2, 1]]))
    b, c, d = s.symbols("b c d")
    point_matrix = s.Matrix([[-b-c, b, 0], [d-c, -b, -b], [-d, -d-c, c-b]])
    check_boundary_curve("abcd", leading, point_matrix, -b*(b**2-3*b*d-3*c**2),
                         [lambda t: (0, 1, t), lambda t: (1, t, Q(1, 3)-t**2)])
    check_axis_symbols(rules, lift, 2, {"cb": [("bb", -1), ("ad", -2*C)], "dc": [("bd", -2)]},
                       [("add", C), ("bbd", 1)])


def concurrent():
    rules = {
        ("c", "b"): [("ad", -2)],
        ("d", "b"): [("bb", 1), ("bc", -2), ("ad", 2), ("ab", -A), ("ac", 2*A), ("aa", F)],
        ("d", "c"): [("bc", -2), ("cc", 1), ("ad", 2), ("ab", -2*A), ("ac", A), ("aa", -E)],
    }
    leading = [("bbc", 1), ("bcc", -1)]
    lift = [
        ("aab", E-2*A), ("aac", F), ("aad", A+2),
        ("abb", A), ("abc", -A-2), ("abd", -2), ("acc", A+2), ("acd", 2), ("add", 1),
        *leading,
    ]
    check("concurrent", rules, lift, leading, "abcd", (0, 2, 2, 3), 6, [("add", 1), *leading])
    b, c, d = s.symbols("b c d")
    point_matrix = s.Matrix([[-c, b, 0], [d-b+c, b, -b], [-c, -d-b+c, c]])
    check_boundary_curve("abcd", leading, point_matrix, 3*b*c*(b-c),
                         [lambda t: (0, 1, -t), lambda t: (1, 0, -t), lambda t: (1, 1, t)])
    check_axis_symbols(rules, lift, 3, {}, [("add", 1), *leading])


if __name__ == "__main__":
    cusp()
    tangent()
    concurrent()
