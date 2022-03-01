from collections import *
import sys
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def nf(): return [float(v) for v in inp().split()]
def ni(): return int(inp())

SHIFT = 2251
C = Counter()
SZ = SHIFT*2
R, Q = nl()
add_cols = [[0]*SZ for _ in range(SZ)]
add_rows = [[0]*SZ for _ in range(SZ)]
def add(dd, x, y0, yN, c):
    dd[x][y0] += c
    dd[x][yN] -= c
for _ in range(R):
    x, y, w, h, c = nl()
    x, y = x + SHIFT, y + SHIFT
    add(add_rows, x, y, y+h, c)
    add(add_rows, x+w, y, y+h, c)
    add(add_cols, y, x, x+w, c)
    add(add_cols, y+h, x, x+w, c)

grid_row = [[0]*SZ for _ in range(SZ)]
for x in range(SHIFT*2):
    add = 0
    for y in range(SHIFT*2):
        add += add_rows[x][y]
        grid_row[x][y] += add
grid_col = [[0]*SZ for _ in range(SZ)]
for y in range(SHIFT*2):
    add = 0
    for x in range(SHIFT*2):
        add += add_cols[y][x]
        grid_col[x][y] += add

def test_print():
    for x in range(SHIFT - 1, SHIFT + 4):
        for y in range(SHIFT - 1, SHIFT + 4):
            print(grid[x][y], end=' ')
        print('')

PREF_row = [[0]*(SZ+1) for _ in range(SZ+1)]
PREF_col = [[0]*(SZ+1) for _ in range(SZ+1)]
for x in range(1, SZ+1):
    for y in range(1, SZ+1):
        a = PREF_row[x-1][y]
        b = PREF_row[x][y-1]
        c = PREF_row[x-1][y-1]
        d = grid_row[x-1][y-1]
        PREF_row[x][y] = d + a + b - c
for x in range(1, SZ+1):
    for y in range(1, SZ+1):
        a = PREF_col[x-1][y]
        b = PREF_col[x][y-1]
        c = PREF_col[x-1][y-1]
        d = grid_col[x-1][y-1]
        PREF_col[x][y] = d + a + b - c

out = []
for _ in range(Q):
    x0, y0, w, h = nl()
    x, y = x0 + SHIFT, y0 + SHIFT
    A = PREF_col[x][y] + PREF_row[x][y]
    B = PREF_col[x+w][y] + PREF_row[x+w+1][y]
    C = PREF_col[x][y+h+1] + PREF_row[x][y+h]
    D = PREF_col[x+w][y+h+1] + PREF_row[x+w+1][y+h]
    SM = D + A - B - C 
    '''
    L = []
    for dx in range(w+1):
        for dy in range(h):
            L.append(grid_row[x+dx][y+dy])
    for dx in range(w):
        for dy in range(h + 1):
            L.append(grid_col[x+dx][y+dy])
    print(sum(L), SM, x0, y0, w, h,  L)
    '''
    out.append(str(SM))
print('\n'.join(out))



