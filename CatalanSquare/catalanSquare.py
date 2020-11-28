N = input()
Q = N + 1
res = [1 for _ in range(Q + 1)]
val = 1
for n in range(1, Q+1):
    val = val * 2 * n * (2 * n - 1) /((n + 1)*n)
    res[n] = val
print res[Q]
