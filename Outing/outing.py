N, K = map(int, raw_input().split())
deps = map(lambda x: int(x) -1, raw_input().split())
# find cycles
cycles = {}
WHITE = -1
colors = [WHITE for _ in range(N)]
depth = [0 for _ in range(N)]
singleNodes = []

def traverse(startnode):
    color = startnode
    n = startnode
    depth[n] = 1
    #print 'node ', n, 'dep', deps[n]
    path = [n]
    while colors[n] == WHITE:
        colors[n] = color
        prev = n
        n = deps[n]
        path.append(n)
        if colors[n] == color:
            #a cycle!
            existing = False
            size = depth[prev] - depth[n] + 1
            if size > 1:
                cycles[color] = [size, depth[prev]]
            else:
                singleNodes.append(depth[prev])
                for node in path:
                    colors[node] = colors[n]
            return
        depth[n] = depth[prev] + 1
    # merged into an existing ending
    #print 'here!, color', colors[n], 'colors', colors[n]
    for node in path:
        colors[node] = colors[n]

    if colors[n] in cycles:
    #    print 'adding', depth[prev], 'to ', cycles[colors[n]]
        cycleSize = cycles[colors[n]][0]
        totSize = cycles[colors[n]][1] + depth[prev]
        cycles[colors[n]] = [cycleSize, totSize]

        #print cycles
    else:

        singleNodes.append(depth[prev])

for node in range(N):
    if colors[node] == WHITE:
        traverse(node)
free = 0
for s in singleNodes:
    free += s

if free >= K:
    print K
    exit(0)
# for each k,
# for each item
# save max v + dp[k - v, n-1], dp[k, n -1], that is max k
# update uppwards
cycleList = []
#print cycles
n = len(cycles)
cycleList.extend(cycles.values())

dp = [[0]*(n + 1) for _ in range(K+1)]
for k in range(K + 1):
    for index,cycle in enumerate(cycleList):
        c = cycle[0]
        v = cycle[1]
        maxV = 0
        if k-c >= 0:
            maxV = v + dp[k-c][index -1]
        dp[k][index] = max(maxV, dp[k][index - 1])
maxK = max(dp[-1])
maxK = min(K, free  + maxK)

print maxK
