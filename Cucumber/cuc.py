from math import sqrt as sq

radius = {1:1.0, 2: 2.0, 3: 1 + 2.0/sq(3), 4: 1 + sq(2), 5: 1 + sq(2 * (1 + 1.0/sq(5))), 6: 3.0, 7:3}
line = input().split()
S, R, N, Z = float(line[0]), float(line[1]), int(line[2]), int(line[3])
best = 0
#print(ratio)
for n in range(N, 0, -1):
    if S >= radius[n] * R and 100 * n * R**2 <= Z * S **2:
        best = n
        break    
print(best)