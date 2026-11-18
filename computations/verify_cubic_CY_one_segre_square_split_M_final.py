"""Exclude the five remaining M hypersurfaces by exact projection and lifting."""
import json
from pathlib import Path

from flint import fmpq_mpoly, fmpq_mpoly_ctx
import sympy as s
from sympy.polys.agca.extensions import MonogenicFiniteExtension

from cubic_flint_rational_function import VARIABLES
from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_double_split_TD import fraction
from verify_cubic_CY_one_segre_square_split_M import lower_m
from verify_cubic_CY_one_segre_square_split_M_simple import GRAPHS, UNITS, factors, polynomial
from verify_cubic_CY_one_segre_square_split_M_witness import normalized_factors, symmetry_translates

VARIABLE_ORDER = z, t, x = s.symbols("z t x")
DIRECTORY = Path(__file__).parent
CONTEXT = fmpq_mpoly_ctx.get(tuple(map(str, VARIABLE_ORDER)))
BASE_UNITS = polynomial(s.prod(unit for unit in UNITS if not unit.has(z)))


def certificate(which):
    return json.loads((DIRECTORY / f"cubic_CY_one_segre_square_split_M_{which}_certificate.json").read_text())


def remove_support(value, excluded):
    assert value
    while not (common := value.gcd(excluded)).is_constant():
        value //= common
    return value


def remaining_supports():
    excluded = polynomial(s.prod(UNITS))
    simple_surfaces = [polynomial(fraction(coordinate-graph)[0]) for _, coordinate, graph in GRAPHS]
    for group in symmetry_translates(simple_surfaces):
        for surface in group.values():
            excluded *= surface

    first = [remaining for f in normalized_factors(certificate("open"))
             if not (remaining := remove_support(f, excluded)).is_constant()]
    first.sort(key=lambda f: (f.degrees()[0], len(f)))
    assert [(f.degrees()[0], len(f)) for f in first] == [(0, 5), (2, 10), (2, 30), (3, 19), (4, 178)]

    alternate_context = fmpq_mpoly_ctx.get(tuple(map(str, VARIABLES)))
    alternate_factors = {data for key, values in certificate("alternate").items()
                         if key.endswith("_factors") for data in values}
    alternate = {}
    for data in sorted(alternate_factors):
        raw = fmpq_mpoly(data, alternate_context)
        # The alternate coefficient field is ordered by X, Z, T.
        transformed = CONTEXT.from_dict({(j, h, i): c for (i, j, h), c in raw.to_dict().items()})
        remaining = remove_support(transformed, excluded)
        if not remaining.is_constant():
            alternate.update(factors(remaining))

    supports = [*symmetry_translates(first), *symmetry_translates(alternate.values())]
    return first, [list(group.values()) for group in supports]


def project_pair(first, second, coordinate):
    assert first != second
    if first.degrees()[coordinate] == 0:
        return factors(first)
    if second.degrees()[coordinate] == 0:
        return factors(second)
    eliminant = first.resultant(second, coordinate)
    return factors(remove_support(eliminant, BASE_UNITS))


def project_groups(left, right):
    assert not set(map(str, left)) & set(map(str, right))
    projected = {}
    for first in left:
        for second in right:
            # With two base equations their individual factors already occur
            # from pairing each equation with a positive-degree factor.
            if first.degrees()[0] or second.degrees()[0]:
                projected.update(project_pair(first, second, 0))
    return list(projected.values())


def group_cost(group):
    return (sum(sum(f.degrees()) for f in group), len(group))


def common_x(groups, first_group=None):
    source = first_group if first_group is not None else min(groups, key=group_cost)
    for equation in source:
        common = None
        for group in sorted(groups, key=group_cost):
            if equation in group:
                continue
            planes = {}
            for other in group:
                planes.update(project_pair(equation, other, 1))
            common = set(planes) if common is None else common & set(planes)
            if not common:
                break
        assert common is not None
        yield from sorted(common)


def base_candidates(first, supports):
    for branch, equation in enumerate(first):
        if branch == 0:
            # The first equation is a base curve. Both supports of each pair
            # contain a positive-Z-degree factor and share no factor.
            pairs = ((2, 4), (2, 6), (3, 4), (3, 6), (2, 5), (3, 7))
            groups = [project_groups(supports[i], supports[j]) for i, j in pairs]
            candidates = sorted(set(common_x(groups, [equation])))
            # Keep the projected conditions when lifting this base branch.
            groups = [[equation], *groups]
        else:
            groups = []
            for group in supports:
                if equation in group:
                    continue
                projected = {}
                for other in group:
                    projected.update(project_pair(equation, other, 0))
                groups.append(list(projected.values()))
            candidates = sorted(set(common_x(groups)))
        print("branch", branch, "possible X factors", len(candidates), flush=True)
        yield branch, equation, groups, candidates


class ResidueFieldExtension(MonogenicFiniteExtension):
    """Use quotient-field division in nested characteristic-zero extensions."""

    alias = "MonogenicFiniteExtension"

    def exquo(self, numerator, denominator):
        return numerator/denominator


