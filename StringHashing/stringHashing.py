import sys
P = 1181118711931201
x = 26

S = raw_input()

pre = [0  for _ in range(len(S) + 1)]
wHash = 0
for i in range(len(S)):
    wHash *= x
    wHash += ord(S[i])
    wHash %= P
    pre[i+1] = wHash

#print pre
Q = int(raw_input())
for q in range(Q):
    L, R = map(int, raw_input().split())
    preSum = pre[L] * pow(x, (R -L), P)
    #print 'presum', preSum
    su = pre[R]
    ha = (su - preSum) %P
    print(ha)
