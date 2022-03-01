import sys
lines = sys.stdin.readlines()

def tobase(n, b):
    digits = []
    if n== 0:
        return '0'
    while n > 0:
        rem = n % b
        digits.append(str(rem))
        n = n//b
    val = digits[::-1]
    return ''.join(val)

for line in lines[0:-1]:
    data = line.split()
    b = int(data[0])
    p = int(data[1], b)
    m = int(data[2], b)
    ans = p % m
    res = tobase(ans, b)
    print(res)
