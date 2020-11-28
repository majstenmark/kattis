from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s): sys.stderr.write('{}\n'.format(s))
def ni(): return int(inp())
def nl(): return [int(_) for _ in inp().split()]

from fractions import Fraction
N, Q = nl()

US = [nl() for _ in range(N)]
for _ in range(Q):
    x, y, v = nl()
    a_x, b_x = US[x-1]
    c = Fraction(100*(v-a_x), b_x-a_x)
    a_y, b_y = US[y-1]
    R = c*Fraction(b_y - a_y, 100) + a_y
    print('{}/{}'.format(R.numerator, R.denominator))
