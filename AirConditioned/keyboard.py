keyboard = ['qwertyuiop',
'asdfghjkl',
'zxcvbnm']
keyval = {}
for linenbr, line in enumerate(keyboard):
    for index, letter in enumerate(line):
        keyval[letter] = (linenbr, index)
def diff(a, b):
    (x1, y1) = keyval[a]
    (x2, y2) = keyval[b]
    return abs(x1 - x2) + abs(y1- y2)

def count(w, orig):
    cnt = 0
    for index in range(len(orig)):
        cnt += diff(w[index], orig[index])
    return cnt

T = int(raw_input())
for t in range(T):
    word, cstr = raw_input().split()
    c = int(cstr)
    cand = [raw_input() for _ in range(c)]
    diffs = [(count(x,word), x) for x in cand]
    diffs.sort()
    for cnt, w in diffs:
        print('{} {}'.format(w, cnt))
    
        