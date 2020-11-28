def nl():
    return [int(v) for v in raw_input().split()]

pascal = [[1]]
for i in range(7):
    row = [0] * (i + 2)
    for j in range(len(pascal[-1])):
        row[j] += pascal[-1][j]
        row[j + 1] += pascal[-1][j]
    pascal.append(row)

def evalA(A, x):
    s = 0
    for i in range(len(A)):
        s += x ** i * A[i]
    return s

def evalC(pascal_row, C):
    s = 0
    for p, c in zip(pascal_row, C):
        s += p * c
    return s


A = nl()[1:][::-1]
C = [0] * len(A)
for i in range(0, len(A)):
    eA = evalA(A, i)
    eC = evalC(pascal[i], C)
    C[i] = eA - eC
print(' '.join(map(str, C)))