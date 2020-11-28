def isPrime(n):
    for i in range(2, int(n**0.5)+ 1):
        if n % i == 0:
            return False
    return True

def matchToPrime(ssum, lastnumber):
    for n in range(lastnumber+1, lastnumber + 50):
        if isPrime(n + ssum):
            return n
    return -1

N, B = [int(v) for v in raw_input().split()]
nbrs = []


for n in range(1, N):
    nbrs.append(n)
s = sum(nbrs)
last = matchToPrime(s, nbrs[-1])
if last > B:
    smudge = last - B
    k = smudge/len(nbrs) + smudge % len(nbrs) > 0
    if nbrs[-1] + k >= B:
        print('impossible')
        exit()
    else:
        for i in range(1, smudge+1):
            nbrs[(len(nbrs) - i) % len(nbrs)] += 1
    nbrs.append(B)
else:
    nbrs.append(last)
for start in range(N):
    line = []
    for i in range(N):
        line.append(str(nbrs[(start + i)%len(nbrs)]))
    print(' '.join(line))
