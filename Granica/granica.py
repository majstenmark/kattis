import math

def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return b if a % b == 0 else gcd(b, a % b)

def getGlobalGCD(nbrs):
    if len(nbrs) == 1:
        return nbrs[0]
    g = gcd(nbrs[0], nbrs[1])
    for nbr in nbrs[2:]:
        g = gcd(g, nbr)
    return g

def getAllDivisors(g):
    c = int(math.sqrt(g))
    divs = set()
    for t in range(2, c+1):
        if g % t == 0:
            divs.add(t)
            divs.add(g/t)
    divs.add(g)
    return divs

N =int(raw_input())
vals = [int(raw_input()) for _ in range(N)]
vals.sort(reverse = True)
diffs = []
for index in range(N-1):
    diffs.append(vals[index] - vals[index+1])

G = getGlobalGCD(diffs)
#print G
divs = getAllDivisors(G)
print ' '.join(map(str, divs))
