def inters(l1, l2):
    a1,b1,c1 = l1
    a2,b2,c2 = l2
    cp = a1*b2 - a2*b1 
    if cp != 0:
        return float(b1*c2 - b2*c1)/cp, float(a2*c1 - a1*c2)/cp
    else:
        return False

def pts2line(p, q):
    return (-q[1] + p[1], 
        q[0] - p[0], 
        p[0]*q[1] - p[1]*q[0])


def on_seg(s, p):
    sx1,sx2 = min(s[0][0], s[1][0]), max(s[0][0], s[1][0])
    sy1,sy2 = min(s[0][1], s[1][1]), max(s[0][1], s[1][1])
    return (sx1 <= p[0] <= sx2 and 
        sy1 <= p[1] <= sy2)    

def intersects(s1, s2):
    L1 = pts2line(s1[0], s1[1])
    L2 = pts2line(s2[0], s2[1])
    X = inters(L1, L2)
    if X == False:
        return False
    
    return on_seg(s1, X) and on_seg(s2, X)

def triangle(s1,s2, s3):
    return (intersects(s1, s2) and intersects(s1, s3)
        and intersects(s2, s3))

def get_triplets(seg):
    N = len(seg)
    triplets =[]
    for i in range(N - 2):
        for j in range(i+1, N-1):
            for k in range(j + 1, N):
                triplets.append((i, j, k))
    return triplets

def solve(seg):
    triplets = get_triplets(seg)
    cnt = 0
    for (i, j, k) in triplets:
        if triangle(seg[i],seg[j], seg[k]):
            
            cnt +=1
    return cnt

N = int(raw_input())
while N != 0:
    segs = []
    for n in range(N):
        x1, y1, x2,y2 = [float(v) for v in raw_input().split()]
        segs.append(((x1, y1), (x2,y2)))
    res = solve(segs)
    print(res)
    N = int(raw_input())
    