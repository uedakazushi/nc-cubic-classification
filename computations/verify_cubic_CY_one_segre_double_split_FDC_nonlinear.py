"""Check every remaining FDC3 point on the L-quadratic and E-affine branches."""
import argparse
from functools import cache
import json

from flint import fmpq, fmpq_mpoly_ctx, fmpq_poly, nmod_poly
import sympy as s

from verify_cubic_CY_one_segre_double_split_FDC_linear import (
    K, L as SYMBOL_L, M as SYMBOL_M, N, P as SYMBOL_P, X,
    chart_parameterization, curve_rank, input_supports, original_rank, projection_candidates,
    residues as standard_residues,
)
from verify_cubic_CY_one_segre_double_split_FDC_projection import (
    CONTEXT, DIRECTORY, M, P, affine_base_groups, affine_branches, chart_data,
    factor_support, intersection, project, quadratic_branches,
)
from verify_cubic_CY_one_segre_square_split_M_final import VARIABLE_ORDER, specialise

CURVE_CONTEXT = fmpq_mpoly_ctx.get(("L", "r"))
L, R = CURVE_CONTEXT.gens()
ONE, ZERO = CURVE_CONTEXT.constant(1), CURVE_CONTEXT.constant(0)
DIFFERENCE = -R**2-1
PRODUCT = ONE+R*DIFFERENCE
R_SYMBOL = s.Symbol("r")
NUMBER_FIELD_GENERATOR = s.Symbol("a")


def residues(poly):
    if poly.domain != s.QQ or poly.degree() <= 1:
        yield from standard_residues(poly)
        return
    for factor, _ in poly.factor_list()[1]:
        yield residue_from_irreducible(factor)


def residue_from_irreducible(factor):
    factor = factor.monic()
    if factor.degree() == 1:
        return factor, s.QQ, -factor.rep.to_list()[-1]
    # A formal residue field is sufficient and avoids complex root isolation.
    field = s.QQ.algebraic_field((factor, NUMBER_FIELD_GENERATOR))
    return factor, field, field.unit


def special_fibre(groups, coordinate, field, values, units):
    specialize = fibre_specializer(field, coordinate, values)
    exclusions = [specialize(unit) for unit in units]
    if any(not unit for unit in exclusions):
        return []
    specialised = [[specialize(f) for f in group] for group in groups]
    return fibre_residues(specialised, exclusions)


def fibre_specializer(field, coordinate, values):
    if not field.is_AlgebraicField:
        return lambda f: specialise(f, field, coordinate, values)
    minimal = fmpq_poly(list(reversed(field.mod.to_list())))
    constants = [None if value is None else fmpq_poly(list(reversed(value.to_list()))) for value in values]

    @cache
    def powers(axis, degree):
        return (constants[axis]**degree) % minimal

    @cache
    def monomial(exponents):
        term = fmpq_poly([1])
        for axis, exponent in enumerate(exponents):
            if axis != coordinate and exponent:
                term = term*powers(axis, exponent) % minimal
        return term

    def specialize(polynomial):
        coefficients = [fmpq_poly() for _ in range(int(polynomial.degrees()[coordinate])+1)]
        for indices, coefficient in polynomial.to_dict().items():
            degree = int(indices[coordinate])
            fixed = tuple(int(i) if j != coordinate else 0 for j, i in enumerate(indices))
            coefficients[degree] += coefficient*monomial(fixed)
        return s.Poly.from_list([field.new(list(reversed(co.coeffs()))) for co in reversed(coefficients)],
                                VARIABLE_ORDER[coordinate], domain=field)

    return specialize


def lift_scalar(value, source, target):
    return value if target == source else target.convert(value, source)


def field_gcd(left, right):
    # Use monic Euclidean remainders. Fraction-free subresultants introduce
    # huge algebraic coefficients in the degree-38 residue calculations.
    while right:
        if right.degree() == 0:
            return s.Poly(1, left.gen, domain=left.domain)
        right = right.monic()
        left, right = right, left.rem(right)
    return left.monic()


def fibre_residues(groups, units):
    usable = [group for group in groups if all(group)]
    assert usable
    usable.sort(key=lambda group: sum(f.degree() for f in group))
    seen = set()
    for polynomial in usable[0]:
        common = polynomial.monic()
        for unit in units:
            while (divisor := field_gcd(common, unit)).degree() > 0:
                common = common.exquo(divisor)
        for group in usable[1:]:
            if common.degree() == 0:
                break
            product = s.Poly(1, common.gen, domain=common.domain)
            for other in group:
                product = (product*field_gcd(other, common)).rem(common)
                if not product:
                    break
            common = field_gcd(common, product)
        for factor, field, value in residues(common):
            if factor not in seen:
                seen.add(factor)
                yield factor, field, value


