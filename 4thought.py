res={}
ops = ['*', '+', '-', '/']
for op1 in ops:
    for op2 in ops:
        for op3 in ops:
            eq= '4 {} 4 {} 4 {} 4'.format(op1, op2, op3)
            x = eval(eq)
            res[x] = eq + ' = ' + str(x)

M = int(raw_input())

for m in range(M):
    N = int(raw_input())
    if N in res:
        print(res[N])
    else:
        print('no solution')    