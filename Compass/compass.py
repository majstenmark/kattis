N1 = int(raw_input())
N2 = int(raw_input())
M = 360
cw = (N2 - N1) % M
ccw = (N1 - N2) % M
if cw <= ccw:
    print cw
else:
    print -ccw
