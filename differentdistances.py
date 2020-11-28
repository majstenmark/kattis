import math
L = raw_input()
while L != '0':
    x1,y1, x2, y2, p =[float(v) for v in L.split()]
    t1 = math.pow(abs(x1 -x2), p) + math.pow(abs(y1 -y2),p)
    res =math.pow(t1, 1.0/p)
    print(res)

    L = raw_input()