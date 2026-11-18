"""First-order central-lift obstruction for three singular symmetric alpha types."""
from itertools import product

import sympy as s


def words(length):
    return list(product(range(3), repeat=length))


def insertions(relations, degree):
    result = []
    for length in range(degree-1):
        for prefix in words(length):
            for suffix in words(degree-2-length):
                for index, relation in enumerate(relations):
                    result.append((
                        {prefix+word+suffix: value for word, value in relation.items()},
                        prefix+(index,)+suffix,
                        index,
                    ))
    return result


def row(coefficients, degree):
    return s.Matrix([[coefficients.get(word, 0) for word in words(degree)]])


def source_projection(relations, degree):
    """Record original insertion rows and the fixed rational quotient projection."""
    source = insertions(relations, degree)
    matrix = s.Matrix.vstack(*(row(relation, degree) for relation, _, _ in source))
    independent_rows = matrix.T.rref()[1]
    independent = matrix.extract(independent_rows, range(3**degree))
    pivot_words = independent.rref()[1]
    pivot_inverse = independent.extract(range(len(independent_rows)), pivot_words).inv()
    assert 3**degree-len(independent_rows) == {3: 10, 4: 15}[degree]

    def coefficients(vectors):
        return vectors.extract(range(vectors.rows), pivot_words)*pivot_inverse

    def project(vectors):
        return vectors-coefficients(vectors)*independent

    return [source[i] for i in independent_rows], coefficients, project


def commutator(generator, element, degree):
    return (
        row({(generator,)+word: value for word, value in element.items()}, degree)
        - row({word+(generator,): value for word, value in element.items()}, degree)
    )


def verify(name, relations, volume):
    _, _, project3 = source_projection(relations, 3)
    selected, coefficients4, project4 = source_projection(relations, 4)
    blocks = []
    for generator in range(3):
        comparison = commutator(generator, volume, 4)
        assert project4(comparison) == s.zeros(1, 81)
        coefficients = coefficients4(comparison)
        derivatives = s.zeros(3, 27)
        for k, (_, word, index) in enumerate(selected):
            derivatives[index, :] += coefficients[k]*row({word: 1}, 3)
        corrections = s.Matrix.vstack(*(
            commutator(generator, {word: 1}, 3)
            for word in words(2) if word[0] <= word[1]
        ))
        blocks.append(project3(derivatives.col_join(corrections)))
    equations = s.Matrix.hstack(*blocks)
    assert equations.rank() == 6
    assert all(vector[:3] == [0, 0, 0] for vector in equations.T.nullspace())
    print("PASS", name, "all three linear deformation coefficients vanish")


def main():
    b, c, d = range(3)
    cb = {(c, b): 1, (b, c): 1}
    dc = {(d, c): 1, (c, d): 1}
    bd = {(b, d): 1, (d, b): 1}
    base = {(b, c, d): 1}
    verify("triangle", [dc, bd, cb], base)
    verify("nodal", [dc | {(b, b): 6}, bd | {(c, c): 6}, cb],
           base | {(b, b, b): 3, (c, c, c): -3})
    verify("secant conic", [dc, bd, cb | {(d, d): 6}], base | {(d, d, d): 3})


if __name__ == "__main__":
    main()
