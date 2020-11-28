import random

def mult(mat, vec):
    n = len(vec)
    res = [0] * n
    for i in range(n):
        v = 0
        for j in range(n):
            v += mat[i][j] * vec[j]
        res[i] = v
    return res

def test(A, B, N):
    x = [random.randint(0, 1000000) for _ in range(N)]
    A1 = mult(A, x)
    A2x = mult(A, A1)
    Bx = mult(B, x)
    for i in range(N):
            if A2x[i] != Bx[i]:
                return False
    return True

N = input()
while N != 0:
    A = []
    B = []
    for n in range(N):
        ij = map(int, raw_input().split())
        A.append(ij)
    for n in range(N):
         ij = map(int, raw_input().split())
         B.append(ij)
    if test(A, B, N):
        print "YES"
    else:
        print "NO"
    Ns = raw_input()
    if Ns == '':
        N = input()
    else:
        N = int(Ns)
