n = input()
def p2(x):
    while x != (x&-x):
        x += (x&-x)
    return x

def solve(x, y, side):
    assert min(x, y) != 0
    if (x==1 and y < 3) or (x < 3 and y==1): return 0
    mid = side//2
    mh = mid//2
    if max(x, y) <= mid:
        if min(x, y) <= mid//2:
            return solve(x, y, mid)
    if y > mid and (y > mid+ mh or x <= mh):
        return 1 + solve(side - y + 1, x, mid)
    elif x > mid and (x > mid+mh or y <= mh):
        return 3 + solve(y, side - x + 1, mid)
    return solve(x - mh, y-mh, mid)




for _ in range(n):
    x, y = map(int, raw_input().split())
    s = 2*max(p2(x+1), p2(y+1))
    print solve(x+1, y+1, s)%4
