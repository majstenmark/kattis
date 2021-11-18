import sys
import bisect

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

def reachable_left(stack, index, x, r):
    if len(stack) == 0: return False
    _, pos = stack[-1]
    return pos >= x - r
    

def reachable_right(stack, index, x, r):
    if len(stack) == 0: return False
    _, pos = stack[-1]
    return pos <= x + r
    


N = ni()
cans = [nl() for _ in range(N)]
cans.sort()
left = [[] for _ in range(N)]
right = [[] for _ in range(N)]

stack = []
for index, (x, r) in enumerate(cans):
    while(reachable_left(stack, index, x, r)):
        other, ox = stack.pop()
        left[index].append((other))
    stack.push((index, x))
    
stack = []
for tmp, (x, r) in enumerate(cans[::-1]):
    index = N -1 - tmp
    while(reachable_right(stack, index, x, r)):
        other, ox = stack.pop()
        right[index].append((other))
    stack.push((index, x))




