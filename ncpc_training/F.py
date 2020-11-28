from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]
import math

def solve(t, a, b):
    if t == 1: return False
    if a%b != 0: return False
    if a == b: return 1
    exp = a - b
    # t**(a - b) <= 10**100
    # a - b <= 100/log_10(t)

    high = 200/math.log(t, 10)
    if exp > high:
        return False
    k = 0
    pw = 1
    for i in range(a//b):
        k += pw
        pw *= t**b
    if k < 10**99:
        return k
    return False
    


for line in sys.stdin:
    t, a, b = map(int, line.split())
    s = solve(t, a, b)
    expr = '({}^{}-1)/({}^{}-1)'.format(t, a, t, b)
    if s == 0:
        print(expr, 'is not an integer with less than 100 digits.')
    else:
        print(expr, s)