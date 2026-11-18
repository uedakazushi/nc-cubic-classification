"""Replay the filtered relative diagonal through cohomological degree five."""
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path

from flint import fmpq, fmpq_mat, fmpq_poly
import sympy as sp

from cubic_sparse_hilbert import SparseGradedAlgebra


class RationalField:
    zero = fmpq(0)
    one = fmpq(1)


def rational(value):
    return fmpq(str(value))


def add(target, source, scale=1):
    for key, value in source.items():
        updated = target.get(key, 0) + scale * value
        if updated:
            target[key] = updated
        else:
            target.pop(key, None)
    return target


class AffineWords:
    def __init__(self, relations):
        homogenized = [{word+(3,)*(2-len(word)): value for word, value in row.items()}
                       for row in relations]
        homogenized += [{(3, i): RationalField.one, (i, 3): -RationalField.one}
                        for i in range(3)]
        self.source = SparseGradedAlgebra(RationalField, 4, homogenized, [0]*4)
        self.source.build(7)
        self.words = [tuple(tuple(v for v in word if v != 3) for word in self.source.basis[d])
                      for d in range(8)]
        for d, basis in enumerate(self.words):
            assert len(set(basis)) == len(basis) == (d+1)*(d+2)*(d+3)//6
            if d:
                assert set(self.words[d-1]).issubset(basis)

    @lru_cache(None)
    def normal(self, word):
        return {self.words[len(word)][i]: value for i, value in self.source.word(word).items()}

    @lru_cache(None)
    def pair_basis(self, degree):
        return [(a, b) for a in self.words[degree] for b in self.words[degree-len(a)]]

    @lru_cache(None)
    def pair_product(self, left, right):
        a, b = left
        c, d = right
        return {(ac, db): x*y for ac, x in self.normal(a+c).items()
                for db, y in self.normal(d+b).items()}

    def multiply(self, left, right):
        out = {}
        for a, x in left.items():
            for b, y in right.items():
                add(out, self.pair_product(a, b), x*y)
        return out

    def act(self, coefficients, word):
        out = {}
        for (left, right), value in coefficients.items():
            add(out, self.normal(left+word+right), value)
        return out

    def derivative(self, polynomial):
        derivatives = [{} for _ in range(3)]
        for word, value in polynomial.items():
            for j, letter in enumerate(word):
                for left, a in self.normal(word[:j]).items():
                    for right, b in self.normal(word[j+1:]).items():
                        add(derivatives[letter], {(left,right): value*a*b})
        return derivatives

    def matrix_product(self, left, right):
        result = [[{} for _ in right[0]] for _ in left]
        for i,j,k in product(range(len(left)), range(len(right[0])), range(len(right))):
            add(result[i][j], self.multiply(left[i][k], right[k][j]))
        return result


def matrix_difference(left, right):
    return [[add(dict(a), b, -1) for a, b in zip(arow,brow)] for arow,brow in zip(left,right)]


def is_zero(matrix):
    return not any(entry for row in matrix for entry in row)


def diagonal(size, entry):
    return [[dict(entry) if i==j else {} for j in range(size)] for i in range(size)]


def pivot_columns(matrix, rank):
    return [next(j for j in range(matrix.ncols()) if matrix[i,j]) for i in range(rank)]


def solve_many(matrix, values):
    rows, cols = matrix.nrows(), matrix.ncols()
    right_size = values.ncols()
    augmented = fmpq_mat(rows, cols+right_size,
                         [v for i in range(rows) for v in
                          [*[matrix[i,j] for j in range(cols)], *[values[i,j] for j in range(right_size)]]])
    reduced, rank = augmented.rref()
    pivots = pivot_columns(reduced, rank)
    assert all(j < cols for j in pivots)
    result = fmpq_mat(cols, right_size)
    for i,j in enumerate(pivots):
        for k in range(right_size):
            result[j,k] = reduced[i,cols+k]
    assert matrix*result==values
    return result


