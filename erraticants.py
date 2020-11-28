inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def solve(s):
    edges = set()
    curr = (0, 0)
    dirs = {'N': (0, -1),'S': (0, 1), 'W': (-1, 0), 'E': (1, 0)}
    for _ in range(s):
        d = inp()
        delta = dirs[d]
        nxt = (curr[0] + delta[0], curr[1] + delta[1])
        edges.add((curr, nxt))
        edges.add((nxt, curr))
        curr = nxt
    q = [(0,0)]
    visited = set([(0, 0)])
    steps = -1
    while q:
        q2 = []
        for sq in q:
            if sq == curr:
                q2 = []
                break
            for d in [(0,1), (0, -1), (-1, 0), (1, 0)]:
                nxt = sq[0] + d[0], sq[1] + d[1]
                if (sq, nxt) in edges and nxt not in visited:
                    visited.add(nxt)
                    q2.append(nxt)
        q = q2
        steps += 1
    print(steps)


N = ni()

for n in range(N):
    inp()
    s = ni()
    solve(s)