"""Recognize the explicit E6 spherical algebras as nodal affine cubic cuts."""
from functools import cache
import json
from pathlib import Path

import sympy as s

from cubic_flint_rational_function import RationalFunctionField

PARAMETERS = s.symbols("f1 f2 g1 l e1 e2 Q")
FIELD = RationalFunctionField(PARAMETERS)
ZERO, ONE = FIELD.zero, FIELD.one
DIRECTORY = Path(__file__).parent


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for word, coefficient in polynomial.items():
            value = result.get(word, ZERO)+coefficient
            if value:
                result[word] = value
            else:
                result.pop(word, None)
    return result


def scale(polynomial, scalar):
    return {word: coefficient*scalar for word, coefficient in polynomial.items()
            if scalar and coefficient}


def tensor(left, right):
    return add(*({a+b: u*v} for a, u in left.items() for b, v in right.items()))


def coordinates(basis, target):
    pivots = {}
    for index, column in enumerate(basis):
        combination = {index: ONE}
        for word, (pivot, expression) in pivots.items():
            if word in column:
                coefficient = column[word]
                column = add(column, scale(pivot, -coefficient))
                combination = add(combination, scale(expression, -coefficient))
        assert column
        word = max(column, key=lambda value: (len(value), value))
        inverse = ONE/column[word]
        pivots[word] = (scale(column, inverse), scale(combination, inverse))
    result = {}
    for word, (pivot, expression) in pivots.items():
        if word in target:
            coefficient = target[word]
            target = add(target, scale(pivot, -coefficient))
            result = add(result, scale(expression, coefficient))
    assert not target
    return result


def nodal_coefficients():
    f1, f2, g1, eigenvalue, e1, e2, q = map(FIELD.from_sympy, PARAMETERS)
    g2 = g1*eigenvalue-eigenvalue*eigenvalue+ONE/eigenvalue
    b_inverse = {"bb": ONE, "b": -f1, "": f2}
    c_inverse = {"cc": ONE, "c": -g1, "": g2}
    inverse_product = tensor(b_inverse, c_inverse)
    inverse_product.pop("bbcc")
    # Etingof–Oblomkov–Rains, Section 8.1, with Q the cube of their q.
    rewriting = {
        "bbb": {"bb": f1, "b": -f2, "": ONE},
        "ccc": {"cc": g1, "c": -g2, "": ONE},
        "bcbc": add({"bc": e2, "": -e1}, scale(tensor(c_inverse, b_inverse), q)),
        "bbcc": add({"cbcb": ONE/q, "cb": -e2/q, "": e1/q}, scale(inverse_product, -ONE)),
    }

    @cache
    def normal(word):
        for lead, relation in rewriting.items():
            position = word.find(lead)
            if position >= 0:
                prefix, suffix = word[:position], word[position+len(lead):]
                return add(*(scale(normal(prefix+part+suffix), coefficient)
                             for part, coefficient in relation.items()))
        return {word: ONE}

    def multiply(left, right):
        return add(*(scale(normal(a+b), u*v)
                     for a, u in left.items() for b, v in right.items()))

    def word(*factors):
        value = {"": ONE}
        for factor in factors:
            value = multiply(value, factor)
        return value

    def braid(left, right):
        return add(multiply(left, right), scale(multiply(right, left), -q))

    derivative = (ONE+ONE+ONE)*eigenvalue*eigenvalue-(ONE+ONE)*g1*eigenvalue+g2
    unit = scale({"cc": ONE, "c": eigenvalue-g1, "": ONE/eigenvalue}, ONE/derivative)
    assert not add(multiply(unit, unit), scale(unit, -ONE))
    x0 = word(unit, {"b": ONE}, unit)
    y0 = word(unit, b_inverse, unit)
    raw_z = word(unit, b_inverse, {"cb": ONE}, unit)
    z0 = add(raw_z, scale(x0, -f2*eigenvalue), scale(y0, -e2))

    xy = coordinates((unit, x0, y0, z0), braid(x0, y0))
    x_shift = -xy[2]/(ONE-q)
    y_shift = -xy[1]/(ONE-q)
    x = add(x0, scale(unit, x_shift))
    y = add(y0, scale(unit, y_shift))
    zx = coordinates((unit, x, y, z0, multiply(y, y)), braid(z0, x))
    yz = coordinates((unit, x, y, z0, multiply(x, x)), braid(y, z0))
    assert not zx.get(3, ZERO) and not yz.get(3, ZERO)
    assert not (zx[1]-yz[2])
    z_shift = -zx[1]/(ONE-q)
    z = add(z0, scale(unit, z_shift))
    bz, az = (coordinates((unit, z), braid(x, y)).get(i, ZERO) for i in range(2))
    by, ay, py = (coordinates((unit, y, multiply(y, y)), braid(z, x)).get(i, ZERO)
                  for i in range(3))
    bx, ax, px = (coordinates((unit, x, multiply(x, x)), braid(y, z)).get(i, ZERO)
                  for i in range(3))
    h, cubic = q*q-ONE, q*q*q-ONE
    assert not (px+eigenvalue*cubic/q)
    assert not (py+cubic/(eigenvalue*eigenvalue))
    assert not (az+eigenvalue*h/(q*derivative))
    print("PASS normalized nodal relations and all translation coefficients", flush=True)

    omega = add(word(x, y, z), scale(add(
        scale(multiply(x, x), ax), scale(multiply(y, y), q*q*ay),
        scale(multiply(z, z), az)), ONE/h),
        scale(add(scale(x, bx), scale(y, q*by), scale(z, bz)), ONE/(q-ONE)))
    volume = add(scale(omega, cubic), scale(word(x, x, x), px),
                 scale(word(y, y, y), q*q*q*py), scale(multiply(x, y), -az*px*py),
                 scale(add(scale(x, -q*ay*az*px), scale(y, -q*ax*az*py),
                           scale(z, az*az*px*py)), ONE/(q+ONE)))
    cut = -coordinates((unit,), volume).get(0, ZERO)/cubic
    coefficients = dict(zip(("P_x", "P_y", "A_z", "A_x", "A_y", "B_x", "B_y", "B_z", "D"),
                            (px, py, az, ax, ay, bx, by, bz, cut), strict=True))
    allowed = eigenvalue*eigenvalue*q*h*cubic*derivative
    for value in (*coefficients.values(), x_shift, y_shift, z_shift):
        denominator = value.d
        while not (common := denominator.gcd(allowed.n)).is_constant():
            denominator //= common
        assert denominator.is_constant()
    print("PASS central nodal cubic maps to a scalar on the whole simple-root chart", flush=True)
    return coefficients


