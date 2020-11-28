from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]

prog = inp()
cnt = 0
nops = 0
for c in prog:
    if c.upper() == c:
        add = (-cnt)%4     
        cnt += add
        nops += add
    cnt += 1
print(nops)