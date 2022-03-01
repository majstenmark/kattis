def solve(x1, y1, x2, y2):
    dx = abs(x1 -x2)
    dy = abs(y1 -y2)
    cmn = min(dx, dy)
    steps = cmn * 2
    left = max(dx, dy) - cmn
    #print(f'Common {cmn}')
    #print(f'Left {left}')
    
    if left > 0:
        if left % 2 == 0:
            steps += left * 2
        else:
            steps += left//2 * 4 + 1
        
    return str(steps)

T = int(input())
out = []
for _ in range(T):
    x1, y1, x2, y2 = [int(v) for v in input().split()]
    out.append(solve(x1, y1, x2, y2))
print('\n'.join(out))