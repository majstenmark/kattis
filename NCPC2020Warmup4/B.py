inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

import sys

itr = (line for line in sys.stdin.read().split('\n'))
firstline = next(itr).split()
M, N = int(firstline[0]), int(firstline[1])
ch = firstline[2][1]
im1 = [list(next(itr)) for m in range(M)]
next(itr)
im2 = [list(next(itr)) for m in range(M)]
bg = [['' for _ in range(N)] for _ in range(M)]
S = set()
T = set()
for r in range(M):
    for c in range(N):
        if im1[r][c] != ch:
            bg[r][c] = im1[r][c]
        else:
            S.add((r, c))
        if im2[r][c] != ch:
            bg[r][c] = im2[r][c]
        else:
            T.add((r, c))
     
A = min(S)
B = min(T)
dx = B[0] - A[0]
dy = B[1] - A[1]
R = set()
for x, y in T:
    R.add((x + dx, y + dy))
for x, y in R:
    if 0<= x < M and 0 <= y < N:
        bg[x][y] = ch
print('\n'.join(''.join(row) for row in bg))

