def divs(s):
    n = len(s)
    d = [1]
    for i in range(2, n//2+ 1):
        if n % i == 0:
            d.append(i)
    return d

def test(d, root):
    
    n = len(S)
    if d == n: return False
    s = list(root)
    s.sort()
    for i in range(d,n - d+ 1, d):
        sx = list(S[i: i+ d])
        sx.sort()
        if s != sx:
            return False
    return True


S = raw_input()
di = divs(S)
for d in di:
    root = S[0:d]
    if test(d, root):
        print(root)
        exit()
print(-1)