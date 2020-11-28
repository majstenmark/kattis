def add(c, s, l, r):
    sub = s[l:r]
    if sub not in c:
        c[sub] = 0
    c[sub] += 1
def rm(c, s, l, r):
    sub = s[l:r]
    c[sub] -= 1
    if c[sub] == 0:
        del c[sub]

def run(n, s):
    possibleStart = []
    for startindex in range(n):
        counter = {}
        index = startindex
        # fill with 2**N sets
        while index + n <= len(s) and index < startindex + n * 2**n:
            add(counter, s, index, index+n)
            index += n
        # slide
        if len(counter) == 2 ** n:
            possibleStart.append(startindex)
            continue

        while index + n <= len(s):
            rm(counter, s, index - n * 2**n, index + n- n * 2**n )
            add(counter, s, index, index+n)

            if len(counter) == 2 ** n:
                possibleStart.append(index + n - n * 2**n)
                index = len(s)
            index += n
    return (len(possibleStart) > 0, min(possibleStart+[len(s)]))

T = int(raw_input())
for t in range(T):
    S = raw_input()
    for N in range(10, 0,-1):
        success, skip = run(N, S)
        if success:
            print('{} {}'.format(N, skip))
            break
