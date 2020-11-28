import heapq

ratioStr, Nstr = raw_input().split()
ratio = float(ratioStr)
N = int(Nstr)
W = [-float(v) for v  in raw_input().split()]
veggies = [(w, w, 1) for w in W]
smallest = max(W)
heapq.heapify(veggies)
largest = veggies[0][0]
r = smallest*1.0/largest
totalcuts = 0
while r + 0.00005 < ratio:
    wn, w, cuts = heapq.heappop(veggies)
    wn = w*1.0/(cuts + 1)
    smallest = max(smallest, wn)
    totalcuts += 1
    heapq.heappush(veggies, (wn, w, cuts + 1))
    largest = veggies[0][0]
    r = smallest*1.0/largest
print(totalcuts)
