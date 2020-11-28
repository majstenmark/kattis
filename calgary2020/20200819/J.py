from collections import *
import sys
try: inp = raw_input
except: inp = input
def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

def place_horiz(f_grid, pos, sz):
    if pos%N + sz > N: return None
    new_f = f_grid
    for i in range(pos, pos + sz):
        x = 1<<(i + pos)
        if new_f & x: return None
        new_f |= x
    return new_f

def place_vert(f_grid, pos, sz):
    row = pos//N
    new_f = f_grid
    if row + sz > N: return None
    for i in range(pos, pos + sz*N, N):
        x = 1<<i
        if new_f & x: return None
        new_f |= x
    return new_f



def genShips(ships, f_grid, pos):
    if len(ships) == 0: return [f_grid]
    if pos == N**2: return []
    O = []
    for s in set(ships):
        v = list(ships)
        v.remove(s)
        new_grid = place_horiz(f_grid, pos, s)
        if not new_grid is None:
            MORE = genShips(v, new_grid, pos+1)
            O.extend(MORE)
        if s > 1:
            new_grid = place_vert(f_grid, pos, s)
            if not new_grid is None:
                MORE = genShips(list(v), new_grid, pos+1)
                O.extend(MORE)
    O.extend(genShips(ships, f_grid, pos+1))
    return O 
N, K = nl()
G = [inp() for _ in range(N)]
fg = []
for l in G: fg.extend(l)
print(fg)
ships = [ni() for _ in range(K)]
V = genShips(ships, 0, 0)
print(len(V))
cnt = 0
exit()
for v in V:
    print(bin(v).count('1'), v)
    ok = True
    for i in range(N*N):
        if fg[i] == '.': continue
        if fg[i] == 'X':
            if v & (1<<i):
                ok = False
                break
        if fg[i] == 'O':
            if v & (1<<i) == 0:
                ok = False
                break
    if ok:
        cnt += 1
print(cnt)


