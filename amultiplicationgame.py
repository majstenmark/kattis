import sys

lines = sys.stdin.readlines()
for line in lines:
    T = int(line)

    saved = {}
    def winnable(n, limit):
        if n in saved:
            return saved[n]
        if n >= limit:
            return False
        for i in range(2, 10):
            if not winnable(n * i, limit):
                saved[n] = True
                return True
        saved[n] = False
        return False
    
    if winnable(1, T):
        print('Stan wins.')
    else:
        print('Ollie wins.')

