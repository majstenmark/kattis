inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def test(mx, grid):
    start = []
    for r in range(R):
        if grid[r][0] <= mx:
            start.append((r, 0))
    end = set()
    for r in range(R):
        if grid[r][-1] <= mx:
            end.add((r, C-1))
    if len(start) == 0 or len(end) == 0:
        return False
    visited = set(start)
    q = start
    while q:
        q2 = []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r, c in q:
            if (r, c) in end:
                return True
            for dx, dy in dirs:
                nr, nc = r + dx, c + dy
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] <= mx:
                    if (nr, nc) not in visited:
                        q2.append((nr, nc))
                        visited.add((nr, nc))
        q = q2
    return False



R, C = nl()
grid = [nl() for _ in range(R)]
hi = 1000001
lo = 0
for _ in range(20):
    mid = (hi + lo)//2
    ok = test(mid, grid)
    if ok:
        hi = mid
    else:
        lo = mid

print(hi)