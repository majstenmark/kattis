import math


N, P  = map(int, raw_input().split())

f = P * 1.0/(N+1)
bestprob = f
resM = 1
T_old = N + 1
for m in range(2, 4 * N):
    T_new = T_old + 1
    f = f * (T_old - P + 1) * 1.0/ T_new
    prob = m * f
    #print 'prob', prob
    if prob < bestprob:

        break
    bestprob = max(bestprob, prob)
    resM =m
    T_old = T_new
print bestprob
