import heapq

R, C = map(int, raw_input().split())
INF = 10**12
dist = [[INF]*C for v in range(R)]
door = 'D'
wall = '#'
car = 'c'
empty = 'E'
indoorMap = []

for rr in range(R):
    line = list(raw_input())
    for i in range(1, C -1, 1):
        if line[i] == 'D' and 0< rr < R - 1:
            line[i] = 'E'
    indoorMap.append(line)
r, c = map(lambda x: int(x) -1, raw_input().split())
# Dijkstra
pq = []
dist[r][c] = 1
pq.append((1, (r,c)))
heapq.heapify(pq)
done = False
while pq and not done:
    (nd, (nr,nc)) = heapq.heappop(pq)
    if indoorMap[nr][nc] == 'D':
        print(dist[nr][nc])
        exit(0)
    else:
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        for (dx, dy) in dirs:
            nx = nr + dx
            ny = nc + dy
            if not (0 <= nx < R and 0 <= ny < C): continue
            if indoorMap[nx][ny] == wall:
                continue
            dd = 1 if indoorMap[nx][ny] == car else 0
            alt = dist[nr][nc] + dd

            if dist[nx][ny] > alt:
                dist[nx][ny] = alt
                heapq.heappush(pq, (alt, (nx, ny)))
raise 'HelloError'
