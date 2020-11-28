def choose(n,k):
    v = 1
    for i in range(1, k +1):
        v= v * (n +1-i)/i
    return v

def solve(s):
    per_foot = s/2
    max_ones = per_foot/3
    if (per_foot- max_ones) % 2 == 1:
        max_ones -= 1
    ways = 0
    for ones in range(max_ones, -1, -2):
        twos = (per_foot - ones)//2
        ways_per_foot = choose(ones+ twos, ones)
        
        #print('Herp {} {} {} {}'.format(per_foot, max_ones, ones, ways_per_foot))
        ways += ways_per_foot ** 2
    return ways


P= int(raw_input())
for p in range(P):
    K, S = [int(v) for v in raw_input().split()]
    print('{} {}'.format(K, solve(S)))