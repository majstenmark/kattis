

P = int(raw_input())
rg = []
gg = []
pairs = []
found = set()
next=[]
for p in range(P):

    K, N = map(int, raw_input().split())
    red = map(int, raw_input().split())
    green = map(int, raw_input().split())
    rg = [[] for _ in range(N)]
    gg = [[] for _ in range(N)]
    for u, v in enumerate(red):
        rg[v].append(u)
    for u, v in enumerate(green):
        gg[v].append(u)

    pairs = [(i, i) for i in range(N)]
    found = set(pairs)
    while pairs:
        next = []
        for u, v in pairs:
            for incoming_u in rg[u]:
                for incoming_v in rg[v]:
                    t = min(incoming_u, incoming_v), max(incoming_u, incoming_v)

                    if t in found:
                        continue
                    found.add(t)
                    next.append(t)
            for incoming_u in gg[u]:
                for incoming_v in gg[v]:
                    t = min(incoming_u, incoming_v), max(incoming_u, incoming_v)

                    if t in found:
                        continue
                    found.add(t)
                    next.append(t)
            
        pairs = next

    solved = len(found) == N * (N-1)/2 + N
 
    if solved:
        print('{} YES'.format(p+1))
    else:
        print('{} NO'.format(p+1))
    