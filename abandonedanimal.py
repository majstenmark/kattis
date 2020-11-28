from collections import defaultdict as dd
import sys

itr = (line for line in sys.stdin.read().split('\n'))
N = int(next(itr))
K = int(next(itr))
ids = {}
id = 0
stores2items= [set() for _ in range(N)]
for k in range(K):
    istr, item = next(itr).split()
    i = int(istr)
    stores2items[i].add(item)

M = int(next(itr))
li = [next(itr) for _ in range(M)]
fw = []
bw = []

curr_store = 0
for item in li:
    while curr_store < N and item not in stores2items[curr_store]:    
        curr_store += 1
    if curr_store == N:
        break
    fw.append(curr_store)

curr_store = N-1
for item in li[::-1]:
    while curr_store >= 0 and item not in stores2items[curr_store]:
        curr_store -= 1
    if curr_store == -1:
        break
    bw.append(curr_store)

if fw == bw[::-1] and len(fw) == M:
    print('unique')
    exit()
elif len(fw) == M:
    print('ambiguous')
    exit()

print('impossible')
    
