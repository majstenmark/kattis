from itertools import combinations


def getNext():
    for node,mark in enumerate(selected):
        if mark == 0:
            return node
    return -1

def legal(li):
    for a in range(len(li)):
        if selected[li[a]] != 0: return False
        for b in range(a+1, len(li)):
            if li[b] in graph[li[a]]:
                return False
    return True

def select(node):
    selected[node] += 1
    for ne in graph[node]:
        selected[ne] += 1

def deselect(node):
    selected[node] -= 1
    for ne in graph[node]:
        selected[ne] -= 1

def getAllSubset(node):
    for x in range(1<<len(graph[node])):
        p = []
        for a in range(len(graph[node])):
            if (1<<a)&x: p.append(graph[node][a])
        if len(p) > 1 and legal(p):
            yield p

def surv(k):
    if k <= 0:
        print 'possible'
        exit()
    node = getNext()
    #print 'selects ', node
    if node == -1:
        return
    select(node)
    #print 'selected ',selected
    surv(k-1)
    deselect(node)

    #print 'deselected ',selected
    for sub in getAllSubset(node):
        #print sub
        for subnode in sub:
            select(subnode)

        #print 'selected ',selected
        surv(k - len(sub))
        for subnode in sub:
            deselect(subnode)
            #print 'deselected ',selected
    return


K = input()
N = input()
graph = [[] for _ in range(N)]
for n in range(N):
    ne = map(lambda x: int(x) - 1, raw_input().split())
    for index in range(1, len(ne)):
        graph[n].append(ne[index])
# print graph
selected = [0 for _ in range(N)]
if N >= 5 * K:
    print 'possible'
else:
    surv(K)
    print 'impossible'
