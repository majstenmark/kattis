
def digvec(x):
    digits = [0] * 10

    while x:
        di = x % 10
        digits[di] += 1
        x //= 10
    return digits


def comp(d1, d2):
    for i in range(len(d1)):
        if d1[i] != d2[i]:
            return False
    return True

xs = input()
x = int(xs)
dv = digvec(x)
mx = 10 ** len(xs)
for n in range(x + 1, mx):
    dv2 = digvec(n)
    if dv == dv2:
        print(n)
        exit()
print(0)
