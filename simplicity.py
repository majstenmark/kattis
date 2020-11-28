from collections import Counter
S = raw_input()
cnt = Counter()
for ch in S:
    cnt[ch] += 1
cnt_list = []
for k, v in cnt.items():
    cnt_list.append((v,k))
cnt_list.sort(reverse=True)
erase = 0
for i in range(2, len(cnt_list)):
    erase += cnt_list[i][0]
print(erase)
