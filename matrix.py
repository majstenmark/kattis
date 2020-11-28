import sys

data = sys.stdin.readlines()
k = len(data)//3
itr = (line for line in data)

for i in range(k):
    a,b = [int(v) for v in next(itr).split()]
    c, d= [int(v) for v in next(itr).split()]
    next(itr)
    t = b*c- a*d
    A =-d/t
    B =b/t
    C= c/t
    D= - a/t
    print('Case {}:'.format(i+1))
    print('{} {}'.format(A, B))
    print('{} {}\n'.format(C, D))
    

