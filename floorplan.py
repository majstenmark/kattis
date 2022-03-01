def test(n, M):
    other = M//n
    if other * n == M:
        b, a = min(n, other), max(n, other)
        k = (a -b)//2
        if a -b == 2 * k:
            m = a - k
            if m >=0 and k >= 0:
                return True, m, k
    return False, 0, 0

N = int(input())

mx = int(N **0.5) + 10
for n in range(1, mx):
    ok, m, k =  test(n, N)
    if ok:
        print(m, k)
        exit()
print('impossible')