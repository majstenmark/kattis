P, D = [int(v) for v in raw_input().split()]
cnt = [[0, 0] for i in range(D)]
wa_tot, wb_tot = 0, 0
V = 0.0
for p in range(P):
    d, a, b = [int(v) for v in raw_input().split()]
    d = d -1
    cnt[d][0] += a
    cnt[d][1] += b
for d in range(D):
    a, b = cnt[d]
    maj = (a + b)//2 + 1
    wa, wb = 0, 0
    if a > b:
        wb = b
        excess = a - maj
        wa = excess
    el f   se:
        wa = a
        excess = b - maj
        wb = excess
    wa_tot += wa
    wb_tot += wb
    V += (a + b)
    print('{} {} {}'.format('A' if a > b else 'B', wa, wb))

gap = abs(wa_tot - wb_tot)/V
print(gap)    
