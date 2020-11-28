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

k, m, n = nl()
r = k%(m+n)
if r < m:
    print("Barb")
else:
    print("Alex")

