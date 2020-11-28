R, N = [int(v) for v in raw_input().split()]
booked = set([int(raw_input()) for _ in range(N)])
for r in range(1, R+1):
    if r not in booked:
        print(r)
        exit()
print('too late')