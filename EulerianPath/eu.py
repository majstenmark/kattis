from collections import deque, namedtuple


IMPOSSIBLE = 'Impossible'
N, M = map(int, raw_input().split())
Edge = namedtuple('Edge', ['node', 'edgeId'])

def rebuild(out, inc , start, end, m):
    startcandidate, endcandidate = -1, -1
    for index in range(start):
        if len(out[index]) == len(inc[index]) + 1 and startcandidate == -1:
            startcandidate = index
        elif len(out[index]) == len(inc[index]) -1 and endcandidate == -1:
            endcandidate = index
        elif len(out[index]) != len(inc[index]):
            return False, False
    if startcandidate > -1 and endcandidate > -1:

        out[start].add(Edge(startcandidate, m))
        out[endcandidate].add(Edge(end, m+1))

        return True, False
    if (startcandidate, endcandidate) == (-1, -1):
        # cycle!
        for anyindex in range(start):
            if len(out[anyindex]) > 0: break

        out[start].add(Edge(anyindex, m))
        out[anyindex].add(Edge(end, m+1))
        return True, True

    return False, False

def pathHelper(fromNode, out):
    p = []
    node = fromNode
    while len(out[node]) > 0:
        anyedge = out[node].pop()
        p.append(anyedge)
        node = anyedge.node
    return p

def getPath(outgoing, start, end, m):
    initialPath = pathHelper(start, outgoing)
    edgePath = [-1 for _ in range(M+2)]
    hasFree = deque()
    #print 'initial path', initialPath


    for index in range(len(initialPath)-1):
        currentEdge = initialPath[index]
        nextEdge = initialPath[(index + 1)]
        edgePath[currentEdge.edgeId] = nextEdge
        if len(outgoing[currentEdge.node]) >0:
            hasFree.append((currentEdge.node, currentEdge, nextEdge))
    #print 'initial edgepath', edgePath


    while hasFree:
        node, inward, outward = hasFree.popleft()
        tmpPath = pathHelper(node, outgoing)
        if len(tmpPath) == 0: continue
        for index in range(len(tmpPath)-1):
            currentEdge = tmpPath[index]
            nextEdge = tmpPath[(index + 1)]
            edgePath[currentEdge.edgeId] = nextEdge
            if len(outgoing[currentEdge.node]) >0:
                hasFree.append((currentEdge.node, currentEdge, nextEdge))
        edgePath[inward.edgeId] = tmpPath[0]
        edgePath[tmpPath[-1].edgeId] = outward
        #print 'looking at node {} and path is {} and uptated edgepath {}'.format(node, tmpPath, edgePath)
    p = []
    edge = initialPath[0]
    #print 'startedge ', m
    #print edgePath
    while edge.node != end:
        p.append(edge.node)
        edge = edgePath[edge.edgeId]

    return p

while (N, M) != (0,0):
    outgoing = [set() for _ in range(N+2)]
    incoming = [set() for _ in range(N+2)]
    for m in range(M):
        u, v = map(int, raw_input().split())
        outgoing[u].add(Edge(v, m))
        incoming[v].add(Edge(u, m))
    ok, cycle = rebuild(outgoing, incoming, N, N+1, M)
    #print 'rebuild ', outgoing
    if not ok:
        print(IMPOSSIBLE)
    else:
        #print('Is ok {} and iscycle {}'.format(ok, cycle))
        path = getPath(outgoing, N, N+1, M) #list of nodes
        #print 'len ', len(path), M
        if len(path) != M + 1:
            print(IMPOSSIBLE)
        else:
            res = []
            for node in path:
                res.append(str(node))
            print(' '.join(res))
    N, M = map(int, raw_input().split())
