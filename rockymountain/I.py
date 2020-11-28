Q, M , S, L = map(int, raw_input().split())
qtime = Q * ((L + M -1)/M)

smachtime = qtime * M - L * Q
#print 'smachtime'
sleft = max(S - smachtime, 0)
#print 'left', sleft
stime = max((sleft + M -1)/M, 0)
print qtime + stime
