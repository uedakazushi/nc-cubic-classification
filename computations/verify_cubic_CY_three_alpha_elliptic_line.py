"""Check the flex-point syzygy and quadratic coefficient for elliptic lines.

All identities are exact over Q[p,q,r,u].  This checks a local coefficient
identity used in the line-module argument; it does not verify properness,
the global line-bundle degree, or the complete H3 admissibility theorem.
"""

import sympy as sp


def main():
    p, q, r, u = sp.symbols("p q r u")
    # Letters x,y,z are encoded by 0,1,2.  Free words are tuples of letters.
    relations = [
        {(1, 2): p, (2, 1): q, (0, 0): r},
        {(2, 0): p, (0, 2): q, (1, 1): r},
        {(0, 1): p, (1, 0): q, (2, 2): r},
    ]
    ell1 = sp.Matrix([1, 1, 0])
    ell2 = sp.Matrix([0, 0, 1])
    m1 = sp.Matrix([p * r, q * r, p * q])
    m2 = sp.Matrix([q**2, p**2, r**2])

    # m1*(x+y) + m2*z = p*r1 + q*r2 + r*r3 in the free algebra.
    residual = {}
    for i in range(3):
        for j in range(3):
            residual[i, j] = m1[i] * ell1[j] + m2[i] * ell2[j]
    for coefficient, relation in zip((p, q, r), relations):
        for word, value in relation.items():
            residual[word] -= coefficient * value
    assert all(sp.expand(value) == 0 for value in residual.values())

    # Modulo L=<x+y,z>, evaluation is at P=(1:-1:0).  This direction
    # annihilates the linear equation before solving for c1,c2.
    alpha1, alpha2 = (p + q) * u, r * u
    linear = alpha1 * m1 + alpha2 * m2
    assert sp.expand(linear[0] - linear[1]) == 0
    c1, c2 = -sp.expand(linear[0]), -sp.expand(linear[2])
    assert all(sp.expand(value) == 0 for value in linear + c1 * ell1 + c2 * ell2)

    quadratic = sp.expand(c1 * alpha1 + c2 * alpha2)
    expected = -r * ((p + q)**3 + r**3) * u**2
    assert sp.expand(quadratic - expected) == 0

    # At (p,q,r)=(1,2,3), replace the parameter u by u/3 to use
    # the manuscript's normalized direction (alpha1,alpha2)=(u,u).
    normalized = sp.expand(quadratic.subs({p: 1, q: 2, r: 3, u: u / 3}))
    assert normalized == -18 * u**2

    print("PASS exact free-word syzygy m1*ell1 + m2*ell2 = p*r1 + q*r2 + r*r3")
    print("PASS exact affine-line direction and its two compensating coefficients")
    print("PASS quadratic coefficient = -r*((p+q)**3+r**3)*u**2")
    print("PASS normalized (1,2,3) coefficient = -18*u**2")


if __name__ == "__main__":
    main()
