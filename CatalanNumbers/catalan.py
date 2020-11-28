Q = int(raw_input())
queries = []
maxQ = 0
for q in range(Q):
    N = int(raw_input())
    queries.append(N)
    maxQ = max(N, maxQ)
res = [1 for _ in range(maxQ + 1)]
val = 1
for n in range(1, maxQ+1):
    val = val * 2 * n * (2 * n - 1) /((n + 1)*n)
    res[n] = val
for q in queries:
    print(res[q])
