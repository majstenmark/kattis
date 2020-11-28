def nl():
    return [int(v) for v in raw_input().split()]
def nl2():
    return [int(v)-1 for v in raw_input().split()]

def ni():
    return int(raw_input())

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a,b = find(a), find(b)
    if a == b:
        return
    if size[a] > size[b]:
        parent[b] = a
        size[a] += size[b]
        su[a] += su[b]
    else:
        parent[a] = b
        su[b] += su[a]
        size[b] += size[a]

def round10(v):
    return v //10 * 10 + int(v % 10 > 0) * 10


N = ni()
psg = nl()
order = nl2()[::-1]
segs = 1

parent = [a for a in range(N)]
size = [1] * N
su = [p for p in psg]

chaos = round10(psg[order[0]])
current = chaos
alive = set([order[0]])
for car in order[1:]:
    diff = 1
    alive.add(car)
    diffc = 0
    if car -1 in alive:
        diffc -= round10(su[find(car-1)])
        union(car-1, car)
        diff -= 1
        
    if car + 1 in alive:
        diffc -= round10(su[find(car+1)])
        union(car, car+1)
        diff -= 1
    diffc += round10(su[find(car)])
    segs += diff
    current += diffc
    alt_chaos = current * segs
    chaos = max(alt_chaos, chaos)
print(chaos)


