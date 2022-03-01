import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def parse(_): return inp().replace('->', ' ').split()


married = 'm'
unmarried = 'u'
unknown = '?'
yes = 1
questionmark = '?'
no = 0

def bfs(q, g):
    visited = set()
    for n in q:
        visited.add(n)
    while q:
        q2 = []
        for node in q:
            if node not in g: continue
            ne = g[node]
            if ne not in visited:
                visited.add(ne)
                q2.append(ne)
        q = q2
    return visited

def maybe(ppl, looksat):
    for a, b in looksat.items():
        if ppl[a] == unmarried or ppl[b] == married: continue
        return True
    return False



N, L = nl()
ppl = {a:b for a, b in map(parse, range(N))}
looksat = {a:b for a, b in map(parse, range(L))}
sets = {married: set(), unmarried: set(), unknown: set()}
for n, s in ppl.items(): sets[s].add(n)

visited = bfs(sets[married], looksat)

if len(visited & sets[unmarried]) > 0: print(yes)
elif maybe(ppl, looksat): print(questionmark)
else: print(no)

    

