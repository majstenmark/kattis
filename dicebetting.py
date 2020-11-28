throws, sides, needed = [int(v) for v in raw_input().split()]
prob = [[0.0 for _ in range(sides+1)] for i in range(throws+1)]
prob[0][0] = 1.0
sinv = 1.0/sides
for throw in range(1, throws + 1):
    for k in range(1, sides + 1):
        prob[throw][k] = prob[throw -1][k-1] *(sides-k +1) * sinv + prob[throw-1][k] * k * sinv
#print(prob)
print(sum(prob[-1][needed:]))

