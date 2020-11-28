inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

ANS = {}
Large = {}
ANS[1] = 0
Large[0] = 0
Large[1] = 1
for i in range(2, 10 **5 + 1):
    s = sum(map(int, str(i)))
    ANS[i] = Large[s-1]
    Large[s] = i

t = ni()
for _ in range(t):
    n = ni()
    print(ANS[n])