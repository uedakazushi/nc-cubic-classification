"""Exclude the six low-degree M surfaces left after T=0 and ZT=1."""
import json
from pathlib import Path

from flint import fmpq, fmpq_mpoly_ctx
import sympy as s
from sympy.polys.agca.extensions import MonogenicFiniteExtension

from cubic_flint_rational_function import RationalFunctionField, VARIABLES
from verify_cubic_CY_one_segre_cross import centre_calculation
from verify_cubic_CY_one_segre_double_split_quadratics import centre_witness
from verify_cubic_CY_one_segre_double_split_TD import fraction
from verify_cubic_CY_one_segre_square_split_M import lower_m
from verify_cubic_CY_one_segre_square_split_M_witness import normalized_factors, symmetry_translates

z, t, x = s.symbols("z t x")
PARAMETERS = (z, t, x)
CONTEXT = fmpq_mpoly_ctx.get(tuple(map(str, PARAMETERS)))
GENERATORS = CONTEXT.gens()
DIRECTORY = Path(__file__).parent
ORDER = (0, 1, 2, 3)
DIMENSIONS = (10, 20, 35)
UNITS = [
    x, x*x-1, t, t*t-1, x*x-t*t, x**4-t*t, z*t-1,
    z*(x+t)**2-t*(x*x+1)-2*x, z*(x-t)**2-t*(x*x+1)+2*x,
]
GRAPHS = [
    ("TX+X^2-2", t, (2-x*x)/x),
    ("TX+2T+2X^2+X", t, -x*(2*x+1)/(x+2)),
    ("ZT+ZX-X-1", z, (x+1)/(t+x)),
    ("ZT+ZX^2-X^2-1", z, (x*x+1)/(t+x*x)),
    ("Z(T^2-X^2)-TX^2-T+2X^2", z, (t*x*x+t-2*x*x)/(t*t-x*x)),
]


def expression(poly):
    return s.sympify(str(poly).replace("^", "**"))


def polynomial(value):
    terms = s.Poly(value, *PARAMETERS, domain=s.QQ).terms()
    return CONTEXT.from_dict({monomial: fmpq(int(co.p), int(co.q)) for monomial, co in terms})


def factors(value):
    result = {}
    for factor, _ in value.factor()[1]:
        monic = factor/factor.leading_coefficient()
        result[str(monic)] = monic
    return result


def restrict_support(all_support, coordinate, graph, units):
    numerator, denominator = map(polynomial, fraction(graph))
    index = PARAMETERS.index(coordinate)
    invertible = polynomial(s.prod(units))

    def transform(poly):
        total_degree = poly.degrees()[index]
        result = CONTEXT.constant(0)
        for exponents, coefficient in poly.to_dict().items():
            degree = exponents[index]
            term = coefficient*numerator**degree*denominator**(total_degree-degree)
            for position, exponent in enumerate(exponents):
                if position != index:
                    term *= GENERATORS[position]**exponent
            result += term
        return result

    restricted = []
    for original in all_support:
        images = [transform(f) for f in original.values()]
        if not all(images):
            continue
        support = {}
        for value in images:
            while not (common := value.gcd(invertible)).is_constant():
                value //= common
            support.update(factors(value))
        restricted.append(support)
    return restricted


def projected_factors(supports, variable, base_units):
    index = PARAMETERS.index(variable)
    projected = {}
    for name, first in supports[0].items():
        if first.degrees()[index] == 0:
            projected[name] = first
            continue
        candidates = []
        for support in supports[1:]:
            if name in support:
                continue
            factors_here = {}
            for other in support.values():
                resultant = first.resultant(other, index)
                assert resultant
                factors_here.update(factors(resultant))
            candidates.append(factors_here)
        assert candidates
        for factor in set.intersection(*(set(item) for item in candidates)):
            projected[factor] = candidates[0][factor]
    return {key: value for key, value in projected.items() if value.gcd(base_units).is_constant()}


