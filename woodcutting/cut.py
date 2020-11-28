T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    pieces  = []
    for line in range(N):
        w = sum([int(v) for v in raw_input().split()[1:]])
        pieces.append(w)
    pieces.sort()
    total = 0.0
    for n in range(N):
        total += pieces[n] * (N-n)
    av = total/N
    print(av)
