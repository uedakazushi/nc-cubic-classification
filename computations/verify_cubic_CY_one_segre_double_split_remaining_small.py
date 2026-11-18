"""Six two-product families and the common isotropic outer relations."""
import json
from pathlib import Path

from flint import fmpq
import sympy as s

from cubic_gaussian_rational_function import CTX, F
from verify_cubic_CY_one_segre_cross import centre_calculation, h, p
from verify_cubic_CY_one_segre_double_split_isolated import marked
from verify_cubic_CY_one_segre_square import word
from verify_cubic_CY_one_segre_square_split import A, K, U, sym

Q = s.Rational
I = s.I
GAUSSIAN = s.QQ.algebraic_field(I)


class GaussianFunctions:
    zero = F(0)
    one = F(1)

    @staticmethod
    def from_sympy(value):
        def polynomial(expression):
            terms = {}
            for (i, j), coefficient in s.Poly(expression, p, h, extension=I).terms():
                for imaginary, part in enumerate(coefficient.as_real_imag()):
                    if part:
                        terms[i, imaginary, j] = fmpq(int(part.p), int(part.q))
            return CTX.from_dict(terms)

        numerator, denominator = s.cancel(value, extension=I).as_numer_denom()
        return F(polynomial(numerator), polynomial(denominator))


def polynomial_expression(value):
    return sum(Q(str(c))*p**i*I**j*h**k for (i, j, k), c in value.to_dict().items())


def factors(expressions, variables):
    return {s.Poly(factor, *variables, extension=I).monic().as_expr()
            for expression in expressions if expression != 1
            for factor, _ in s.factor_list(expression, *variables, extension=I)[1]}


def rank_factors(source, variables):
    algebra, rank = centre_calculation(source, (0, 1, 2, 3), GaussianFunctions,
                                       GaussianFunctions.from_sympy)
    assert rank == 20
    polynomials = [algebra.pivot_product.n, algebra.pivot_product.d]
    polynomials.extend(entry.d for n in (2, 3, 4) for row in algebra.right[n].values()
                       for entry in row.values())
    expressions = {polynomial_expression(value) for value in polynomials}
    expressions.update(s.cancel(value, extension=I).as_numer_denom()[1] for value in source)
    return factors(expressions, variables)


def check(name, source, variables, units, curves=()):
    support = rank_factors(source, variables)
    exceptional = support - factors(units, variables)
    substitutions = []
    subcharts = []
    if curves:
        assert exceptional == factors([equation for equation, _, _ in curves], variables), (name, exceptional)
        for equation, substitutions_on_curve, allowed in curves:
            assert s.cancel(equation.subs(substitutions_on_curve, simultaneous=True)) == 0
            target = source.subs(substitutions_on_curve, simultaneous=True).applyfunc(s.cancel)
            subcharts.append(check(str(equation), target, (h,), allowed))
    elif exceptional:
        assert variables == (h,), (name, exceptional)
        for factor in sorted(exceptional, key=str):
            polynomial = s.Poly(factor, h, extension=I)
            assert polynomial.degree() <= 2, factor
            for root in s.solve(polynomial.as_expr(), h):
                field = s.QQ.algebraic_field(I, root)
                _, special_rank = centre_calculation(source.subs(h, root), (0, 1, 2, 3),
                                                     field, field.from_sympy)
                assert special_rank == 20, (name, root)
                substitutions.append(str(root))
    print("PASS", name, "rank 20, all specializations", substitutions)
    return {
        "chart": name,
        "pivot_factor_support": sorted(map(str, support)),
        "recomputed_values": substitutions,
        "curve_recomputations": subcharts,
    }


