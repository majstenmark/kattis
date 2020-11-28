N, M = map(int, raw_input().split())
forward = raw_input()
backward = raw_input()
T = input()
o = ['' for _ in range(100)]
rest = []
for index, ant in enumerate(backward):
     o[index*2] = ant
for t in range(min(T, len(forward))):
    jumpingAnt = forward[t]
    place = (T - t -1)*2 +1
    o[place] = jumpingAnt
for r in range(T, len(forward)):
    rest.append(forward[r])

s = ''.join(rest[::-1]) + ''.join(o)
print s