def lift_rows(ops, differential, targets, degree):
    source, output = len(differential), len(differential[0])
    previous, next_ = ops.pair_basis(degree), ops.pair_basis(degree+1)
    source_keys = tuple(product(range(source), previous))
    target_keys = tuple(product(range(output), next_))
    lookup = {key:i for i,key in enumerate(target_keys)}
    matrix = fmpq_mat(len(target_keys), len(source_keys))
    for j,(i,word) in enumerate(source_keys):
        for k,entry in enumerate(differential[i]):
            for coefficient,value in ops.multiply({word:RationalField.one},entry).items():
                matrix[lookup[k,coefficient], j] = value
    right = fmpq_mat(len(target_keys),len(targets))
    for j,row in enumerate(targets):
        for k,entry in enumerate(row):
            for word,value in entry.items():
                right[lookup[k,word],j] = value
    answer = solve_many(matrix,right)
    result = [[{} for _ in range(source)] for _ in targets]
    for j,(i,word) in enumerate(source_keys):
        for k in range(len(targets)):
            if answer[j,k]:
                result[k][i][word]=answer[j,k]
    assert ops.matrix_product(result,differential)==targets
    return result


def homotopies(ops, relations, cubic):
    d1 = [[{((i,), ()): RationalField.one, ((), (i,)): -RationalField.one}] for i in range(3)]
    d2 = [ops.derivative(relation) for relation in relations]
    d3 = [[d1[i][0] for i in range(3)]]
    differentials = {1:d1,2:d2,3:d3}
    assert is_zero(ops.matrix_product(d2,d1))
    assert is_zero(ops.matrix_product(d3,d2))

    difference = {}
    for word,value in cubic.items():
        for reduced, coefficient in ops.normal(word).items():
            add(difference, {(reduced,()):value*coefficient})
            add(difference, {((),reduced):-value*coefficient})
    s0 = [ops.derivative(cubic)]
    assert ops.matrix_product(s0,d1)==[[difference]]
    s1 = lift_rows(ops,d2,matrix_difference(diagonal(3,difference),ops.matrix_product(d1,s0)),2)
    s2 = lift_rows(ops,d3,matrix_difference(diagonal(3,difference),ops.matrix_product(d2,s1)),2)
    assert ops.matrix_product(d3,s2)==[[difference]]
    high_target = matrix_difference([[{}, {}, {}]], ops.matrix_product(s0,s1))
    high = lift_rows(ops,d3,high_target,3)
    assert is_zero(matrix_difference(ops.matrix_product(d1,high),
                                    matrix_difference([[{}],[{}],[{}]],ops.matrix_product(s1,s2))))
    print("PASS all relative diagonal homotopy identities",flush=True)
    return differentials, {0:s0,1:s1,2:s2}, high


RANKS = (1,3,3,1)


