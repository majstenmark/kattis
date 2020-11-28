cans = [int(v) for v in raw_input().split()][1:]
n = len(cans)

while n > 0:
    total=sum(cans)
    cals = [[False]*(total+1) for _ in range(n)]
    cals[0][0]=True
    cals[0][cans[0]]=True
    for i in range(1,n):
        cal = cans[i]
        for k in range(len(cals[i-1])):
            if cals[i-1][k]:
                cals[i][k]=True
                cals[i][k+cal]=True

    half=total/2
    bestDiff=half
    lunch=0
    for (index, val) in enumerate(cals[-1]):
        if val and abs(index-half) < bestDiff:
            bestDiff=abs(index-half)
            lunch=index
    dinner=total - lunch
    lunch, dinner = max(lunch,dinner), min(lunch, dinner)
    s='{} {}'.format(lunch,dinner)
    print(s)
    cans = [int(v) for v in raw_input().split()][1:]
    n = len(cans)
