N , S, R = [int(v) for v in raw_input().split()]
Si =[int(v)-1 for v in raw_input().split()]
Ri = [int(v)-1 for v in raw_input().split()]
Ri.sort()
#take own
broken = [False] * N
spare = [False] * N
for s in Si:
    broken[s] = True
for r in Ri:
    if not broken[r]:
        spare[r] = True
    else:
        broken[r] = False

INF = 10**12

def get_next():
    for r,v in enumerate(spare):
        if v:
            return r
    return INF

def assign():
    n = 0
    while n < N:
        if broken[n]:
            next_spare = get_next()
            if next_spare == INF:
                return
            if abs(next_spare -n) <= 1:
                #take it!
                spare[next_spare] = False
                broken[n] = False
            elif n > next_spare:
                spare[next_spare] = False
                #will try the same team again
            else:
                # it was too far ahead
                n += 1
        else:
            n+= 1
assign()
cnt = broken.count(True)
print(cnt)


