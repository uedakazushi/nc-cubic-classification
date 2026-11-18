"""Verify absence of cubic centres on the four L-linear FDC3 branches."""
import argparse
from functools import cache
import json

import sympy as s
from flint import fmpq, fmpq_mpoly_ctx

from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_double_split_FDC import e, four_cross_both_outer, m, p, ratio
from verify_cubic_CY_one_segre_double_split_FDC_projection import (
    CONTEXT, intersection, group_cost, project, projection_groups, reversed_polynomial,
)
from verify_cubic_CY_one_segre_double_split_FDC_witness import (
    DIRECTORY, RationalFunctionField, SYMBOLS, factor_support, normalized_parameters, pull,
    rank_witness, regularity_factors,
)
from verify_cubic_CY_one_segre_double_split_TD import fraction
from verify_cubic_CY_one_segre_square_split_M_final import (
    ResidueFieldExtension, allowed_part, common_fibre, specialise,
)

P, M, L, E = SYMBOLS
X, T = s.symbols("x t")
BASE_CONTEXT = fmpq_mpoly_ctx.get(("E", "M", "P"))
N = P*M
K = (P**2-1)*(M**2-1)
LINEAR_ROOTS = {
    "product": -1/N,
    "product_plus_one": -1/(N+1),
    "product_minus_one": -1/(N-1),
    "K": (1-N)/K,
}
ORDERS = ((0, 1, 2, 3), (3, 2, 0, 1))


@cache
def input_supports():
    certificates = [
        json.loads((DIRECTORY / f"cubic_CY_one_segre_double_split_FDC_{name}_certificate.json").read_text())
        for name in ("witness", "alternate")
    ]
    return [list(map(reversed_polynomial, group))
            for record in certificates for group in record["symmetry_supports"].values()]


def polynomial(value, variables, context):
    return context.from_dict({indices: fmpq(int(c.p), int(c.q))
                              for indices, c in s.Poly(value, *variables, domain=s.QQ).terms()})


def restrict_graph(value, root):
    numerator, denominator = root.as_numer_denom()
    numerator, denominator = [polynomial(f, (E, M, P), BASE_CONTEXT) for f in (numerator, denominator)]
    degree = int(value.degrees()[1])
    coefficients = [{} for _ in range(degree+1)]
    for (i, j, k, l), coefficient in value.to_dict().items():
        coefficients[int(j)][i, k, l] = coefficient
    return sum((BASE_CONTEXT.from_dict(row)*numerator**index*denominator**(degree-index)
                for index, row in enumerate(coefficients) if row), BASE_CONTEXT.constant(0))


def local_witness(parameters, coordinates, extra_units=()):
    field = RationalFunctionField(parameters)
    values = [field.from_sympy(v) for v in (*coordinates, parameters[-1])]
    M0 = values[1]
    units = [pull(f, values, field).n for f in regularity_factors()] + [M0.n]
    units.extend(field.from_sympy(s.denom(value)).n for value in coordinates)
    units.extend(field.from_sympy(f).n for f in extra_units)
    if not all(units):
        return [], units
    groups = []
    for order in ORDERS[:1 if len(parameters) == 3 else 2]:
        denominators, pivots = rank_witness(order, parameters, dict(zip(SYMBOLS[:3], coordinates, strict=True)))
        reverse = BASE_CONTEXT if len(parameters) == 3 else fmpq_mpoly_ctx.get(("t", "x"))
        ordered = [reverse.from_dict({index[::-1]: c for index, c in f.to_dict().items()})
                   for f in denominators+pivots]
        reversed_units = [reverse.from_dict({index[::-1]: c for index, c in f.to_dict().items()})
                          for f in units]
        groups.append(factor_support(ordered, reversed_units))
        if not groups[-1]:
            break
    return groups, reversed_units


def graph_supports(root):
    local, units = local_witness((P, M, E), (P, M, root))
    supports = list(local)
    for group in input_supports():
        restricted = [restrict_graph(f, root) for f in group]
        if all(restricted):
            supports.append(factor_support(restricted, units))
    return supports, units


