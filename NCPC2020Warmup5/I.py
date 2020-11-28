from operator import mul
PRIME = 10 ** 9 + 7

class Mat(list):
    def __matmul__(A, B):
        SUM = 0
        N = len(A)
        RES = [[0]*N for _ in range(N)]
        for i in range(N):
            for k in range(N):
                for j in range(N):
                    RES[i][j] += A[i][k]*B[k][j]
                    RES[i][j] %= PRIME
        return Mat(RES)
 
    def __pow__(A, k):
        dim = len(A)
        result = Mat([ [int(i==j) for i in range(dim)] for j in range(dim)]) # n x n identity
        while k > 0:
            if k % 2 == 1:
                result = A @ result
            A @= A
            k //= 2
        return result

for _ in range(int(input())):
    n, k, *lengths = map(int, input().split())

    numways = [[0] * 50 for _ in range(50)]

    for i in range(49):
        numways[i][i+1] += 1

    for i in range(k):
        numways[lengths[i] - 1][0] += 1

    N = Mat(numways).__pow__(n)
    print(N[0][0] if N[0][0] else "IMPOSSIBLE")
