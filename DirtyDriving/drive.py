N, P = map(int, raw_input().split())
cars = map(int, raw_input().split())
cars.sort()
back = 0
for n in range(N):
    reqDist = P * (n +1)
#    print reqDist,n,cars[n]
    back += max(0, reqDist - cars[n]-back)
#    print back
print back + cars[0]
