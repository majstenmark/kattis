N = int(input())
grid = [input() for _ in range(N)]
def check(grid):
    for r in range(N):
        w = 0
        b = 0
        lastw = 0
        lastb = 0
        for c in range(N):
            if grid[r][c] == 'W':
                w += 1
                conseq = c - lastb
                if conseq >= 3:
                    return False
                lastw = c
            else:
                b += 1
                conseq = c - lastw
                if conseq >= 3:
                    return False
                lastb = c
        if w != b:
            return False
    return True

def flip(grid):
    new_grid = [[''] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            new_grid[c][r]  = grid[r][c]
    return new_grid

if check(grid) and check(flip(grid)):
    print(1)
else:
    print(0)



