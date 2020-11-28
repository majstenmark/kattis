n = input()
from collections import Counter
C = Counter()
def rot_l(v):
    return [v[0], v[1], v[5], v[4], v[2], v[3]]

def rot_h(v):
    return [v[2], v[3], v[1], v[0], v[4], v[5]]

for _ in range(n):
    v = map(int, raw_input().split())
    v2 = rot_l(v)
    MIN = list(v)
    
    for i in range(4):
        a1 = list(v)
        a2 = list(v2)
        for _ in range(i):
            a1 = rot_h(a1)
            a2 = rot_h(a2)
        for j in range(4):
            a1 = rot_l(a1)
            a2 = rot_l(a2)
            MIN = min(MIN, a1)
            MIN = min(MIN, a2)
    C[tuple(MIN)] += 1
print(max(C.values()))
