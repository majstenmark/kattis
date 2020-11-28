def digsum(num):
    s = str(num)
    su = 0
    for ch in s:
        su += int(ch)
    return su

def solve(n):
    ds = digsum(n)
    #print('orig', ds)
    for num in range(11, 10**8):
        m = num * n
        test_ds = digsum(m)
        if test_ds == ds:
            return num
    return None

N = int(raw_input())
while N != 0:
    res = solve(N)
    print(res)
    N = int(raw_input())
    