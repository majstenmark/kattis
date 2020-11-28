from collections import *
import sys
sys.setrecursionlimit(10000)
inp = input
def ni(): return int(inp())
def nl(): return [int(v) for v in inp().split()]

R = {
    'N' : 'E',
    'E' : 'S',
    'S' : 'W',
    'W' : 'N'}

L = {
    'S' : 'E',
    'W' : 'S',
    'N' : 'W',
    'E' : 'N'}
class Bot:
    def __init__(self, id, x, y, d):
        self.id = id
        self.x = x
        self.y = y
        self.d = d
    def pos(self):
        return (self.x, self.y)
    def forward(self):
        d = self.d
        if d == 'E':
            self.x += 1
        if d == 'W':
            self.x -= 1
        if d == 'N':
            self.y += 1
        if d == 'S':
            self.y -= 1
    def left(self):
        self.d = L[self.d]
    def right(self):
        self.d = R[self.d]
        

def solve():
    A, B = nl()
    N, M = nl()
    R = []
    Occ = {}
    for i in range(N):
        x, y, d = inp().split()
        b = Bot(i+1, int(x), int(y), d)
        R.append(b)
        Occ[b.pos()] = b
    Instrs = [inp().split() for _ in range(M)]
    for id, a, r in Instrs:
        id = int(id) - 1
        r = int(r)
        bot = R[id]
        if a == 'F':
            for _ in range(r):
                del Occ[bot.pos()]
                bot.forward()
                nP = bot.pos()
                if nP in Occ:
                    return 'Robot {} crashes into robot {}'.format(bot.id, Occ[nP].id)
                x, y = nP
                #print(bot.id, x, y)
                if x <= 0 or x > A or y <= 0 or y > B:
                    return 'Robot {} crashes into the wall'.format(bot.id)
                Occ[nP] = bot
        elif a == 'R':
            for _ in range(r):
                bot.right()
        else:
            for _ in range(r):
                bot.left()
    return 'OK'
        

K = ni()
for _ in range(K):
    print(solve())