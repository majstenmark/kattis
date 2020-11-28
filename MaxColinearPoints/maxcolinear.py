from collections import defaultdict as ddict

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return b if a % b == 0 else gcd(b, a % b)

def lineeq(p1, p2):
    A, B, C = line(p1, p2)
    g = gcd(gcd(A, B), C)
    A, B, C = A/g, B/g, C/g
    if (A < 0) or (A == 0 and B < 0) or ((A, B) == (0, 0) and C < 0):
        return -A, -B, -C
    return A, B, C

def f(): return 1

N = int(raw_input())
while N != 0:
    points = []

    eqs = ddict(set)
    for n in range(N):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    for i in range(N-1):
        for j in range(i+1, N):
            eq = lineeq(points[i], points[j])
            eqs[eq].add(points[i])
            eqs[eq].add(points[j])

            #print('Equation for p1 {} and p2 {} is {}'.format(points[i], points[j], eq))
    maxCol = 1
    if N == 1:
        print 1
    else:
        for eq in eqs.keys():
            maxCol = max(maxCol, len(eqs[eq]))
        print maxCol

    N = int(raw_input())
