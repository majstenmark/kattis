from collections import defaultdict as dd
from heapq import heappop as pop
from heapq import heappush as push


def topsort(ppl, parents,family):
    li = []
    q = []
    for person in ppl:
        push(q, (parents[person], person))
    while q:
        p, f = pop(q)
        if p == 0:
            li.append(f)
            for child in family[f]:
                parents[child] -= 1
                push(q, (parents[child], child))
    return li

N, M = map(int, raw_input().split())
king = raw_input()
family = dd(list)
blood = dd(int)
blood[king] = 1.0
parents = dd(int)
parents[king]= 0
ppl = set()

for rel in range(N):
    child, dad, mom = raw_input().split()
    family[dad].append(child)
    family[mom].append(child)
    parents[child] = 2
    ppl.add(child)
    ppl.add(mom)
    ppl.add(dad)

claims = []
for m in range(M):
    claims.append(raw_input())

topsorted = topsort(ppl, parents, family)
#print topsorted

for person in topsorted:
#    print 'looking at ', person
    halfblood = blood[person] * 0.5

    for child in family[person]:

        blood[child] += halfblood

#        print 'added  ', halfblood,  ' to ', child, blood[child]

mostBlood = 0.0
succ = ''
for claimant in claims:
#    print claimant, blood[claimant]
    if blood[claimant] > mostBlood:
        succ = claimant
        mostBlood = blood[claimant]
print succ