def expression(value):
    symbols = {str(generator): generator for generator in PARAMETERS}
    return (s.sympify(str(value.n).replace("^", "**"), locals=symbols)
            /s.sympify(str(value.d).replace("^", "**"), locals=symbols))


def check_dominance(coefficients):
    q = PARAMETERS[-1]
    baseline = dict.fromkeys(PARAMETERS[:-1], 0)
    baseline[PARAMETERS[3]] = 1
    scaling_weights = ((-2, 1, 1), (1, -2, 1), (1, 1, -1), (-1, 1, 1), (1, -1, 1),
                       (0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1))
    jacobian, point = [], {}
    for (name, value), weights in zip(coefficients.items(), scaling_weights, strict=True):
        formula = expression(value)
        ordinary_value = s.factor(formula.subs(baseline))
        point[name] = str(ordinary_value)
        jacobian.append([s.cancel(s.diff(formula, symbol).subs(baseline)) for symbol in PARAMETERS[:-1]]
                        +[exponent*ordinary_value for exponent in weights])
    determinant = s.factor(s.Matrix(jacobian).det(method="domain-ge"))
    expected = (q-1)**17*(q+1)**6*(q*q+q+1)**3/(59049*q**8)
    assert s.cancel(determinant-expected) == 0
    print("PASS nonzero Jacobian for every allowed q", flush=True)
    return point, str(determinant)


def main():
    coefficients = nodal_coefficients()
    point, determinant = check_dominance(coefficients)
    certificate = {
        "coefficients": {key: {"numerator": str(value.n), "denominator": str(value.d)}
                         for key, value in coefficients.items()},
        "group_algebra_point": point,
        "scaled_jacobian": determinant,
    }
    (DIRECTORY / "cubic_CY_three_alpha_nodal_E6_certificate.json").write_text(
        json.dumps(certificate, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
