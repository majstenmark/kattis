from random import randint

import naive
import crypto

for t in range(10000):
   
    N = 10

    b = [randint(0 if i!=0 else 1, 9) for i in range(N)]
    B = ''.join(map(str, b))
    c1 = naive.solve(N, B)
    c2 = crypto.solve(N, B)
    print(B)
    assert c1 == c2, "{} {} {}".format(c1,c2, B)