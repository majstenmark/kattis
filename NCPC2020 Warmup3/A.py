inp = raw_input

def ni():
    return int(inp())

def nl():
    return [int(v) for v in inp().split()]

t = ni()

for _ in range(t):
    n, m=nl()
    prices = [nl() for _ in range(n)]
    stickers = nl()
    SUM= 0
    for L in prices:
        MAX = stickers[L[1]-1]
        for id in L[1:-1]:
            MAX = min(MAX, stickers[id-1])
        SUM += MAX * L[-1]
    print(SUM)