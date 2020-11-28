def inside_rect(x, y, rect):
    x1, x2, y1, y2 = rect
    return x1 <= x<= x2 and y1 <= y<= y2

def inside_circ(x, y, mid, r):
    xc, yc = mid
    return (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2

def check(x, y, w, h, r, msx, msy, corner_cuts, circles):
    for i in range(4):
        corner = corner_cuts[i]
        circle = circles[i]
        if inside_rect(msx, msy, corner) and not inside_circ(msx, msy, circle, r):
            return False
    return inside_rect(msx, msy, (x, x + w, y, y+h))



N = int(raw_input())
for n in range(N):
    data = [float(v) for v in raw_input().split()]
    x, y, w, h, r = data[0], data[1], data[2], data[3], data[4]
    
    ms = [] 
    for click in range(6, len(data), 2):
        ms.append((data[click], data[click+1]))
    corner_cuts = [(x, x+r, y, y+r), (x +w -r, x + w, y, y+r), (x, x+r, y+h-r, y +h), (x+ w-r, x+ w,y+ h-r, y+h)]
    circles= [(x + r,y + r), (x+w - r, y +r), (x + r,y+ h -r), (x + w-r, y + h - r)]
    for msx, msy in ms:
        res = check(x, y, w, h, r, msx, msy, corner_cuts, circles)
        out= 'inside' if res else 'outside'
        print(out)
    print('')
