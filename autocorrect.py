N , M = map(int, raw_input().split())

class Node:

    def __init__(self, i):
        self.to = {}
        self.i = i

    def addEdge(self, t, tid):
        self.to[t] = tid

    def addTab(self, fullword):
        self.to['tab'] = fullword

    def addDel(self, backnode):
        self.to['del'] = backnode

def bfs(q, g, strokes):
    for node in q:
        strokes[node] = 0
    while q:
        q2 = []
        for node in q:
            for ne in g[node].to.values():
                if strokes[ne] == -1:
                    strokes[ne] = strokes[node] + 1
                    q2.append(ne)
        q = q2


graph = []
graph.append(Node(0))
for n in range(N):
    word = raw_input()

    node = graph[0]
    fromTabId = -1
    for letter in word:

        if letter not in node.to:
            newNode = Node(len(graph))
            graph.append(newNode)
            node.to[letter] = newNode.i
            newNode.addDel(node.i)
            node = newNode
            if fromTabId == -1:
                fromTabId = node.i

        else:
            node = graph[node.to[letter]]

    if fromTabId != -1:
        #print '{}: adding tab from {} to {}'.format(word, fromTabId, node.i)
        branchingNode = graph[fromTabId]
        branchingNode.addTab(node.i)

strokes = [-1 for x in range(len(graph))]

q = [0]
bfs(q, graph, strokes)

for m in range(M):
    testword = raw_input()
    nbrOfStrokes = len(testword)

    node = graph[0]
    for index in range(len(testword)):
        letter = testword[index]
        if letter not in node.to:
            break
        node = graph[node.to[letter]]
        nbrOfStrokes = min(nbrOfStrokes, strokes[node.i] + (len(testword) - index -1))


    print nbrOfStrokes
