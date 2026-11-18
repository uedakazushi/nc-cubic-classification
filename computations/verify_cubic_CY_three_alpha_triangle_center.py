"""Central-cubic identities for triangular, nodal, and secant leading forms."""
from collections import defaultdict
from functools import cache

import sympy as s


def verify(with_cubes):
    q = s.Symbol("q", nonzero=True)
    ax, ay, az, bx, by, bz = s.symbols("ax ay az bx by bz")
    px, py = s.symbols("px py") if with_cubes else (0, 0)
    rules = {
        ("y", "x"): [("xy", 1/q), ("z", -az/q), ("", -bz/q)],
        ("z", "y"): [("yz", 1/q), ("x", -ax/q), ("", -bx/q)],
        ("z", "x"): [("xz", q), ("y", ay), ("", by)],
    }

    if with_cubes:
        rules["z", "y"].append(("xx", -px/q))
        rules["z", "x"].append(("yy", py))

    @cache
    def reduce(word):
        for i, pair in enumerate(zip(word, word[1:])):
            if pair not in rules:
                continue
            result = defaultdict(lambda: 0)
            for replacement, coefficient in rules[pair]:
                for ordered, value in reduce(word[:i]+replacement+word[i+2:]).items():
                    result[ordered] += coefficient*value
            return {word: value for word, raw in result.items() if (value := s.cancel(raw))}
        return {word: 1}

    def commutator(generator, element):
        coefficients = defaultdict(lambda: 0)
        for word, scalar in element.items():
            for ordered, value in reduce(generator+word).items():
                coefficients[ordered] += scalar*value
            for ordered, value in reduce(word+generator).items():
                coefficients[ordered] -= scalar*value
        return [s.cancel(coefficient) for coefficient in coefficients.values()]

    omega = {
        "xyz": 1, "xx": ax/(q*q-1), "yy": q*q*ay/(q*q-1), "zz": az/(q*q-1),
        "x": bx/(q-1), "y": q*by/(q-1), "z": bz/(q-1),
    }
    if with_cubes:
        omega = {word: (q**3-1)*coefficient for word, coefficient in omega.items()}
        omega.update({"xxx": px, "yyy": q**3*py, "xy": -az*px*py})
        omega["x"] -= q*ay*az*px/(q+1)
        omega["y"] -= q*ax*az*py/(q+1)
        omega["z"] += az**2*px*py/(q+1)
    for generator in "xyz":
        assert all(coefficient == 0 for coefficient in commutator(generator, omega))
    if with_cubes:
        print("PASS scaled volume, including both specializations at a primitive cube root")
        return

    root_polynomial = q*q+q+1
    for element in ({"xxx": 1, "x": q*q*ay*az},
                    {"yyy": 1, "y": q*q*ax*az},
                    {"zzz": 1, "z": q*q*ax*ay}):
        for generator in "xyz":
            for coefficient in commutator(generator, element):
                numerator, denominator = coefficient.as_numer_denom()
                assert s.rem(numerator, root_polynomial, q) == 0
                assert s.gcd(denominator, root_polynomial) == 1
    print("PASS central volume and all three pure-cube lifts in six coefficients")


if __name__ == "__main__":
    verify(False)
    verify(True)
