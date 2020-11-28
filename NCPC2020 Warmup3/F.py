inp = input

from fractions import Fraction

def gaussmm(A, b, monoid=None):
    def Z(v): return v == 0
    N = len(A[0])
    for i in range(N):
        m = next(j for j in range(i, N) if Z(A[j][i]) == False)
        if i != m:
            A[i], A[m] = A[m], A[i]
            b[i], b[m] = b[m], b[i]
        
        for j in range(i+1, N):
            sub = A[j][i]/A[i][i]
            b[j] -= sub*b[i]
            for k in range(N):
                A[j][k] -= sub*A[i][k]
    for i in range(N-1, -1, -1):
        for j in range(N-1, i, -1):
            sub = A[i][j]/A[j][j]
            b[i] -= sub*b[j]
            A[i][k] -= sub*A[j][k]
        b[i], A[i][i] = b[i]/A[i][i], A[i][i]/A[i][i]
    return b


def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n + 1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = A[i][n] / A[i][i]
        for k in range(i - 1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    return x


def ni():
    return int(inp())

def nl():
    return [int(v) for v in inp().split()]



def one(vals):
    x1, x2 = vals[0], vals[1]
    d = x2 //x1
    for i in range(len(vals) -1):
        xii = vals[i]
        xi = vals[i+1]
        if xii * d != xi:
            return False, -1
    
    return True, d * vals[-1]

def two(vals):
    x1, x2, x3, x4 = vals[0:4]
    try:
        b = (x4 * x2 - x3 ** 2) // (x2 **2 - x1 * x3)
        a = (x3 - b * x1) // x2
    except:
        return False, -1

    for i in range(len(vals) -2):
        x1 = vals[i]
        x2 = vals[i+1]
        x3 = vals[i+2]
        if x1 * b + x2 * a != x3:
            return False, -1
    return True, int(a * vals[-1] +b * vals[-2])


def three(vals):   
    x1, x2, x3, x4, x5, x6 = [Fraction(x, 1) for x in  vals[0:6]]

    a1 = [[x1, x2, x3], [x2, x3, x4], [x3, x4, x5]]
    A = [[x1, x2, x3, x4], [x2, x3, x4, x5], [x3, x4, x5, x6]]
    B = [x4, x5, x6]
    coord = gaussmm(a1, B)
    c, b, a = coord
    return True, int(a * vals[-1] + b * vals[-2] + c * vals[-3])
 

def solve(vals):
    for f in [one, two, three]:
        ok, alt = f(vals)
        if ok:
            return alt
    


t = ni()
for _ in range(t):
    vals = nl()[1:]
    nxt = solve(vals)
    print(nxt)