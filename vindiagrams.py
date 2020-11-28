def bfs(pos, g, fromch, toch, checkC):
    visited = set()
    visited.add(pos)
    q = [pos]
    while q:
        q2 = []
        for r, c in q:

            cand = [(-1, 0), (1, 0), (0, -1), (0,1)]
            for dr, dc in cand:
                rr = r + dr
                cc = c + dc
                if 0<= rr < R and 0 <= cc < C and (rr, cc) not in visited:
                    if g[rr][cc] == fromch:
                        visited.add((rr, cc))
                        g[rr][cc] = toch
                        q2.append((rr, cc))
                    if checkC and g[rr][cc] == 'C':
                        visited.add((rr, cc))
                        visited.add((r + 2 * dr, c + 2 * dc))
                        g[r + 2 * dr][c+ 2 * dc] = toch
                        q2.append((r + 2 * dr, c + 2 * dc))
                
        q = q2
    return visited

def intersects(r, c):
    if r == 0 or c == 0 or r == R -1 or c == C-1:
        return False
    return (grid[r][c] == 'X' and grid[r-1][c] == 'X' and 
        grid[r+1][c] == 'X' and grid[r][c-1] == 'X' and grid[r][c+1] == 'X' and
        grid[r-1][c-1] == '.' and grid[r-1][c+1] == '.' and grid[r+1][c+1] == '.' and grid[r+1][c-1] == '.') 


def fill(pos, fromch, toch):
    bfs(pos, grid, fromch, toch, True)    

def floodfill(pos):
    vis = bfs(pos, grid, '.', '.', False)
    return len(vis)

def getinside(rc):
    cand = [(-1, -1), (-1, 1), (1, -1), (1,1)]
    r, c= rc
    inside = -1,-1
    aside= -1,-1
    bside=-1, -1
    for dr, dc in cand:
        if grid[r + dr][c +dc] == 'O':
            inside = r - dr, c - dc
    cand2 = [(-1, 0), (1, 0), (0, -1), (0,1)]
    for dr, dc in cand2:
        ir, ic = inside
        if grid[ir+dr][ic+dc] == 'A':
            bside = ir + 2 * dr,ic + 2 * dc
        if grid[ir+dr][ic+dc] == 'B':
            aside = ir + 2 * dr,ic + 2 * dc
    return inside, aside, bside

uR, uC = [int(v) for v in raw_input().split()]
grid = [['.'] * (uC + 2)]
for r in range(uR):
    li = ['.'] + list(raw_input()) + ['.']
    grid.append(li)
grid.append(['.'] * (uC + 2))

R, C, = uR + 2, uC + 2

apos = 0, 0
bpos= 0,0
cross = []
for r in range(R):
    for c in range(C):
        if intersects(r, c):
            grid[r][c] = 'C'
            cross.append((r, c))
        if grid[r][c] == 'A':
            apos = r, c
        if grid[r][c] == 'B':
            bpos = r,c

fill(apos, 'X', 'A')
fill(bpos, 'X', 'B')
fill((0, 0), '.', 'O')
inside, aside,bside = getinside(cross[0])
Acnt =floodfill(aside)
Bcnt= floodfill(bside)
Ccnt = floodfill(inside)

print('{} {} {}'.format(Acnt, Bcnt, Ccnt))


