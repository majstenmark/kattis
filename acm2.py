N, P = [int(v) for v in raw_input().split()]
probs = [int(v) for v in raw_input().split()]
first = probs[P]
others = probs[0:P] + probs[P+1:]
others.sort()
order = [first] + others
last = 0
solved = 0
penalty = 0
for pr in order:
    last = last + pr
    if last > 300:
        break
    solved += 1
    penalty += last
print('{} {}'.format(solved, penalty))