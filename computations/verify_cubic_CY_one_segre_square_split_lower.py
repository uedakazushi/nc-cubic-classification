"""Centre ranks in the square-split lower charts and the last family’s boundary charts."""
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


def lower_open():
    z = s.Symbol("z")
    k = h*h/4-Q(1, 64)
    w = p
    d0 = 64*(k*w+1)
    m = ((32*k+1)*w+32)/(16*h*(k*w+1))
    n = (32*k+1)/(16*h)
    C = w*w*z-2*k*w-1
    D = w*z-k
    E = z+k*k
    B = n-m*D
    A = -m*B
    v = -m*E-2*k*k/h
    coefficients = [w*A, A, 2*k-m*v, w*B, C, B, v, D, E, h, 0, -h, 1, k, 1]
    branch_units = [
        32*z*((4*h+sign)**2*w+64)**2-(4*h+sign)**4*d0+128*(4*h+sign)**2
        for sign in (1, -1)
    ]
    return cross(coefficients, Q(1, 8), 3), [h, 4*h-1, 4*h+1, d0, w, *branch_units], z


def lower_open_wminus():
    source, units, z = lower_open()
    substitution = {p: -64/(4*h-1)**2, z: p}
    source = source.subs(substitution, simultaneous=True).applyfunc(s.cancel)
    units = numerator_and_denominator(unit.subs(substitution, simultaneous=True) for unit in units)
    exceptional_curves = [
        3*h**5/32-5*h**4/128-h**3/256+3*h**2/1024+h*p-h/8192-Q(1, 32768),
        h**5/16-h**4/64-h**3/128+h**2/512+h*p+h/4096-Q(1, 16384),
        h**5/8-5*h**4/64+h**3/64-h**2/512+h*p+h/2048-Q(1, 16384),
    ]
    curves = [(curve, {p: s.cancel(-curve.subs(p, 0)/h)}, h) for curve in exceptional_curves]
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


def validate(name, source, units, curves, permutation=PERMUTATION):
    rank, all_factors = rank_chart(source, permutation)
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


def validate_mzero():
    source, units, z = lower_open()
    substitution = {p: -64/(16*h*h+1), z: p}
    source = source.subs(substitution, simultaneous=True).applyfunc(s.cancel)
    units = numerator_and_denominator(unit.subs(substitution, simultaneous=True) for unit in units)
    forbidden = factors(units)
    rank, required = rank_chart(source, (0, 2, 1, 3))
    assert rank == 20
    linear = [
        p-h*h/64-Q(1, 1024),
        h**5/16-h**4/64-h**3/128-h**2/512+h*p-3*h/4096-Q(1, 16384),
        h**6/16-h**4/256+h*h*p-h*h/4096+Q(1, 65536),
    ]
    quadratic = (h**10/256-3*h**8/4096+h**6*p/8+h**6/32768-h**4*p/64
                 +9*h**4/524288+h*h*p*p-3*h*h*p/2048
                 +13*h*h/16777216+Q(1, 268435456))
    assert required-forbidden == factors([*linear, quadratic])
    records = []
    for curve in linear:
        root = s.solve(curve, p)[0]
        relations = source.subs(p, root).applyfunc(s.cancel)
        allowed = numerator_and_denominator(unit.subs(p, root) for unit in units)
        local_rank, local_factors = rank_chart(relations, PERMUTATION)
        assert local_rank == 20 and local_factors <= factors(allowed)
        records.append({"curve": str(s.factor(curve)), "projection_and_minor_factors": sorted(map(str, local_factors))})
        print("PASS lower_open_Mzero", s.factor(curve), flush=True)

    discriminant = s.factor(s.discriminant(quadratic, p))
    square = h*(16*h*h+1)**2/8192
    assert s.cancel(discriminant+square*square) == 0
    z_on_curve = s.cancel((-quadratic.diff(p).subs(p, 0)+s.I*square)/(2*h*h))
    assert s.cancel(quadratic.subs(p, z_on_curve)) == 0
    # The other graph follows by conjugation over QQ. Factor over QQ(i), since
    # taking norms would not record which unit is nonzero on this graph.
    relations = source.subs(p, z_on_curve).applyfunc(s.cancel)
    field = s.QQ_I.frac_field(h)
    algebra, curve_rank = centre_calculation(relations, PERMUTATION, field, field.from_sympy)
    assert curve_rank == 20
    minor = algebra.pivot_product
    all_values = [minor.numer.as_expr(), minor.denom.as_expr()]
    all_values += [c.denom.as_expr() for degree in (2, 3, 4) for row in algebra.right[degree].values()
                   for c in row.values()]

    def factors_i(values):
        return {f.monic().as_expr() for v in values for f, _ in s.Poly(v, h, domain=s.QQ_I).factor_list()[1]}

    allowed = numerator_and_denominator(unit.subs(p, z_on_curve) for unit in units)
    local_factors = factors_i(all_values)
    assert local_factors-factors_i(allowed) <= {h-Q(1, 2)+s.I/4}
    point = Q(1, 2)-s.I/4
    point_record = fixed_rank(relations.subs(h, point), s.QQ_I)
    records.append({"curve": str(quadratic), "z_on_chart": str(z_on_curve),
                    "projection_and_minor_factors": sorted(map(str, local_factors)),
                    "residual_s": str(point), "specialization": point_record})
    print("PASS lower_open_Mzero conjugate quadratic graphs", flush=True)
    return {"name": "lower_open_Mzero", "rank": rank, "required_factors": sorted(map(str, required)),
            "exceptional_curves": records}


def main():
    result = [
        validate("lower_single", *lower_single()),
        validate("lower_zero", *lower_zero()),
        validate("lower_open_Wminus", *lower_open_wminus(), permutation=(1, 0, 2, 3)),
        validate_mzero(),
    ]
    Path(__file__).with_name("cubic_CY_one_segre_square_split_lower_certificate.json").write_text(
        json.dumps(result, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
