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

N = ni()
x = nl()

cnt = 1
base = x[0]
for b in x[1:]:
    if b > base:
        cnt += 1
    base = b
print(cnt)
