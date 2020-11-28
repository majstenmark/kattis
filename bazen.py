def area(b,h):
    return b * h //2

def btn_area(btn, top_point):
    b = side[0] - btn[0]
    h = top_point[1] - btn[1]
    return area(b, h)

def on_triangle(x1, y1):
    return 0 <= x1 <= 250 and 0 <= y1 <= 250

def result(ax, ay):
    print('{:.2f} {:.2f}'.format(ax, ay))
    exit()

def point_from_base(x,y):
    br = 250.0 - x
    if br > 0.0:
        ans_y = AREA /br
        ans_x = 250 -ans_y #lineeq y = 250-x
    # print(ans_x, ans_y)
        if on_triangle(ans_x, ans_y):
            return ans_x, ans_y
    bl = x
    if bl > 0.0:
        ans_y= AREA /bl
        ans_x = 0
    #  print(ans_x, ans_y)
        
        if on_triangle(ans_x, ans_y):
            return ans_x, ans_y
    return -1, -1


def point_from_height(x,y):
    ans_y = 0
    h = y
    if h >0.0:
        bx = AREA /h
        ans_x = 250 - bx
        
        if on_triangle(ans_x, ans_y):
        
            return ans_x, ans_y
    h = x
    if h > 0.0:
        by = AREA/h
        ans_y = 250 -by
        ans_x = 0

        if on_triangle(ans_x, ans_y):
            return ans_x, ans_y
    return -1, -1

x, y = [int(v) for v in raw_input().split()]
AREA = 250.0 * 250.0 /2

if y == 0:
    ansx, ansy = point_from_base(x, y)
    result(ansx, ansy)
if x == 0:
    ansy, ansx = point_from_base(y, x)
    result(ansx, ansy)
ansx, ansy = point_from_height(x, y)
result(ansx, ansy)    

        
   
    

    