N = int(raw_input())
nbrs = map(int, raw_input().split())
nbrs.sort()
intervals = []
currentInterval = [nbrs[0]]
intervals.append(currentInterval)

for n in range(1, N):
    if nbrs[n] == nbrs[n-1] + 1:
        currentInterval.append(nbrs[n])
    else:
        currentInterval = [nbrs[n]]
        intervals.append(currentInterval)
out = []
for interval in intervals:
    if len(interval)> 2:
        out.append(str(interval[0]) + '-' + str(interval[-1]))
    else:
        s = ' '.join(map(str, interval))
        out.append(s)
print(' '.join(out))