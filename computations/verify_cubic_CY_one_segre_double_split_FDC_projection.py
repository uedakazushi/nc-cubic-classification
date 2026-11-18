"""Project the two nonlinear FDC3 branches to the (P,M) plane."""
import json
from pathlib import Path

from flint import fmpq_mpoly, fmpq_mpoly_ctx

from verify_cubic_CY_one_segre_double_split_FDC_witness import CONTEXT as NORMAL_CONTEXT
from verify_cubic_CY_one_segre_double_split_FDC_witness import associate, factor_support

CONTEXT = fmpq_mpoly_ctx.get(("E", "L", "M", "P"))
E, L, M, P = CONTEXT.gens()
DIRECTORY = Path(__file__).parent


def reversed_polynomial(value):
    polynomial = fmpq_mpoly(value, NORMAL_CONTEXT)
    return associate(CONTEXT.from_dict({index[::-1]: co for index, co in polynomial.to_dict().items()}))


def chart_data():
    primary = json.loads((DIRECTORY / "cubic_CY_one_segre_double_split_FDC_witness_certificate.json").read_text())
    alternate = json.loads((DIRECTORY / "cubic_CY_one_segre_double_split_FDC_alternate_certificate.json").read_text())
    K = (P*P-1)*(M*M-1)
    N = P*M
    linear = [L*N+1, L*(N+1)+1, L*(N-1)+1, K*L+N-1]
    quadratic = associate(N*K*L*L+(K+N*N+N-2)*L+N+1)
    ordinary = [reversed_polynomial(f) for f in alternate["factors"]]
    affine, = [f for f in ordinary if f.degrees()[0] > 0]
    assert affine.degrees()[0] == 1
    common = [reversed_polynomial(f) for f in alternate["common_factors"]]
    assert set(map(str, ordinary)) == {str(associate(f)) for f in [*linear, quadratic, affine, *common]}
    units = [reversed_polynomial(f) for f in primary["regularity_units"]]+[M, *common, *linear]
    witnesses = [factor_support([reversed_polynomial(f) for f in group], units)
                 for record in (primary, alternate) for group in record["symmetry_supports"].values()]
    return affine, quadratic, units, witnesses


def project(fixed, support, coordinate):
    assert fixed != support
    if fixed.degrees()[coordinate] == 0:
        return fixed
    if support.degrees()[coordinate] == 0:
        return support
    return fixed.resultant(support, coordinate)


def group_cost(group):
    return len(group), sum(map(len, group.values()))


def projection_groups(fixed, groups, coordinate, units):
    projected = [
        factor_support([project(fixed, other, coordinate) for other in group.values()], units)
        for group in groups if str(fixed) not in group
    ]
    assert projected
    return projected


def intersection(groups):
    assert groups
    return set.intersection(*(set(group) for group in groups))


def describe(groups):
    return {"factor_counts": list(map(len, groups)), "common": sorted(intersection(groups))}


def affine_base_groups(equation, witnesses, base_units):
    first = projection_groups(equation, witnesses, 0, base_units)
    assert not intersection(first)
    return first


def affine_branches(first, plane_units):
    for fixed in min(first, key=group_cost).values():
        assert fixed.degrees()[1] > 0
        yield fixed, projection_groups(fixed, first, 1, plane_units)


def affine_projection(equation, witnesses, base_units, plane_units):
    reports = []
    first = affine_base_groups(equation, witnesses, base_units)
    for fixed, second in affine_branches(first, plane_units):
        proof = describe(second)
        proof["degrees_L_M_P"] = list(map(int, fixed.degrees()[1:]))
        reports.append(proof)
        print("affine L factor", len(fixed), "plane curves", len(proof["common"]), flush=True)
    return reports


def quadratic_branches(equation, witnesses, base_units, plane_units):
    active = [group for group in witnesses if str(equation) not in group]
    for fixed in min(active, key=group_cost).values():
        first = projection_groups(fixed, active, 0, base_units) if fixed.degrees()[0] else [{str(fixed): fixed}]
        second = [
            factor_support([project(equation, other, 1) for other in group.values()], plane_units)
            for group in first if str(equation) not in group
        ]
        yield fixed, second


def quadratic_projection(equation, witnesses, base_units, plane_units):
    reports = []
    for fixed, second in quadratic_branches(equation, witnesses, base_units, plane_units):
        proof = describe(second)
        proof["degrees_E_L_M_P"] = list(map(int, fixed.degrees()))
        reports.append(proof)
        print("quadratic branch factor", len(fixed), "plane curves", len(proof["common"]), flush=True)
    return reports


def main():
    affine, quadratic, units, witnesses = chart_data()
    base_units = [value for value in units if value.degrees()[0] == 0]
    plane_units = [value for value in base_units if value.degrees()[1] == 0]
    results = {
        "quadratic_branch": quadratic_projection(quadratic, witnesses, base_units, plane_units),
        "affine_branch": affine_projection(affine, witnesses, base_units, plane_units),
    }
    expected = {
        "quadratic_branch": [M-P+1, M-P-1, M*P+1, M*M+4*M*P+P*P+3],
        "affine_branch": [M*P+M-P, (P*M-1)**2+(M-P)**2*(M-P+1)],
    }
    for label, branches in results.items():
        curves = {factor for branch in branches for factor in branch["common"]}
        assert curves == {str(associate(value)) for value in expected[label]}
    (DIRECTORY / "cubic_CY_one_segre_double_split_FDC_projection_certificate.json").write_text(
        json.dumps(results, indent=2)+"\n"
    )
    print("PASS both nonlinear FDC3 projections and all six plane curves", flush=True)


if __name__ == "__main__":
    main()
