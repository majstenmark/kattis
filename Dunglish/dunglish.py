from collections import defaultdict as dd

N = int(raw_input())
dutch = raw_input().split()
M = int(raw_input())
correct = dd(list)
incorrect = dd(list)
for trans in range(M):
    d, e, c = raw_input().split()
    if c == 'correct':
        correct[d].append(e)
    else:
        incorrect[d].append(e)
corr_cnt = 1
for word in dutch:
    corr_cnt *= len(correct[word])
tot_cnt = 1
for word in dutch:
    tot_cnt *= (len(correct[word]) + len(incorrect[word]))
inc_cnt = tot_cnt - corr_cnt
if tot_cnt == 1:
    trans= []
    for word in dutch:
        if len(correct[word]) > 0:
            trans.append(correct[word][0])
        else:
            trans.append(incorrect[word][0])
    print(' '.join(trans))
    print('correct' if corr_cnt > 0 else 'incorrect')
else:
    print('{} correct'.format(corr_cnt))
    print('{} incorrect'.format(inc_cnt))