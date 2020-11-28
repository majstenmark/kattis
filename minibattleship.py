from copy import copy, deepcopy

N, K = [int(v) for v in raw_input().split()]
grid = [list(raw_input()) for _ in range(N)]
ships= [int(raw_input()) for _ in range(K)]
orig = deepcopy(grid)

DP= {} #r,c, length = cnt



def okHorizontal(r, c, shipL, shipId, grid):
    ok = True
    for cc in range(c, c + shipL):
        if cc >= N:
            return False
        elif not (grid[r][cc] == '.' or grid[r][cc] == 'O'):
            return False

    for cc in range(c, c+ shipL):
        grid[r][cc] = str(shipId)
    return ok
        
def okVertical(r, c, shipL, shipId, grid):
    ok = True
    for rr in range(r, r + shipL):
        if rr >= N:
            return False
        elif not (grid[rr][c] == '.' or grid[rr][c] == 'O'):
            return False
    for rr in range(r, r + shipL):
        grid[rr][c] = str(shipId)
    return ok
        
def undoHorizontal(r, c, shipL, grid):
    for cc in range(c, c + shipL):
        grid[r][cc] = orig[r][cc]

def undoVertical(r, c, shipL, grid):
    for rr in range(r, r+ shipL):
        grid[rr][c] = orig[rr][c]

def printgrid(grid):
    for r in range(N):
        out = []
        for c in range(N):
            out.append(grid[r][c])
        print(''.join(out))
    print('')

def ok(grid):
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 'O':
                return 0
    return 1
    
def solve(shipId, grid):
    
    if shipId == K:
        res=ok(grid)
        #if res:
        #    printgrid(grid)
        return res

    
    shipL = ships[shipId]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if grid[r][c] == '.' or grid[r][c] == 'O':
                res = 0            
                if (r, c, shipL, 'H') in DP:
                    cnt += DP[(r, c, shipL, 'H')]
                elif okHorizontal(r, c, shipL, shipId, grid):
                    res = solve(shipId+1, grid)
                    undoHorizontal(r, c, shipL, grid)
                    DP[(r, c, shipL, 'H')] = res
                    cnt += res
                
                if (r, c, shipL, 'V') in DP:
                    cnt += DP[(r, c, shipL, 'V')]
                elif shipL > 1 and okVertical(r, c, shipL, shipId, grid):
                    res = solve(shipId+1, grid)
                    undoVertical(r, c, shipL, grid) 
                    DP[(r, c, shipL, 'V')] = res
                    cnt+=res

    return cnt           
      
cnt = solve(0, grid)
print(DP)
print(cnt)