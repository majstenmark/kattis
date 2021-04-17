S = input()

L = [1] * len(S)
for i, ch in enumerate(S):
    mx = 1
    for j in range(0, i):
        ch2 = S[j]
        if ch2 < ch:
            alt = 1 + L[j]
            mx = max(mx, alt)
    L[i] = mx
mx = max(L)

print(26-mx)
