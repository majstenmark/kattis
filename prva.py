import copy

def horizontal(r, c):
    letters = []
    for rr in range(r, R):
        if hcw[rr][c] != '#':
            letters.append(hcw[rr][c])
            hcw[rr][c] = '#'
        else:
            return ''.join(letters)
    return ''.join(letters)

def vertical(r, c):
    letters = []
    for cc in range(c, C):
        if vcw[r][cc] != '#':
            letters.append(vcw[r][cc])
            vcw[r][cc] = '#'
        else:
            return ''.join(letters)
    return ''.join(letters)

R, C = [int(v) for v in raw_input().split()]
hcw = [list(raw_input()) for _ in range(R)]
vcw = copy.deepcopy(hcw)

words = []
for r in range(R):
    for c in range(C):
        cand = [horizontal(r, c), vertical(r, c)]
        for word in cand:
            if len(word) >= 2:
                words.append(word)
words.sort()
print(words[0])