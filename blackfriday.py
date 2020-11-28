from collections import Counter
N =int(raw_input())
ai =[int(v)-1 for v in raw_input().split()]
index = [-1] * 6
for i, v in enumerate(ai):
    index[v] = i

ai.sort(reverse = True)
cnt = Counter()
for v in ai:
    cnt[v] +=1
for hi in ai:
    if cnt[hi] == 1:
        print(index[hi] +1)
        exit()
print('none')