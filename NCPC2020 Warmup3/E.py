inp = input

def ni():
    return int(inp())

def nl():
    return [int(v) for v in inp().split()]
import math
t = ni()

def incB(B, R):
    add = round(B*R/100)
    return B + add

for tc in range(t):
    R, B, M = [float(x) for x in inp().split()]
    B = round(B*100)
    M = round(M*100)
    B = incB(B, R)
    ok = False

    for i in range(1, 1201):

        if B <= M:
            print(i)
            ok = True
            break
        B -= M
        B = incB(B, R)
    if not ok:
        print('impossible')