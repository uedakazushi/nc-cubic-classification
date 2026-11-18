"""Central cubics in the twelve pencils of the rank-three central quotient."""
from pathlib import Path
import json

import sympy as s

from verify_cubic_CY_one_segre_cross import PivotAlgebra, p, h
from verify_cubic_CY_one_segre_square import Q, comm, word

eta, u, v = s.symbols("eta u v")
L0 = s.Matrix([[-v, u, 0], [0, -v, u]])


def central_quotient(first, second):
    """Take the quadratic dual of the exact eight-relation Segre pencil."""
    relations = [comm(0, 2), comm(1, 3), word(0, 3)-word(2, 1), word(3, 0)-word(1, 2)]

    def sym(i, j):
        return (word(i, j)+word(j, i))/2

    for row in (first, second):
        a, b, c, d, e, f = [s.expand(expr).coeff(base) for expr in row for base in (u, v)]
        crossed = (sym(0, 3)+sym(1, 2))/2
        relations.extend([
            a*word(0, 0)+b*sym(0, 2)+c*sym(0, 1)+d*crossed+e*word(1, 1)+f*sym(1, 3),
            a*sym(0, 2)+b*word(2, 2)+c*crossed+d*sym(2, 3)+e*sym(1, 3)+f*word(3, 3),
        ])
    dual = s.Matrix.hstack(*relations)
    result = s.Matrix.hstack(*dual.T.nullspace()).applyfunc(s.cancel)
    assert result.shape == (16, 8)
    assert (dual.T*result).applyfunc(s.cancel) == s.zeros(8)
    return result


def zero_drop(change):
    pencil = L0*change.inv()
    return central_quotient(pencil.row(0), pencil.row(1))


def fourpoint(lam, mu):
    return central_quotient(
        (mu*(lam-1)*v, -lam*(mu-1)*u+(mu-lam)*v, 0),
        (0, (mu-lam)*u+(1-mu)*v, (lam-1)*u),
    )


def factor_set(expressions, variables):
    factors = set()
    if variables:
        for expr in expressions:
            assert expr
            factors.update(factor.monic().as_expr()
                           for factor, _ in s.Poly(expr, *variables, domain=s.QQ).factor_list()[1])
    return factors


def evaluate(name, relations, units=(), base=s.QQ, generators=(0, 1, 2, 3)):
    variables = tuple(sorted(relations.free_symbols, key=str))
    field = base.frac_field(*variables) if variables else base
    source = []
    for j in range(8):
        relation = {}
        for i in range(16):
            if relations[i, j]:
                a, b = divmod(i, 4)
                relation[generators[a], generators[b]] = field.from_sympy(relations[i, j])
        source.append(relation)
    algebra = PivotAlgebra(field, 4, source, [0]*4)
    minors = []
    for n, dimension in [(2, 8), (3, 12), (4, 16)]:
        algebra.pivot_product = field.one
        algebra.build(n)
        assert len(algebra.basis[n]) == dimension, name
        minors.append(field.to_sympy(algebra.pivot_product))
    equations = [{} for _ in range(64)]
    for j, word_tuple in enumerate(algebra.basis[3]):
        for gen in range(4):
            values = algebra.word(word_tuple+(gen,))
            algebra.addto(values, algebra.word((gen,)+word_tuple), -field.one)
            for i, coefficient in values.items():
                equations[16*gen+i][j] = coefficient
    algebra.pivot_product = field.one
    pivots = algebra.echelon(equations)
    centre_minor = field.to_sympy(algebra.pivot_product)
    values = [field.to_sympy(c) for n in (2, 3, 4) for row in algebra.right[n].values() for c in row.values()]
    denominator_values = [v.as_numer_denom()[1] for v in [*relations, *values]]
    all_factors = factor_set([*denominator_values,
                             *(x for m in [*minors, centre_minor] for x in m.as_numer_denom())], variables)
    unit_factors = factor_set([x for unit in units for x in s.cancel(unit).as_numer_denom()], variables)
    excess = all_factors-unit_factors
    inverse_permutation = tuple(generators.index(j) for j in range(4))
    kernel = []
    for basis_index in sorted(set(range(12))-pivots.keys()):
        vector = {basis_index: field.one}
        for i in sorted(pivots, reverse=True):
            vector[i] = -sum((c*vector.get(j, field.zero) for j, c in pivots[i].items() if i != j), field.zero)
        kernel.append({
            "".join("abcd"[inverse_permutation[k]] for k in algebra.basis[3][i]): str(field.to_sympy(coefficient))
            for i, coefficient in vector.items() if coefficient
        })
    record = {"chart": name, "quotient_minors": [str(s.factor(m)) for m in minors],
              "center_rank": len(pivots), "centre_minor": str(s.factor(centre_minor)),
              "extra_factors": sorted(map(str, excess)), "centre_kernel": kernel}
    return record, excess


