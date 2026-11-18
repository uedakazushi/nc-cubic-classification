"""Verify a regular central quadric on the full FDC3 four-cross chart."""
import argparse
from collections import defaultdict
from itertools import product

import sympy as sym

from cubic_flint_rational_function import RationalFunctionField
from verify_cubic_CY_one_segre_cross import PivotAlgebra
from verify_cubic_CY_one_segre_double_split_isolated import marked

Q = sym.Rational
p, m, ratio, e = sym.symbols("p m ratio e")


def four_cross_both_outer():
    s, t = (p+m)/2, (p-m)/2
    h, k = Q(1, 64)-p*p/4, Q(1, 64)-m*m/4
    slope = m/(k*p)
    # FEA1–FEA2 with ratio=d/e. The relations are affine in e.
    A_over_e = s*(ratio+m)/(p*k)
    C_over_d = 2*(s*t-16*m*h*ratio)/(p*k*ratio)
    z = (A_over_e*e+k)/s
    v = e-k*k/s
    f = v-k*k/t
    x2 = 1/s+A_over_e*(A_over_e*e+2*k)/(s*s)
    x4 = -h*h/t-h*k*C_over_d/(16*t)+f*C_over_d*C_over_d/1024
    x6, x7, x8 = z, -h*k/t+f*C_over_d/32, v
    x5 = slope*(x7-h*x6)+x8/k
    x1 = slope*(x5-h*x2-s)+x6/k
    x3 = slope*(x4-h*x5-h*t)+x7/k
    x0 = slope*(x3-h*x1)+(x5-m)/k
    coordinates = (x0, x1, x2, x3, x4, x5, x6, x7, x8, s, 1, 1, h, k, t)
    source = marked(dict(enumerate(coordinates)), Q(1, 8), linear_columns=True)
    U, V = (1, 0, -h/s, -k/s), (0, s, 1, 1)
    mixed = 64*h*k*A_over_e*A_over_e/s+32*p*m*A_over_e+64*s
    return source, U, V, (A_over_e*A_over_e, mixed, 1)


def check():
    source, U, V, coefficients = four_cross_both_outer()
    field = RationalFunctionField((p, m, ratio, e))
    a, b, c = coefficients
    relations = []
    for j in range(6):
        column = {i: field.from_sympy(source[i, j]) for i in range(16)}
        relations.append({i: value for i, value in column.items() if value})
    for i in range(4):
        for j in range(4):
            assert not field.from_sympy(U[i]*V[j]-V[i]*U[j]-source[4*i+j, 4])

    quadratic = {}
    for i, j in product(range(4), repeat=2):
        coefficient = field.from_sympy(a*U[i]*U[j]+b*U[i]*V[j]+c*V[i]*V[j])
        if coefficient:
            quadratic[4*i+j] = coefficient
    rows = [{16*j+i: co for i, co in relation.items()} for relation, j in product(relations, range(4))]
    rows += [{4*i+j: co for i, co in relation.items()} for relation, j in product(relations, range(4))]
    targets = []
    for gen in range(4):
        target = {16*gen+i: co for i, co in quadratic.items()}
        for i, co in quadratic.items():
            key = 4*i+gen
            target[key] = target.get(key, field.zero)-co
        targets.append({i: co for i, co in target.items() if co})

    columns = defaultdict(set)
    active = dict(enumerate(rows))
    for i, row in active.items():
        for j in row:
            columns[j].add(i)

    def score(position):
        i, j = position
        value = active[i][j]
        unit = value.n.is_constant() and value.d.is_constant()
        return (not unit, (len(active[i])-1)*(len(columns[j])-1),
                len(value.n)+len(value.d), i, j)

    def subtract(vector, row, column):
        if column not in vector:
            return vector
        output = dict(vector)
        scale = output.pop(column)
        for i, coefficient in row.items():
            if i != column:
                value = output.get(i, field.zero)-scale*coefficient
                if value:
                    output[i] = value
                else:
                    output.pop(i, None)
        return output

    rank = 0
    while active:
        i, j = min(((i, j) for i, row in active.items() for j in row), key=score)
        row = active.pop(i)
        pivot = {k: value/row[j] for k, value in row.items()}
        for k in row:
            columns[k].remove(i)
        for k in list(columns[j]):
            old = active.pop(k)
            for index in old:
                columns[index].remove(k)
            new = subtract(old, pivot, j)
            if new:
                active[k] = new
                for index in new:
                    columns[index].add(k)
        targets = [subtract(target, pivot, j) for target in targets]
        rank += 1
    assert rank == 44 and not any(targets)
    print("PASS FDC3 degree-three relation span, rank 44, all four commutators zero")


def check_product_plane():
    source, _, _, _ = four_cross_both_outer()
    s = (p+m)/2
    h, k = Q(1, 64)-p*p/4, Q(1, 64)-m*m/4
    P, M, L = sym.symbols("P M L")
    moving = sym.Matrix([[4*p+1, 1-4*p], [1-4*m, 4*m+1]]).inv()
    block = sym.Matrix([[1, 0, 0, 0], [0, 1/s, 0, 0],
                        [h/s, -1/s, 1, 0], [k/s, -1/s, 0, 1]])
    change = sym.diag(1/(64*s), 1, moving)*block
    field = RationalFunctionField((p, m, ratio, e))
    tensor = sym.kronecker_product(change, change)
    rows = [{j: field.from_sympy(tensor[i, j]) for j in range(16) if tensor[i, j]}
            for i in range(16)]
    relations = []
    for column in range(source.cols):
        vector = {j: field.from_sympy(source[j, column])
                  for j in range(source.rows) if source[j, column]}
        transformed = {}
        for i, row in enumerate(rows):
            value = sum((co*vector[j] for j, co in row.items() if j in vector), field.zero)
            if value:
                transformed[i] = value
        relations.append(transformed)
    engine = PivotAlgebra(field, 4, [], [0]*4)
    engine.pivot_product = field.one
    pivots = engine.echelon(relations)
    assert len(pivots) == 6
    assert not engine.reduce({1: field.one, 11: field.one}, pivots)
    assert not engine.reduce({4: field.one, 11: field.one}, pivots)

    mixed = (P*P-1)*(M*M-1)*L*L+2*P*M*L+1
    factors = sym.prod(1+(P+i)*(M+j)*L for i, j in product((-1, 1), repeat=2))
    assert sym.expand(mixed*mixed-4*L*L-factors) == 0
    print("PASS FDC3 product relations and split quadric discriminant")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--product-plane", action="store_true")
    if parser.parse_args().product_plane:
        check_product_plane()
    else:
        check()
