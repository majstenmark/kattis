N = int(raw_input())
days = [int(v) for v in raw_input().split()]
min_day = days.index(min(days))
print(min_day)