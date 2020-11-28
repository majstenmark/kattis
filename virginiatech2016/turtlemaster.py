from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s): sys.stderr.write('{}\n'.format(s))
def ni(): return int(inp())
def nl(): return [int(_) for _ in inp().split()]

def fail():
    print('Bug!')
    exit()

B = [list(inp()) for _ in range(8)]
prog = inp()
B[-1][0] = '.'
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y, d = 7, 0, 0
def inside(x, y):
    return (0 <= x < 8 and 0 <= y < 8)

def ok(x, y):
    if not inside(x, y): return False
    if B[x][y] == 'C': return False
    if B[x][y] == 'I': return False
    return True
for c in prog:
    if c == 'L':
        d = (d-1)%4
    if c == 'R':
        d = (d+1)%4
    if c == 'F':
        dx, dy = D[d]
        x, y = x + dx, y + dy
        if not ok(x, y):
            fail()
    if c == 'X':
        dx, dy = D[d]
        nx, ny = x + dx, y + dy
        if inside(nx, ny) and B[nx][ny] == 'I':
            B[nx][ny] = '.'
        else:
            fail()
        

if B[x][y] == 'D':
    print('Diamond!')
    exit()
else:
    fail()

