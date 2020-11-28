inp = input
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

H, W, N, M = nl()
img = [nl() for _ in range(H)]
kernel = [nl()[::-1]  for _ in range(N)][::-1]
out = []
for r in range(H - N + 1):
    row = []
        
    for c in range(W - M + 1):
        el = 0
        for kr in range(len(kernel)):
            for kc in range(len(kernel[0])):
                el += img[r + kr][c + kc] * kernel[kr][kc]
        row.append(str(el))
    out.append(' '.join(row))
print('\n'.join(out))
    
