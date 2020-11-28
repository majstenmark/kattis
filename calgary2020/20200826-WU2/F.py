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

S0 = [ord(c) - ord('A') for c in inp()]
S1 = [ord(c) - ord('A') for c in inp()]

out = []
for i, (m, k) in enumerate(zip(S0, S1)):
    mul = -1 if i%2==0 else 1
    v = (m + mul*k)%26
    out.append(chr(v + ord('A')))
print(''.join(out))

