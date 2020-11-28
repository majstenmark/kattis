def isOk(ws, L, maxL, N):
    nextIndex = 0
    trains = 1
    newWagon = maxL
    if ws[0] >= maxL:
        trains += 1
        newWagon = ws[0] + maxL
    
    while nextIndex < len(ws) and newWagon <= ws[-1] :
        while ws[nextIndex] < newWagon:
            nextIndex += 1
        
        #should I clean away empty wagons?
        #next train is [newwagon, newwagon + maxL -1]
        if ws[nextIndex] > newWagon + maxL:
            trains += 1 #add an extra train!
            newWagon = ws[nextIndex]
        trains += 1 
        newWagon += maxL # new break point! 
    if newWagon < N:
        trains += 1
    return trains <= L



def solve(ws, L, N):
    hi = N//L + int(N % L > 0) #ok
    lo = 0 #not ok
    while hi > lo + 1:
        mid = (hi + lo)//2
        if isOk(ws, L, mid, N):
            hi = mid
        else:
            lo = mid
    return hi

T = int(raw_input())
for t in range(T):
    N, W, L = [int(v) for v in raw_input().split()]
    ws = [int(v) -1 for v in raw_input().split()]
    res = solve(ws, L, N)
    print(res)