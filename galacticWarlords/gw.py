W,N=map(int,raw_input().split())
def sameLine(p1,p2,pp1,pp2):
    line1=[p2[0]-p1[0],p2[1]-p1[1]]
    line2=[pp2[0]-pp1[0],pp2[1]-pp1[1]]
    line3=[pp2[0]-p1[0],pp2[1]-p1[1]]
    return inPar(line1,line2) and inPar(line1,line3)

def inPar(line1,line2):
    return line1[0]*line2[1] == line1[1]*line2[0]

if N>0:
    uniqueLines=[]
    ox1,oy1,ox2,oy2=map(int,raw_input().split())
    uniqueLines.append(([ox1,oy1], [ox2,oy2]))
    testPar = True
    for line in range(N-1):
        x1,y1,x2,y2=map(int,raw_input().split())
        if not inPar([x2-x1,y2-y1],[ox2-ox1,oy2-oy1]):
            testPar=False
        newLine=True
        for (p1,p2) in uniqueLines:
            if sameLine(p1,p2,[x1,y1],[x2,y2]):
                newLine=False
                break
        if newLine:
            uniqueLines.append(([x1,y1],[x2,y2]))
    if(testPar):

        infSpace= len(uniqueLines)+1
        if infSpace < W:
            needed = 1
            infSpace = 2*infSpace
            needed += max(0,(W - infSpace +1)/2)
            print(needed)
        else:
            print(0)
    else:
        infSpace=2*len(uniqueLines)
        needed = max(0,(W - infSpace +1)/2)
        print(needed)
else:
    print(0)
