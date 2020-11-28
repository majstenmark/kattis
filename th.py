
import sys
itr = (line for line in sys.stdin.read().split('\n'))

def nl(): return [int(v) for v in next(itr).split()]
def ni(): return int(next(itr))


from typing import List, Tuple, Optional

N, M = nl()

Point = Tuple[float, float]

def on_segment(p: Point, q: Point, r: Point) -> bool:
    """ is p on qr? """
    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]) 



def orientation(p: Point, q: Point, r: Point) -> Optional[bool]:
    """
    # returns:
    # None : Colinear points
    # True : Clockwise points
    # False : Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    return None if val == 0 else bool(val > 0)


def intersect(p: Point, q: Point, r: Point, s: Point) -> bool:
    # Next line allows endpoints to be the same, normally not revelant
    if p == r or p == s or q == r or q == s:
        return False

    o1 = orientation(p, q, r)
    if o1 is None and on_segment(p, r, q):
        return True

    o2 = orientation(p, q, s)
    if o2 is None and on_segment(p, s, q):
        return True

    o3 = orientation(r, s, p)
    if o3 is None and on_segment(r, p, s):
        return True

    o4 = orientation(r, s, q)
    if o4 is None and on_segment(r, q, s):
        return True

    return o1 != o2 and o3 != o4


vertices: List[Point] = []
for _ in range(N):
    x, y = nl()
    vertices.append((x, y))


def find(p: List[int], i: int):
    if p[i] < 0:
        return i
    p[i] = find(p, p[i])
    return p[i]


def union(p: List[int], i: int, j: int):
    i_ = find(p, i)
    j_ = find(p, j)
    assert p[i_] < 0 and p[j_] < 0
    if i_ != j_:
        if p[i_] < p[j_]:
            i_, j_ = j_, i_
        p[j_] += p[i_]
        p[i_] = j_


p = [-1] * N

edges: List[Tuple[int, int]] = []
for _ in range(M):
    i, j = nl()
    edges.append((i, j))
    union(p, i, j)

if sum(1 for i in p if i < 0) > 1:
    print("-1")
    exit()

for a in range(M):
    e = edges[a]
    i, j = e
    for b in range(a + 1, M):
        f = edges[b]
        if intersect(vertices[i], vertices[j], vertices[f[0]], vertices[f[1]]):
            print("-1")
            exit()

    for k in range(N):
        if intersect(vertices[i], vertices[j], vertices[k], vertices[k]):
            print("-1")
            exit()


print(len(edges) - len(vertices) + 2)
