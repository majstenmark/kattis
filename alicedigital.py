import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def solve(Ns, M):
    li = [0, 0]
    seenM = 0
    mx = 0
    for i in Ns:
        if i > M:
            li[seenM] += i
        elif i == M:
            if seenM :
                alt = li[0] + M + li[1]
                mx = max(mx,alt)
            li = [li[seenM], 0]
            seenM = 1
        else:
            #i < M
            if seenM == 1:
                alt = li[0] + M + li[1]
                mx = max(mx,alt)
            seenM = 0
            li = [0, 0]
    if seenM  == 1:
    
        alt = li[0] + M + li[1]
        mx = max(mx,alt)
    return mx


T = ni()
for _ in range(T):
    N, M = nl()
    Ns = nl()
    print(solve(Ns, M))