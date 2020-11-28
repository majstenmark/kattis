R, C, Zr, Zc = [int(v) for v in raw_input().split()]
out = []
for r in range(R):
    row = raw_input()
    out_row = []
    for ch in row:
        out_row.extend([ch]* Zc)
    s = ''.join(out_row)
    out.extend([s] * Zr)
res = '\n'.join(out)
print(res)
