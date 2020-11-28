def bfs(start, g):
    g[start[0]][start[1]] = 'V'
    q = [start]
    while q:
        q2 = []
        for r, c in q:
            candidates = [(r-1, c), (r + 1, c), (r, c+1), (r, c-1)]
            for ne_r, ne_c in candidates:
                if 0 <= ne_r < R and 0 <= ne_c < C:
                    if g[ne_r][ne_c] == 'L' or g[ne_r][ne_c] == 'C':
                        g[ne_r][ne_c] = 'V'
                        q2.append((ne_r, ne_c))
        q = q2
    

R, C = [int(v) for v in raw_input().split()]
grid = [list(raw_input()) for _ in range(R)]
lands = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'L':
            lands.append((r, c))
cnt = 0
for r, c in lands:
    if grid[r][c] == 'L':
        cnt += 1
        bfs((r, c), grid)
print(cnt)

