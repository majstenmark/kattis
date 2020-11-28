from collections import deque
n, k = map(int, raw_input().split())
reqs = []
for t in range(n):
    ti = int(raw_input())
    reqs.append(ti)
servers = deque([])
maxlen = 0
for t in reqs:
    while len(servers)>0 and servers[0] + 1000 <= t:
        servers.popleft()
    servers.append(t)
    needed = (len(servers) + k-1)/k
    maxlen = max(needed, maxlen)
print(maxlen)
