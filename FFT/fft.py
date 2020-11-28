import cmath
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

a = [1, 0, 0, 1, 0, 0, 0, 0]
b= [1, 0, 0, 1,  0, 0, 0, 0]
fftA = FFT(a)
fftB = FFT(b)
fftC = []
N = 8
for n in range(N):
    fftC.append(fftA[n] * fftB[n])
print 'fftc', fftC
coeffs = FFT(fftC, True)
pretty = []
for c in coeffs:
    pretty.append(int(c.real))
    if abs(c.imag) > 0.00001:
        print "IMG"
print 'coeffs', pretty
