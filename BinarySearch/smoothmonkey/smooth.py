D,W,C = map(int, raw_input().split())

def H(ws,c):
    s = 0.0
    n = int(ws * 1.0) +1

    for k in range(1, n):
        s += 1.0/(2*k - 1)
    return  c*s

wmin = 0.0
wmax = W
for i in range(10):
    wf = (wmin + wmax)/2.0
    ws = W - D - wf

    dist = H(ws, C)
    s = 'to goal {} and ws {} and dist {}'.format(wf + D, ws, dist)
    print(s)
    if dist < wf + D:
        wmax = wf
    else:
        wmin = wf
print(wmin)
