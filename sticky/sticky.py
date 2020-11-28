N= int(input())
if N > 100:
    print('possible')
    exit(0)
sticks = [int(v) for v in input().split()]
sticks.sort(reverse = True)

for i in range(N-2):
    if sticks[i] < sticks[i+1] + sticks[i + 2]:
        print('possible')
        exit(0)

print('impossible')