def hom_basis(ops, n):
    out = []
    for a in range(n//2+1):
        i = n-2*a
        if i <= 3:
            out.extend((a,j,word,len(word)-i-3*a)
                       for j in range(RANKS[i]) for word in ops.words[i+3*a])
    return out


def coboundary(ops, homotopy_data, source, target, n):
    differentials, homotopy, high = homotopy_data
    rows = {(a,j,w): i for i,(a,j,w,_) in enumerate(target)}
    result = fmpq_mat(len(target),len(source))
    for column,(a,j,word,_) in enumerate(source):
        for delta in (0,1,2):
            b = a+delta
            degree = n+1-2*b
            if degree < 0 or degree > 3:
                continue
            if delta==0:
                block=differentials.get(degree)
            elif delta==1:
                block=homotopy.get(degree)
            else:
                block=high if degree==0 else None
            if block is None:
                continue
            for i, row in enumerate(block):
                for output,value in ops.act(row[j],word).items():
                    result[rows[b,i,output],column] = value
    return result


def submatrix(matrix, rows, cols):
    return fmpq_mat(len(rows), len(cols), [matrix[i,j] for i in rows for j in cols])


def nullspace(matrix):
    reduced,rank=matrix.rref()
    pivots=pivot_columns(reduced,rank)
    free=[j for j in range(matrix.ncols()) if j not in pivots]
    result=fmpq_mat(matrix.ncols(),len(free))
    for k,j in enumerate(free):
        result[j,k]=1
        for i,p in enumerate(pivots):
            result[p,k]=-reduced[i,j]
    assert not any((matrix*result).entries())
    return result


def concatenate(left, right):
    assert left.nrows() == right.nrows()
    rows = [
        [left[i, j] for j in range(left.ncols())]
        + [right[i, j] for j in range(right.ncols())]
        for i in range(left.nrows())
    ]
    return fmpq_mat(rows)


def central_image(ops, cubic, basis, value):
    lookup = {(a, j, word): index for index, (a, j, word, _) in enumerate(basis)}
    source = [(a, j, word) for a, j, word, weight in basis if weight <= -3]
    operator = {(word, ()): coefficient for word, coefficient in cubic.items()}
    add(operator, {((), ()): -value})
    image = fmpq_mat(len(basis), len(source))
    for column, (a, j, word) in enumerate(source):
        for reduced, coefficient in ops.act(operator, word).items():
            image[lookup[a, j, reduced], column] = coefficient
    assert image.rank() == len(source)
    return image


def check_specialized_window(ops, cubic, bases, differentials, multiplication):
    dimensions = {}
    for value in (0, 1):
        images = [central_image(ops, cubic, basis, value) for basis in bases]
        ranks = []
        for differential, image in zip(differentials, images[1:]):
            ranks.append(concatenate(differential, image).rank() - image.ncols())
        dimension = len(bases[1]) - images[1].ncols() - sum(ranks)
        specialized = fmpq_mat(multiplication)
        for i in range(specialized.nrows()):
            specialized[i, i] -= value
        assert dimension == 8 - specialized.rank()
        dimensions[str(value)] = dimension
    return dimensions


def cohomology(ops, cubic, homotopy_data):
    bases=[hom_basis(ops,n) for n in (3,4,5)]
    d3,d4=[coboundary(ops,homotopy_data,bases[n-3],bases[n-2],n) for n in (3,4)]
    assert not any((d4*d3).entries())
    lower = [ [i for i,(*_,w) in enumerate(basis) if w<=-3] for basis in bases]
    d3_low=submatrix(d3,lower[1],lower[0])
    d4_low=submatrix(d4,lower[2],lower[1])
    cycles=nullspace(d4_low)
    rank=d3_low.rank()
    assert cycles.ncols()-rank==8
    count=len(lower[1])
    expanded=fmpq_mat(count,d3_low.ncols()+cycles.ncols(),
                      [v for i in range(count) for v in
                       [*[d3_low[i,j] for j in range(d3_low.ncols())],
                        *[cycles[i,j] for j in range(cycles.ncols())]]])
    reduced, total=expanded.rref()
    representatives=submatrix(cycles,list(range(count)),
                               [j-d3_low.ncols() for j in pivot_columns(reduced,total) if j>=d3_low.ncols()])
    assert representatives.ncols()==8
    rows = {(a,j,w): i for i,(a,j,w,_) in enumerate(bases[1])}
    low_in_high = fmpq_mat(len(bases[1]),8)
    translated = fmpq_mat(len(bases[1]),8)
    for i,index in enumerate(lower[1]):
        a,j,word,_ = bases[1][index]
        terms = ops.act({(mon, ()):c for mon,c in cubic.items()},word)
        for k in range(8):
            co=representatives[i,k]
            low_in_high[index,k] = co
            if co:
                for mon,value in terms.items():
                    translated[rows[a,j,mon],k] += co*value
    assert not any((d4*translated).entries())
    cols=fmpq_mat(len(bases[1]),d3.ncols()+8,
                  [v for i in range(len(bases[1])) for v in
                   [*[d3[i,j] for j in range(d3.ncols())], *[low_in_high[i,j] for j in range(8)]]])
    solution=solve_many(cols, translated)
    multiplication=submatrix(solution,list(range(d3.ncols(),d3.ncols()+8)), list(range(8)))
    dimensions = check_specialized_window(ops, cubic, bases, (d3, d4), multiplication)
    return multiplication.charpoly(), dimensions


def sample(scales):
    relations=[]
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        row={(j,k):rational(1), (k,j):rational(2), (i,i):rational(3)}
        if scales[i]:
            row[i,]=-rational(scales[i])
        relations.append(row)
    certificate = Path(__file__).with_name("cubic_CY_three_alpha_elliptic_character_boundary_certificate.json")
    entries=json.loads(certificate.read_text())["central_lift"]
    substitutions=dict(zip("q r a b c d e f".split(),[2,3,sp.Rational(str(scales[0])),0,sp.Rational(str(scales[1])),0,0,sp.Rational(str(scales[2]))]))
    cubic={}
    for word,value in entries.items():
        coefficient=rational(sp.sympify(value).subs(substitutions))
        if coefficient:
            add(cubic,{tuple("xyz".index(letter) for letter in word if letter!="t"):coefficient})
    return relations,cubic


def check_small_representations(relations, central, discriminant):
    x, y, z, inverse = sp.symbols("x y z inverse")
    traces = (x, y, z)

    def evaluate(polynomial, word_value):
        return sp.expand(sum(sp.Rational(str(value))*word_value(word)
                             for word, value in polynomial.items()))

    def scalar_value(word):
        return sp.prod(traces[i] for i in word)

    scalar_relations = [evaluate(relation, scalar_value) for relation in relations]
    hessian = sp.Matrix(scalar_relations).jacobian(traces)
    pairing = -hessian.adjugate()
    determinant = hessian.det()

    def matrix_trace(word):
        value = scalar_value(word)
        for i, j in combinations(range(len(word)), 2):
            factors = sp.prod(traces[word[k]] for k in range(len(word)) if k != i and k != j)
            value += pairing[word[i], word[j]]*factors
        if len(word) == 3:
            value -= sp.LeviCivita(*word)*determinant
        return value

    cases = (
        (scalar_value, scalar_relations, [], traces),
        (matrix_trace, [evaluate(relation, matrix_trace) for relation in relations],
         [inverse*determinant-1], (*traces, inverse)),
    )
    for word_value, equations, open_conditions, variables in cases:
        basis = sp.groebner(equations, *traces, order="grevlex", domain=sp.QQ)
        central_value = evaluate(central, word_value)
        remainder = 0
        for coefficient in reversed(discriminant.coeffs()):
            remainder = basis.reduce(sp.expand(remainder*central_value + sp.Rational(str(coefficient))))[1]
        empty = sp.groebner([*(entry.as_expr() for entry in basis.polys), remainder, *open_conditions],
                            *variables, order="grevlex", domain=sp.QQ)
        assert [entry.as_expr() for entry in empty.polys] == [1]
    print("PASS all eight roots have neither a character nor a two-dimensional simple", flush=True)


def main():
    certificate = {}
    for scales in ((0, 0, 0), (1, 1, fmpq(1,2)), (1, 2, 4)):
        relations, cubic = sample(scales)
        ops = AffineWords(relations)
        for i in range(3):
            left = ops.act({(word, (i,)): c for word, c in cubic.items()}, ())
            right = ops.act({((i,), word): c for word, c in cubic.items()}, ())
            assert left == right
        polynomial, dimensions = cohomology(ops, cubic, homotopies(ops, relations, cubic))
        if scales == (0, 0, 0):
            assert polynomial == fmpq_poly([0]*8+[1])
        elif scales == (1, 1, fmpq(1,2)):
            assert polynomial[0] == 0
        else:
            _, factors = polynomial.factor()
            assert len(factors) == 1 and factors[0][0].degree() == 8 and factors[0][1] == 1
            check_small_representations(relations, cubic, polynomial)
        key = ",".join(map(str, scales))
        certificate[key] = {
            "monic_coefficients_ascending": [str(c) for c in polynomial.coeffs()],
            "specialized_weight_zero_HH4_dimensions": dimensions,
        }
        print("PASS finite window specialization at zero and one", scales, dimensions, flush=True)
        print("PASS eight-dimensional discriminant", scales, polynomial.factor(), flush=True)
    certificate["1,2,4"]["character_ideal"] = [1]
    certificate["1,2,4"]["two_dimensional_simple_ideal"] = [1]
    path = Path(__file__).with_name("cubic_CY_three_alpha_elliptic_diagonal_certificate.json")
    path.write_text(json.dumps(certificate, indent=2)+"\n")


if __name__ == "__main__":
    main()
