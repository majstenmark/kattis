import math

N = input()
L, W = map(int, raw_input().split())
D = L * 1.0/(N/2 -1)
S = N/2
W2 =W **2
def right(t, n):
    dx = abs(t - n * D)
    return math.sqrt(dx **2 + W2)

def left(t, n):
    return abs(t - n * D)

pos = []
for n in range(N):
    pos.append(input())
pos.sort()
#print pos
INF = 10**12
dist = [[INF] * (S+1) for _ in range(S+1)]
dist[0][0] = 0

for r in range(S + 1):
    for l in range(S + 1):
        index = r + l
        if index == N:
            break
        treepos = pos[index]
    #    print 'tree', treepos
        toLeft = left(treepos, l) + + dist[r][l]
        toRight = right(treepos, r) + dist[r][l]
        if r + 1 <= S:

            dist[r + 1][l] = min(dist[r + 1][l], toRight)

#            print 'toRight', toRight, 'r', r +1, 'new val', dist[r + 1][l]
        if l + 1 <= S:

            dist[r][l+1] = min(dist[r][l+1], toLeft)

#            print 'toleft', toLeft, 'l', l+1, 'new val', dist[r][l+1]
#print dist
print dist[S][S]
