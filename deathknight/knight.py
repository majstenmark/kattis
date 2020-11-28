def fight(ki):
    pairs = zip(ki[0:],ki[1:])
    for p in pairs:
        if p == ('C', 'D'):
            return False
    return True

N = input()
wins = 0
for n in range(N):
    ki = raw_input()
    if fight(ki):
        wins += 1
print wins
