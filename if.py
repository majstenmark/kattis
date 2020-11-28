import math
def small(N):
    n=10
    val=1
    for a in range(1, n):
        val*=a
        if val==N:
            print(a)
            break

#40320 = 9!
fact = raw_input()
if len(fact) <= 6:
    small(int(fact))

else:
    L=0
    n=1
    length=len(fact) - 1
    while L + 0.1 < length:
        n+=1
        L+=math.log(n,10)
        #print(L)
    print(n)
