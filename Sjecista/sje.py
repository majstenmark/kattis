N = input()
corners = N - 2
tot = 0
for s in range(1, corners):
    p = corners - s
    tot += (s * p)
print N* tot/4
