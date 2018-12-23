from __future__ import division
from fractions import gcd

class Rational(object):
    def __init__(self, numer, denom):
        GCD = gcd(numer, denom)
        self.numer = int(numer / GCD)
        self.denom = int(denom / GCD)

        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = (self.numer * other.denom) + (other.numer * self.denom)
        return Rational(numer, other.denom * self.denom)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), self.denom)

    def __pow__(self, power):
        return Rational(pow(self.numer, power), pow(self.denom, power))

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    def __neg__(self):
        return Rational(self.numer*(-1), self.denom)

