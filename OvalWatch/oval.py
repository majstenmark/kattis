N, K = map(int, raw_input().split())
legs = []
for k in range(K):
    a, b = map(int, raw_input().split())
    legs.append((b, a, a+1))
legs.sort()
lines = [i for i in range(N)]
for b, left,right in legs:
   # print('{} {}'.format(left, right))
    lines[left], lines[right] = lines[right], lines[left]
  #  print(lines)
out = [0] * N
for i, v in enumerate(lines):
    out[v] = i

print(' '.join(map(str, out)))