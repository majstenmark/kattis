S = input().split()
ae = 0
for w in S:
    if 'ae' in w:
        ae += 1
if ae >= 0.4 * len(S):
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')