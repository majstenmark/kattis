N = input()
bonds  = []
for n in range(N):
    probs = map(lambda x: float(x)*0.01, raw_input().split())
    bonds.append(probs)
missions = [-1 for n in range(2 ** N)]
missions[0] = 1

def assign(left, n):
    if missions[left] > -1:
        return missions[left]
    m = 0
    for i in range(N):
        if (1<< i) & left != 0:
            leftNext = left - (1<< i)
            res = assign(leftNext, n-1)
            m = max(bonds[n][i] * res, m)
    missions[left] = m
    return m

print assign(2 ** N -1, N-1) * 100
