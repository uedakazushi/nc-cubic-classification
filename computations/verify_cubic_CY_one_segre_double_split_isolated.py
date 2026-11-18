"""All five isolated two-product envelopes have no domain central cubic cut."""
import sympy as s

from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_square import word
from verify_cubic_CY_one_segre_square_split import A, C, J, K, U, sym

a, b, c, d = range(4)
Q = s.Rational


def marked(coefficients, volume, linear_columns=False):
    """Use the six independent relation columns of (DE1) and (DA2)."""
    x = [s.sympify(coefficients.get(i, 0)) for i in range(15)]
    mixed = s.Matrix([
        [x[10], x[0], x[1], x[3], x[14]+x[5]-x[9], -x[10]],
        [x[11], x[1], x[2], x[5]-x[9], x[6], x[11]],
        [-x[12], x[3], x[14]+x[5], x[4], x[7], -x[12]],
        [-x[13], x[5], x[6], x[7], x[8], x[13]],
    ])
    skew = s.Matrix(x[9:])
    index = next(i for i, coefficient in enumerate(skew) if coefficient == 1)
    binary = sym(a, b)+sym(c, d)
    if linear_columns:
        return s.Matrix.hstack(U*A+K*mixed.T, K*skew,
                               binary+U*mixed[:, index]+K*(C+volume*J)[:, index])
    difference = C+volume*J-mixed.T*A.inv()*mixed
    return s.Matrix.hstack(U+K*mixed.T*A.inv(), K*skew,
                           binary+K*difference[:, index])


def exceptional_cubes(algebra, field):
    gamma = s.I*s.sqrt(3)
    omega = (-1+gamma)/2
    ell = {a: field.one, d: field.from_sympy(gamma/18)}
    m = {b: field.one, c: field.from_sympy(-6*gamma)}

    mixed = {}
    for i, u in ell.items():
        for j, v in m.items():
            algebra.addto(mixed, algebra.word((j, i)), u*v)
            algebra.addto(mixed, algebra.word((i, j)), -field.from_sympy(omega**2)*u*v)
    assert not mixed

    def cube(form):
        value = {}
        for i, u in form.items():
            for j, v in form.items():
                for k, w in form.items():
                    algebra.addto(value, algebra.word((i, j, k)), u*v*w)
        for gen in range(4):
            difference = {}
            for i, u in form.items():
                for j, v in form.items():
                    for k, w in form.items():
                        algebra.addto(difference, algebra.word((gen, i, j, k)), u*v*w)
                        algebra.addto(difference, algebra.word((i, j, k, gen)), -u*v*w)
            assert not difference
        return value

    left, right = cube(ell), cube(m)
    assert len(algebra.echelon([left, right])) == 2


def main():
    external = s.Matrix.hstack(
        word(d, a)-s.I*word(a, d), word(b, a)+word(d, c),
        word(c, a)-word(d, b)/4, word(b, d)+4*word(a, c),
        word(c, d)+word(a, b), word(c, b)+s.I*word(b, c),
    )
    single = s.Matrix.hstack(
        word(c, a)+s.I*word(a, c), word(b, a)-4*word(a, c)+word(c, d),
        word(d, a)+word(c, b)/4, word(b, c)-4*word(a, d),
        word(d, c)+word(a, b)-4*s.I*word(a, c), word(d, b)-s.I*word(b, d),
    )
    gaussian = s.QQ.algebraic_field(s.I)
    gamma = s.I*s.sqrt(3)
    eta = gamma/18
    different_volume = marked(
        {0: -108*eta, 5: -eta/2, 8: eta/108, 9: eta, 10: 1, 13: Q(1, 108), 14: 2*eta},
        Q(1, 12),
    )
    eighth_volume = {0: 8*s.I, 5: s.I/8, 8: s.I/512, 9: s.I/8,
                     10: 1, 13: Q(1, 64), 14: s.I/8}
    cases = [
        ("DE2", external, gaussian, 20),
        ("DC1", single, gaussian, 20),
        ("EN3-0", marked(eighth_volume, Q(1, 8)), gaussian, 20),
        ("EN3-1", marked({**eighth_volume, 4: 1}, Q(1, 8)), gaussian, 20),
        ("DX1", different_volume, s.QQ.algebraic_field(gamma), 18),
    ]
    for name, relations, field, expected_rank in cases:
        algebra, rank = centre_calculation(relations, (0, 1, 2, 3), field, field.from_sympy)
        assert rank == expected_rank
        if name == "DX1":
            exceptional_cubes(algebra, field)
        print("PASS", name, "central commutator rank", rank)


if __name__ == "__main__":
    main()
