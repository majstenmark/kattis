from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]

T = ni()
for _ in range(T):
    V = nl()[1:]
    no = 1
    for v in V:
        no += v - 1
    print(no)