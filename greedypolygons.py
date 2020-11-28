import math

def orig_area(n, l):
    return 0.25 * n * l **2 / math.tan(math.pi/n)

N = int(raw_input())
for n in range(N):
    n, l, d, g = [int(v) for v in raw_input().split()]
    orig = orig_area(n, l)
    side_area = n * l * d * g
    r = d * g
    circ = r **2 * math.pi
    tot = orig + side_area + circ
    print(tot)