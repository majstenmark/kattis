import sys
from collections import defaultdict as dd, deque
from heapq import heappush as push, heappop as pop

def nl(): return [int(v) for v in input().split()]

reuse = {}
prev = 1
found = []
lowest = []
pricetocity = {}
queries = 0

def ask(mid):
    global queries
    #print('Testing ask ', mid)
    if mid == 1: return 0
    if mid in reuse:
        return reuse[mid]
    '''
    if mid == C+1 or queries == 1500:
        s = '1' * A
        print(f'A {s}', flush = True)
        exit()
    '''
    print(f'Q {mid}', flush = True)
    queries += 1
    res = int(input())
    reuse[mid] = res
    pricetocity[res] = mid
    push(found, (res, mid))
    push(lowest, (res, mid))
    return res

def gethighest(pony):
    while len(found) > 0 and found[0][0] <= pony:
        price, index = pop(found)
    if len(found) > 0:
        return found[0][1]
    return C+1
'''
def getlowest(pony):
    hi = gethighest(pony)
    for p in range(prev, hi):
        
    return prev
'''
def check(a, b):
    if a in reuse and b in reuse:
        if reuse[b] - reuse[a] == b - a:
            for i in range(a, b):
                reuse[a+i] = reuse[a] + i


def find(pony):
    if pony in pricetocity:
        return pricetocity[pony]
    lo = 1#getlowest(pony)
    hi = C+1 #gethighest(pony)
    #print('Pony ', pony, ' hi = ', hi)
    while lo + 1< hi:
        #print('Lo = ', lo, 'hi = ', hi)
        mid = (lo + hi)//2
        check(lo, hi)
        price = ask(mid)
        if price <= pony:
            lo = mid
        else:
            hi = mid
    return lo


C, A = nl()
S = nl()
ponies = [(p, i) for i, p in enumerate(S)]
ponies.sort(reverse = True)
res = {}
for pony, index in ponies:
    #print('Doing pony', pony)
    city = find(pony)
    res[index] = city
    prev = city
out = []
for i in range(A):
    out.append(str(res[i]))
s = ' '.join(out)
print(f'A {s}')