import math
D, V = [int(v) for v in raw_input().split()]
while (D, V) != (0, 0):
    d = (D ** 3 - 6 * V/math.pi) ** (1.0/3)
    print(d)
    D, V = [int(v) for v in raw_input().split()]