def finite_projection(groups, coordinate, units):
    # These resultants are univariate. Intersect products by GCD before
    # factoring, since the first pair can give large extraneous factors.
    ordered = sorted(groups, key=lambda group: sum(map(len, group.values())))
    candidates = {}
    for fixed in ordered[0].values():
        common = None
        for group in ordered:
            if str(fixed) in group:
                continue
            image = fixed.context().constant(1)
            for other in group.values():
                resultant = project(fixed, other, coordinate)
                assert resultant
                if common is None:
                    image *= resultant
                else:
                    image = (image*common.gcd(resultant)) % common
                    if not image:
                        break
            common = image if common is None else common.gcd(image)
            if common.is_constant():
                break
        assert common is not None
        candidates.update(factor_support([common], units))
    return candidates


def off_curves(projected, units):
    common = intersection(projected)
    curve_units = [projected[0][name] for name in sorted(common)]
    reduced = [{name: f for name, f in group.items() if name not in common} for group in projected]
    p_units = [u for u in units if u.degrees()[:3] == (0, 0, 0)]
    candidates = finite_projection(reduced, 2, p_units)
    return reduced, [*units, *curve_units], candidates


def dense_m_coefficients(poly, minimal):
    coefficients = [{} for _ in range(int(poly.degrees()[2])+1)]
    for (i, j, k, l), coefficient in poly.to_dict().items():
        assert not (i or j)
        coefficients[int(k)][int(l)] = coefficient
    return [fmpq_poly([terms.get(i, 0) for i in range(max(terms, default=-1)+1)]) % minimal
            for terms in coefficients]


def reduce_modulo_prime(poly, prime):
    denominator = int(poly.denom()) % prime
    if not denominator:
        raise ZeroDivisionError("coefficient denominator vanishes")
    inverse = pow(denominator, -1, prime)
    return nmod_poly([(int(value) % prime)*inverse for value in poly.numer().coeffs()], prime)


def modular_degree_bound(minimal, dense_groups):
    # A simple root of the P polynomial embeds its number field into Q_p.
    # One group with leading units makes every common M integral there.
    # Its monic common divisor has integral coefficients, so retains its
    # degree and divides every group product after reduction.
    for prime in (101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
                  151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199):
        try:
            reduced = reduce_modulo_prime(minimal, prime)
            roots = [root for root, mult in reduced.roots() if mult == 1]
            if not roots:
                continue
            coefficients = [[[reduce_modulo_prime(p, prime) for p in row] for row in group]
                            for group in dense_groups]
        except ZeroDivisionError:
            continue
        for root in roots:
            fibres = [[nmod_poly([int(c(root)) for c in row], prime) for row in group]
                      for group in coefficients]
            integral = any(all(image and image.degree() == max(
                (i for i, coefficient in enumerate(row) if coefficient), default=-1)
                              for row, image in zip(group, fibre, strict=True))
                           for group, fibre in zip(dense_groups, fibres, strict=True))
            if not integral:
                continue
            common = nmod_poly([], prime)
            for fibre in fibres:
                if all(fibre):
                    common = common.gcd(s.prod(fibre))
                    if common.degree() == 0:
                        return 0, prime, int(root)
            if common and common.degree() <= 1:
                return common.degree(), prime, int(root)
    return None


def evaluate_dense(coefficients, value, minimal):
    result = fmpq_poly()
    for coefficient in reversed(coefficients):
        result = result*value % minimal+coefficient
    return result


@cache
def seed_roots():
    certificate = DIRECTORY / "cubic_CY_one_segre_double_split_FDC_affine_M_input.json"
    return json.loads(certificate.read_text())


def certified_m_root(label, field, minimal, dense, units):
    seed = seed_roots().get(label)
    bound = modular_degree_bound(minimal, dense) if seed is not None else None
    if bound is None:
        return None
    degree, prime, root = bound
    if degree == 0:
        print("empty M fibre by integral reduction", minimal.degree(), prime, root, flush=True)
        return []
    value = fmpq_poly([fmpq(c) for c in seed]) % minimal
    assert all(any(not evaluate_dense(f, value, minimal) for f in group) for group in dense), label
    if any(not evaluate_dense(f, value, minimal) for f in units):
        return []
    exact = field.new(list(reversed(value.coeffs())))
    factor = s.Poly.from_list([field.one, -exact], SYMBOL_M, domain=field)
    print("unique M fibre by degree bound and exact root", minimal.degree(), prime, root, flush=True)
    return [(factor, field, exact)]


