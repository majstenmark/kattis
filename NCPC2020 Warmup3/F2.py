inp = input

from fractions import Fraction

def gauss(A, b, monoid=None):
    def Z(v): return v == 0
    N = len(A[0])
    for i in range(N):
        try:
            m = next(j for j in range(i, N) if Z(A[j][i]) == False)
        except:
            return None 
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
    x1, x2, x3, x4 = [Fraction(x, 1) for x in  vals[0:4]]

    A = [[x1, x2], [x2, x3]]
    b = [x3, x4]
    coord = gauss(A, b)
    if coord == None:
        return False, -1
    b, a = coord
    if int(b) != b or int(a) != a:
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

    A = [[x1, x2, x3], [x2, x3, x4], [x3, x4, x5]]
    b = [x4, x5, x6]
    coord = gauss(A, b)
    if coord == None:
        return False, -1
    c, b, a = coord
    if int(b) != b or int(a) != a or int(c) != c:
        return False, -1

    for i in range(len(vals) -3):
        x1 = vals[i]
        x2 = vals[i+1]
        x3 = vals[i+2]
        x4 = vals[i+3]
        
        if x1 * c + x2 * b + x3 * a != x4:
            return False, -1
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