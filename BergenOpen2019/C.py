def nl():
    return [int(v) for v in raw_input().split()]

def ni():
    return int(raw_input())

N, R, K = nl()
mx = max(N+R + (N+R)%2, 2 * K, 2 * R)
print(mx)