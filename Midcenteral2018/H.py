def getdigs(c):
    digs=set()
    while c:
        digs.add(c % 10)
        c /= 10
    return digs

def div(c, digits):
    for d in digits:
        if d == 0 or c % d != 0:
            return False
    return True

def check(c):
    digits = getdigs(c)
    return len(digits) == 6 and div(c, digits)

L, H = map(int, raw_input().split())
cnt = 0
for n in range(L, H +1):
    if check(n):
        cnt += 1
print cnt
