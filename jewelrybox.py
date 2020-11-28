def vol(X, Y,h):
    a =X - 2 * h
    b =Y - 2 * h
    V = a * b * h
    return V

T = int(raw_input())
for t in range(T):
    X, Y = [int(v) for v in raw_input().split()]
    ph = (X+Y)/6.0
    h1 = ph + (ph**2 - X*Y/12.0) ** 0.5
    h2 = ph - (ph**2 - X*Y/12.0) ** 0.5
    v1 =vol(X, Y, h1)
    v2 =vol(X, Y, h2)
    
    print(max(v1, v2))