A, B, C = 'A', 'B', 'C'

Adrain = [A, B, C, A, B, C, A, B, C, A, B, C]
Bruno = [B, A, B, C, B, A, B, C, B, A, B, C]
Goran = [C, C, A, A, B, B, C, C, A, A, B, B ]

N = int(raw_input())
ans = raw_input()
a, b, g = 0, 0, 0
for i in range(N):
    ch = ans[i]
    if Adrain[i%12] == ch:
        a += 1
    if Bruno[i%12] == ch:
        b += 1
    if Goran[i%12] == ch:
        g += 1

max_res = max([a, b, g])
print(max_res)
if a == max_res:
    print('Adrian')
if b == max_res:
    print('Bruno')
if g == max_res:
    print('Goran')