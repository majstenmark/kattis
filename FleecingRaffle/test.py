import math

def opt(N, P):


    f = P * 1.0/(N+1)
    bestprob = f
    resM = 1
    T_old = N + 1
    for m in range(2, 4 * N):
        T_new = T_old + 1
        f = f * (T_old - P + 1) * 1.0/ T_new
        prob = m * f
        #print 'prob', prob
        if prob < bestprob:

            break
        bestprob = max(bestprob, prob)
        resM =m
        T_old = T_new
    #print bestprob
    print 'opt res M ', resM
    return bestprob

def topf(n, k):
    v = 1
    for nn in range(n, n - k, -1):
        v *= nn
    return v

def fac(k):
    return math.factorial(k)


def subopt(N, P):

    bestprob = 0.0
    rest = topf(N, P-1)/fac(P-1)

    pfac = fac(P)
    f = topf(N, P)* 1.0/pfac
    T_old = N
    resM = 0
    for m in range(1, 4 * N):
        T_new = T_old + 1
        f = f/(T_old - P + 1) * T_new
        prob = m * rest * 1.0/f
        if prob < bestprob:
            break
        bestprob = max(bestprob, prob)
        resM = m
        T_old = T_new
    #print bestprob
    print 'subopt m ', resM
    return bestprob

for n in range(2, 1000000):
    for p in range(2, n+1):
        op = opt(n, p)
        oo = subopt(n, p)
        if abs(op - oo) > 10 ** -6:
            print 'Error at N= {} and P = {} op = {} and oo = {} (diff = {})'.format(n , p, op, oo, abs(op - oo))
            exit(0)
        else:
            print 'Res at N= {} and P = {} both = {}'.format(n , p, op)
