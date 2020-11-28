def insert(n, seq):
    li = []
    for pos in range(n):
        s = seq[0:pos] + [n] + seq[pos: n]
        li.append(s)
    return li

def generate(n):
    if n == 1:
        return [[1]]
    smallerSeqs = generate(n-1)
    thisseqs = []
    for index, smaller in enumerate(smallerSeqs):

        li = insert(n, smaller)
        if index % 2 == 0:
            #backward
            thisseqs.extend(li[::-1])
        else:
            # forward
            thisseqs.extend(li)
    return thisseqs

N = input()
seq = generate(N)
for s in seq:
    o = ' '.join(map(str, s))
    print o
