import sys

itr = (line for line in sys.stdin.read().split('\n'))

N = int(next(itr))
adj = [[] for _ in range(N)]
for n in range(N):
    ln = map(int, next(itr).split()
    adj[n].append(ln)

DP = {}
def solve(l, r):
    k = (l + 1) % N
    while k != r:
        #add edge
        