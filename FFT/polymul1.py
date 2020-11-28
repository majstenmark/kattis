import cmath
import math
# A has to be of length a power of 2.
def FFT(A, inverse=False):
    N = len(A)
    if N <= 1:
        return A
    if inverse:
        D = FFT(A) # d_0/N, d_{N-1}/N, d_{N-2}/N, ...
        return map(lambda x: x/N, [D[0]] + D[:0:-1])
    evn = FFT(A[0::2])
    odd = FFT(A[1::2])
    Nh = N//2
    return [evn[k%Nh]+cmath.exp(2j*cmath.pi*k/N)*odd[k%Nh]
            for k in range(N)]

T = input()
for t in range(T):
    Na = input()
    acoeffs = map(int, raw_input().split())
    Nb = input()
    bcoeffs = map(int, raw_input().split())


    helper = []
    N = Nb + Na + 1
    Nk = N
    buff = int(math.log(N, 2))
    if 2 ** buff < N:
        Nk = 2 ** (buff + 1)


    #print 'Nk', Nk

    bcoeffs = bcoeffs + [0] * (Nk - Nb -1)
    acoeffs = acoeffs + [0] * (Nk - Na -1)
    #print 'buffer'
    #print len(acoeffs)
#    print len(bcoeffs)
    fftA = FFT(acoeffs)
    fftB = FFT(bcoeffs)
    fftC = []
    for n in range(Nk):
        fftC.append(fftA[n] * fftB[n])
    coeffs = FFT(fftC, True)
    pretty = []
    last = 0
    for n in range(Nk):
#        print 'coeff', coeffs[n]
        v = int(round(coeffs[n].real, 0))
        pretty.append(v)
        if v != 0:
            last = n
    o = []
#    print 'pretty', pretty
    for n in range(last +1):
        o.append(str(pretty[n]))
    s = ' '.join(o)
    print len(o) -1
    print s
