M , A, B, C = map(int, raw_input().split())
li = [A, B, C]
li.sort(reverse = True)
overlapping = max(li[0] + li[1] - M, 0)
if M - overlapping >= li[2]:
    print 'possible'
else:
    print 'impossible'