def main():
    records = []
    for name, relations, units, exceptional, ranks in families():
        record, excess = evaluate(name, relations, units)
        assert record["center_rank"] == 12
        assert excess <= set(exceptional), (name, excess)
        records.append(record)
        for factor, rank in zip(exceptional, ranks):
            point = s.solve(factor, eta)[0]
            assert s.Poly(s.minpoly(point, eta), eta).monic() == s.Poly(factor, eta).monic()
            base = s.QQ if point.is_Rational else s.QQ.algebraic_field(point)
            result, excess = evaluate(f"{name} at {factor}", relations.subs(eta, point), base=base)
            assert not excess and result["center_rank"] == rank, (name, result)
            records.append(result)
        print("PASS", name, record["extra_factors"], flush=True)
    records.extend(fourpoint_strata())
    Path(__file__).with_name("cubic_CY_three_rankthree_quotient_certificate.json").write_text(json.dumps(records, indent=2)+"\n")


def fourpoint_units(lam, mu):
    return [lam, mu, lam-1, mu-1, lam-mu]


def fourpoint_strata():
    records = []
    record, excess = evaluate("fourpoint", fourpoint(p, h), fourpoint_units(p, h))
    A = (4*h-1)*p*p-6*h*h*p-h**4+4*h**3
    B = p*p+(-4*h**3+6*h*h-4*h)*p+h**4
    assert record["center_rank"] == 12
    assert excess == factor_set([A, B, p-h*h, (2*h-1)*p-h*h, p-2*h+h*h], (h, p))
    records.append(record)
    assert s.factor(s.discriminant(A, p)) == 16*h**3*(h-1)**2
    assert s.factor(s.discriminant(B, p)) == 16*h*h*(h-1)**2*(h*h-h+1)
    mu_B = s.cancel((-1-2*eta)/(eta*eta-1))
    square_root_B = 1+eta*mu_B
    lambda_B = s.cancel(2*mu_B**3-3*mu_B**2+2*mu_B+2*mu_B*(mu_B-1)*square_root_B)
    for name, curve, lam, mu, expected in [
        ("lambda_square", p-h*h, h*h, h, 12),
        ("first_linear", (2*h-1)*p-h*h, h*h/(2*h-1), h, 12),
        ("second_linear", p-2*h+h*h, 2*h-h*h, h, 12),
        ("A", A, (3*eta**4+2*eta**3*(eta*eta-1))/(4*eta*eta-1), eta*eta, 12),
        ("B", B, lambda_B, mu_B, 11),
    ]:
        lam, mu = s.cancel(lam), s.cancel(mu)
        assert s.cancel(curve.subs({p: lam, h: mu}, simultaneous=True)) == 0
        units = [*fourpoint_units(lam, mu), lam.as_numer_denom()[1], mu.as_numer_denom()[1]]
        result, additional = evaluate(f"fourpoint_{name}", fourpoint(lam, mu), units)
        assert result["center_rank"] == expected, (name, result)
        if name == "B":
            assert additional <= {eta*eta-5*eta-5}, additional
            assert result["centre_kernel"] == [{"dcc": "1", "ccc": "1/3 - eta/3"}]
            root = (5+3*s.sqrt(5))/2
            assert s.Poly(s.minpoly(root, eta), eta).monic().as_expr() == eta*eta-5*eta-5
            special, ignored = evaluate("fourpoint_B_quadratic",
                                        fourpoint(lam.subs(eta, root), mu.subs(eta, root)),
                                        base=s.QQ.algebraic_field(root))
            assert not ignored and special["center_rank"] == 11, special
            records.append(special)
        else:
            assert not additional, (name, additional)
        records.append(result)
        print("PASS", name, "fourpoint centre rank", expected, flush=True)
    point, ignored = evaluate("fourpoint_A_linear_point", fourpoint(Q(5, 32), Q(1, 4)))
    assert not ignored and point["center_rank"] == 12
    records.append(point)
    return records


def families():
    yield "scalar", zero_drop(s.eye(3)), [], [], []
    yield "double", zero_drop(s.diag(1, -1/eta, 1)), [eta, eta-1, eta+1], [eta-2, eta+2, eta**2-2], [11, 11, 12]
    yield "J3", zero_drop(s.Matrix([[1, 1, 0], [0, 1, 0], [0, 0, 1]])), [], [], []
    yield "J21", zero_drop(s.Matrix([[1, 0, 1], [0, 1, 0], [0, 0, 1]])), [], [], []
    yield "J21param", zero_drop(s.Matrix([[1, eta-1, 0], [0, eta, 0], [0, 0, eta]])), [eta, eta-1], [
        eta-Q(1, 4), eta-Q(1, 2), eta-Q(3, 4)
    ], [11, 12, 12]
    yield "two_drop_meet", central_quotient((u, u, 0), (0, v, 0)), [], [], []
    yield "two_drop_disjoint", central_quotient((u, u*eta, u), (0, v, 0)), [eta-2, eta+2], [eta, eta**2+4], [12, 12]
    yield "two_drop_secant", central_quotient((u+v, 0, -u+v), (u, 0, u)), [], [], []
    yield "two_drop_tangent", central_quotient((u, v, 0), (0, u, 0)), [], [], []
    yield "one_drop_meet", central_quotient((u, u, v), (0, v, 0)), [], [], []
    yield "one_drop_disjoint", central_quotient((u+v, u*eta, u-v), (0, v, 0)), [eta-2, eta+2], [eta], [12]


if __name__ == "__main__":
    main()
