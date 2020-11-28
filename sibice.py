import math
N, W, H = map(int, raw_input().split())
ml = math.sqrt(W **2 + H**2)
for n in range(N):
    L = int(raw_input())
    print('DA' if L <= ml else 'NE')
    