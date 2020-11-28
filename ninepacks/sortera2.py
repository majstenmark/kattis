N = int(raw_input())
li = [int(raw_input()) for _ in range(N)]
cnt = 0
sorted_li = li.sort()
pos_orig = {}
pos_sorted = {}

for index, item in enumerate(li):
    pos_orig[item] = index

for index, item in enumerate(sorted_li):
    pos_sorted[item] = index

for item in li:
    pos1 = pos_orig[item]
    pos2 = pos_sorted

print(cnt)
    
