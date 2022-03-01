from collections import *
try: inp = raw_input
except: inp = input
def ni(): return int(inp())
def nl(): return [int(x) for x in inp().split()]

N = ni()
L = [ni() for _ in range(N)]
print(sum(L) - len(L) + 1)