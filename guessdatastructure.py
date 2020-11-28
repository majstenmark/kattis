from collections import deque
from heapq import heappush as push, heappop as pop

class S:
    def __init__(self):
        self.stack = []

    def push(self, i): 
        self.stack.append(i)
    
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    
    def name(self):
        return 'stack'
    

class Q:

    def __init__(self):
        self.q = deque()

    def push(self, i): 
        self.q.append(i)
    
    def pop(self):
        if not self.q:
            return None
        return self.q.popleft()
    
    def name(self):
        return 'queue'

class PQ:
    
    def __init__(self):
        self.pq = []

    def push(self, i): 
        push(self.pq, -i)
    
    def pop(self):
        if not self.pq:
            return None
        return -pop(self.pq)
    
    def name(self):
        return 'priority queue'



import sys
lines = sys.stdin.read().strip().split('\n')
itr = (line for line in lines)

while itr:
    N = int(next(itr, -1))
    if N == -1:
        exit()
    ok = [True] * 3
    datastructures = [Q(), S(),PQ()]
    for n in range(N):
        
        cmd, i = [int(v) for v in next(itr).split()]
        if cmd == 1:
            for index, ds in enumerate(datastructures):
                if ok[index]:
                    ds.push(i)
        else:
            for index, ds in enumerate(datastructures):
                if ok[index]:
                    r = ds.pop()
                    if r != i:
                        ok[index] =False
    oks = ok.count(True)
    
    if oks == 1:
        ok_index = ok.index(True)
        print(datastructures[ok_index].name())
    elif oks > 1:
        print('not sure')
    else:
        print('impossible')
    
