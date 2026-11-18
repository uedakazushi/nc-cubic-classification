"""Exclude FDC3 cubic centres on m=0, including every exceptional fibre."""
import argparse
import json
from pathlib import Path

from flint import fmpq_mpoly
import sympy as s

from cubic_flint_rational_function import RationalFunctionField, VARIABLES
from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_double_split_FDC import e, fdc_coefficients, four_cross_both_outer, m, p, ratio
from verify_cubic_CY_one_segre_double_split_FDC_witness import CONTEXT as FDC_CONTEXT
from verify_cubic_CY_one_segre_double_split_FDC_witness import (
    coefficient_symmetry, normalized_parameters, regularity_factors, scalar,
)
from verify_cubic_CY_one_segre_double_split_quadratics import centre_witness, quadratic_quotient
from verify_cubic_CY_one_segre_square_split_M_final import (
    ResidueFieldExtension, allowed_part, centre_rank, common_fibre, specialise,
)
from verify_cubic_CY_one_segre_square_split_M_simple import (
    CONTEXT, check_fibre, expression, factors, polynomial, projected_factors, t, x, z,
)
from verify_cubic_CY_one_segre_square_split_M_witness import rank_witness
from verify_cubic_CY_one_segre_double_split_TD import fraction

DIRECTORY = Path(__file__).parent
PREFIX = "cubic_CY_one_segre_double_split_FDC_mzero"
P, W, E = x, t, z
ORDER = (0, 1, 2, 3)
DIMENSIONS = (10, 20, 35)
QUAD_DIMENSIONS = (9, 16, 25)
K = P*P-1
UNITS = (P, W, E, K)
ISOMORPHISMS = ({}, {P: -P}, {W: -1/(K*W), E: 1-E},
                {P: -P, W: -1/(K*W), E: 1-E})
CHARTS = (
    ("E1", {E: 1}, (P, W)),
    ("dplus", {W: 1/(P+1)}, (P, E)),
    ("dminus", {W: -1/(P+1)}, (P, E)),
    ("circle", {P: (1-x*x)/(1+x*x), W: (1+x*x)/(2*x)}, (x, E)),
    ("hyperbola", {P: (1+x*x)/(1-x*x), W: (1-x*x)/(2*x)}, (x, E)),
    ("affine", {E: (1-K*W)/(1+K*W*W)}, (P, W)),
    ("PW1", {W: 1/P}, (P, E)),
    ("W2P", {P: 1-1/W**2}, (W, E)),
    ("Eminus", {E: (W*P*P+W-1)/(K*W*W+2*W-1)}, (P, W)),
    ("Eplus", {E: (-K*W-1)/(K*W*W+2*W-1)}, (P, W)),
)


def input_polynomials(certificate):
    return {key for label, group in certificate.items() if label.endswith("_factors") for key in group}


def strip_units(poly, unit):
    assert poly
    while not (common := poly.gcd(unit)).is_constant():
        poly //= common
    return poly


def support(values, unit):
    result = {}
    for value in values:
        result.update(factors(strip_units(value, unit)))
    return result


def restrict_fdc(value):
    return CONTEXT.from_dict({(E, L, P): co*2**int(E)
                              for (P, M, L, E), co in value.to_dict().items() if M == 0})


def product_of(values):
    result = CONTEXT.constant(1)
    for value in values:
        result *= value
    return result


def check_isomorphisms():
    field = RationalFunctionField((P, W, E))
    parameter = tuple(map(field.from_sympy, (P, W, E)))

    def state(values):
        P, W, E = values
        p, m, ratio, e, s0, t0, h, k = normalized_parameters(
            field, (P, field.zero, W, scalar(field, 2)*E)
        )
        coefficients, _, _, _ = fdc_coefficients(
            p, m, ratio, e, lambda numerator, denominator=1: scalar(field, numerator, denominator)
        )
        return s0, t0, h, k, coefficients[:9]

    source = state(parameter)
    for action, word in ((ISOMORPHISMS[1], "SQP"), (ISOMORPHISMS[2], "S")):
        moved = source
        for generator in word:
            moved = coefficient_symmetry(moved, generator)
        expected = state(tuple(field.from_sympy(value.subs(action, simultaneous=True)) for value in (P, W, E)))
        assert all(not (a-b) for a, b in zip(moved[:4], expected[:4], strict=True))
        assert all(not (a-b) for a, b in zip(moved[-1], expected[-1], strict=True))
    print("PASS m=0 sign involution and block exchange", flush=True)


