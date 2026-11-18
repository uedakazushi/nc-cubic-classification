"""Rational functions using FLINT multivariate polynomials."""
from flint import fmpq, fmpq_mpoly_ctx
import sympy as s

VARIABLES = s.symbols("p u w")


class RationalFunction:
    __slots__ = ("n", "d")

    def __init__(self, numerator, denominator):
        if not denominator:
            raise ZeroDivisionError("zero rational-function denominator")
        if not numerator:
            self.n = numerator
            self.d = numerator.context().constant(1)
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
        if not self:
            return self
        if not other:
            return other
        cross_left = self.n.gcd(other.d)
        cross_right = other.n.gcd(self.d)
        return RationalFunction((self.n//cross_left)*(other.n//cross_right),
                                (self.d//cross_right)*(other.d//cross_left))

    def __truediv__(self, other):
        return RationalFunction(self.n*other.d, self.d*other.n)


class RationalFunctionField:
    def __init__(self, variables):
        self.variables = variables
        self.context = fmpq_mpoly_ctx.get(tuple(map(str, variables)))
        one = self.context.constant(1)
        self.zero = RationalFunction(self.context.constant(0), one)
        self.one = RationalFunction(one, one)

    def from_sympy(self, expression):
        def polynomial(value):
            terms = s.Poly(value, *self.variables, domain=s.QQ).terms()
            return self.context.from_dict({
                exponents: fmpq(int(coefficient.p), int(coefficient.q))
                for exponents, coefficient in terms
            })

        numerator, denominator = s.cancel(expression).as_numer_denom()
        return RationalFunction(polynomial(numerator), polynomial(denominator))


RationalFunctions = RationalFunctionField(VARIABLES)
