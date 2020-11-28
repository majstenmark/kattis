from collections import defaultdict as dd

data = raw_input().split()
N = int(data[0])
code = list(data[1])
guess = list(data[2])
r = 0
s = 0
for n in range(N):
    c = code[n]
    g = guess[n]
    if c == g and c != '':
        r +=1
        code[n] = ''
        guess[n] = ''
colors_code = dd(int)
for n in range(N):
    c = code[n]
    if c != '':
        colors_code[c] += 1
for n in range(N):
    c = guess[n]
    if colors_code[c] > 0:
        colors_code[c] -= 1
        s += 1
print('{} {}'.format(r, s))