def global_supports():
    units = support([restrict_fdc(value) for value in regularity_factors()], CONTEXT.constant(1))
    unit = product_of(units.values())
    certificate = json.loads((DIRECTORY / f"{PREFIX}_input.json").read_text())
    p0, u0, w0 = VARIABLES
    coordinate = {p0: P/4, u0: E/(256*P), w0: P*W/4}
    first = [fraction(s.sympify(f.replace("^", "**")).subs(coordinate, simultaneous=True))[0]
             for f in sorted(input_polynomials(certificate))]
    old = []
    for action in ISOMORPHISMS:
        values = [polynomial(fraction(f.subs(action, simultaneous=True))[0]) for f in first]
        old.append(support(values, unit))
    shared = set.intersection(*(set(group) for group in old))
    assert len(shared) == 7
    strong = []
    later = json.loads((DIRECTORY / "cubic_CY_one_segre_double_split_FDC_witness_certificate.json").read_text())
    for group in later["symmetry_supports"].values():
        images = [restrict_fdc(fmpq_mpoly(value, FDC_CONTEXT)) for value in group]
        if all(images):
            strong.append(support(images, unit))
    assert len(strong) == 4
    off_units = [*units.values(), polynomial(E-1), *(old[0][key] for key in sorted(shared))]
    off = [support(group.values(), product_of(off_units)) for group in old+strong]
    assert [len(group) for group in off] == [10, 10, 10, 10, 5, 5, 5, 5]
    return list(units.values()), old, strong, sorted(shared), off_units, off


def chart_polynomial(value, substitution, variables):
    expr = value.subs(substitution, simultaneous=True)
    rename = dict(zip(variables, (x, t), strict=True))
    return fraction(expr.subs(rename, simultaneous=True))[0]


def chart_relations(source, substitution, variables):
    return source.subs(substitution, simultaneous=True).subs(
        dict(zip(variables, (x, t), strict=True)), simultaneous=True
    ).applyfunc(s.cancel)


def local_supports(source, quad, name, substitution, variables, units, global_groups):
    real = chart_relations(source, substitution, variables)
    quotient = chart_relations(quad, substitution, variables)
    local_units = [chart_polynomial(expression(value), substitution, variables) for value in units]
    local_units += [s.denom(value).subs(dict(zip(variables, (x, t), strict=True)), simultaneous=True)
                    for value in substitution.values()]
    unit = polynomial(s.prod(local_units))
    assert unit
    field = RationalFunctionField((x, t))
    witnesses = [centre_witness(real, (2, 1, 3, 0), DIMENSIONS, field)]
    if name in {c[0] for c in CHARTS[:6]}:
        witnesses = [
            centre_witness(quotient, ORDER, QUAD_DIMENSIONS, field),
            centre_witness(quotient[:, [6, 5, 3, 2, 0, 4, 1]], (3, 2, 0, 1), QUAD_DIMENSIONS, field),
            *witnesses,
        ]
    groups = [support([polynomial(expression(f)) for f in sorted(input_polynomials(cert))], unit)
              for cert in witnesses]
    for group in global_groups:
        images = [chart_polynomial(expression(value), substitution, variables) for value in group.values()]
        if all(images):
            groups.append(support([polynomial(value) for value in images], unit))
    return real, local_units, groups


def check_curve(source, formula, units):
    f = expression(formula)
    if s.degree(f, t) == 1:
        change = {t: s.cancel(-f.subs(t, 0)/f.diff(t))}
    else:
        assert s.expand(f-t*t*(x*x+1)+s.Rational(1, 2)) == 0
        change = {x: (x*x-4*x+2)/(x*x-2), t: -(x*x-2)/(2*(x*x-2*x+2))}
    assert s.cancel(f.subs(change, simultaneous=True)) == 0
    allowed = [fraction(unit.subs(change, simultaneous=True))[0] for unit in units]
    allowed.extend(s.denom(value) for value in change.values())
    assert all(allowed)
    sample = source.subs(change, simultaneous=True).applyfunc(s.cancel)
    witness = centre_witness(sample, ORDER, DIMENSIONS, RationalFunctionField((x,)))
    invertible = polynomial(s.prod(allowed))
    residual = support([polynomial(expression(factor)) for factor in input_polynomials(witness)], invertible)
    for q in sorted(residual):
        assert check_fibre(sample, [[t]], t, expression(q), allowed) == [1]
    return {"equation": formula, "exceptional_base_factors": sorted(residual)}


