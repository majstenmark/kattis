import math
N =int(raw_input())
for n in range(N):
    A,B = map(int, raw_input().split())
    val = 0
    cnt = 1
    n = 0
    while True:
       # print('n', n)
        v = 2 ** n
        n += 1
        val += v
        if val > A +B:
            break
        top = max(val - B, 0)
        right = max(val - A, 0)
        cnt += val + 1 - top - right
      #  print('cnt {} val  {} v {} top {} right {}'.format(cnt, val, v, top, right))
        
    print(cnt)