inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

import math
r, h, s = nl()
while r != 0:
    circ = 2 * math.pi * r
    cat = (h ** 2 - r **2) ** 0.5
    alpha = math.asin(cat/h)
    gamma = 2 * math.pi - 2 * alpha
    circL = gamma/(2 * math.pi) * circ
    proc = s/100 + 1
    L = (circL + 2 * cat) * proc
    print('{:.2f}'.format(L))
    r, h, s = nl()
