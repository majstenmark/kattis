import math
L, K,T1, T2, H = map(float, raw_input().split())
if H < L:
    print '{} {}'.format(H, H)
    exit()
h = H - L # above the leak
c = L + K * T1 + K * T2 + h
f1 = 0.5 * c/T1 - math.sqrt((c/2/T1)**2 - K*L/T1)
f2 = 0.5 * c/T1 + math.sqrt((c/2/T1)**2 - K*L/T1)
F2 = f2 * T1

if H == L:
    print '{} {}'.format(H, F2)
else:
    print '{} {}'.format(F2, F2)
#print '{} {}'.format(F1, F2)
