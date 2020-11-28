def draw(s, g):
    visited = set()
    visited.add(s)
    q = [s]
    g[s[0]][s[1]] = 'E'
    
    while q:
        q2 = []
        for r, c in q:
            cand = [(-1, 0), (1, 0), (0,1), (0, -1)]
            for dr, dc in cand:
                rr, cc = r + dr, c + dc
                if 0 <= rr < R and 0<= cc < C and g[rr][cc] == '.':
                    if (rr, cc) not in visited:
                        if g[r][c] != 'E':
                            g[rr][cc] = 'E'
                        visited.add((rr, cc))
                        q2.append((rr, cc))
        q = q2
    return visited


R, C = [int(v) for v in raw_input().split()]
grid = [[] for _ in range(R)]

for r in range(R):
    l = list(raw_input())
    grid[r] = l
vis = set()
for r in range(R):
    for c in range(C):
        if (r, c) not in vis and grid[r][c] == '.':
            v = draw((r, c), grid)
            vis |= v

for r in range(R):
    print(''.join(grid[r]))
