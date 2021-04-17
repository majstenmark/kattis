#from fractions import Fraction
import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

INF = 10**12

def floydWarshall(graph):
    V = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
 
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] * dist[k][j])
    return dist

def printsol(dist):
    for n in range(C):
        #print(dist[n][n])
        if dist[n][n] < 1:
            print('Arbitrage')
            return
    print('Ok')

C = ni()
while C != 0:
    curs = inp().split()
    ids = {c:i for i, c in enumerate(curs)}
    R = ni()
    g = [[INF] * C for _ in range(C)]
    for r in range(R):
        data = inp().split()
        c1 = ids[data[0]]
        c2 = ids[data[1]]
        a,b = map(int, data[2].split(':'))
        #backward edge
        g[c1][c2] = a/b
    
    dist = floydWarshall(g)
    printsol(dist)

    C = ni()
    

