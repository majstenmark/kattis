from math import cos, sin, pi, acos, asin, sqrt

def law_of_cos_SSS(s1, s2, opposite_s):
    q = (s1 **2 + s2 **2 - opposite_s**2)/(2.0 * s1 * s2)
    
    return acos(q)

def law_of_cos_SAS(s1, a, s2):
    q =  s1 **2 + s2**2 - 2.0 * s1 * s2 * cos(a)
    return sqrt(q)

def gamma(x, c2, beta):
    q = c2 * sin(beta)/x
  
    return asin(q) 

N = int(raw_input())
L = 0.0
for n in range(N):
    A, B, C = [int(v) for v in raw_input().split()]
    c = law_of_cos_SSS(A, B, C)
    b = law_of_cos_SSS(A, C, B)
    a = law_of_cos_SSS(B, C, A)
    #print(a, b, c)
    if a < b:
        a, b = b, a
        A, B = B, A
    
    x = law_of_cos_SAS(A, b, C/2.0)
    #print('x', x)
    gamma1 = gamma(x, C/2.0, b)
    #print('gamma1', gamma1)
    delta = pi/2 - gamma1 -b
    #print('delta', delta)
    X = C * cos(delta)
    L += X
print(L)
