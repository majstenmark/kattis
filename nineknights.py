inp = input

def check(r, c, grid):
    pos = [(2, 1),(-2,1),(2,-1),(-2, -1), (1,2),(-1,2),(-1, -2), (1,-2)]
    for dr, dc in pos:
                nr = r +dr
                nc = c + dc
                if 0 <= nr < 5 and 0 <= nc < 5:
                    if grid[nr][nc] == 'k':
                        return False
    return True

grid = [inp() for _ in range(5)]
ks = 0
for r in range(5):
    for c in range(5):
        if grid[r][c] == 'k':
            ks += 1
            if not check(r, c, grid):
                print('invalid')
                exit()
if ks == 9:    
    print('valid')
else:
    print('invalid')