def check_fibre(source, supports, variable, base, units):
    minimal = s.Poly(base, x, domain=s.QQ)
    field = s.QQ.algebraic_field((minimal, s.CRootOf(minimal, 0)))

    def convert(value):
        terms = {
            exponent: field.new(s.Poly(coefficient, x, domain=s.QQ).rem(minimal).rep.to_list())
            for exponent, coefficient in s.Poly(value, variable).terms()
        }
        return s.Poly.from_dict(terms, variable, domain=field)

    common = s.Poly(0, variable, domain=field)
    for support in supports:
        product = s.Poly(1, variable, domain=field)
        for value in support:
            product *= convert(value)
            if not product:
                break
        common = common.gcd(product)
    assert common
    for unit in units:
        excluded = common.gcd(convert(unit))
        while excluded.degree() > 0:
            common = common.exquo(excluded)
            excluded = common.gcd(excluded)

    records = []
    for minimal_fibre, _ in common.factor_list()[1]:
        extension = MonogenicFiniteExtension(minimal_fibre)

        def evaluate(value):
            def evaluate_polynomial(poly):
                result = extension.zero
                for coefficient in convert(poly).rep.to_list():
                    result = result*extension.generator+extension.convert(coefficient, field)
                return result

            numerator, denominator = fraction(value)
            return evaluate_polynomial(numerator)/evaluate_polynomial(denominator)

        _, rank = centre_calculation(source, ORDER, extension, evaluate)
        assert rank == 20, (base, minimal_fibre, rank)
        records.append(minimal_fibre.degree())
    return records


def main():
    certificate = json.loads((DIRECTORY / "cubic_CY_one_segre_square_split_M_open_certificate.json").read_text())
    initial = [f for f in normalized_factors(certificate) if str(f) not in ("t", "z*t - 1")]
    global_supports = symmetry_translates(initial)
    p, u, w = VARIABLES
    k = (x*x-1)/64
    w0 = (1+t)/(k*(1-t))
    normal = {p: x/4, u: k*(z+1)/w0, w: w0}
    source = lower_m()[0].subs(normal, simultaneous=True).applyfunc(s.cancel)
    results = {}
    for name, coordinate, graph in GRAPHS:
        free = z if coordinate == t else t
        field = RationalFunctionField((x, free))
        sample = source.subs(coordinate, graph).applyfunc(s.cancel)
        witness = centre_witness(sample, ORDER, DIMENSIONS, field)
        units = [s.denom(graph)]+[fraction(f.subs(coordinate, graph))[0] for f in UNITS]
        invertible = polynomial(s.prod(units))
        exceptional = {}
        for key, values in witness.items():
            if not key.endswith("_factors"):
                continue
            for value in values:
                poly = polynomial(expression(value))
                while not (common := poly.gcd(invertible)).is_constant():
                    poly //= common
                exceptional.update(factors(poly))
        number_fields = []
        if exceptional:
            sets = [exceptional, *restrict_support(global_supports, coordinate, graph, units)]
            assert not set.intersection(*(set(group) for group in sets))
            base_units = polynomial(x*(x*x-1)*(s.denom(graph) if coordinate == t else 1))
            base = projected_factors(sets, free, base_units)
            supports = [[expression(poly) for poly in group.values()] for group in sets]
            for key in sorted(base):
                degrees = check_fibre(sample, supports, free, expression(base[key]), units)
                number_fields.append({"base_factor": key, "fibre_degrees": degrees})
        results[name] = {"witness": witness, "number_fields": number_fields}
        print("PASS", name, "allowed residue fields",
              sum(len(item["fibre_degrees"]) for item in number_fields), flush=True)

    # The reflected base chart is linearly transformed by the opposite algebra.
    assert s.expand((t*x+2*t+2*x*x+x).subs(x, -x)+(t*x-2*t-2*x*x+x)) == 0
    count = sum(len(entry["fibre_degrees"]) for value in results.values() for entry in value["number_fields"])
    assert count == 78, count
    (DIRECTORY / "cubic_CY_one_segre_square_split_M_simple_certificate.json").write_text(
        json.dumps(results, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
