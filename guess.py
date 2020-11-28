lo= 1
hi = 1000
ans = 'blah'
while ans != co:
    mid = (lo + hi) /2
    print(mid)
    ans = raw_input()
    if ans == 'lower':
        hi = mid -1
    if ans == 'higher':
        lo = mid + 1
    if ans =='correct':
        break

