N = int(input())
H = 0
s = 1
tot = 0
p = s**2
while tot + p <= N:
    tot += p
    s += 2
    p = s **2
    H += 1
print(H)
