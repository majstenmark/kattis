R, C = [int(v) for v in raw_input().split()]
grid = [list(raw_input()) for i in range(R)]
cnt = [0] * 5
for r in range(R-1):
    for c in range(C-1):
        spaces = [grid[r][c], grid[r+1][c], grid[r][c+1], grid[r+1][c+1]]
        houses = spaces.count('#')
        if houses == 0:
            cars = spaces.count('X')
            cnt[cars] += 1
for i in range(len(cnt)):
    print(cnt[i])
    