def check_chart(source, quad, chart, units, global_groups):
    name, substitution, variables = chart
    real, allowed, groups = local_supports(source, quad, name, substitution, variables, units, global_groups)
    common = set.intersection(*(set(group) for group in groups))
    projected_groups = [{key: poly for key, poly in groups[0].items() if key not in common}, *groups[1:]]
    base_units = polynomial(s.prod(unit for unit in allowed if not unit.has(t)))
    projection = projected_factors(projected_groups, t, base_units)
    original = [[expression(value) for value in group.values()] for group in groups]
    curves = [check_curve(real, f, allowed) for f in sorted(common)]
    fibres = {f: check_fibre(real, original, t, expression(f), allowed) for f in sorted(projection)}
    print("PASS", name, len(curves), "curves", sum(map(len, fibres.values())), "residue fields", flush=True)
    return {"curves": curves, "residue_fields": fibres}


def elimination_groups(first, groups, coordinate, units):
    results = []
    for group in groups:
        if str(first) in group:
            continue
        polynomials = []
        for other in group.values():
            if first.degrees()[coordinate] == 0:
                polynomials.append(first)
            elif other.degrees()[coordinate] == 0:
                polynomials.append(other)
            else:
                polynomials.append(first.resultant(other, coordinate))
        results.append(support(polynomials, units))
    assert results
    return results


def check_last_branch(groups, units):
    first_group = groups[4]
    assert len(first_group) == 5
    expected = [
        W*P-1, W*W*P-W*W+1,
        E*(K*W*W+2*W-1)-W*(P*P+1)+1,
        E*(K*W*W+2*W-1)+W*K+1,
    ]
    expected = {str(value/value.leading_coefficient()) for value in map(polynomial, expected)}
    remaining = set(first_group)-expected
    assert len(remaining) == 1 and expected <= set(first_group)
    equation, = remaining
    base_units = product_of(value for value in units if value.degrees()[0] == 0)
    projected = elimination_groups(first_group[equation], groups, 0, base_units)
    assert not set.intersection(*(set(group) for group in projected))
    x_units = product_of(value for value in units if value.degrees()[:2] == (0, 0))
    residues = set()
    for factor in min(projected, key=lambda group: sum(map(len, group.values()))).values():
        x_groups = elimination_groups(factor, projected, 1, x_units)
        residues.update(set.intersection(*(set(group) for group in x_groups)))
    assert not residues
    print("PASS last branch, no candidate projection point", flush=True)
    return {"equation": equation, "projected_factor_counts": list(map(len, projected)), "base_factors": []}


def regenerate_source():
    p0, u0, w0 = VARIABLES
    matrix = quadratic_quotient(four_cross_both_outer()).subs(
        {m: 0, ratio: w0, e: u0}, simultaneous=True).applyfunc(s.cancel)
    raw = rank_witness(matrix)
    (DIRECTORY / f"{PREFIX}_input.json").write_text(json.dumps(raw, indent=2)+"\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regenerate-source", action="store_true")
    if parser.parse_args().regenerate_source:
        regenerate_source()
    check_isomorphisms()
    regular_units, old, strong, common, off_units, off = global_supports()
    source_data = four_cross_both_outer()
    norm = {p: P/4, m: 0, ratio: P*W/4, e: E/(256*P)}
    source = source_data[0].subs(norm, simultaneous=True).applyfunc(s.cancel)
    quad = quadratic_quotient(source_data).subs(norm, simultaneous=True).applyfunc(s.cancel)
    assert s.cancel((1+K*W*W).subs(W, 1/K)-P*P/K) == 0
    assert s.cancel((K*W*W+2*W-1).subs(W, 1/(P*P+1))+P*P*K/(P*P+1)**2) == 0
    assert s.cancel((K*W*W+2*W-1).subs(W, -1/K)+P*P/K) == 0
    results = {}
    for number, chart in enumerate(CHARTS):
        if number == 0:
            units, supports = regular_units, old[:2]+strong
        elif number < 6:
            units, supports = regular_units+[polynomial(E-1)], old+strong
        else:
            units, supports = off_units, off
        results[chart[0]] = check_chart(source, quad, chart, units, supports)
    proof = {"global_common_factors": common, "charts": results,
             "last_branch": check_last_branch(off, off_units)}
    (DIRECTORY / f"{PREFIX}_certificate.json").write_text(json.dumps(proof, indent=2)+"\n")


if __name__ == "__main__":
    main()
