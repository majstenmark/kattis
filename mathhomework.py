import sys

itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

B, D, C, L = nl()
ans = []
for b in range(L+1):
    for d in range(L+1):
        for c in range(L+1):
            if b * B + d * D + c * C == L:
                ans.append(f'{b} {d} {c}')

#print('WUT', ans)
if len(ans)> 0:
    print('\n'.join(ans))
else:
    print('impossible')