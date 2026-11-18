"""Decide fullness of a simple-root E6 spherical idempotent by finite rank."""
from functools import cache
from itertools import product

import sympy as s

from cubic_sparse_hilbert import SparseGradedAlgebra

LEADING_WORDS = ("bbb", "cc", "bcbc", "cbcb", "bbcbbc", "cbbcbb")
NORMAL_WORDS = tuple("".join(letters) for size in range(9)
                     for letters in product("bc", repeat=size)
                     if not any(lead in "".join(letters) for lead in LEADING_WORDS))
assert len(NORMAL_WORDS) == 17


def quotient_dimension(field, f1, f2, g1, eigenvalue, e1, e2, q):
    """Return dim(H/HeH), for coefficients already converted into the field."""
    zero, one = field.zero, field.one

    def add(*polynomials):
        result = {}
        for polynomial in polynomials:
            for key, coefficient in polynomial.items():
                value = result.get(key, zero)+coefficient
                if value:
                    result[key] = value
                else:
                    result.pop(key, None)
        return result

    def scale(poly, coefficient):
        return {key: value*coefficient for key, value in poly.items() if value and coefficient}

    def tensor(left, right):
        return add(*({a+b: x*y} for a, x in left.items() for b, y in right.items()))

    kappa = g1-eigenvalue
    b_inverse = {"bb": one, "b": -f1, "": f2}
    c_inverse = {"c": -eigenvalue, "": eigenvalue*kappa}
    bc_inverse = tensor(c_inverse, b_inverse)
    cb_inverse = tensor(b_inverse, c_inverse)
    inverse_squares = {}
    for leading, inverse, direct in (("bbcbbc", cb_inverse, "cb"),
                                     ("cbbcbb", bc_inverse, "bc")):
        square = tensor(inverse, inverse)
        coefficient = square.pop(leading)
        inverse_squares[leading] = scale(add(scale(inverse,e1/q),
                                             {"": -e2/q, direct: one/q},
                                             scale(square, -one)), one/coefficient)
    rules = {
        "bbb": {"bb": f1, "b": -f2, "": one},
        "cc": {"c": kappa, "": -one/eigenvalue},
        "bcbc": add({"bc": e2, "": -e1}, scale(bc_inverse, q)),
        "cbcb": add({"cb": e2, "": -e1}, scale(cb_inverse, q)),
        **inverse_squares,
    }
    assert all(len(tail) < len(lead) for lead, relation in rules.items()
               for tail, coefficient in relation.items()
               if coefficient)

    @cache
    def rewrite(word):
        for lead, relation in rules.items():
            place = word.find(lead)
            if place >= 0:
                prefix, suffix = word[:place], word[place+len(lead):]
                return add(*(scale(rewrite(prefix+tail+suffix), coefficient)
                             for tail, coefficient in relation.items() if coefficient))
        return {word: one}

    positions = {word: index for index, word in enumerate(NORMAL_WORDS)}
    multiplication = {
        generator: [{positions[term]: coefficient for term, coefficient in rewrite(generator+word).items()}
                    for word in NORMAL_WORDS]
        for generator in "bc"
    }
    identity = [{index: one} for index in range(len(NORMAL_WORDS))]

    def act(matrix, vector):
        return add(*(scale(matrix[index], coefficient) for index, coefficient in vector.items()))

    def compose(left, right):
        return [act(left, column) for column in right]

    b, c = multiplication["b"], multiplication["c"]
    b2, c2, bc = compose(b, b), compose(c, c), compose(b, c)
    bc2 = compose(bc, bc)
    defects = [
        add(v3, scale(v2, -f1), scale(v1, f2), scale(unit, -one))
        for v3, v2, v1, unit in zip(compose(b, b2), b2, b, identity, strict=True)
    ]
    defects += [
        add(v2, scale(v1, -kappa), scale(unit, one/eigenvalue))
        for v2, v1, unit in zip(c2, c, identity, strict=True)
    ]
    defects += [
        add(v3, scale(v2, -e2), scale(v1, e1), scale(unit, -q))
        for v3, v2, v1, unit in zip(compose(bc, bc2), bc2, bc, identity, strict=True)
    ]

    engine = SparseGradedAlgebra(field, len(NORMAL_WORDS), [], [0]*len(NORMAL_WORDS))
    span = engine.echelon(defects)
    while len(span) < len(NORMAL_WORDS):
        generated = [act(matrix, vector) for matrix in (b,c) for vector in span.values()]
        extended = engine.echelon(list(span.values())+generated)
        if len(extended) == len(span):
            break
        span = extended
    return len(NORMAL_WORDS)-len(span)


def main():
    field = s.QQ

    def values(b, c, bc, root):
        b, c, bc = ([field.convert(x) for x in roots] for roots in (b,c,bc))
        return (sum(b), b[0]*b[1]+b[1]*b[2]+b[0]*b[2], sum(c), field.convert(root),
                bc[0]*bc[1]+bc[1]*bc[2]+bc[0]*bc[2], sum(bc), bc[0]*bc[1]*bc[2])

    baseline = tuple(map(field.convert, (0,0,0,1,0,0,2)))
    assert quotient_dimension(field, *baseline) == 0
    nonfull = values((1,2,s.Rational(1,2)), (1,3,s.Rational(1,3)), (6,1,s.Rational(1,3)), 1)
    dimension = quotient_dimension(field, *nonfull)
    assert dimension > 0
    print("PASS zero and nonzero 17-word idempotent quotients", dimension)


if __name__ == "__main__":
    main()
