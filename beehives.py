inp = input
def nl(): return [int(v) for v in inp().split()]
def nf(): return [float(v) for v in inp().split()]

def ni(): return int(inp())
def read(): 
    a, b = inp().split()
    return float(a), int(b)

def dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx **2 + dy **2) ** 0.5

D, N = read()
while N > 0:
    hives = [nf() for _ in range(N)]
    sour = set()
    for i in range(N):
        for j in range(i + 1, N):
            d = dist(hives[i], hives[j])
            if d <= D:
                sour.add(i)
                sour.add(j)
                
    print('{} sour, {} sweet'.format(len(sour), N - len(sour)))
    
    D, N = read()
