T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    shops = map(int, raw_input().split())
    leftmost = min(shops)
    rightmost = max(shops)
    print 2 * (rightmost - leftmost)
