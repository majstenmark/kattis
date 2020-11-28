import sys

tokens = (int(t) for t in sys.stdin.read().split())

#START = 'L'
#WALL = '#'
#ROOM = '.'
INF = 2#10**12
X = next(tokens)

def sign(value):
    return -1 if value < 0 else 1 if value > 0 else 0

while X > -1:
    # testcase
    Y = next(tokens)
    T = next(tokens)
    L = next(tokens)
    W = next(tokens)

    # for each testcase!
    q = []
    visited = [[INF for xxx in range(Y)] for _ in range(X)]
    for leak in range(L):
        x = next(tokens) -1
        y = next(tokens) -1
        q.append((x, y))
        visited[x][y] = 1

    for wall in range(W):
        x1 = next(tokens) -1
        y1 = next(tokens) -1
        x2 = next(tokens) -1
        y2 = next(tokens) -1

        xstep = sign(x2 - x1)
        ystep = sign(y2 - y1)


        x = x1
        y = y1
        visited[x][y] = -1
        while x != x2 or y != y2:
                x += xstep
                y += ystep
                visited[x][y] = -1
    time = 0
    count = 0
    while q and time < T:
        q2 = []
        count += len(q)
        for (x, y) in q:

            candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for (nx, ny) in candidates:
                if 0 <= nx < X and 0 <= ny < Y and visited[nx][ny] == INF:
                    visited[nx][ny] = 1
                    q2.append((nx, ny))

        q = q2
        time += 1
    print(count)

    X = next(tokens)
