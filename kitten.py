import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

K = ni()
tree = {}
while True:
    branch = nl()
    if branch[0] == -1:
        break
    p = branch[0]
    for c in branch[1:]:
        tree[c] = p
path = []
curr = K
while curr in tree:
    path.append(curr)
    curr = tree[curr]
path.append(curr)
print(' '.join(map(str, path)))