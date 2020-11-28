try: inp = raw_input
except: inp = input

def nl():
    return [int(v) for v in inp().split()]


def solve2(S):
    S.sort()
    for i in range(len(S) - 1):
        L1 = len(S[i])
        if S[i] == S[i+1][:L1]:
            return 'NO'
    
    return 'YES'


import sys

data = sys.stdin.read().split('\n')
CURR_IDX = -1
def inp():
    global CURR_IDX
    CURR_IDX += 1
    return data[CURR_IDX]
T = int(inp())

for t in range(T):
    N = int(inp())
    S = [inp() for _ in range(N)]

    print(solve2(S))