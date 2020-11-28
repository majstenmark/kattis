def redist(pos,node):
    scale = 1.0- pos[node]
    pos[node] = 0
    for n in range(N):
        pos[n] = pos[n]/scale
    return pos

def redistMeet(pos, node0, dieProb):
    scale = 1.0 - dieProb
    pos[node0] -= dieProb

    for n in range(N):
        pos[n] = pos[n]/scale
    return pos

def mult(P, pos):
    post = [0] * N
    for r in range(N):
        for e in range(N):
            post[e] += P[r][e] * pos[r]
    return post

N = input()
L = input()
walk = map(int, raw_input().split())
adj = []
M = 0.0
degs = []
for n in range(N):
    ni = map(int, raw_input().split())
    deg = ni[0]
    M += deg
    adjli = [0] * N
    prob = 1.0/deg
    for ne in ni[1:]:
        adjli[ne] = prob
    adj.append(adjli)
    degs.append(deg)

prob = [0] *N
for n in range(N):
    prob[n] = degs[n]/M



survive = 1.0

for step in range(len(walk) -1):
    survStep  = 1 - prob[walk[step]]
    prob = redist(prob, walk[step])
    dieMeeting = prob[walk[step+1]] * 1.0/degs[walk[step+1]]
    survMeet = 1 - dieMeeting
    prob = mult(adj, prob)
    prob = redistMeet(prob,walk[step], dieMeeting)
    survive *= survStep * survMeet

survStep  = 1 - prob[walk[-1]]
survive *=survStep
print survive
