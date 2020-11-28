def knapsack(items, totstorage):
    bestvalues = [[0] * (totstorage + 1) for _ in xrange(len(items) +1)]
    # app nbr, used storage
    # nbr of apps, last app index, last app size 
    for i, (_, index, download, storage) in enumerate(items):
        i += 1
        for used in xrange(totstorage + 1):
            if used + max(download, storage) <= totstorage:
                noinstall = bestvalues[i-1][used]
                val = noinstall + 1
                bestvalues[i][used + storage] = max(bestvalues[i][used+storage], val)
            bestvalues[i][used] = max(bestvalues[i][used] , bestvalues[i-1][used])

    reconstruction = []
    used = 0
    
    for u in xrange(totstorage+1):
        if bestvalues[-1][u] > bestvalues[-1][used]:
            used = u
    
    for i in range(len(items), 0, -1):
        if bestvalues[i][used] > bestvalues[i-1][used]:
            reconstruction.append(items[i-1][1])
            used -= items[i-1][3]
    assert used == 0
    
    reconstruction.reverse()

    return reconstruction

N, C = map(int, raw_input().split())
apps = []
for n in range(N):
    d, s = map(int, raw_input().split())
    apps.append((d,s))
diff = []
for index, (d,s) in enumerate(apps):
    r = s - d
    diff.append((r, index +1, d, s))
#print diff
diff.sort()

rec = knapsack(diff, C)
print len(rec)
if len(rec) > 0:
    print ' '.join(map(str, rec))
