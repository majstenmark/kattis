from fractions import Fraction
s = input()
a, b = map(int, s.split('/'))
f = Fraction(a, b)
c = (f - Fraction(32,1)) * Fraction(5, 9)
d, e = c.numerator, c.denominator
print('{}/{}'.format(d, e))