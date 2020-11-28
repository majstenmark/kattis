import sys


def find(x, parents):
    if parents[x][0] != x:
        parents[x][0] = find(parents[x][0], values)
    return parents[x][0]

def add(a, a_parent, b_parent, parents):

    p,size,ssum= parents[b_parent]
    size += parents[a_parent][1]
    ssum += parents[a_parent][2]
    parents[b_parent] =  [b_parent, size, ssum]
    parents[a_parent][0] = b_parent

def union(a,b,parents):
    a_parent = find(a,values)
    b_parent = find(b, values)
    if a_parent == b_parent:
        return

    if parents[a_parent][1] < parents[b_parent][1]:
        add(a,a_parent, b_parent, parents)
    else:
        add(b, b_parent,a_parent, parents)

def move(a,b, parents):

    ap = find(a,parents)
    bp= find(b,parents)
    if ap == bp:
        return
    parents[bp][1] += 1
    parents[bp][2] += a+1

    parents[ap][1] -= 1
    parents[ap][2] -= (a+1)

    parents[a][0] = bp


data = (int(v) for v in sys.stdin.read().split())

try:
    while 1:
        N = next(data)
        M = next(data)

        values = [[n + N, 1, n +1] for n in range(N)] + [[n + N, 1, n+1] for n in range(N)] # parent, size, sum

        for i in range(M):
            cmd = next(data)
            p = next(data) -1
            # do the command
            # if 3 print
            if cmd == 3:

                parent  = find(p, values)
                parent, size, ssum = values[parent]
                s= '{} {}'.format(size, ssum)
                print(s)
                continue
            q = next(data) -1
            if cmd == 1:
                union(p,q, values)

            #    s = 'After union {} and {}'.format(p,q)
            #    print(s)
            #    print(values)

            if cmd== 2:

                move(p, q, values)

            #    s = 'After move {} and {}'.format(p,q)
            #    print(s)
            #    print(values)

except StopIteration:
    pass