def projection_candidates(groups, coordinate, units):
    candidates = {}
    for fixed in min(groups, key=group_cost).values():
        common = None
        for group in sorted(groups, key=group_cost):
            if str(fixed) in group:
                continue
            projected = factor_support([project(fixed, other, coordinate) for other in group.values()], units)
            common = projected if common is None else {key: value for key, value in common.items() if key in projected}
            if not common:
                break
        if common is None:
            assert fixed.degrees()[coordinate] == 0, fixed
            common = {str(fixed): fixed}
        candidates.update(common)
    return candidates


def residues(poly):
    if poly.degree() <= 0:
        return
    if poly.degree() == 1:
        factor = poly.monic()
        yield factor, poly.domain, -factor.rep.to_list()[-1]
        return
    for factor, _ in poly.factor_list()[1]:
        factor = factor.monic()
        field = poly.domain
        if factor.degree() == 1:
            yield factor, field, -factor.rep.to_list()[-1]
        elif field == s.QQ:
            # The symbol in specialised polynomials can also occur in the ambient field.
            minimal = s.Poly(factor.as_expr(), factor.gen, domain=s.QQ)
            root = s.CRootOf(minimal, 0)
            extended = s.QQ.algebraic_field((minimal, root))
            yield factor, extended, extended.from_sympy(root)
        else:
            extended = ResidueFieldExtension(factor)
            yield factor, extended, extended.generator


@cache
def terms(poly, variables):
    return s.Poly(poly, *variables, domain=s.QQ).terms()


def evaluate(poly, field, variables, point):
    numerator, denominator = fraction(poly)

    def at(value):
        return sum((field.convert(s.QQ.convert(c), s.QQ)*s.prod(
            v**int(power) for v, power in zip(point, powers, strict=True))
                    for powers, c in terms(value, variables)), field.zero)

    return at(numerator)/at(denominator)


@cache
def source():
    return four_cross_both_outer()[0].applyfunc(s.cancel)


def original_rank(field, point):
    parameters = normalized_parameters(field, point)[:4]
    return centre_calculation(source(), (0, 1, 2, 3), field,
                              lambda value: evaluate(value, field, (p, m, ratio, e), parameters))[1]


def lift_center(groups, units, base, field, fibre_base=None):
    # The last coordinate of the parameter tuple is the unknown E.
    groups, units = [list(group.values()) for group in groups], list(units)
    if fibre_base is None:
        fibre_base = (None, base[1], base[0])
    cut = [specialise(f, field, 0, fibre_base) for f in units]
    if any(not f for f in cut):
        return []
    fibre = allowed_part(common_fibre(groups, 0, field, fibre_base), cut)
    records = []
    for factor, extension, root in residues(fibre):
        coordinates = [extension.convert(co, field) for co in base]
        assert original_rank(extension, (*coordinates, root)) == 20
        records.append(str(factor.as_expr()))
    return records


def chart_parameterization(equation):
    if s.degree(equation, M) == 1:
        numerator = equation.subs(M, 0).subs(P, X)
        denominator = equation.diff(M).subs(P, X)
        assert s.gcd(numerator, denominator) == 1
        return X, s.cancel(-numerator/denominator)
    assert s.total_degree(equation) == 2
    M0 = next(v for v in (0, 1, -2) if not equation.subs({P: 1, M: v}))
    U = s.Dummy("U")
    restricted = s.Poly(equation.subs({P: 1+U, M: M0+X*U}, simultaneous=True), U)
    assert s.gcd(restricted.nth(1), restricted.nth(2)) == 1
    distance = -restricted.nth(1)/restricted.nth(2)
    return s.cancel(1+distance), s.cancel(M0+X*distance)


