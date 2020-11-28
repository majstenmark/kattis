inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

n, m = nl()
rules = {}
for _ in range(n):
    rule = inp().replace('->', ' ').split()
    rules[rule[0]] = rule[-1]
S = inp()
for _ in range(m):
    S1 = []
    for ch in S:
        if ch in rules:
            S1.append(rules[ch])
        else:
            S1.append(ch)
    S = ''.join(S1)
print(S)