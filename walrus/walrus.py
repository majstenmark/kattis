def getBest():
    bestUnder = max(q[1000])
    diff = 1000 - bestUnder
    for row in range(1001, 1001+diff):
        best = max(q[row])
        if best == row:
            return best
    return bestUnder

N = int(raw_input())
ws = [0] +[int(raw_input()) for _ in range(N)]
q = [[0] * (N +1) for x in range(2001)]
for w in range(2001):
    for n in range(1, N + 1):
        if w - ws[n] >= 0:
            q[w][n] = max(ws[n] + q[w - ws[n]][n-1], q[w][n-1])
        else:
            q[w][n] = q[w][n-1]
#print(q)
best = getBest()
print(best)
