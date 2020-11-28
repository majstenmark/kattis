def expl(S, L):
    prefix = S[:L]
    k = (len(S) + L -1)/L
    _str = prefix * k
    return  _str.startswith(S)

def solve(S):
    for L in range(1, len(S) +1):
        if expl(S, L):
            return L
    return L

N = int(raw_input())
for n in range(N):
    S = raw_input()
    res = solve(S)
    print(res)