def curve_rank(coordinates, extra_units=()):
    local, units = local_witness((X, T), coordinates, extra_units)
    if not local:
        return {"allowed": False}
    candidates = projection_candidates(local, 0, [u for u in units if not u.degrees()[0]])
    regularity = [reversed_polynomial(f) for f in regularity_factors()]+[CONTEXT.gen(2)]
    data = []
    for equation in sorted(candidates.values(), key=str):
        minimal = specialise(equation, s.QQ, 1, (None, None))
        for _, field, root in residues(minimal):
            try:
                point = [evaluate(f, field, (X,), (root,)) for f in coordinates]
            except ZeroDivisionError:
                continue
            regular = [specialise(f, field, 0, (None, point[2], point[1], point[0])) for f in regularity]
            regular.extend(specialise(f, field, 0, (None, root)) for f in units)
            if any(not u for u in regular):
                continue
            fibre = allowed_part(common_fibre(input_supports(), 0, field,
                                              (None, point[2], point[1], point[0])), regular)
            for group in local:
                specialised = [specialise(f, field, 0, (None, root)) for f in group.values()]
                if all(specialised):
                    fibre = fibre.gcd(s.prod(f.gcd(fibre) for f in specialised))
            for factor, extension, value in residues(fibre):
                base = [extension.convert(v, field) for v in point]
                assert original_rank(extension, (*base, value)) == 20
                data.append((str(equation), str(factor.as_expr())))
    return {"local_counts": list(map(len, local)), "base_factors": sorted(candidates), "residue_fields": data}



def off_curves(root, fixed, projected, groups, units):
    on_plane = {name: projected[0][name] for name in intersection(projected)}
    projected = [{name: f for name, f in group.items() if name not in on_plane} for group in projected]
    units = [*units, *on_plane.values()]
    p_units = [f for f in units if f.degrees()[:2] == (0, 0)]
    m_units = [f for f in units if f.degrees()[0] == 0]
    candidates = projection_candidates(projected, 1, p_units)
    points = []
    for equation in sorted(candidates.values(), key=str):
        for _, initial, P0 in residues(specialise(equation, s.QQ, 2, (None, None, None))):
            fibre = common_fibre([list(group.values()) for group in projected], 1, initial, (None, None, P0))
            fibre = allowed_part(fibre, [specialise(u, initial, 1, (None, None, P0)) for u in m_units])
            for factor, field, M0 in residues(fibre):
                p0 = field.convert(P0, initial)
                l0 = evaluate(root, field, (P, M), (p0, M0))
                for report in lift_center([*groups, {str(fixed): fixed}], units, (p0, M0, l0), field):
                    points.append((str(equation), str(factor.as_expr()), report))
    return on_plane, {"E_equation_terms": len(fixed), "P_factors": sorted(candidates),
                      "residue_fields": points}


def solve_chart(root):
    groups, units = graph_supports(root)
    assert all(not groups[0][f].degrees()[0] for f in intersection(groups))
    plane = {}
    finite = []
    for fixed in min(groups, key=group_cost).values():
        if not fixed.degrees()[0]:
            plane[str(fixed)] = fixed
            continue
        projected = projection_groups(fixed, groups, 0, [u for u in units if not u.degrees()[0]])
        on_plane, checked = off_curves(root, fixed, projected, groups, units)
        plane.update(on_plane)
        finite.append(checked)
        print("PASS finite projection", len(fixed), len(checked["P_factors"]),
              len(checked["residue_fields"]), flush=True)
    curves = {}
    for name in sorted(plane):
        equation = s.sympify(name.replace("^", "**"), locals={"P": P, "M": M})
        P0, M0 = chart_parameterization(equation)
        L0 = s.cancel(root.subs({P: P0, M: M0}, simultaneous=True))
        curves[name] = curve_rank((P0, M0, L0))
        print("PASS base curve", name, flush=True)
    return {"support_counts": list(map(len, groups)), "curves": curves, "finite": finite}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("charts", nargs="*", default=list(LINEAR_ROOTS))
    arguments = parser.parse_args()
    for name in arguments.charts:
        assert name in LINEAR_ROOTS
        data = solve_chart(LINEAR_ROOTS[name])
        (DIRECTORY / f"cubic_CY_one_segre_double_split_FDC_linear_{name}_certificate.json").write_text(
            json.dumps(data, indent=2)+"\n")
        print("PASS FDC3 L-linear chart", name, flush=True)


if __name__ == "__main__":
    main()
