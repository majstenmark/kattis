import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

a, b, c = nl()
a, b = max(a, b), min(a, b)
res = a * (b/c)
print("{:.10f}".format(res))