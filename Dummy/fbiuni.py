incorr = {'B': '8', 'G': 'C', 'I': '1', 'O':'0', 'Q':'0', 'S':'5', 'U':'V','Y': 'V', 'Z':'2'}
nbrs = '0123456789ACDEFHJKLMNPRTVWX'
vals = {}
for val, n in enumerate(nbrs):
    vals[n] = val
hash = [2, 4, 5, 7, 8, 10, 11, 13]
T = int(raw_input())
for t in range(T):
    testcase, uni = raw_input().split()
    check_sum = 0
    totval = 0
    for index, ch in enumerate(uni[0:-1]):
        if ch in incorr:
            ch = incorr[ch]
        check_sum += hash[index] * vals[ch]
        totval *= 27
        totval += vals[ch]
        check_sum %= 27
    lastval= uni[-1]
    if lastval in incorr:
        lastval = incorr[lastval]
    if check_sum == vals[lastval]:

        print('{} {}'.format(testcase, totval))
    else:
        print('{} {}'.format(testcase, 'Invalid'))