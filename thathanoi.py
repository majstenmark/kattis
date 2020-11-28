import math

def sanity(li):
    for i in range(len(li) -1):
        if li[i] < li[i+1]:
            return False
    return True

def solve(s, h, g, n):
    cnt = 0
    #print(s, h, g, n)
    if len(s) == len(g) == len(h) == 0:
        return True, 0
    if len(s) > 0 and s[0] == n:
        #on start
        #print('On start', n)
        ok, c  = solve(s[1:], g, h, n-1)
        if not ok:
            return False, -1
        cnt += c
    elif len(g) >0 and g[0] == n:
        #on goal

        #print('On gaol', n)
        cnt += math.pow(2, n-1)
        ok, c = solve(h, s, g[1:], n-1)
        if not ok:
            return False, -1
        cnt += c
    else:
        #on help
        #print('On help', n)
        return False, -1
    #print(n, 'returns ', int(cnt))
    return True, int(cnt)

start = [int(v) for v in raw_input().split()][1:]
help = [int(v) for v in raw_input().split()][1:]
goal = [int(v) for v in raw_input().split()][1:]
N = len(start) + len(help) + len(goal)
if sanity(start) and sanity(help) and sanity(goal):
    ok, cnt = solve(start, help, goal, N)
    if ok:
        print(int(math.pow(2, N)) - 1 - cnt)
    else:
        print('No')
else:
    print('No')
