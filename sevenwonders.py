H = raw_input()
T, C, G = 0, 0, 0
for c in H:
    if c == 'T':
        T += 1
    if c == 'C':
        C += 1
    if c == 'G':
        G += 1
sets = min([T, C, G])
points = T **2 + C ** 2 + G **2 + 7 * sets
print(points)