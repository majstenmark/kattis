n, k, c= map(int, raw_input().split())
names = {}
g = [[] for _ in range(n)]
for i in range(n):
    name = raw_input()
    names[name] = i
for enemies in range(k):
    a,b = raw_input().split()
    idA = names[a]
    idB = names[b]
    g[idA].append(idB)
    g[idB].append(idA)

ind = []
a = [i for i in range(n)]
for subset in powerset(i):
    if independent(subset):
        ind.append(subset)

def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
