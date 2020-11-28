P = 1181118711931201
x = 360000

def my_hash(p, L):
    pHash = 0
    for k in range(L):
        pHash *= x
        pHash += p[k]
        pHash %= P
    return pHash

def match(dists2x, distsOrig, L):
    X = pow(x, (L -1), P)
    haOrig = my_hash(distsOrig, L)
    ha = my_hash(dists2x, L)

    for first in range(L):
        ha -= (dists2x[first] * X)
        ha *= x
        ha += dists2x[first + L]
        ha %= P
        if haOrig == ha:
            return True

    return False

L = int(raw_input())
origClock = map(int, raw_input().split())
secondClock = map(int, raw_input().split())
origClock.sort()
secondClock.sort()
distOrig = [(origClock[(i+1)%L] - origClock[i])%360000 for i in range(L)]
dist2nd = [(secondClock[(i+1)%L] - secondClock[i])%360000 for i in range(L)]
dists2x = dist2nd * 2
if match(dists2x, distOrig, L):
    print('possible')
else:
    print('impossible')
