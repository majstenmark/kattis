import sys
data = sys.stdin.read().strip().split()
itr = (item for item in data)


T = int(next(itr))
for t in range(T):
    L, N = int(next(itr)), int(next(itr))
    ants = [int(next(itr)) for v in range(N)]
    if N == 0:
        print('0 0')
        continue
    ants.sort()
    shortest = 0
    for ant in ants:
        edge = min(ant, L - ant)
        shortest = max(shortest, edge)
    longest = max(L - ants[0], ants[-1])
    print('{} {}'.format(shortest, longest))