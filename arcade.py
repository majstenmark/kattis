import sys
from collections import defaultdict as dd

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nf(): return [float(v) for v in inp().split()]
def ni(): return int(inp())



# monoid needs to implement
# __add__, __mul__, __sub__, __div__ and isZ 
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

R = ni()
H = nl()
probs = [nf() for _ in range(len(H))]
arc = [[] for _ in range(R)]
index = 0
variables = {}
for k in range(R):
    for i in range(k+1):
        arc[k].append(H[index])
        variables[k, i] = index
        index += 1

g = dd(list)
for r in range(R):
    for c in range(r+1):
        alt = [(r-1, c-1), (r-1, c), (r+1, c), (r+ 1, c+ 1)]
        for rr, cc in alt:
            if 0 <= rr < R and 0 <= cc <= rr:
                g[r, c].append((rr, cc))
            else:
                g[r, c].append(None)
N = len(H)
#print(g)
A = [[0] * (N) for _ in range(N)]

b = [0.0] * (N)
for (r, c), li in g.items():
    i = variables[r, c]
    
    for k in range(4):
        if li[k] != None:
            rr, cc = li[k]
            j = variables[rr, cc]
            pij = probs[i][k]
            A[i][j] += pij
    
    
    b[i] = -probs[i][-1] * H[i]

for i in range(N):
    A[i][i] -= 1.0

X = gauss(A, b)
print(X[0])

