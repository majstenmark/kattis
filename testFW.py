import random as rand

class NaiveTree:
    arr = []
    def __init__(self, n):
        self.arr = [0 for _ in range(n)]

    def inc(self, i, val):
        self.arr[i] += val

    def sum(self, a, b):
        s = 0
        for i in range(a, b + 1):
            s += self.arr[i]
        return s
    def toString(self):
        return ' '.join(map(str, self.arr))

N = 10
randomNbrs = 100
INF = 10 * 8
ntree = NaiveTree(N)
for r in range(randomNbrs):
    rindex = rand.randint(0, N -1)
    rval = rand.randint(0, INF)
    ntree.inc(rindex, rval)
test1 = ntree.sum(1,3)
test2 = ntree.sum(3,9)
test3 = ntree.sum(5,6)
test4 = ntree.sum(1,1)
print(ntree.toString())
print('{} {} {} {}'.format(test1, test2, test3, test4))
