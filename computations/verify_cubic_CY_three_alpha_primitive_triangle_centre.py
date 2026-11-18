"""Check the cubic equation of the primitive-third-root triangular centre."""
from collections import defaultdict
from functools import cache

import sympy as s
from sympy.polys.rings import ring


def main():
    root = (-1+s.sqrt(-3))/2
    field = s.QQ.algebraic_field(root)
    coefficients, ax, ay, az, bx, by, bz = ring("ax,ay,az,bx,by,bz", field)
    q = coefficients.ground_new(field.from_sympy(root))
    zero, one = coefficients.zero, coefficients.one
    rules = {
        "yx": {"xy": q*q, "z": -az*q*q, "": -bz*q*q},
        "zy": {"yz": q*q, "x": -ax*q*q, "": -bx*q*q},
        "zx": {"xz": q, "y": ay, "": by},
    }

    @cache
    def reduce(word):
        for index in range(len(word)-1):
            pair = word[index:index+2]
            if pair not in rules:
                continue
            result = defaultdict(lambda: zero)
            for replacement, coefficient in rules[pair].items():
                for normal, value in reduce(word[:index]+replacement+word[index+2:]).items():
                    result[normal] += coefficient*value
            return {normal: value for normal, value in result.items() if value}
        return {word: one}

    def multiply(left, right):
        result = defaultdict(lambda: zero)
        for a, ca in left.items():
            for b, cb in right.items():
                for normal, value in reduce(a+b).items():
                    result[normal] += ca*cb*value
        return {normal: value for normal, value in result.items() if value}

    def inverse(value):
        return coefficients.ground_new(field.one/value)

    q_number = field.from_sympy(root)
    denominator2 = inverse(q_number*q_number-field.one)
    denominator1 = inverse(q_number-field.one)
    X = {"xxx": one, "x": q*q*ay*az}
    Y = {"yyy": one, "y": q*q*az*ax}
    Z = {"zzz": one, "z": q*q*ax*ay}
    omega = {
        "xyz": one,
        "xx": ax*denominator2, "yy": ay*q*q*denominator2, "zz": az*denominator2,
        "x": bx*denominator1, "y": by*q*denominator1, "z": bz*denominator1,
    }
    first = (2*q+1)/9
    second = (q-1)/3
    right = defaultdict(lambda: zero)

    def accumulate(coefficient, element):
        for word, value in element.items():
            right[word] += coefficient*value

    accumulate(one, multiply(multiply(X, Y), Z))
    accumulate(second*ax*ay*az, multiply(omega, omega))
    omega_linear = -(q+2)*bx*by*bz/3
    constant = zero
    for a, b, c, d, f, g, central in [(ax, ay, az, bx, by, bz, X),
                                       (ay, az, ax, by, bz, bx, Y),
                                       (az, ax, ay, bz, bx, by, Z)]:
        accumulate(first*a**3, multiply(central, central))
        accumulate(a*d, multiply(omega, central))
        linear = -2*(q-1)*a*a*b*c*d/9-q*a*a*f*g/3-first*d**3
        accumulate(linear, central)
        omega_linear -= (q+1)*b*c*d*d/3
        constant += -(q+2)*a*b*b*c*c*d*d/9+(q-1)*a*f*f*g*g/9
    accumulate(omega_linear, omega)
    accumulate(constant, {"": one})

    assert multiply(multiply(omega, omega), omega) == {
        word: value for word, value in right.items() if value
    }
    print("PASS primitive-third-root centre equation in all six coefficients")


if __name__ == "__main__":
    main()
