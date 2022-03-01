import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


class Node:
    
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None

class Tree:
    def __init__(self, li):
        self.root = Node(li[0])
        for l in li[1:]:
            self.add(self.root, l)
    
    def add(self, node, elem):
        if elem < node.elem:
            if node.left == None:
                node.left = Node(elem)
            else:
                self.add(node.left, elem)
        else:
            if node.right == None:
                node.right = Node(elem)
            else:
                self.add(node.right, elem)
        

    def traverse(self, parent, li):
        if parent != None:
            li.append('L')
            self.traverse(parent.left, li)
            li.append('R')
            self.traverse(parent.right, li)
            li.append('U')
            
    
    def tostring(self):
        out = []
        self.traverse(self.root, out)
        return ''.join(out)
            

    
    
    

N, K = nl()
data = [nl() for _ in range(N)]
roots = set()
for tree in data:
    t = Tree(tree)
    roots.add(t.tostring())
print(len(roots))

