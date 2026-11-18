"""Recover the six E6 fundamental orbit sums from the normalized nodal cuts."""
from collections import defaultdict
from functools import cache
from itertools import product
import json
from pathlib import Path

from flint import fmpq, fmpq_poly
import sympy as s

DIRECTORY = Path(__file__).parent
F1, F2, G1, LAMBDA, E1, E2, Q, U, V = s.symbols("f1 f2 g1 l e1 e2 Q u v")
TRACE_VARIABLES = (F1, F2, U, V, E1, E2)
WEIGHTS = ((1, 0), (0, 1), (-1, -1))
ZERO_PAIR = (0, 0)
ZERO_WEIGHT = ZERO_PAIR*3
T = fmpq_poly([0, 1])


def subtract(left, right):
    return tuple(a-b for a, b in zip(left, right, strict=True))


BETA = subtract(WEIGHTS[0], WEIGHTS[1])
GAMMA = subtract(WEIGHTS[1], WEIGHTS[2])
SIMPLE_ROOTS = (
    (-1, 0)*3,
    BETA+ZERO_PAIR*2, GAMMA+ZERO_PAIR*2,
    ZERO_PAIR+BETA+ZERO_PAIR, ZERO_PAIR+GAMMA+ZERO_PAIR,
    ZERO_PAIR*2+BETA,
)


def pairing_times_three(left, right):
    return sum(2*left[i]*right[i]+2*left[i+1]*right[i+1]
               -left[i]*right[i+1]-left[i+1]*right[i] for i in (0, 2, 4))


