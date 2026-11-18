"""Centre ranks for the square-split lower single and zero-cd charts."""
import json
from pathlib import Path

import sympy as s

from verify_cubic_CY_one_segre_cross import centre_calculation, rank_chart, h, p
from verify_cubic_CY_one_segre_shared_squares import factors
from verify_cubic_CY_one_segre_square_split import Q, cross

PERMUTATION = (0, 1, 2, 3)


def lower_single():
    w, e = p, h
    T = w*(w+32)*e-1
    coefficients = [
        w*(w+32)*T/16, (w+32)*T/16, e*(w+32)**2/16, w*T/4, w*w*e-1,
        T/4, e*(w+32)/4, w*e, e, -Q(1, 4), 0, Q(1, 4), 1, 0, 1,
    ]
    source = cross(coefficients, Q(1, 8), 3)
    units = [w, e, e*(w+16)**2-1]
    t = p
    w_e = 16*(2*t-1)/(t-1)**2
    w_f = (128-64*t)/(t*t-5)
    y = 32+t*w_f
    curves = [
        (p+32, {p: -32}, h),
        (h*p*(p+16)-1, {h: 1/(p*(p+16))}, p),
        (h*p*(p+32)-1, {h: 1/(p*(p+32))}, p),
        (h*h*p**3*(p+16)-2*h*p*(p+16)+1, {p: w_e, h: t/(w_e*(w_e+16))}, p),
        (h*h*p**3*(p+16)**2-2*h*p*(p*p+24*p+256)+p+16,
         {p: w_f, h: (w_f*w_f+24*w_f+256+8*y)/(w_f*w_f*(w_f+16)**2)}, p),
    ]
    return source, units, curves


def lower_zero():
    k = h*h/4-Q(1, 64)
    C = p*p+2*p/h
    D = -k*C-p/(16*h)
    coefficients = [1, -k, k*k, p, C, -k*p, k*k*p, D, k*k*C, h, 0, 0, 1, k, 0]
    source = cross(coefficients, Q(1, 8), 3)
    units = [h, p, 4*h-1, 4*h+1]
    b = h*h-Q(1, 16)
    u = p

    def change(x):
        a = s.cancel(u/(2*(x+2)))
        return {h: a, p: s.cancel(a*x/(a*a-Q(1, 16)))}

    curves = [
        (b*b*p**3+8*h*b*p*p+(20*h*h-Q(3, 4))*p+16*h,
         change(4*(1-u*u)/(u*u-3)), p),
        (h*b*p*p+4*b*p+4*h, change(u*u-1), p),
        (b*p+2*h, {p: -2*h/b}, h),
        ((h+Q(1, 4))*p+2, {p: -2/(h+Q(1, 4))}, h),
        (b*p*p+(4*h-Q(1, 3))*p+4, change(-2*(u*u-1)/(u*u-1-2*u/3)), p),
    ]
    return source, units, curves


def numerator_and_denominator(expressions):
    result = []
    for expr in expressions:
        result.extend(s.cancel(expr).as_numer_denom())
    return result


def fixed_rank(relations, field):
    algebra, rank = centre_calculation(relations, PERMUTATION, field, field.from_sympy)
    assert rank == 20
    return {"rank": rank, "minor": str(field.to_sympy(algebra.pivot_product))}


def specialize(relations, parameter, root, field):
    """Evaluate rational coefficients by Horner arithmetic in the number field."""
    value = field.from_sympy(root)

    def evaluate(polynomial):
        polynomial = s.Poly(polynomial, parameter, domain=s.QQ)
        result = field.zero
        for coefficient in polynomial.rep.to_list():
            result = result*value + field.convert(coefficient, s.QQ)
        return result

    def coefficient(expr):
        numerator, denominator = expr.as_numer_denom()
        return field.to_sympy(evaluate(numerator)/evaluate(denominator))

    return relations.applyfunc(coefficient)


def validate(name, source, units, curves):
    rank, all_factors = rank_chart(source, PERMUTATION)
    assert rank == 20
    expected = [s.Poly(f, p, h, domain=s.QQ).monic().as_expr() for f, _, _ in curves]
    assert all_factors-factors(units) == set(expected)
    records = []
    for curve, substitution, parameter in curves:
        assert s.cancel(curve.subs(substitution, simultaneous=True)) == 0
        R = source.subs(substitution, simultaneous=True).applyfunc(s.cancel)
        local_units = numerator_and_denominator(unit.subs(substitution, simultaneous=True)
                                               for unit in units)
        local_units += [s.cancel(expr).as_numer_denom()[1] for expr in substitution.values()]
        chart_rank, chart_factors = rank_chart(R, PERMUTATION)
        assert chart_rank == 20
        points = []
        for factor in sorted(chart_factors-factors(local_units), key=str):
            polynomial = s.Poly(factor, parameter, domain=s.QQ)
            assert polynomial.degree() in (1, 2) and polynomial.is_irreducible
            root = s.solve(factor, parameter)[0]
            assert s.Poly(s.minpoly(root, parameter), parameter).monic() == polynomial
            field = s.QQ if root.is_Rational else s.QQ.algebraic_field(root)
            specialized = specialize(R, parameter, root, field)
            record = fixed_rank(specialized, field)
            points.append({"factor": str(factor), **record})
        records.append({
            "curve": str(s.factor(curve)),
            "parameterization": {str(key): str(s.factor(expr)) for key, expr in substitution.items()},
            "projection_and_minor_factors": sorted(map(str, chart_factors)),
            "specializations": points,
        })
        print("PASS", name, s.factor(curve), flush=True)
    record = {"name": name, "rank": rank, "required_factors": sorted(map(str, all_factors)),
              "exceptional_curves": records}
    if name == "lower_zero":
        point = {h: Q(3, 8), p: -Q(48, 5)}
        assert s.cancel(curves[-1][0].subs(point)) == 0
        record["zero_x_plus_two"] = fixed_rank(source.subs(point), s.QQ)
        assert record["zero_x_plus_two"]["rank"] == 20
    return record


def main():
    result = [validate("lower_single", *lower_single()), validate("lower_zero", *lower_zero())]
    Path(__file__).with_name("cubic_CY_one_segre_square_split_lower_certificate.json").write_text(
        json.dumps(result, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