def plane_points(projected, units, candidates, use_seeds=False):
    m_units = [f for f in units if f.degrees()[:2] == (0, 0)]
    groups = [list(group.values()) for group in projected]
    for label in sorted(candidates):
        polynomial = s.Poly(label.replace("^", "**"), SYMBOL_P, domain=s.QQ)
        _, field, p0 = residue_from_irreducible(polynomial)
        print("M fibre over P of degree", polynomial.degree(), flush=True)
        if field == s.QQ:
            fibres = special_fibre(groups, 2, field, (None, None, None, p0), m_units)
        else:
            minimal = fmpq_poly(list(reversed(field.mod.to_list())))
            dense = [[dense_m_coefficients(f, minimal) for f in group] for group in groups]
            dense_units = [dense_m_coefficients(f, minimal) for f in m_units]
            fibres = certified_m_root(label, field, minimal, dense, dense_units) if use_seeds else None
            if fibres is None:
                fibres = lift_m(field, dense, dense_units)
        for mf, extension, m0 in fibres:
            yield (label, str(mf.as_expr())), extension, lift_scalar(p0, field, extension), m0


def lift_m(field, dense_groups, dense_units):
    def polynomial(row):
        coefficients = [field.new(list(reversed(entry.coeffs()))) for entry in reversed(row)]
        return s.Poly.from_list(coefficients, SYMBOL_M, domain=field)

    units = [polynomial(row) for row in dense_units]
    if not all(units):
        return []
    groups = [[polynomial(row) for row in group] for group in dense_groups]
    return fibre_residues(groups, units)


def lift_points(plane, l_groups, e_groups, units):
    l_units = [u for u in units if not u.degrees()[0]]
    results = []
    for labels, base, p0, m0 in plane:
        for lf, extension, l0 in special_fibre(l_groups, 1, base, (None,None,m0,p0), l_units):
            p1, m1 = [lift_scalar(v, base, extension) for v in (p0, m0)]
            for ef, field, e0 in special_fibre(e_groups, 0, extension, (None,l0,m1,p1), units):
                coordinates = [lift_scalar(v, extension, field) for v in (p1, m1, l0)]+[e0]
                assert original_rank(field, coordinates) == 20
                results.append((*labels, str(lf.as_expr()), str(ef.as_expr())))
    return results


def lift_off_curves(projected, l_groups, e_groups, units, use_seeds=False):
    reduced, units, candidates = off_curves(projected, units)
    print("possible P factors", len(candidates), flush=True)
    checked = lift_points(plane_points(reduced, units, candidates, use_seeds), l_groups, e_groups, units)
    print("PASS finite base projection", len(candidates), len(checked), flush=True)
    return {"P_factors": sorted(candidates), "residue_fields": checked}


def quadratic_curves():
    for shift in (-1, 1):
        product = X*(X+shift)
        yield f"shift {shift}, first root", (X, X+shift, -(product+1)/product**2)
        yield f"shift {shift}, second root", (X, X+shift, -1/(product-2))
    yield "product -1", (X, -1/X, 1-2/((X**2-1)*(X**-2-1)))
    p0, m0 = chart_parameterization(SYMBOL_M**2+4*SYMBOL_M*SYMBOL_P+SYMBOL_P**2+3)
    product = s.cancel(p0*m0)
    yield "conic, first root", (p0, m0, -1/(product+2))
    yield "conic, second root", (p0, m0, -(product+1)/(product*(product+2)))


def solve_quadratic(quadratic, witnesses, units, base_units, plane_units):
    finite = []
    for fixed, projected in quadratic_branches(quadratic, witnesses, base_units, plane_units):
        l_groups = [[quadratic]] if fixed.degrees()[0] else [[quadratic], [fixed]]
        finite.append(lift_off_curves(projected, l_groups, [*input_supports(), [fixed]], units))
    extra = [
        N*SYMBOL_L+1, (N+1)*SYMBOL_L+1, (N-1)*SYMBOL_L+1, K*SYMBOL_L+N-1,
        1+(SYMBOL_P-1)*(SYMBOL_M+1)*SYMBOL_L, 1+(SYMBOL_P+1)*(SYMBOL_M-1)*SYMBOL_L,
    ]
    curves = {}
    for name, point in quadratic_curves():
        substitution = dict(zip((SYMBOL_P, SYMBOL_M, SYMBOL_L), point, strict=True))
        curves[name] = curve_rank(tuple(map(s.cancel, point)),
                                  [f.subs(substitution, simultaneous=True) for f in extra])
        print("PASS quadratic branch on", name, flush=True)
    return {"off_curves": finite, "curves": curves}


