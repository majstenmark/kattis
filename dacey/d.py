T = int(raw_input())

def diceroll(dirX, dirY, down, right, north):
    if dirY == 1: # right
        return (right, 7 - down, north)
    if dirY == -1: #left
        return (7 - right, down, north)
    if dirX == - 1: # up
        return (north, right, 7 - down)
    return (7 - north, right, down) # down


def roll():
    N = int(raw_input())
    start = (0,0, 0, 0, 0)

    q = []
    forest = [['.' for c in range(N)] for r in range(N)]
    visited = set()
    for n in range(N):
        line = raw_input()
        for c in range(N):
            if line[c] == 'S':
                start = (n, c, 6, 2, 4)
                q.append(start)

                visited.add(start)
            if line[c] == 'H':
                home = (n, c, 5, 0, 0)
            #    s = 'Home is at {}, {} with {} down, {} right, {} north'.format(n, c, 5, 0, 0)
            #    print(s)

            forest[n][c] = line[c]
#    print(forest)
    found = False
    while q and not found:
        q2 = []
        for (x, y, down, right, north) in q:
        #    s = 'Looking at {}, {} with {} down, {} right, {} north'.format(x, y, down, right, north)
        #    print(s)
            if x == home[0] and y == home[1] and down == home[2]:
                found = True
                break
            dirs = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for (nx, ny) in dirs:
                if nx < 0 or nx >= N or ny < 0 or ny >= N or forest[nx][ny] == '*':
                    continue
                newDown, newRight, newNorth = diceroll(nx - x, ny - y, down, right, north)
                newpos = (nx, ny, newDown, newRight, newNorth)

                if not newpos in visited:
                    visited.add(newpos)
                #    s = 'Added {}, {} with {} down, {} right, {} north'.format(nx, ny, newDown, newRight, newNorth)
                #    print(s)
                    q2.append(newpos)
        q = q2
    if found:
        print('Yes')
    else:
        print('No')

for test in range(T):
    roll()
