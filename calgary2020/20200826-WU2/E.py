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

SCALE = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
NOT2ID = {v:k for k, v in enumerate(SCALE)}

def shift(A, i):
    return [SCALE[(NOT2ID[a] + i)%12] for a in A]


def transp(A, B):
    for i in range(12):
        if shift(A, i) == B:
            return True
    return False

def inv(A):
    out = []
    p = NOT2ID[A[0]]
    for a in A:
        p_a = NOT2ID[a]
        v = (p + (p - p_a))%12
        out.append(SCALE[v])
    return out


def inver(A, B):
    return inv(A) == B

l = ni()
A = inp().split()
B = inp().split()
if A == B[::-1]:
    print('Retrograde')
elif transp(A, B):
    print('Transposition')
elif inver(A, B):
    print('Inversion')
else:
    print('Nonsense')
