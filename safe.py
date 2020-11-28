INF = 10**12

def bit_set(sz):
    v = []
    for i in range(N):
        if sz&(1<<i):
            v.append(i)
    return v

def pairs(bits):
    bit_arr = bit_set(bits)
    for ai in range(len(bit_arr)):
        for bi in range(ai+1, len(bit_arr)):
            yield bit_arr[ai], bit_arr[bi]
        

def solve(bits, side):
    if (bits, side) in times:
        return times[bits, side]
    times[bits, side] = INF
    if side:
        for a, b in pairs(bits):
            pair_time = max(ns[a], ns[b])
            the_others = bits ^ (1 << a) ^ (1 << b)
           # print(bits, a, b)

            others_time = solve(the_others, not side)
            times[bits, side] = min(pair_time + others_time, times[bits, side])
    else:
        for a in bit_set(orig - bits):
            my_time = ns[a]
           # print(bits, a)
            the_others = bits ^ (1 << a)
            others_time = solve(the_others, not side)
            times[bits, side] = min(my_time + others_time, times[bits, side])
    return times[bits, side]

NN = [int(v) for v in raw_input().split()]
N = NN[0]
ns = NN[1:]
orig = 2 ** N - 1
times = {}
times[0, False] = 0
best_time = solve(orig, True)
print(best_time)


            

