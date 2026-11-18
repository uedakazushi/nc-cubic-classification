"""Rational functions in three variables using FLINT multivariate polynomials."""
from flint import fmpq, fmpq_mpoly_ctx
import sympy as s

VARIABLES = s.symbols("p u w")
CONTEXT = fmpq_mpoly_ctx.get(tuple(map(str, VARIABLES)))


class RationalFunction:
    __slots__ = ("n", "d")

    def __init__(self, numerator=0, denominator=1):
        if not hasattr(numerator, "gcd"):
            numerator = CONTEXT.constant(numerator)
        if not hasattr(denominator, "gcd"):
            denominator = CONTEXT.constant(denominator)
        if not denominator:
            raise ZeroDivisionError("zero rational-function denominator")
        if not numerator:
            self.n = CONTEXT.constant(0)
            self.d = CONTEXT.constant(1)
            return
        common = numerator.gcd(denominator)
        leading = denominator.leading_coefficient()/common.leading_coefficient()
        self.n = (numerator//common)/leading
        self.d = (denominator//common)/leading

    def __bool__(self):
        return bool(self.n)

    def __neg__(self):
        return RationalFunction(-self.n, self.d)

    def __add__(self, other):
        if not isinstance(other, RationalFunction):
            other = RationalFunction(other)
        if not self:
            return other
        if not other:
            return self
        if self.d == other.d:
            return RationalFunction(self.n+other.n, self.d)
        common = self.d.gcd(other.d)
        left, right = self.d//common, other.d//common
        return RationalFunction(self.n*right+other.n*left, left*other.d)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        if not isinstance(other, RationalFunction):
            other = RationalFunction(other)
        if not self or not other:
            return RationalFunction()
        cross_left = self.n.gcd(other.d)
        cross_right = other.n.gcd(self.d)
        return RationalFunction((self.n//cross_left)*(other.n//cross_right),
                                (self.d//cross_right)*(other.d//cross_left))

    def __truediv__(self, other):
        return RationalFunction(self.n*other.d, self.d*other.n)


class RationalFunctions:
    zero = RationalFunction()
    one = RationalFunction(1)

    @staticmethod
    def from_sympy(expression):
        def polynomial(value):
            terms = s.Poly(value, *VARIABLES, domain=s.QQ).terms()
            return CONTEXT.from_dict({exponents: fmpq(int(coefficient.p), int(coefficient.q))
                                      for exponents, coefficient in terms})

        numerator, denominator = s.cancel(expression).as_numer_denom()
        return RationalFunction(polynomial(numerator), polynomial(denominator))
