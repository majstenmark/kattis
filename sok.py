import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

A, B, C = nl()
I, J, K = nl()
no = min(A/I, B/J, C/K)
a = max( 0, A - no * I)
b = max( 0, B - no * J)
c = max( 0, C - no * K)
print('{:.6f} {:.6f} {:.6f}'.format(a, b, c))

