import math

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def dist(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx** 2 + dy ** 2)

def area(p1, p2, p3):
    a = dist(p1, p2)
    b = dist(p1, p3)
    c = dist(p2, p3)
    s = (a + b + c)/2
    area = math.sqrt(s * (s -a) * (s - b) * (s - c))
    return area

N = int(raw_input())
while N:
    points = []
    for n in range(N):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    hull = convex_hull(points)
    origo = hull[0]
    a = 0
    for other in range(1, len(hull) -1):
        a += area(origo, hull[other], hull[other+1])
    print(a)
    N = int(raw_input())