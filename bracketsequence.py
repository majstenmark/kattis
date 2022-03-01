import sys
import functools
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def isint(i):
    try:
        int(i)
        return True
    except:
        return False

def int_convert(s):
    if isint(s):
        return int(s)
    return s

def lazy_ints(li):
    li = list(map(int_convert, li)) 
    return li

def prod(li):
    p = 1
    for l in li:
        p *= l
        p %= MOD
    return p



MOD = 10**9+7
N = ni()
seq = lazy_ints(inp().split())

stack = [[]]
depth = 0
for t in seq:
    if t == '(':
        depth += 1
        stack.append([])
    elif t == ')':
        li = stack.pop()
        if depth %2 == 0:
            val = sum(li)
        else:
            val = prod(li)
        stack[-1].append(val)
        
        depth -= 1

    else:
        stack[-1].append(t)

s = sum(stack[-1]) % MOD 
print(s)
    