def specialise(poly, field, coordinate, values):
    terms = {}
    for exponents, coefficient in poly.to_dict().items():
        value = field.convert(s.QQ(int(coefficient.p), int(coefficient.q)), s.QQ)
        for point, exponent in zip(values, exponents, strict=True):
            if point is not None:
                value *= point**int(exponent)
        key = (int(exponents[coordinate]),)
        terms[key] = terms.get(key, field.zero)+value
    return s.Poly.from_dict(terms, VARIABLE_ORDER[coordinate], domain=field)


def common_fibre(groups, coordinate, field, values):
    variable = VARIABLE_ORDER[coordinate]
    common = s.Poly(0, variable, domain=field)
    for group in sorted(groups, key=len):
        specialised = [specialise(p, field, coordinate, values) for p in group]
        if any(not p for p in specialised):
            continue
        if not common:
            common = s.prod(specialised)
        else:
            product = s.Poly(1, variable, domain=field)
            for p in specialised:
                product = (product*p.gcd(common)).rem(common)
            common = common.gcd(product)
        if common.degree() == 0:
            break
    assert common, (coordinate, values)
    return common


def allowed_part(poly, excluded):
    for unit in excluded:
        while (common := poly.gcd(unit)).degree() > 0:
            poly = poly.exquo(common)
    return poly


def centre_rank(relations, field, X, T, Z):
    def evaluate_polynomial(value):
        result = field.zero
        for (dz, dt, dx), coefficient in s.Poly(value, z, t, x, domain=s.QQ).terms():
            result += field.convert(s.QQ.convert(coefficient), s.QQ)*Z**dz*T**dt*X**dx
        return result

    def evaluate(value):
        numerator, denominator = fraction(value)
        return evaluate_polynomial(numerator)/evaluate_polynomial(denominator)

    return centre_calculation(relations, (0, 1, 2, 3), field, evaluate)[1]


def lift(relations, source_supports, equation, projected, x_factor):
    min_x = s.Poly(x_factor.replace("^", "**"), x, domain=s.QQ)
    root_x = s.CRootOf(min_x, 0)
    field_x = s.QQ.algebraic_field((min_x, root_x))
    X = field_x.from_sympy(root_x)
    base_units = [polynomial(f) for f in UNITS if not f.has(z)]
    all_units = list(map(polynomial, UNITS))
    fibre_t = common_fibre(projected, 1, field_x, (None, None, X))
    fibre_t = allowed_part(fibre_t, (specialise(f, field_x, 1, (None, None, X)) for f in base_units))

    rows = []
    for min_t, _ in fibre_t.factor_list()[1]:
        min_t = min_t.monic()
        if min_t.degree() == 1:
            field_t, X1, T = field_x, X, -min_t.rep.to_list()[-1]
        else:
            field_t = ResidueFieldExtension(min_t)
            X1, T = field_t.convert(X, field_x), field_t.generator
        fibre_z = common_fibre([[equation], *source_supports], 0, field_t, (None, T, X1))
        fibre_z = allowed_part(fibre_z, (specialise(f, field_t, 0, (None, T, X1)) for f in all_units))
        if fibre_z.degree() == 0:
            continue
        squarefree = fibre_z.exquo(fibre_z.gcd(fibre_z.diff())).monic()
        if squarefree.degree() == 1:
            z_factors = [squarefree]
        else:
            assert field_t is field_x
            z_factors = [f.monic() for f, _ in squarefree.factor_list()[1]]
        for min_z in z_factors:
            if min_z.degree() == 1:
                rank = centre_rank(relations, field_t, X1, T, -min_z.rep.to_list()[-1])
            else:
                field_z = ResidueFieldExtension(min_z)
                rank = centre_rank(relations, field_z, field_z.convert(X1, field_t),
                                   field_z.convert(T, field_t), field_z.generator)
            assert rank == 20, (x_factor, min_t, min_z, rank)
            rows.append({"T": str(min_t.as_expr()), "Z": str(min_z.as_expr()), "rank": rank})
    return {"X": x_factor, "T_degree": fibre_t.degree(), "allowed": rows}


def main():
    first, supports = remaining_supports()
    k = (x*x-1)/64
    old_w = (1+t)/(k*(1-t))
    normal = dict(zip(VARIABLES, (x/4, k*(z+1)/old_w, old_w), strict=True))
    relations = lower_m()[0].subs(normal, simultaneous=True).applyfunc(s.cancel)
    proof = []
    for index, equation, projected, x_factors in base_candidates(first, supports):
        results = [lift(relations, supports, equation, projected, factor) for factor in x_factors]
        count = sum(len(fibre["allowed"]) for fibre in results)
        print("PASS branch", index, "allowed residue fields", count, flush=True)
        proof.append({"equation": str(equation), "fibres": results, "allowed_residue_fields": count})
    output = DIRECTORY / "cubic_CY_one_segre_square_split_M_final_certificate.json"
    output.write_text(json.dumps(proof, indent=2)+"\n")


if __name__ == "__main__":
    main()
