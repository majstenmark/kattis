def lagom(a, b, c):
    return c **2 == a**2 + b**2 - a*b

N = int(raw_input())

used = set()
for a in range(1, N +1):
    for b in range(1, N +1):
        for c in range(1, N+1):
            
            if lagom(a, b, c) :
                #print('{} {} {}'.format(a, b,c))
                s1, s2, s3 = sorted((a, b, c))
                tri = (s1, s2, s3)
                used.add(tri)
                
print(len(used))

    