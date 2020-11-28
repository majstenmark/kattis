import math

class rmq:
    M = [[]]
    A = []
    def __init__(self, arr):
        N = len(arr)
        self.A = arr
        llog = int(math.ceil(math.log(N, 2)))
        self.M = [[-1] * llog for _ in range(N)]
        M =self.M
        for i in range(N):
            M[i][0] = i
        for k in range(1, llog):
            L = 2 **k
            for i in range(N - L + 1):
                if arr[M[i][k -1]] < arr[M[i + 2 ** (k -1)][k -1]]:
                    M[i][k] = M[i][k -1]
                else:
                    M[i][k] = M[i + 2 ** (k -1)][k -1]
    def rmqMin(self, i, j):
        i,j = min(i, j), max(i, j)
        k = int(math.floor(math.log(j - i +1, 2)))
        A =self.A
        M = self.M
        tmpI = j - 2 ** k + 1
        if A[M[i][k]] <= A[M[tmpI][k]]:
            return M[i][k]
        return M[tmpI][k]

def dfs(this, d):
    invDepth[this] = len(depth)
    depth.append(d)

    if len(children[this]) == 0:
        count[this] = 1
        return 1
    c = 1
    for child in children[this]:
        c += dfs(child, d + 1)
        depth.append(d)
    count[this] = c
    return c

N= int(raw_input()) + 1
tree = map(int, raw_input().split())
children = [[] for n in range(N)]
count = [0 for n in range(N)]

invDepth = [-1 for _ in range(N)]
depth = []

for id, parent in enumerate(tree):
    children[parent].append(id + 1)


dfs(0, 0)
R = rmq(depth)

P = [set() for n in range(N)]
Q = int(raw_input())
queries = []
for q in range(Q):
    Ms = list(map(int, raw_input().split()))[1:]
    queries.append(Ms)

#print('count ', count)

for query in queries:
    #print(q)
    q =list(set(query))
    use = [True for _ in range(len(q))]
    for index in range(len(q) -1):
        for index2 in range(index+1, len(q)):
            parent = R.rmqMin(invDepth[q[index]], invDepth[q[index2]])
            #print 'parent: {} of {} {}'.format(parent, q[index], q[index2])
            if depth[parent] == depth[invDepth[q[index]]]:
                use[index2] = False
            if depth[parent] == depth[invDepth[q[index2]]]:
                use[index] = False
    size = 0
    for index in range(len(q)):
        if use[index]:
            size +=  count[q[index]]
    print(size)
