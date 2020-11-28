def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

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

N = int(raw_input())
while N != 0:
    points = []
    for n in range(N):
        x, y = map(int, raw_input().split())
        points.append((x, y))
    hull = convex_hull(points)

    print(len(hull))
    for x, y in hull:
        print('{} {}'.format(x, y))

    N = int(raw_input())
