from collections import defaultdict as dd

def dowalk(steps, r, c, walks):
    if steps == 0 and (r, c) == (0, 0):
        return 1
    if steps == 0:
        return 0
    if (steps, r, c) in walks:
        return walks[(steps, r, c)]


    dirs = [(0, -1), (0, 1), (-1, -1), (-1, 0), (1, 1), (1, 0)]
    cnt = 0
    for dx, dy in dirs:
        cnt += dowalk(steps -1, dx + r, dy + c, walks)
    walks[(steps, r, c)] = cnt
#    print 'Added {} to steps {} r {} c {}'.format(cnt, steps, r, c)
    return cnt

def walkH(steps):
    walks = {}
    dirs = [(0, -1), (0, 1), (-1, -1), (-1, 0), (1, 1), (1, 0)]
    for dr, dc in dirs:
        walks[(1, dr, dc)] = 1
    cnt = 0
    #print walks
    for dx, dy in dirs:
        cnt += dowalk(steps-1, dx, dy, walks)
    return cnt

T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    print walkH(N)
