from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

s, t, n = nl()
D = nl()
b = nl()
c = nl()

t0 = s + D[0]
for i in range(n):
    cc = c[i]
    v = (t0 + cc - 1)//cc*cc
    t0 = v + D[i+1]

if t0 <= t:
    print('yes')
else:
    print('no')

