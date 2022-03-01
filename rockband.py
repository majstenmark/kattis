import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nl1(): return [int(v)-1 for v in inp().split()]
def ni(): return int(inp())

M, S = nl()
prefs = [nl1() for _ in range(M)]
song_mx = [0] * S
for li in prefs:
    for index, s in enumerate(li):
        song_mx[s] = max(song_mx[s], index+1)
cnt = [0] * (S+1)
for mx in song_mx:
    cnt[mx] += 1

def printres(tot, mx):
    out = []
    for s, v in enumerate(song_mx):
        if v <= mx:
            out.append(str(s+1))
    print(tot)
    print(' '.join(out))

tot = 0
for mx, no in enumerate(cnt):
    tot += no
    if tot > 0 and tot == mx:
        #found
        printres(tot, mx)
        exit()