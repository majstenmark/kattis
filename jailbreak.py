import sys
from collections import defaultdict as dd, deque
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def get4nb(node):
    r, c = node
    rmin = 0 
    rmax = R
    cmin = 0
    cmax = C
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    nb = []
    for dr, dc in diff:
        if rmin <= r + dr < rmax and cmin <= c + dc < cmax:
            nb.append((r+dr, c + dc))
    return nb 

def bfs(q, g):
    visited = set()
    dists = dd(lambda: 10**30)
    for node in q:

        visited.add(node)
        if grid[node[0]][node[1]] == '#':
            dists[node] = 1
        else:
            dists[node] = 0

    while q:
        node = q.popleft()
        for ne in get4nb(node):
            t = grid[ne[0]][ne[1]]
            if t == '*': continue
            
            if ne not in visited:
                visited.add(ne)
                    
                if t == '#':
                    dists[ne] = dists[node] + 1
                    q.append(ne)
                else:
                    dists[ne] = dists[node]
                    q.appendleft(ne)
                    
    return dists


T = ni()

for _ in range(T):
    R, C = nl()
    grid = [inp() for _ in range(R)]
    prisoners = []
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '$':
                prisoners.append((r, c))

    walls = deque()
    for r in range(R):
        if grid[r][0] == '#':
            walls.append((r, 0))
        
        if grid[r][C-1] == '#':
            walls.append((r, C-1))
        if grid[r][0] == '.' or grid[r][0] == '$':
            walls.appendleft((r, 0))
        
        if grid[r][C-1] == '.' or grid[r][C-1] == '$':
            walls.appendleft((r, C-1))


    for c in range(C):
        if grid[0][c] == '#':
            walls.append((0, c))
        if grid[R-1][c] == '#':
            walls.append((R-1, c))
        
        if grid[0][c] == '.' or grid[0][c] == '$':
            walls.appendleft((0, c))
        if grid[R-1][c] == '.' or grid[R-1][c] == '$':
            walls.appendleft((R-1, c))
    

    walldist = bfs(walls, grid)
    q1 = deque()
    q1.append(prisoners[0])
    p1dists = bfs(q1, grid)
    q2 = deque()
    q2.append(prisoners[1])
    p2dists = bfs(q2, grid)
    
    mn = 10**30
    for r in range(R):
        for c in range(C):
            if grid[r][c] != '*':
                su = walldist[r, c] + p1dists[r, c] + p2dists[r,c]
                if grid[r][c] == '#':
                    su -= 2
                mn = min(mn,su)
    print(mn)
