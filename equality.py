import sys
from collections import defaultdict as dd
from heapq import heappush as push, heappop as pop

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())


def modlist(S):
    inpar = False
    out = []
    for ch in S:
        if ch == '[':
            inpar = True
            out.append(ch)
        elif ch == ']':
            inpar = False
            out.append(ch)
        elif inpar and ch == ',':
            out.append(';')
        else:
            out.append(ch)
    return ''.join(out)

def parse(S):
    S = modlist(S)
    S = S.replace('(', ' ')
    S = S.replace(')', ' ')
    S = S.replace(',', ' ')
    return build(S)

CONCAT = 'CONCAT'
SHUFFLE = 'SHUFFLE'
SORT = 'SORTED'
LIST = 'LIST'
IGNORE = 'IGNORE'



def build(S):

    types = {}
    types[-1] = 'ROOT'
    tree = dd(list)
    tokens = S.split()
    stack = [(-1, "ROOT")]
    cnt = dd(int)
    id = 0
    order = []
    no_ssh = 0
    for w in tokens:
        par, _ = stack[-1]
        tree[par].append(id)
        if len(w) == 0: continue
        if w == 'concat':
            stack.append((id, CONCAT))
            types[id] = CONCAT

        elif w == 'shuffle':
            stack.append((id, SHUFFLE))
            if no_ssh > 0: 
                types[id] = IGNORE
            else:
                types[id] = SHUFFLE
            no_ssh += 1
            
        elif w == 'sorted':
            stack.append((id, SORT))
            if no_ssh > 0:
                types[id] = IGNORE
            else:
                types[id] = SORT
            no_ssh += 1
            
        else:
            types[id] = LIST, tolist(w)
            order.append(id)

        cnt[par] += 1
        id += 1
        
        while len(stack) > 0:
            par, ty = stack[-1]
            if ty == 'ROOT': break
            c = cnt[par]
            if ty == CONCAT and c == 2:
                stack.pop()
                order.append(par)
            
            elif ty != CONCAT and c == 1:
                if ty == SORT: no_ssh -= 1
                if ty == SHUFFLE: no_ssh -= 1
                stack.pop()
                order.append(par)
            else:
                break
    order.append(-1)
    return tree, types, order

def tolist(S):
    S = S.replace('[', '')     
    S = S.replace(']', '')
    S = S.replace(';', ' ')
    li = []
    for w in S.split():
        li.append(int(w))
    return li

from collections import deque

def evaltree(tree, order, types, inc = True):
    dp = dd(list)
    for id in order:
        ty = types[id]
        children = tree[id]
        #print(f'Handling {id} {children}')
        if ty == CONCAT:
            if len(dp[children[0]]) < len(dp[children[1]]):
                for ch in dp[children[0]]:
                    dp[children[1]].appendleft(ch)
                dp[id] = dp[children[1]]
            else:
                dp[children[0]].extend(dp[children[1]])
                dp[id] = dp[children[0]]

        elif ty == SORT:
            li = sorted(list(dp[children[0]]))
            dp[id] = deque(li)
        elif ty == SHUFFLE:
            if inc:
                li = sorted(list(dp[children[0]]))
                dp[id] = deque(li)
            else:
                li = sorted(list(dp[children[0]]), reverse = True)
                dp[id] = deque(li)
        elif ty == IGNORE:
            dp[id] = dp[children[0]]
        elif ty == 'ROOT':
            out = []
            #print(types)
            for ch in children:
                out.extend(dp[ch])
            return out
        else:
            typ, vals = ty
            assert typ == LIST
            dp[id] = deque(vals)
    #print(types)
    return dp[-1]
            


    
    

A = inp()
B = inp()

atree, atypes, aorder = parse(A)
btree, btypes, border = parse(B)
ainc = evaltree(atree, aorder, atypes, inc = True)
adec = evaltree(atree, aorder, atypes, inc= False)
binc = evaltree(btree, border, btypes, inc = True)
bdec = evaltree(btree, border, btypes, inc = False)
'''
print(ainc)
print(binc)
print(adec)
print(bdec)
'''
if ainc == binc and adec == bdec:
    print('equal')
else:
    print('not equal')
