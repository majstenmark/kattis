import math

lines, exectime, addline = map(int, raw_input().split())

times = [-1]* (lines +1)
def time(loc):
    if loc<=1:
        return 0
    if times[loc] != -1:
        return times[loc]
    opt = 10**20
    for added in range(1, int(math.sqrt(loc)) +1):
        left = (loc + added)/(added+1)
        test = added*addline + exectime + time(left)
        opt = min(opt, test)
    i = (loc + added)/(added+1)
    for j in range(i, 0, -1):
        added = (loc + j -1)/j - 1
        #s = '{} {} {}'.format(loc,added, j)
        #print(s)
        test = added*addline + exectime + time(j)
        opt = min(opt, test)

    times[loc] = opt
    return opt
print(time(lines))
