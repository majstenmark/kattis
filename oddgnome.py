inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def king(li):
    for i in range(1, len(li)):
        if li[i] != li[i-1] + 1:
            return i+1
    return 0



N = ni()
for _ in range(N):
    gn = nl()[1:]
    print(king(gn))
