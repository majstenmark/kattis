N = int(raw_input())
seen = set()
last = raw_input()
seen.add(last)
lost = 0
for n in range(1, N):
    next = raw_input()
    if last[-1] != next[0] or next in seen:
        lost = (n%2+1)
        break
    last = next
    seen.add(next)

if lost == 0:
    print 'Fair Game'
else:
    print 'Player {} lost'.format(lost)
