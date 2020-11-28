K = int(raw_input()) -1
N = int(raw_input())
time = 0
dead = 210
for n in range(N):
    d= raw_input().split()
    dur = int(d[0])
    res =d[1]
    if time + dur >= dead:
        print(K+1) 
        exit()
    time += dur
    if res == 'T':
        K += 1
        K %= 8

