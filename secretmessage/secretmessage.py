from math import sqrt as sq

def encrypt(orig):
    L = len(orig)
    K = int(sq(L-1)) + 1
    grid = [['*'] * K for _ in range(K)]
    index = 0
    for row in range(K):
        for col in range(K):
            grid[row][col] = orig[index]
            index+= 1
            if index == L:
                break
    output = []
    #print(grid)
    for col in range(K):
        for row in range(K-1, -1, -1): 
            if grid[row][col] != '*':
                output.append(grid[row][col])
    return ''.join(output)

N = int(raw_input())
for n in range(N):
    orig = raw_input()
    print(encrypt(orig))