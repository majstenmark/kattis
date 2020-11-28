ab = 'abcdefghijklmnopqrstuvwxyz'
w = {ch: index + 1 for index, ch in enumerate(ab)}
L, W = map(int, raw_input().split())
if W > L * 26 or W < L:
    print 'impossible'
    exit()
res = ['a'] * L
cnt = L
start = 0
while cnt < W:
    toset = min(26, W - cnt + 1)
    res[start] = ab[toset -1]
    start += 1
    cnt -= 1
    cnt += w[ab[toset -1]]

print ''.join(res)
