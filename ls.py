def match(p,s):
    mat = [[0]* (len(p)+1) for _ in range(len(s) +1)]
    mat[0][0] = 1
    for row in range(len(s)):
        for col in range(len(p)):
            if not mat[row][col]:
                continue
            if p[col] == '*':
                mat[row +1][col] = 1
                mat[row+1][col+1]= 1
                mat[row][col+1]= 1
            elif p[col] == s[row]:
                mat[row+1][col+1]= 1
    return mat[-1][-1]


P = raw_input()

#print regex
N = input()
for file in range(N):
    filename = raw_input()
    if match(P,filename):
        print filename
