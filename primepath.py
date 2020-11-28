def gen_primes():
    p = set()
    pa = [True] * 10000
    for k in range(2, 10000):
        for s in range(2 *k, 10000, k):
            pa[s] = False
            
    for s in range(1000, 10000):
        if pa[s]:
            p.add(s)
    
    return p

def make_list(n):
    li_rev = []
    while n >0:
        r = n % 10
        li_rev.append(r)
        n = n //10
    return li_rev[::-1]

def neigh(n):
    li = make_list(n)
    nei = []
    for place in range(0, 4):
        orig = li[place]
        for k in range(0, 10):
            li[place] = k
            val = 1000 * li[0] + 100 * li[1] + 10 * li[2]+ li[3] 
            if val in primes:
                nei.append(val)
        li[place] = orig
    
    return nei
            


def bfs(s, t):
    visited.add(s)
    q = [s]
    layer = 0
    while q:
        q2 = []
        for node in q:
            if node == t:
                return layer
            for ne in neigh(node):
                if ne not in visited:
                    visited.add(ne)
                    q2.append(ne)
        q = q2
        layer += 1
    return 'Impossible'
visited = set()
primes = gen_primes()

N = int(raw_input())
for n in range(N):
    visited = set()
    S, T = [int(v) for v in raw_input().split()]
    print(bfs(S, T))