inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def dists(pack, t):
    d = []
    for t0, v in pack:
        d.append((t -t0) * v)
    return d

N = ni()
pack = [nl() for _ in range(N)]
lo = max(pack)[0]
hi = 10**10
for _ in range(200):
    m1 = (lo * 2 + hi)/3.0
    m2 = (lo + 2 * hi)/3.0
    d1 = dists(pack, m1)
    d2 = dists(pack, m2)
    sc1 = max(d1) - min(d1)
    sc2 = max(d2) - min(d2)
    if sc1 < sc2:
        hi = m2
    else:
        lo = m1

print(sc1)