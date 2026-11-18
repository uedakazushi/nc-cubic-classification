"""Check the central lifts and point extensions for alpha models with repeated lines."""
from collections import defaultdict
from functools import cache
from itertools import combinations

import sympy as s


def check_lift(rules, lift, leading):
    """Reduce the four commutators in the ordered-word basis."""

    @cache
    def reduce(word):
        for i, (x, y) in enumerate(zip(word, word[1:])):
            if x <= y:
                continue
            branches = [(y + x, 1), *rules.get((x, y), [])]
            terms = defaultdict(lambda: 0)
            for replacement, factor in branches:
                for ordered, coefficient in reduce(word[:i] + replacement + word[i+2:]).items():
                    terms[ordered] += factor * coefficient
            return {w: s.expand(c) for w, c in terms.items() if s.expand(c) != 0}
        return {word: 1}

    assert all(reduce(word) == {word: 1} for word, _ in lift)
    assert [(word, coefficient) for word, coefficient in lift if "a" not in word] == [(leading, 1)]
    for x in "abcd":
        coefficients = defaultdict(lambda: 0)
        for word, scalar in lift:
            for w, coefficient in reduce(x + word).items():
                coefficients[w] += scalar * coefficient
            for w, coefficient in reduce(word + x).items():
                coefficients[w] -= scalar * coefficient
        assert all(s.expand(c) == 0 for c in coefficients.values()), x


def check_tangent(rules, lift, character, pivot, monodromy):
    """Check all equations for upper triangular tails at a fixed point."""
    active = "abcd".replace(pivot, "")
    variables = dict(zip("abcd", s.symbols("za zb zc zd")))
    point = {variables[x]: character[x] for x in variables}
    polynomial = sum(coefficient * s.prod(variables[x] for x in word) for word, coefficient in lift)
    assert s.expand(polynomial.subs(point)) == 0
    assert all(s.expand(polynomial.diff(var).subs(point)) == 0 for var in variables.values())

    f = s.Matrix(s.symbols("fa fb fc"))
    f_next = s.Matrix(s.symbols("ga gb gc"))

    def tangent(word):
        x, y = word
        left = character[y] * f[active.index(x)] if x != pivot else 0
        right = character[x] * f_next[active.index(y)] if y != pivot else 0
        return left + right

    relations = []
    for x, y in [("b", "a"), ("c", "a"), ("d", "a"), *rules]:
        value = tangent(x + y) - tangent(y + x)
        value -= sum(coefficient * tangent(word) for word, coefficient in rules.get((x, y), []))
        relations.append(value)
    matrix = s.Matrix(relations).jacobian([*f, *f_next])
    assert any(matrix.extract(rows, (3, 4, 5)).det() in (-1, 1)
               for rows in combinations(range(6), 3))
    assert (matrix * f.col_join(monodromy * f)).applyfunc(s.expand) == s.zeros(6, 1)
    assert monodromy.det() == 1


def check_model(name, cb, db, dc, lift, monodromy):
    rules = {("c", "b"): cb, ("d", "b"): db, ("d", "c"): dc}
    check_lift(rules, lift, "bbb")
    check_tangent(rules, lift, dict(a=0, b=0, c=0, d=1), "d", monodromy)
    print("PASS", name, "central lift and all self-extension recurrences")


def triple_line():
    parameter = s.Symbol("E")
    identity = s.eye(3)
    case_i = identity.copy()
    case_i[1, 0] = 1
    case_ii = identity.copy()
    case_ii[2, 0] = -1
    check_model("I", [("ac", -1)], [("ad", 1)], [("bb", -3), ("aa", -parameter)],
                [("bbb", 1), ("acd", 1), ("abb", -s.Rational(3, 2)), ("aab", parameter+s.Rational(1, 2))],
                case_i)
    check_model("II", [("ab", -1)], [("ac", 2)], [("bb", -3), ("ad", -1)],
                [("bbb", 1), ("abd", 1), ("acc", 1), ("aac", 1)], case_ii)
    check_model("III", [("aa", -1)], [("ac", 2)], [("bb", -3)],
                [("bbb", 1), ("acc", 1), ("aad", 1)], identity)
    check_model("IV", [("aa", -1)], [("ab", 1)], [("bb", -3), ("ac", -1)],
                [("bbb", 1), ("abc", 1), ("aad", 1)], identity)


def double_line():
    A, B, C, D, E, F, G, r = s.symbols("A B C D E F G r")
    rules = {
        ("c", "b"): [("ab", -B), ("ac", -C), ("ad", -2*D), ("aa", -G)],
        ("d", "b"): [("bb", 1), ("ac", 2*A), ("ad", C), ("aa", F)],
        ("d", "c"): [("bc", -2), ("ab", B), ("ac", C), ("ad", 2*D-B), ("aa", G-E)],
    }
    lift = [
        ("bbc", 1), ("acc", A), ("abd", B-2*D), ("acd", C), ("add", D),
        ("abc", -2*C), ("abb", -B/2), ("aab", E+B*C/2-G),
        ("aac", F+A*B-2*A*D+C**2), ("aad", G+C*D),
    ]
    check_lift(rules, lift, "bbc")
    for substitutions, character, pivot, monodromy in [
        ({D: -A*r**2-C*r}, dict(a=0, b=0, c=r, d=1), "d",
         s.Matrix([[1, 0, 0], [2*A*r+C, 1, 0], [-B-r*(2*A*r+C), -2*r, 1]])),
        ({A: 0}, dict(a=0, b=0, c=1, d=0), "c",
         s.Matrix([[1, 0, 0], [-C, 1, 0], [-C, 2, 1]])),
    ]:
        def specialize(terms):
            return [(word, s.sympify(coefficient).subs(substitutions)) for word, coefficient in terms]

        point_rules = {pair: specialize(terms) for pair, terms in rules.items()}
        check_tangent(point_rules, specialize(lift), character, pivot, monodromy)
    print("PASS double line, all seven lower coefficients and both boundary charts")


if __name__ == "__main__":
    triple_line()
    double_line()
