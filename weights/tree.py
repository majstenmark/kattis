N = int(raw_input())
ws = {}


def add(row, rowNbr):
    for n in range(N):
        w = row[n]
        if w not in ws:
            ws[w] = [rowNbr, n]
        else:
            ws[w].extend([rowNbr, n])
def findMax(a, b, row):
    if a <= b:
        return max(row[a:b+1])
    return 0
# frist row
row1 = [int(v) for v in raw_input().split()]
add(row1, 0)

# second row
row2 = [int(v) for v in raw_input().split()]
add(row2, 1)
rows = [row1, row2]
uniqueWs = sorted(ws.keys(), reverse = True)

maxW = 0
#print(ws)
for w in uniqueWs:
    r1, i1, r2, i2 = ws[w]
    if r1 != r2:
        maxW = max(maxW, w)
        break
    elif maxW >= w:
        break
    else:
        left = min(i1, i2)
        right = max(i1, i2)
        tmpMax = findMax(left+1, right - 1, rows[r1])
        #print('w = {}, index {} and {}, tmpMax {} '.format(w, i1, i2, tmpMax))
        tmpMax = min(tmpMax, w)
        maxW = max(tmpMax, maxW)

print(maxW)
