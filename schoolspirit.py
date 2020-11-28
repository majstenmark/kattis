inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
ki = 0
av = 0
for n in range(N):
    score = ni()
    
    s = 0.2 * score * 0.8 **n
    ki += s
    av += n * s/0.8 + (N-n-1) * s

print(ki)
print(av/N)

