S = input()
N = len(S)
MOD = 10 ** 9 + 7
pref1 = [0] * N # antal 1:or innan
pref0 = [0] * N #antal 0:or bakom
prefqm = [0] * N
sufqm = [0] * N
cnt = 0
qm = 0
for i in range(N):
    ch = S[i]
    pref1[i] = cnt
    if ch == '1':
        cnt += 1
    prefqm[i] = qm 
    if ch == '?':
        qm += 1
K = qm
cnt = 0
qm = 0
for i in range(N-1, -1, -1):
    ch = S[i]
    pref0[i] = cnt
    if ch == '0':
        cnt += 1
    sufqm[i] = qm 
    if ch == '?':
        qm += 1

inv = 0
for i, ch in enumerate(S):
    if ch == '0':
        inv += pref1[i]

times = pow(2, K, MOD)
inv = (times * inv) % MOD
if K >= 2:
    twoqm = K * (K-1) //2 * pow(2, K-2, MOD)
    inv += twoqm
if K:
    oth = pow(2, K-1, MOD)

for i, ch in enumerate(S):
    if ch == '?':
        inv += oth * pref1[i]
        inv += oth * pref0[i]
        inv %= MOD
    
print(inv% MOD)
        
