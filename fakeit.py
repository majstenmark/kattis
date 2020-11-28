N, M = [int(v) for v in raw_input().split()]
P = [int(v) for v in raw_input().split()]
R = [int(v) for v in raw_input().split()]
C = []
for n in range(N):
    c, t = [int(v) for v in raw_input().split()]
    C.append((t, c -1)) #type starts with 1
C.sort()

timestamps = {}
cnt = 0
for i, (t, c) in enumerate(C):
    relevant_times = [t - P[i], t, t + R[i]]
    for time in relevant_times:
        if time not in timestamps:
            timestamps[time] = cnt
            cnt += 1
#nbr of ppl served at time t

change = [0 for _ in range(N)]
no_change = [0 for _ in range(N)]
prev = [-1 for _in range(N)]
prev_type = {c: -1 for c in range(M)}

for i, (t, c) in enumerate(C):
    prev[i] = prev_type[c]
    prev_type[c] = i
    
print(prev)
for n in range(N):
    #no change

    #no change after
    t, c = C[n]
    prev_index = prev[n]
    prev_timestamp = timestamp[C[prev_index][0]]
    my_timestamp = timestamp[t]
    alt1 = no_change[prev_timestamp] #nbr of ppl finished where the last had the same outfit as this pony
    no_change[my_timestamp] = max(no_change[my_timestamp], alt1 + 1)
    #change after
    timestamp_after = timestamp[t + R[n]]
    change[timestamp_after] = max(change[timestamp_after], alt1 + 1)

    #change before and change after
    must_end_time = t - P[n]
    end_timestamp = timestamp[must_end_time]
    alt2 =  
    #change before, do not change after