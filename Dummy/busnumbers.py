from collections import defaultdict as dd
import math

M = int(raw_input())

squares = []
for n in range(1, int(M ** (1.0/3)) + 1):
    squares.append(n**3)
res = dd(list)
#print(squares)
for i in range(len(squares)):
    for j in range(i + 1, len(squares)):
        r = squares[i] + squares[j]
        res[r].append((squares[i], squares[j]))
for r in range(M, -1, -1):
    if len(res[r]) >= 2:
       # print(res[r])
        break
if r > 0:
    print(r)
else:
    print('none')