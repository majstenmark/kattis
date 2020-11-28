def convexhull(points):
    points = sorted(set(points))
    if len(points) <= 1:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def lineeq(p, q):
    return (-q[1] + p[1],
        q[0] - p[0],
        p[0]*q[1] - p[1]*q[0])

def lineintersect(L1, L2):
    a1,b1,c1 = L1
    a2,b2,c2 = L2
    cp = a1*b2 - a2*b1 
    if cp != 0:
        return float(b1*c2 - b2*c1)/cp, float(a2*c1 - a1*c2)/cp
    else:
        return False


def online(P, S):
    x1, y1 = S[0]
    x2, y2= S[1]
    xmin, xmax = min(x1, x2),max(x1, x2)
    ymin, ymax = min(y1, y2),max(y1, y2)
    return xmin <= P[0] <= xmax and ymin <= P[1] <= ymax

def intersect(S1, S2):
    L1 = lineeq(S1[0], S1[1])
    L2 = lineeq(S2[0], S2[1])
    P = lineintersect(L1, L2)
    if P:
        if online(P, S1) and online(P, S2):
            return P
    return False 

def dist2(P1, P2):
    return (P1[0] - P2[0])**2 + (P1[1] - P2[1]) **2 

P, A= [int(v) for v in raw_input().split()]
if min(P,A) < 3:
    print(0)
    exit()
pines = [tuple(map(float, raw_input().split())) for _ in range(P)]
alms = [tuple(map(float, raw_input().split())) for _ in range(A)]
hullP =convexhull(pines)
hullA =convexhull(alms)
iP = [[] for _ in range(len(hullP))]
iA = [[] for _ in range(len(hullA))]

intersectP = {}
intersectA = {}

hA =[]
hB =[]

for i in range(len(hullP)):
    S1 = hullP[i], hullP[(i+ 1)%len(hullP)]
    for j in range(len(hullA)):
        S2 = hullA[j], hullA[(j+ 1)%len(hullA)]
        P = intersect(S1, S2)
        if P:
            iP[i].append(P)
            iA[j].append(P)

def sortbydist(intersectionlist, hull):
    for i in range(len(hull)):
        intersectionlist[i].sort(key = lambda x: dist2(x, hull[i]))

def extendHull(intersectionlist, hull):
    newHull = []
    intersections = set()
    for i in range(len(hull)):
        newHull.append(hull[i])
        for p in intersectionlist[i]:
            intersections.add(len(newHull))
            newHull.append(p)
    return newHull, intersections

def mapids(ip1, ip2):
    ids1 = {}
    ids2 = {}
    starti = -1
    for i in ip1:
        for j in ip2:
            if dist2(hullP[i], hullA[j]) < 0.0000001:
                #same
                ids1[i] = j
                ids2[j] = i
                if starti == -1:
                    starti = i
    return ids1, ids2, starti

sortbydist(iP, hullP)
sortbydist(iA, hullA)
hullP, intersectP = extendHull(iP, hullP)
hullA, intersectA = extendHull(iA, hullA)
ids_from_i_to_j, ids_from_j_to_i, starti = mapids(intersectP, intersectA)


#calc two areas
#one starting with P inner, and the other with A inner
def calcPoly(p_inner):
    startj = ids_from_i_to_j[starti]
    fst = hullA[startj] if p_inner else hullP[starti]
    poly = [fst, hullP[starti]]
    curri = (starti +1) % len(hullP)
    currj = (startj + 1) % len(hullA)
    while currj != startj and curri != starti:
        if p_inner:        
            poly.append(hullP[curri])
            if curri in intersectP:
                currj = ids_from_i_to_j[curri]
                currj += 1
                currj %= len(hullA)
                p_inner = not p_inner

            else:
                curri +=1
                curri %= len(hullP)
        else:
            poly.append(hullA[currj])
            if currj in intersectA:
                curri= ids_from_j_to_i[currj]
                curri += 1
                curri %= len(hullP)
                
                p_inner = not p_inner
            else:
                currj +=1
                currj %= len(hullA)
        
    return poly

def is_inside(P, hull):
    far_away = 10000.0, 100000.0
    cnt = 0
    S_far = P, far_away
    for i in range(len(hull)):
        S =hull[i], hull[(i + 1)%len(hull)]
        if intersect(S_far, S):
            cnt += 1
    return cnt % 2 == 1
        
def area(poly):
    A = 0.0
    for i in range(len(poly)):
        pi = poly[i]
        pj = poly[(i + 1)%len(poly)]
        A += pi[0] * pj[1] - pj[0]* pi[1]
    return 0.5 * abs(A)


if starti == -1:
    #no intersections
    #they can be inside each other
    if is_inside(hullP[0], hullA) or is_inside(hullA[0], hullP):

        a1 = area(hullP)
        a2 = area(hullA)
        
        print(min(a1, a2))
    else:
        print(0)
    exit()

p_inner = True
poly1 = calcPoly(True)
poly2 = calcPoly(False)

a1 = area(poly1)
a2 = area(poly2)
print(min(a1, a2))

