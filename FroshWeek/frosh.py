def mergeCount(A,B):
    C = []
    i = 0
    j = 0
    cnt = 0
    while i < len(A) and j < len(B):
        C.append(min(A[i],B[j]))
        if B[j] < A[i]:
           cnt += len(A) - i
           j+=1
        else:
           i+=1

    if i < len(A):
         C.extend(A[i::])
    if j < len(B):
        C.extend(B[j::])
    return cnt, C



def sortAndCount(L):
    n = len(L)
    if n <= 100:
        c = 0
        for i in range(n):
            for j in range(i+1, n):
                if L[i] > L[j]: c += 1
        L.sort()
        return c, L
    mid = len(L)/2
    A = L[0:mid]
    B = L[mid::]

    rA,A = sortAndCount(A)
    rB, B = sortAndCount(B)
    r, L = mergeCount(A,B)
    return (rA +rB + r), L

N = input()
data = []
for n in range(N):
    nbr = input()
    data.append(nbr)
cnt, _ = sortAndCount(data)
print cnt
