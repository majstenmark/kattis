import sys
data = sys.stdin.read().split()
d2 = []
inside = False
query = False
START = '<text>'
END = '</text>'
Q = '<top'
for w in data:
    if not inside:
        inside = True
        if w == Q:
            query = True
        elif w == START:
            query = False
        else:
            assert 0
        push = []
    else:
        if query:
            if len(push) == 0:
                d2.append((1, int(w)))
                push.append(1)
            else:
                inside = False
        else:
            if w == END:
                inside = False
                d2.append((0, push))
            else:
                push.append(w)



from collections import *
C = Counter()
days = []
for c, d in d2:
    if c == 1:
        V = sorted(C.items(), key=lambda x: (-x[1], x[0]))
        out = V[:d]
        i = d
        while i < len(V) and V[i][1] == out[-1][1]:
            out.append(V[i])
            i += 1
        print('<top {}>'.format(d))
        print('\n'.join(map(lambda x: '{} {}'.format(x[0], x[1]), out)))
        print('</top>')
    else:
        D = filter(lambda x: len(x) > 3, d)
        days.append(D)
        if len(days) > 7:
            for w in days[-8]:
                C[w] -= 1
        for w in D:
            C[w] += 1
