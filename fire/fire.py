n = int(raw_input())


FIRE = '*'
START = '@'
WALL = '#'
ROOM = '.'
INF = 10**12

for i in range(n):

    w, h = map(int, raw_input().split())
    q = []
    dist_to_fire = [[INF for x in range(w)] for _ in range(h)]
    time = [[-1 for x in range(w)] for _ in range(h)]
    room = [[] for _ in range(h)]
    for hh in range(h):
        line = raw_input()
        for ww in range(w):
            room[hh].append(line[ww])
            if line[ww] == FIRE:
                dist_to_fire[hh][ww] = 0
                q.append((hh, ww))
            if line[ww] == START:
                start = (hh, ww)

    while q:
        q2 = []
        for (x, y) in q:
            candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for (nx, ny) in candidates:
                if 0 <= nx < h and 0 <= ny < w and (room[nx][ny] == ROOM or room[nx][ny] == START):
                    if dist_to_fire[nx][ny] == INF:
                        dist_to_fire[nx][ny] = dist_to_fire[x][y] + 1
                        q2.append((nx, ny))
        q = q2
    
    # try to escape
    q = [start]
    time[start[0]][start[1]] = 0
    esc = False
    while q and not esc:
        q2 = []
        for (x, y) in q:
            if (0 == x or x == h -1 or 0 == y or y == w - 1) and (room[x][y] == ROOM or room[x][y] == START):
                esc = True
                print(str(time[x][y] + 1))
                break
            candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for (nx, ny) in candidates:
                if 0 <= nx < h and 0 <= ny < w and (room[nx][ny] == ROOM and dist_to_fire[nx][ny] > time[x][y] + 1):
                    if time[nx][ny] == -1:
                        time[nx][ny] = time[x][y] + 1
                        q2.append((nx, ny))

        q = q2

    if not esc:
        print("IMPOSSIBLE")
