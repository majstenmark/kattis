C, R = map(int, raw_input().split())
OBST = '#'
GRAVEL= '.'
ICE = '_'
GOAL = 'M'
q = []

# h, u, v, n
maze = [[] for ii in range(R)]
dist = [[-1 for i in range(C)] for ii in range(R)]
for i in range(R):
    line = raw_input()
    for ch in range(C):
        if line[ch] == GOAL:
            q.append((i, ch))
            dist[i][ch] = 0
            maze[i].append(GRAVEL)
        else:
            maze[i].append(line[ch])

def slide(origX, origY, deltaX, deltaY, q):
    origX = x
    origY = y
    nx = origX + deltaX
    ny = origY + deltaY
    while maze[nx][ny] == ICE:
        if dist[nx][ny] == -1:
            dist[nx][ny] = dist[origX][origY] + 1
            q.append((nx, ny))

        nx = nx + deltaX
        ny = ny + deltaY
    if maze[nx][ny] == GRAVEL and dist[nx][ny] == -1:
        dist[nx][ny] = dist[origX][origY] + 1
        q.append((nx, ny))

while  q:
    q2 = []
    for (x, y) in q:
        candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        mirror = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for i in range(4):
            (nx, ny) = candidates[i]
            (x_m, y_m) = mirror[i]
            if maze[x][y] == ICE and maze[x_m][y_m] == OBST:

                slide(x, y, nx -x, ny - y, q2)

            if maze[x][y] == GRAVEL and maze[nx][ny] == ICE:
                slide(x, y, nx -x, ny - y, q2)

            if maze[x][y] == GRAVEL and maze[nx][ny] == GRAVEL and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1

                q2.append((nx, ny))
    q = q2
out = []
for r in dist:
    s = ' '.join(map(str, r))
    out.append(s)

print('\n'.join(out))
