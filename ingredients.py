from collections import deque

B = input()
N = input()
names = {}
edges= []
if N == 0:
    print '0'
    print '0'
    exit()
for n in range(N):
    line = raw_input().split()
    rec,base, cost, prestige = line[0], line[1], int(line[3]), int(line[4])
    if base not in names:
        names[base] = len(names)
    if rec not in names:
        names[rec] = len(names)
    recId = names[rec]
    baseId = names[base]
    edges.append((baseId, recId, cost, prestige))

sz = len(names)
topsort = [0] * sz
parents = [[] for _ in range(sz)]
dec = [[] for _ in range(sz)]

for base, rec, cost, prestige in edges:
    parents[rec].append((base, cost, prestige))
    dec[base].append(rec)
    topsort[rec] += 1

q = deque([])
INF = 10**12
costpres = [(INF, 0) for _ in range(sz)]
for n in range(sz):
    if topsort[n] == 0:
        q.append(n)
        costpres[n] = (0, 0)
sorted = []
while q:
    n = q.popleft()
    sorted.append(n)
    for d in dec[n]:
        topsort[d] -= 1
        if topsort[d] <= 0:
            q.append(d)
for n in sorted:
    cost = costpres[n][0]
    prestige=costpres[n][1]
    for b, c, p in parents[n]:
        if costpres[b][0] + c < cost:
            cost = costpres[b][0] + c
            prestige = costpres[b][1] +p
        if costpres[b][0] + c == cost:
            prestige = max(prestige, costpres[b][1] + p)
    costpres[n] = (cost, prestige)
#print names

#print sorted
#print costpres
#Knapsack
DP = [[0] * sz for _ in range(B+1)] # budget and items as keys. Value is max prestige
if costpres[0][0] <= B:
    DP[costpres[0][0]][0] = costpres[0][1]

for b in range(B+1):
    for r in range(1, sz):
        DP[b][r] = DP[b][r-1]

        if b >= costpres[r][0]:
            pres_if_picked = DP[b - costpres[r][0]][r-1] + costpres[r][1]
            DP[b][r] = max(DP[b][r], pres_if_picked)
MAXPRES = DP[-1][-1]
MAXCOST = B

for b in range(B, -1, -1):
    pres = DP[b][-1]
    if pres == MAXPRES:
        MAXCOST = b
    else:
        break
print MAXPRES
print MAXCOST
