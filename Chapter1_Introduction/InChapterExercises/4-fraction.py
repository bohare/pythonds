# coding: utf-8
"""A class representing fractions and various methods which can be called on them."""


def gcd(m, n):
    # Finds the Greatest Common Divisor of two numbers
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    """def show(self):
        print(self.num, "/", self.den)"""

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __sub__(self, other):
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __div__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

    def __gt__(self, other):
        newnum_self = self.num * other.den
        newnum_other = self.den * other.num

        return newnum_self > newnum_other

    def __lt__(self, other):
        newnum_self = self.num * other.den
        newnum_other = self.den * other.num

        return newnum_self < newnum_other


#Sample fractions
x = Fraction(1, 2)
y = Fraction(2, 3)

#Results
print('The first fraction is: {}'.format(x))
print('The second fraction is: {}'.format(y))
print('Addition result: {}'.format(x + y))
print('Subtraction result: {}'.format(x - y))
print('Multiplication result: {}'.format(x * y))
print('Division result: {}'.format(x / y))
print('Whether x and y are equal: {}'.format(x == y))
print('Whether x is greater than y: {}'.format(x > y))
print('Whether x is smaller than y: {}'.format(x < y))
