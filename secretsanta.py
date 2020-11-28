from itertools import permutations
from collections import defaultdict as dd

res = dd(lambda: 0.632120558679)
V = [1.0
,0.5
,0.666666666667
,0.625
,0.633333333333
,0.631944444444
,0.632142857143
,0.632118055556
,0.632120811287
,0.632120535714
,0.632120560766]
for i, v in enumerate(V):
    res[i+1] = v

N = int(raw_input())
print(res[N]) 
