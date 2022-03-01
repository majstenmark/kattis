from collections import *
try: inp = raw_input
except: inp = input
def ni(): return int(inp())
def nl(): return [int(x) for x in inp().split()]

def accept(itr):
    w = next(itr)
    if w == 'truther':
        return ('T', int(next(itr)))
    if w == 'fabulist':
        return ('F', int(next(itr)))
    if w == 'charlatan':
        return ('C', int(next(itr)))
    if w == 'not':
        return ('N', accept(itr))
    if w == 'and':
        s1 = accept(itr)
        s2 = accept(itr)
        return ('A', s1, s2)
    if w == 'xor':
        s1 = accept(itr)
        s2 = accept(itr)
        return ('X', s1, s2)

def parse(line):
    words = line.split()
    src = words[0]
    itr = (w for w in words[1:])
    return int(src), accept(itr)

def evalStmt(assignments, stmt):
    op = stmt[0]
    for v in 'TFC':
        if op == v:
            return assignments[stmt[1]] == v
    if op == 'N':
        return not evalStmt(assignments, stmt[1])
    if op == 'A':
        return evalStmt(assignments, stmt[1]) and evalStmt(assignments, stmt[2])

    if op == 'X':
        return evalStmt(assignments, stmt[1]) ^ evalStmt(assignments, stmt[2])
        
    assert 0

def isOK(A, stmts):
    state = defaultdict(lambda: True)
    first = {}
    for src, stmt in stmts:
        x = evalStmt(A, stmt)
        tp = A[src]
        if tp == 'T' and not x: return False, 'T tells F'
        if tp == 'F' and x: return False, 'F tells T'
        if tp == 'C':
            if src not in first:
                first[src] = x
                if x == False: return False, 'cat False directly.' 
            if x and state[src] == False: return False, 'trueth again'
            if not x and state[src]:
                state[src] = False
    for k, v in A.items():
        if v == 'C':
            if state[k]:
                return False, 'catalan never lies'
    return True, 'OK'


N, K = nl()
stmts = []
for _ in range(K):
    stmts.append(parse(inp()))

def gen(n):
    if n == 0: return ['']
    out = []
    V = gen(n-1)
    for x in 'TFC':
        for L in V:
            out.append(L + x)
    return out
        
    

import itertools

for c in gen(N):
    A = {}
    for i in range(N):
        A[i+1] = c[i]
    ok, msg = isOK(A, stmts)
    if ok:
        for x in c:
            if x == 'T': print('truther')
            if x == 'F': print('fabulist')
            if x == 'C': print('charlatan')



