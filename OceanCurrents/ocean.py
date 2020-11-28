from collections import deque

R, C = map(int, raw_input().split())
ocean = [[0] * C for _ in range(R)]
id = 0
for r in range(R):
    for c in range(C):
        ocean[r][c] = id
        id += 1

g = [[] for _ in range(id)]
all = [[] for _ in range(id)]


for r in range(R):
    line = raw_input()
    for c in range(C):
        this = ocean[r][c]
        dir = line[c]
        if dir == '0' and r-1 >= 0:
            g[ocean[r-1][c]].append(this)
        if dir == '1' and r-1 >= 0 and c+1 < C:
            g[ocean[r-1][c+1]].append(this)
        if dir == '2' and c+1 < C:
            g[ocean[r][c+1]].append(this)
        if dir == '3' and r+ 1 < R and c+1 < C:
            g[ocean[r+1][c+1]].append(this)
        if dir == '4' and r+ 1 < R:
            g[ocean[r+1][c]].append(this)
        if dir == '5' and r+ 1 < R and c-1 >= 0:
            g[ocean[r+1][c-1]].append(this)
        if dir == '6' and c-1 >= 0:
            g[ocean[r][c-1]].append(this)
        if dir == '7' and r- 1 >= 0 and c-1 >= 0:
            g[ocean[r-1][c-1]].append(this)
        for rn in range(max(0, r-1), min(R, r+2)):
            for cn in range(max(0, c-1), min(C, c+2)):
                if rn != r or cn != c:
                    all[ocean[rn][cn]].append(this)


def zobfs(startid, destid, N):
    # go backwards from destid
    INF = 10**12
    dist = [INF] * N
    dist[destid] = 0
    q = deque([destid])
    while q:
        curr = q.popleft()
        if curr == startid:
            return dist[curr]

        for zeronode in g[curr]:
            if dist[zeronode] > dist[curr]:
                q.appendleft(zeronode)

                dist[zeronode] = dist[curr]
        for onenode in all[curr]:

            if dist[onenode] > dist[curr] + 1:
                dist[onenode] = dist[curr] + 1

                q.append(onenode)
    return -1


trips = input()
for trip in range(trips):
    rs, cs, rd, cd = map(int, raw_input().split())
    startid = ocean[rs-1][cs-1]
    destid = ocean[rd-1][cd-1]
    energy = zobfs(startid, destid, id)
    print energy
