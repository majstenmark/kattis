import sys
import math
import collections
itr = (line for line in sys.stdin.read().split('\n'))
def inp(): return next(itr)
def nl(): return [int(v) for v in inp().split()]
def ni(): return int(inp())

N = ni()
B = nl()
P = sum(B)

def log10(x): return math.log(x, 10)

logfac = [0.0] * (365 * P + 1)
L = 0.0
for i in range(2, 365 * P + 1):
    L += log10(i)
    logfac[i] = L
    
def logchoose(n, k):
    return logfac[n] - logfac[n-k] - logfac[k]

su = 0.0
ppl_left = P
log365 = log10(365)
B.sort(reverse = True)

for bday_no, b in enumerate(B):
    logways = 0
    if b > 1:
        logways = logchoose(ppl_left, b)
    su += logways + log10(365-bday_no) - b * log365
    ppl_left -= b
print(su) 
