"""Check arithmetic and geometric monodromy of the degree-eight discriminant."""
import json
from pathlib import Path

from flint import nmod_poly
import sympy as sp

from verify_cubic_CY_three_alpha_elliptic_diagonal import (
    AffineWords,
    cohomology,
    homotopies,
    sample,
)


def evaluate_diagonal(scales):
    relations, cubic = sample(scales)
    algebra = AffineWords(relations)
    polynomial, _ = cohomology(algebra, cubic, homotopies(algebra, relations, cubic))
    return polynomial


def reduce_rational(coefficient, prime):
    return int(coefficient.numerator) * pow(int(coefficient.denominator), -1, prime) % prime


def arithmetic_cycle_types(polynomial):
    factors_over_q = polynomial.factor()[1]
    assert len(factors_over_q) == 1 and factors_over_q[0][0].degree() == 8
    types = {}
    for prime, expected in ((5, [1, 7]), (17, [2, 3, 3])):
        reduced = nmod_poly([reduce_rational(c, prime) for c in polynomial.coeffs()], prime)
        factors = reduced.factor()[1]
        assert all(multiplicity == 1 for _, multiplicity in factors)
        degrees = sorted(factor.degree() for factor, _ in factors)
        assert degrees == expected
        types[str(prime)] = degrees
    print("PASS specialization gives a 7-cycle and a permutation with a transposition power", flush=True)
    return types


def interpolate_slice(prime):
    values = []
    for diagonal_entry in range(25):
        polynomial = evaluate_diagonal((1, 2, diagonal_entry))
        values.append([reduce_rational(c, prime) for c in polynomial.coeffs()])
        print("Interpolation value", diagonal_entry, flush=True)

    variable = nmod_poly([0, 1], prime)
    basis = []
    for i in range(25):
        term = nmod_poly([1], prime)
        denominator = 1
        for j in range(25):
            if i != j:
                term *= variable - j
                denominator = denominator * (i - j) % prime
        basis.append(pow(denominator, -1, prime) * term)

    coefficients = []
    for exponent in range(9):
        coefficient = sum((value[exponent] * term for value, term in zip(values, basis)),
                          nmod_poly([], prime))
        assert coefficient.degree() <= 3 * (8 - exponent)
        coefficients.append(coefficient)
    return coefficients


def check_odd_multiplicity(prime, coefficients):
    parameter, eigenvalue = sp.symbols("a lambda")
    expression = sum(int(value) * parameter**j * eigenvalue**i
                     for i, coefficient in enumerate(coefficients)
                     for j, value in enumerate(coefficient.coeffs()))
    discriminant = sp.Poly(expression, eigenvalue, parameter, modulus=prime).discriminant()
    discriminant = sp.Poly(discriminant, parameter, modulus=prime)
    reduced = nmod_poly([int(discriminant.nth(i)) for i in range(discriminant.degree() + 1)], prime)
    factors = reduced.factor()[1]
    witness = nmod_poly([21, 9, 22, 2, 1], prime)
    assert (witness, 3) in factors
    # Evaluate the multivariate discriminant independently at unused interpolation points.
    for value in range(25, prime):
        polynomial = nmod_poly([int(coefficient(value)) for coefficient in coefficients], prime)
        expected = int(sp.Poly.from_list(list(reversed([int(c) for c in polynomial.coeffs()])),
                                         eigenvalue, modulus=prime).discriminant()) % prime
        assert int(reduced(value)) == expected
    print("PASS the characteristic-zero discriminant on the slice is not a square", flush=True)
    return {
        "prime": prime,
        "odd_factor_ascending": [int(c) for c in witness.coeffs()],
        "odd_factor_multiplicity": 3,
        "reduced_factor_degrees_and_multiplicities": sorted(
            [factor.degree(), multiplicity] for factor, multiplicity in factors
        ),
    }


def main():
    certificate = {
        "arithmetic_cycle_types": arithmetic_cycle_types(evaluate_diagonal((1, 2, 4))),
        "slice_a11_a22_fixed_at_1_2": check_odd_multiplicity(37, interpolate_slice(37)),
    }
    path = Path(__file__).with_name("cubic_CY_three_alpha_elliptic_monodromy_certificate.json")
    path.write_text(json.dumps(certificate, indent=2) + "\n")


if __name__ == "__main__":
    main()
