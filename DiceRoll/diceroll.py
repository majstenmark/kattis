N, M = map(int, raw_input().split())
sums = [0 for v in range((M + 1) + (N+1))]
for m in range(1, M+1):
    for n in range(1, N + 1):
        val = m +n
        sums[val] += 1
maxVal = max(sums)
for index, v in enumerate(sums):
    if v == maxVal:
        print index