def isotropic():
    a, b, c, d = range(4)
    sigma, A0, B0, C0 = s.symbols("sigma A B C")
    minus, plus = 4*sigma-1, 4*sigma+1
    q = plus/minus
    corrections = [
        s.Matrix([[A0, B0, 0, -sigma], [B0, C0, -sigma, 0],
                  [0, 0, 0, 0], [0, 0, 0, 0]]),
        s.Matrix([[A0, B0, A0, B0-sigma], [B0, C0, B0-sigma, C0],
                  [A0, B0, A0, B0-sigma], [B0, C0, B0-sigma, C0]]),
    ]
    for index, mixed in enumerate(corrections):
        N = s.zeros(4, 1).row_join(mixed).row_join(s.zeros(4, 1))
        source = s.Matrix.hstack(U+K*N.T*A.inv(), K[:, 0], sym(a, b)+sym(c, d)+K[:, 5]/(8*sigma))
        # b is unchanged, while e=a in the first case and e=a+b in the second.
        coordinate = s.eye(4)
        coordinate[1, 0] = -index
        source = (s.kronecker_product(coordinate, coordinate)*source).applyfunc(s.cancel)
        expected = s.Matrix.hstack(
            word(b, a)-word(a, b), word(c, a)+word(a, c), word(d, a)+word(a, d),
            word(c, b)-q*word(b, c)+8*(B0*word(a, c)+C0*word(a, d))/minus,
            word(d, b)-word(b, d)/q+8*(A0*word(a, c)+B0*word(a, d))/plus,
            word(d, c)+q*word(c, d)+8*sigma*(word(a, b)-index*word(b, b))/minus,
        )
        pivot = [4*j+i for j in range(4) for i in range(j)]
        solve = expected.extract(pivot, range(6)).inv()*source.extract(pivot, range(6))
        assert (expected*solve-source).applyfunc(s.cancel) == s.zeros(16, 6)
        determinant = s.factor(solve.det())
        assert determinant == (4*sigma-1)**2*(4*sigma+1)/(128*sigma)
        print("PASS isotropic presentation", index, determinant)


def main():
    k = -h*h+I*h/4
    dd = marked({0: 1/h, 2: 1, 4: Q(1, 16), 5: h, 8: -k*k/h,
                 9: h, 10: 1, 13: k, 14: -h}, 0)
    sigma = I/8
    q, y = 2*sigma+64*h, sigma+64*h
    en = marked({**dict(enumerate([64*y, 64*q, 64*q, 64*h, h, y, q, h, y/64])),
                 9: sigma, 10: 1, 13: Q(1, 64), 14: sigma}, Q(1, 8))
    da = marked({0: 4+16*p*p*h, 1: p+4-16*p*p*h, 2: 4+16*p*p*h, 3: 4*p*h,
                 4: h, 5: Q(1, 4)-4*p*h, 6: 4*p*h, 7: -h, 8: h,
                 9: Q(1, 4), 10: 1, 11: 1}, Q(1, 8))
    t = Q(1, 4)-p
    k = p*t
    q = Q(1, 4)+k*h
    eb = marked({**dict(enumerate([1/p+h, q, k*q, h, h, p+k*h, k*q, k*h, k*(p+k*h)])),
                 9: p, 10: 1, 13: k, 14: t}, Q(1, 8))
    tn = marked({0: h, 1: -64*sigma, 2: -64*sigma, 3: -sigma, 4: -sigma/64,
                 9: sigma, 10: 1, 11: 1, 12: Q(1, 64), 14: -sigma}, Q(1, 8))
    fz = marked({**dict(enumerate([4096*p,4096*h,4096*p,64*h,p,64*p,64*h,h,p])),
                 10: 1, 11: 1, 12: Q(1, 64), 13: Q(1, 64)}, Q(1, 8))
    constant = Q(1, 262144)
    first = (constant/h-h)/4
    second = (constant/h-h)/2
    curves = [
        (p-h+Q(1, 512), {p: h-Q(1, 512)}, []),
        (p-h-Q(1, 512), {p: h+Q(1, 512)}, []),
        ((p-h)*(p+3*h)-constant, {h: first, p: first+h}, [h]),
        ((p-h)*(p+h)-constant, {h: second, p: second+h}, [h]),
    ]
    results = [
        check("DD1", dd, (h,), [h, h-I/4]),
        check("EN2", en, (h,), []),
        check("DA1", da, (p, h), [p, h]),
        check("EB2", eb, (p, h), [p, t, h, q]),
        check("TN1", tn, (h,), []),
        check("FZ1", fz, (p, h), [p-h], curves),
    ]
    isotropic()
    Path(__file__).with_name("cubic_CY_one_segre_double_split_small_certificate.json").write_text(
        json.dumps(results, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
