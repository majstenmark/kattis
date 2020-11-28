import math

def intersects(rf, sf, rs, ss):
    return (rf - rs)* 1.0/(sf - ss)

def dist(x1,y1, x2, y2):
    return math.sqrt((x1 - x2) **2 + (y1 - y2) ** 2)

xs, ys, ss, ri, rf = map(int, raw_input().split())
xa, ya, sa = map(int, raw_input().split())
d = dist(xa, ya, xs, ys)
# Inside ri but faster
# Inside rf
if (d <= ri and sa >= ss) or d <= rf:
    print '0'
    exit()

timeToSafe = (d - rf)*1.0/sa
#print 'tts',timeToSafe
# Outside and faster
if d > ri and sa > ss:
    ti = intersects(d, sa, ri, ss)
    unsafetime = min(timeToSafe, ti)
    print unsafetime
    exit()

# Outside and slower
if d > ri and sa <= ss:
    print timeToSafe
    exit()
if d <= ri and sa < ss:
    ti = intersects(ri, ss, d, sa)
    unsafetime =  max(0, timeToSafe - ti)
    print unsafetime
    exit()
print timeToSafe

# Inside slower
