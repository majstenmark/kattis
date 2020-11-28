def word2int(w):
    val = 0
    for ch in w:
        val = val | 1 << (ord(ch) - ord('a'))
    return val

def countFrom(index, used):
    if index == N:
        return 0
    # use or do not use
    # use the word
    nused = used | wordints[index]
    if nused == 2 ** 26 - 1:
        withWord = 2 ** (N - index -1)
    else:
        withWord = countFrom(index + 1, nused)
    # without
    withoutWord = countFrom(index + 1, used)
    return withWord + withoutWord


N = int(raw_input())
words = [raw_input() for n in range(N)]
wordints = [word2int(w) for w in words]
count = countFrom(0, 0)
print(count)
