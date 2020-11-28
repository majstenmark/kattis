N = input()
grid = [raw_input() for _ in range(N)]
ways = [[0] *N for _ in range(N)]
ways[0][0] = 1
BIG = 2**31 -1
for c in range(N):
    for r in range(N):
        if grid[r][c] == '.' :
            if  r + 1 < N:
                ways[r+1][c] += ways[r][c] % BIG

            if c + 1 < N:
                ways[r][c+1] += ways[r][c] % BIG
if ways[-1][-1] > 0:
    print ways[-1][-1] % BIG
    exit()

def bfs():
    visited = [[False] * N for _ in range(N)]
    q = [(0, 0)]
    visited[0][0] = True
    while q:
        q2 = []
        for x,y in q:
            if (x,y) == (N-1, N-1):
                return True
            cand = [(x+1, y), (x-1, y),(x, y+ 1), (x ,y-1)]
            for nx, ny in cand:
                if 0<=nx <N and 0 <= ny < N and grid[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q2.append((nx,ny))
        q = q2
    return False

canReach = bfs()
if canReach:
    print 'THE GAME IS A LIE'
else:
    print 'INCONCEIVABLE'
