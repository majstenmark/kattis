from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]

A = ni()
op = inp()
B = ni()
print(eval('{}{}{}'.format(A, op, B)))