N = int(raw_input())
times = [int(v) for v in raw_input().split()]
mx = max(times)
su = sum(times)
print(max(2 *mx, su))