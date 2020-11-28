R,C = [int(v) for v in raw_input().split()]
grid = [[''] * C for _ in range(R)]
dirs = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1), 'T': (-1, -1)}
for r in range(R):
    line = raw_input()
    for c in range(C):
        grid[r][c] = dirs[line[c]]
visited = set()
curr = 0,0
visited.add(curr)
steps = 0
while True:
    dir = grid[curr[0]][curr[1]]
    if dir == (-1, -1):
        print(steps)
        exit()
    steps += 1
    curr = curr[0] + dir[0], curr[1] + dir[1]
    if curr in visited:
        #loop
        print('Lost')
        exit()
    #print(steps,curr)
    if not (0 <= curr[0] < R and 0 <= curr[1] < C):
        print('Out')
        exit()
    visited.add(curr)

    