def rational_restriction(f):
    degree = int(f.degrees()[2])
    return sum((co*L**int(j)*R**int(k+l)*(R+1)**(degree-int(k))
                for (i,j,k,l), co in f.to_dict().items()), ZERO)


def quadratic_product(left, right):
    a, b = left
    c, d = right
    return a*c+b*d*PRODUCT, a*d+b*c-b*d*DIFFERENCE


@cache
def quadratic_power(axis, exponent):
    if not exponent:
        return ONE, ZERO
    coordinates = ((L,ZERO), (DIFFERENCE,ONE), (ZERO,ONE))
    return quadratic_product(coordinates[axis], quadratic_power(axis, exponent-1))


def quadratic_norm(f):
    a, b = ZERO, ZERO
    for (i,j,k,l), coefficient in f.to_dict().items():
        assert not i
        u, v = quadratic_product(quadratic_power(0, j),
                                 quadratic_product(quadratic_power(1, k), quadratic_power(2, l)))
        a += coefficient*u
        b += coefficient*v
    return a*a-DIFFERENCE*a*b-PRODUCT*b*b


def curve_candidates(projected, restriction, units):
    groups = []
    for group in projected:
        values = [restriction(f) for f in group.values()]
        if all(values):
            groups.append(factor_support(values, units))
    assert not intersection(groups)
    return projection_candidates(groups, 0, [u for u in units if not u.degrees()[0]])


def affine_plane_points(candidates, quadratic):
    for label in sorted(candidates):
        poly = s.Poly(label.replace("^", "**"), R_SYMBOL, domain=s.QQ)
        for _, field, r0 in residues(poly):
            if quadratic:
                d = -r0**2-field.one
                n = field.one+r0*d
                equation = s.Poly.from_list([field.one, d, -n], SYMBOL_P, domain=field)
                for pf, extension, p0 in residues(equation):
                    yield (label, str(pf.as_expr())), extension, p0, p0+lift_scalar(d, field, extension)
            elif r0+field.one:
                yield (label,), field, r0, r0/(r0+field.one)


def solve_affine(affine, witnesses, units, base_units, plane_units):
    projected = affine_base_groups(affine, witnesses, base_units)
    l_groups = [list(group.values()) for group in projected]
    e_groups = [*input_supports(), [affine]]
    rational_units = [rational_restriction(u) for u in base_units]+[R+1]
    assert all(rational_units)
    # r=1 gives P=1 and M=-1, and r^2+1=0 gives P=M. The other factor
    # vanishes on the excluded (PM-1)L+1=0 branch.
    norm_units = [R-1, R**2+1, L*(R**3+R)-1]
    curves = {}
    for norm, restrict, inverted in ((False, rational_restriction, rational_units),
                                    (True, quadratic_norm, norm_units)):
        candidates = curve_candidates(projected, restrict, inverted)
        checked = lift_points(affine_plane_points(candidates, norm), l_groups, e_groups, units)
        curves["norm" if norm else "rational"] = {"base_factors": sorted(candidates), "residue_fields": checked}
        print("PASS affine branch base curve", norm, len(candidates), len(checked), flush=True)
    finite = []
    for fixed, groups in affine_branches(projected, plane_units):
        finite.append(lift_off_curves(groups, [[fixed], *l_groups], e_groups, units,
                                      use_seeds=fixed.degrees()[1] == 7))
    return {"off_curves": finite, "curves": curves}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("branches", nargs="*", default=["quadratic", "affine"])
    arguments = parser.parse_args()
    affine, quadratic, units, witnesses = chart_data()
    base_units = [u for u in units if not u.degrees()[0]]
    plane_units = [u for u in base_units if not u.degrees()[1]]
    for name in arguments.branches:
        if name == "quadratic":
            result = solve_quadratic(quadratic, witnesses, units, base_units, plane_units)
        else:
            assert name == "affine"
            result = solve_affine(affine, witnesses, units, base_units, plane_units)
        (DIRECTORY / f"cubic_CY_one_segre_double_split_FDC_nonlinear_{name}_certificate.json").write_text(
            json.dumps(result, indent=2)+"\n")
        print("PASS full FDC3 nonlinear branch", name, flush=True)


if __name__ == "__main__":
    main()
