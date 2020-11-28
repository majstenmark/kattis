import math

def solve(A, L, X):
    B = int(round((X * A * 10 ** L - A)/(10.0 - X),0))
    #print('B', B)
    val = A * 10 ** L + B

    test1 = 10 * B + A
    test2 = val * X
    #print(test1, ' ', test2)
    if abs(test1 - test2) < 10 ** -6 and B >= 0:
        if val < 10 ** 8 and int(math.ceil(math.log(B + 1, 10))) == L:
            #print('Testing {} {} {} {} {}'.format(A, L, val, test1, B))
            return val, True
    return 0, False

X = float(raw_input())

res = []
if X < 10:
    for A in range(1, 10):
        for L in range(0, 9):
            val, solved = solve(A, L, X)
            if solved:
                res.append(val)
    res.sort()
    for c in res:
        print(c)
if len(res) == 0:
    print('No solution')
