#NOT FINISHED
import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def gauss(A, b, monoid=None):
    def Z(v): return abs(v) < 1e-6 if not monoid else v.isZ()

    N = len(A[0])
    for i in range(N):
        try:
            m = next(j for j in range(i, N) if Z(A[j][i]) == False)
        except:
            return None #A is not independent!
        if i != m:
            A[i], A[m] = A[m], A[i]
            b[i], b[m] = b[m], b[i]
        for j in range(i+1, N):
            sub = A[j][i]/A[i][i]
            b[j] -= sub*b[i]
            for k in range(N):
                A[j][k] -= sub*A[i][k]

    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            sub = A[i][j]/A[j][j]
            b[i] -= sub*b[j]
        b[i], A[i][i] = b[i]/A[i][i], A[i][i]/A[i][i]
    return b

N = ni()
plaintext = inp()
cypher = inp()

txt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
MAP1 = {}
for i, lt in enumerate(txt):
    MAP1[lt] = i

def todigs(text):
    digits = []
    for lt in text:
        digits.append(MAP1[lt])
    return text

def tovectors(digs):
    vectors = [[]]
    for d in digs:
        if len(vectors[-1]) == N:
            vectors.append([])
        if len(vectors[-1]) < N:
            vectors[-1].append(d)
    return vectors

plain = todigs(plaintext)
in_vecs = tovectors(plain)
cyph = todigs(cypher)
out_vecs = tovectors(cyph)
seen = set()
unique = []
for i, v in enumerate(in_vecs):
    t = tuple(v)
    if t not in seen:
        unique.append((v, out_vecs[i]))

if len(unique) < N:
    print('Too many solutions')
    exit()

tot = N*N
b = [0] * tot
A = [[0] * tot for _ in range(len(unique))]
