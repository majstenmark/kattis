def pattern(p):
    r = ''.join('R' if x == 'L' else 'L' for x in p[::-1])
    return p + 'L' + r

def zfun(t):
    z = [0]*len(t)
    n = len(t)
    l, r = (0,0)
    for i in range(1,n):
        if i < r:
            z[i] = min(z[i-l], r-i+1)
        while z[i] + i < n and t[i+z[i]] == t[z[i]]:
            z[i]+=1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z

patterns = ['L']
for n in range(1, 10):
    patterns.append(pattern(patterns[n-1]))


T = int(raw_input())
for t in range(T):
    line = raw_input().split()
    N = int(line[0])
    S = line[1]
    index = -1 if N > len(patterns) else N -1
#    print patterns[index]
    z = zfun(S + '#' + patterns[index])

    p = max(z)
    if p >= len(S):
        print 'Case {}: Yes'.format(t+1)
    else:
        print 'Case {}: No'.format(t+1)
