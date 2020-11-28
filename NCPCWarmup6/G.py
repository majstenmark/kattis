inp = input
def nl(): return [int(v) for v in inp().split()]
def nf(): return [float(v) for v in inp().split()]
def ni(): return int(inp())

import itertools
import math

def test(p1, p2, v1, v2, a, T):

    dx = math.cos(a) * v2 * T
    dy = math.sin(a) * v2 * T
    nx, ny = p2[0] + dx, p2[1] + dy
    dist = ((nx - p1[0])  ** 2 + (ny - p1[1]) ** 2)
    ok = dist <= (v1 * T)**2
    #print('dist', dist, 'v1', v1, p1)
    #print('test time ', T, nx, ny, ok)
    if ok:
        return ok, (nx, ny)
    else:
        return False, None

def catch(p1, p2, v1, v2, a, best):
    lo = 0
    hi = best
    pos = p1
    for i in range(30): 
        mid = (lo + hi)/2
        ok, p =  test(p1, p2, v1, v2, a, mid)
        if ok:
            hi = mid
            pos = p
        else:
            lo = mid
    return hi, pos

def time(order, seniors, V, besttime):
    pos = 0, 0
    currtime = 0
    timetobus = 0
    
    for p in order:
        x, y, v, a = seniors[p]
        #print(x, y, v, a)
        dx = math.cos(a) * v * currtime
        dy = math.sin(a) * v * currtime
        xp, yp = x + dx, y + dy
        dt, pos = catch(pos, (xp, yp), V, v, a, besttime)
        currtime += dt
        if currtime > besttime:
            return besttime
        #print('dt', dt)
        #print('pos', pos)
        disttobus = (pos[0]  ** 2 + pos[1] ** 2)**0.5
        timetobus = max(timetobus, currtime + disttobus/v)    
    

    return round(timetobus)


def solve(seniors, v):
    best = 10 ** 8
    index = [i for i in range(len(seniors))]
    for order in itertools.permutations(index):
        t = time(order, seniors, v, best)
        best = min(t, best)
    return best

N = ni()
while N != 0:
    v = float(inp())
    seniors= [nf() for _ in range(N)]
    print(solve(seniors, v))
    
    N = ni()