def reflect(weight, root):
    times_three = pairing_times_three(weight, root)
    assert times_three % 3 == 0
    return subtract(weight, tuple((times_three//3)*v for v in root))


def dominant_coordinates(weight):
    coordinates = tuple(pairing_times_three(weight, root) for root in SIMPLE_ROOTS)
    if any(value < 0 for value in coordinates):
        return None
    assert all(value % 3 == 0 for value in coordinates)
    return tuple(value//3 for value in coordinates)


def multiply(left, right):
    result = defaultdict(fmpq_poly)
    for weight, coefficient in left.items():
        for other, value in right.items():
            target = tuple(a+b for a, b in zip(weight, other, strict=True))
            result[target] += coefficient*value
    return {weight: coefficient for weight, coefficient in result.items() if coefficient}


@cache
def trace_power(axis, orientation, exponent_t, power):
    if not power:
        return {ZERO_WEIGHT: fmpq_poly([1])}
    trace = {ZERO_PAIR*axis+tuple(orientation*co for co in weight)+ZERO_PAIR*(2-axis):
             T**exponent_t for weight in WEIGHTS}
    return multiply(trace, trace_power(axis, orientation, exponent_t, power-1))


def normalized_trace_coefficients():
    data = json.loads((DIRECTORY / "cubic_CY_three_alpha_nodal_E6_certificate.json").read_text())
    names = {str(v): v for v in (F1, F2, G1, LAMBDA, E1, E2, Q)}
    coefficients = {
        label: s.sympify(record["numerator"].replace("^", "**"), locals=names)/
               s.sympify(record["denominator"].replace("^", "**"), locals=names)
        for label, record in data["coefficients"].items()
    }
    az = coefficients["A_z"]
    scales = {"A_x": 1/az, "A_y": LAMBDA**2/az, "B_x": LAMBDA/az**2,
              "B_y": LAMBDA**2/az**2, "B_z": LAMBDA/az**2, "D": LAMBDA**2/az**3}
    field = s.QQ.frac_field(*TRACE_VARIABLES, Q)
    character = s.Poly(Q**2*LAMBDA**3-Q*U*LAMBDA**2+V*LAMBDA-1, LAMBDA, domain=field).monic()
    for name, scale in scales.items():
        expression = s.cancel((scale*coefficients[name]).subs(G1, U+(1-Q)*LAMBDA))
        numerator, denominator = [s.Poly(v, LAMBDA, domain=field) for v in expression.as_numer_denom()]
        reduced = (numerator.rem(character)*denominator.invert(character)).rem(character)
        assert reduced.degree() == 0
        yield name, s.factor(reduced.as_expr())


def orbit_expansion(expression):
    numerator, denominator = expression.as_numer_denom()
    result = defaultdict(fmpq_poly)
    polynomial = s.Poly(numerator, *TRACE_VARIABLES, Q, domain=s.QQ)
    # At Q=T^3 the three determinant-one traces and their dual traces
    # occur in the order f1, f2, u/T, v/T^2, e1/T^2, e2/T.
    traces = ((0, 1, 0), (0, -1, 0), (1, 1, 1), (1, -1, 2), (2, 1, 2), (2, -1, 1))
    for powers, coefficient in polynomial.terms():
        terms = {ZERO_WEIGHT: fmpq(int(coefficient.p), int(coefficient.q))*T**(3*powers[-1])}
        for trace, power in zip(traces, powers[:-1], strict=True):
            terms = multiply(terms, trace_power(*trace, power))
        for weight, value in terms.items():
            result[weight] += value
    return {weight: value for weight, value in result.items() if value}, denominator


def dominant_terms(values):
    return {dominant_coordinates(weight): value for weight, value in values.items()
            if dominant_coordinates(weight) is not None}


def unit_coefficient(index):
    return tuple(int(i == index) for i in range(6))


def check_roots():
    orbit = {SIMPLE_ROOTS[0]}
    pending = [SIMPLE_ROOTS[0]]
    for weight in pending:
        for root in SIMPLE_ROOTS:
            moved = reflect(weight, root)
            if moved not in orbit:
                orbit.add(moved)
                pending.append(moved)
    internal = {ZERO_PAIR*i+subtract(a, b)+ZERO_PAIR*(2-i)
                for i in range(3) for a, b in product(WEIGHTS, repeat=2) if a != b}
    mixed = {tuple(sign*co for co in a+b+c)
             for a, b, c in product(WEIGHTS, repeat=3) for sign in (1, -1)}
    assert orbit == internal | mixed and len(orbit) == 72


def check_geometric_action(values_by_name, specifications):
    c = Q**3-1
    scales = {"A_x": (1, 4, c**2), "A_y": (1, 2, c**2), "B_x": (-1, 5, c**3),
              "B_y": (-1, 4, c**3), "B_z": (1, 3, c**2), "D": (1, 6, c**4)}
    generators = s.symbols("m1:7")
    m1, m2, m3, m4, m5, m6 = generators
    orbit_labels = {unit_coefficient(i): value for i, value in enumerate(generators)}
    orbit_labels[ZERO_WEIGHT] = 1
    orbit_labels[(0,0,1,0,1,0)] = m3*m5-6*m6-27
    coordinates = {}
    for name, values in values_by_name.items():
        sign, shift, normalizing_denominator = scales[name]
        previous_denominator = specifications[name][2]
        terms = []
        for weight, coefficient in dominant_terms(values).items():
            polynomial = 0
            for index, value in enumerate(coefficient.coeffs()):
                if value:
                    assert (index+shift) % 3 == 0
                    polynomial += s.Rational(int(value.p), int(value.q))*Q**((index+shift)//3)
            terms.append(polynomial*orbit_labels[weight])
        coordinates[name] = sign*sum(terms)/(normalizing_denominator*previous_denominator)
    ax, ay, bx, by, bz, cut = coordinates.values()
    reciprocal = {Q: 1/Q, m2: m4, m4: m2, m3: m5, m5: m3}
    targets = [Q**2*ay, Q**2*ax, Q**4*by, Q**4*bx, -Q**3*bz, -Q**6*(cut-bz/c)]
    assert all(s.cancel(value.subs(reciprocal, simultaneous=True)-target) == 0
               for value, target in zip(coordinates.values(), targets, strict=True))
    for left, right in (("A_x", "A_y"), ("B_x", "B_y"), ("B_z", "B_z"), ("D", "D")):
        left_weights = {tuple(-v for v in weight) for weight in values_by_name[left]
                        if weight != ZERO_WEIGHT}
        assert left_weights == set(values_by_name[right])-{ZERO_WEIGHT}
    found = {}
    for name, weights in values_by_name.items():
        exponents = {sum(weight[2:4])-sum(weight[4:6]) for weight in weights}
        exponents = {value % 3 for value in exponents}
        assert len(exponents) == 1
        found[name], = exponents
    assert tuple(found.values()) == (2, 1, 1, 2, 0, 0)
    print("PASS central multiplication and inversion in every q fibre", flush=True)
    return {name: str(s.factor(value)) for name, value in coordinates.items()}


def main():
    cartan = s.Matrix([[pairing_times_three(a, b)//3 for a in SIMPLE_ROOTS] for b in SIMPLE_ROOTS])
    assert cartan.det() == 3
    assert [list(cartan.row(i)).count(-1) for i in range(6)] == [3, 2, 1, 2, 1, 1]
    check_roots()
    d = (Q-1)*(Q+1)**2
    specs = {
        "A_x": (3, T**2, 1, set()),
        "A_y": (5, T**4, 1, set()),
        "B_x": (2, -T**7, d, {unit_coefficient(4)}),
        "B_y": (4, -T**8, d, {unit_coefficient(2)}),
        "B_z": (6, -T**6, d, {ZERO_WEIGHT}),
        "D": (1, T**15, Q*(Q-1)**3*(Q+1)**3,
              {ZERO_WEIGHT, unit_coefficient(5), (0, 0, 1, 0, 1, 0)}),
    }
    values_by_name, table = {}, {}
    for name, expression in normalized_trace_coefficients():
        values, denominator = orbit_expansion(expression)
        assert all(values[reflect(weight, root)] == value for weight, value in values.items()
                   for root in SIMPLE_ROOTS)
        dominant = dominant_terms(values)
        index, coefficient, expected_denominator, lower = specs[name]
        assert s.cancel(denominator-expected_denominator) == 0
        assert dominant[unit_coefficient(index-1)] == coefficient
        assert set(dominant) == {unit_coefficient(index-1), *lower}
        table[name] = {"numerator_dominant_coefficients": {str(k): str(v) for k, v in sorted(dominant.items())},
                       "denominator": str(denominator)}
        values_by_name[name] = values
        print("PASS invariant orbit expansion", name, len(values), flush=True)
    product = dominant_terms(multiply(values_by_name["A_x"], values_by_name["A_y"]))
    assert product == {ZERO_WEIGHT: 27*T**6, unit_coefficient(5): 6*T**6,
                       (0, 0, 1, 0, 1, 0): T**6}
    coordinates = check_geometric_action(values_by_name, specs)
    (DIRECTORY / "cubic_CY_three_alpha_nodal_E6_surjective_certificate.json").write_text(
        json.dumps({"cartan": [list(map(int, row)) for row in cartan.tolist()],
                    "root_counts": {"internal": 18, "mixed": 54}, "orbit_coefficients": table,
                    "normalized_q_coordinates": coordinates},
                   indent=2)+"\n")
    print("PASS triangular generators of the E6 torus invariant ring", flush=True)


if __name__ == "__main__":
    main()
