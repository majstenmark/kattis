import sys
from heapq import heappush, heappop

def store(d):
    med = 0 if len(big) == 0 else big[0]
    if d > med:
        heappush(big, d)
    else:
        heappush(small, -d)
    if len(big) > len(small) + 1:
        heappush(small, - heappop(big))
    if len(small) == len(big) + 1:
        heappush(big, - heappop(small))


def send():
    med = heappop(big)
    if len(big) > len(small) + 1:
        heappush(small, - heappop(big))
    if len(small) == len(big) + 1:
        heappush(big, - heappop(small))
    return med


big = []
small = []


for req in sys.stdin.readlines():
    if req.strip() == '#':
        print send()
    else:
        d = int(req)
        store(d)
