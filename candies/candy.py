T = int(raw_input())
for t in range(T):
    raw_input()
    N = int(raw_input())
    candies = []
    for n in range(N):
        candies.append(int(raw_input()))
    s = sum(candies)
    if s % N == 0:
        print('YES')
    else:
        print('NO')
