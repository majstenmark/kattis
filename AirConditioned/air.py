N = int(raw_input())
intervals = []
START = 0
END = 1
for n in range(N):
    L, U = map(int, raw_input().split())
    intervals.append((L, START, n))
    intervals.append((U, END, n))
intervals.sort()
cnt = 1
started = 0
current = set()
for time, typ, i in intervals:   
   # print('{} {} {} {}'.format(time, typ, started, cnt)) 
    if typ == START:
        started += 1
        current.add(i)
    if started >= N:
        break    
    if typ == END and i in current and started < N:
        cnt += 1
        current = set()
    
print(cnt)