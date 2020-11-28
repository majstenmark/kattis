def calcdist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
pos  = {}
for i in range(3):
   nbrs = [int(v) for v in raw_input().split()]
   for j, n  in enumerate(nbrs):
       pos[n] = (i,j) #row, col
dist = 0.0
for i in range(1, 9):
    dist += calcdist(pos[i], pos[i+1])
print(dist)