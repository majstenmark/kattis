parents = []
def find(x):
    y = parents[x]
    while y != x:
        parents[x] = parents[y]
        x, y = y, parents[y]
    return parents[x]

def add(a, a_parent, b_parent):

    sizes[b_parent] =  sizes[a_parent]
    parents[a_parent] = b_parent

def union(a,b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent == b_parent:
        return False

    if sizes[a_parent] < sizes[b_parent]:
        add(a,a_parent, b_parent)
    else:
        add(b, b_parent,a_parent)
    return True

N, Q = map(int, raw_input().split())
parents = [x for x in range(N +1)]
sizes = [1 for x in range(N+1)]
for q in range(Q):
    op, astr, bstr = raw_input().split()
    a = int(astr)
    b = int(bstr)
    if op == '=':
        union(a, b)
    else:

        a_parent = find(a)
        b_parent = find(b)
        if a_parent == b_parent:
            print 'yes'
        else:
            print 'no'
