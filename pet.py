score = []
for n in range(5):
    p = [int(v) for v in raw_input().split()]
    score.append((sum(p), n+1))
score.sort(reverse = True)
print('{} {}'.format(score[0][1], score[0][0]))