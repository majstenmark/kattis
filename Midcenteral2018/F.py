import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

x,y, x1, y1, x2, y2 = map(int, raw_input().split())
if x1 <= x<= x2:
    md = min(abs(y - y1), abs(y - y2))
    print md
elif y1 <= y <= y2:
    md = min(abs(x - x1), abs(x - x2))
    print md
else:

    p = (x, y)
    c1 = (x1, y1)
    c2 = (x1, y2)
    c3 = (x2, y2)
    c4 = (x2, y1)
    md = min(dist(p, c1), dist(p, c2), dist(p, c3), dist(p, c4))
    print md
