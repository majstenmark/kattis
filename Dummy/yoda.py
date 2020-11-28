N =raw_input()[::-1]
M = raw_input()[::-1]
smallest = min(len(M), len(N))
biggest = max(len(M), len(N))
mcoll = []
ncoll = []
for i in range(smallest):
    mm= int(M[i])
    nn = int(N[i])
    if nn > mm:
        ncoll.append(nn)
    if mm > nn:
        mcoll.append(mm)
    if mm == nn:
        ncoll.append(nn)
        mcoll.append(mm)

large, L = (mcoll, M) if len(M) > len(N) else (ncoll, N)
#print(large)
for i in range(smallest, biggest):
  #  print(i)
    large.append(int(L[i]))
mr =mcoll[::-1]
nr =ncoll[::-1]
nval =0
mval = 0
for i in nr:
    nval *= 10
    nval += i

for i in mr:
    mval *= 10
    mval += i
if len(ncoll) > 0:
    print(nval)
else:
    print('YODA')
if len(mcoll) >0:

    print(mval)
else:
    print('YODA')