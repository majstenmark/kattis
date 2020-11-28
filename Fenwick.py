import random as rand


class FenwickTree:
    arr = []
    def __init__(self, n):
        self.arr = [0 for _ in range(n + 1)]

    def inc(self, i, val):
        self.private_inc(i + 1, val)

    def sum(self, a, b):
        return self.private_sum(b+1) - self.private_sum(a)

    def private_inc(self, i, val):

        while i < len(self.arr):
            self.arr[i] += val
            i += i & -i

    def private_sum(self, i):
        s = 0
        while i > 0:
            s += self.arr[i]
            i -= i & -i
        return s


class SegmentTree:
    hi, lo, delta, mi = [], [], [], []
    n = 0
    INF = 10**12

    def __init__(self, n):
        self.n = n
        self.hi = [0] * (4*n+1)
        self.lo = [0] * (4*n+1)
        self.delta = [0] * (4*n+1)
        self.mi = [0] * (4*n+1)

        self.private_init(1, 1, n)

    def private_init(self, i, a, b):
        self.lo[i] = a
        self.hi[i] = b
        if a == b:
            return
        mid = (a + b)/2
        self.private_init(2* i, a, mid)
        self.private_init(2* i + 1, mid +1, b)


    def incIndex(self, i, val):
        self.private_inc(1, i+1,i+1, val)

    def inc(self, a, b, val):
        self.private_inc(1, a+1, b+1, val)

    def private_prop(self, i):
        self.delta[2 *i] += self.delta[i]
        self.delta[2 *i +1] += self.delta[i]
        self.delta[i] = 0

    def private_update(self, i):
        self.mi[i] = min(self.mi[2*i]+self.delta[2*i], self.mi[2*i+1] + self.delta[2*i+1])

    def min(self, a, b):
        return self.private_min(1, a+1, b+1)

    def private_inc(self, i, a, b, val):
        if b < self.lo[i] or a > self.hi[i]:
            return
        if a <= self.lo[i] and self.hi[i] <= b:
            self.delta[i] += val
            return
        self.private_prop(i)
        self.private_inc(2 *i, a, b, val)
        self.private_inc(2 *i + 1, a, b, val)
        self.private_update(i)

    def private_min(self, i, a, b):
        if b < self.lo[i] or a > self.hi[i]:
            return self.INF
        if a <= self.lo[i] and self.hi[i] <= b:
            return self.mi[i] + self.delta[i]

        self.private_prop(i)
        leftMin = self.private_min(2 *i, a, b)
        rightMin = self.private_min(2 *i + 1, a, b)
        self.private_update(i)
        return min(leftMin, rightMin)


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
    def min(self, a, b):
        m = 10 ** 12
        for i in range(a, b + 1):
            m = min(self.arr[i], m)
        return m

    def toString(self):
        return ' '.join(map(str, self.arr))

N = 10111
randomNbrs = 100000
INF = 10 * 8
ntree = NaiveTree(N)
#fwtree = FenwickTree(N)
stree = SegmentTree(N)

"""
for t in range(N):
    rindex = t
    rindex = rand.randint(0, N -1)
    rindex2 = rand.randint(rindex, N -1)
    rval =rand.randint(0, INF)
    for index in range(rindex, rindex2 +1):
        ntree.inc(index, rval)
#    stree.incIndex(rindex, rval)
    stree.inc(rindex, rindex2, rval)
"""
for t in range(randomNbrs):
    rindex = rand.randint(0, N -1)
    rindex2 = rand.randint(rindex, N -1)
    #v1 = ntree.min(rindex, rindex2)
    v2 = stree.min(rindex, rindex2)
#    print('{} {}'.format(v1,v2))
    assert(v1 == v2)
    rval =rand.randint(-INF, INF)
    #for index in range(rindex, rindex2 +1):
    #    ntree.inc(index, rval)
#    stree.incIndex(rindex, rval)
    stree.inc(rindex, rindex2, rval)
print('yeeeeaaaay!')
