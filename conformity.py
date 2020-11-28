from collections import Counter

N = int(raw_input())
cnt = Counter()
comb = set()
for n in range(N):
    courses =[int(v) for v in raw_input().split()]
    courses.sort()
    s = str(courses)
    cnt[s] +=1
    comb.add(s)
max_cnt = 0
for c in comb:
    max_cnt = max(max_cnt, cnt[c])
pop = 0
for c in comb:
    if cnt[c]== max_cnt:
        pop += cnt[c]
print(pop)
