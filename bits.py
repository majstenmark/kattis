def solve(x):
    L = len(x)
    v = 0
    mx = 0
    for ch in x:
        digit = int(ch)
        v *= 10
        v += digit
        binary = bin(v)
        ones =binary.count('1')
        mx = max(mx, ones)
    return mx

T = int(raw_input())
for t in range(T):
    X = raw_input()
    print(solve(X))