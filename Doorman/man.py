from collections import deque

X = input()
q = deque(list(raw_input()))

if X  == 0:
    print 0
    exit()
if len(q) <= 2:
    print 2
    exit()

counts = {'M': 0, 'W': 0}


while abs(counts['M'] - counts['W']) <= X and q:
    if abs(counts['M'] - counts['W']) == 0:
    #    print 'let in ', q[0]
        counts[q.popleft()] += 1

    elif counts['M'] < counts['W']:
        if q[0] == 'M':
            #print 'let in ', q[0]
            counts[q.popleft()] += 1
        elif len(q) > 1:
            if q[1] == 'W' and abs(counts['M'] - counts['W']) == X:
                 break
            f = q.popleft()
        #    print 'next person', f, q[0]
            counts[q.popleft()] += 1

            q.appendleft(f)
        else:
            if len(q) == 1 and abs(counts['M'] - counts['W']) < X:
                counts[q.popleft()] += 1

            break


    elif counts['W'] < counts['M']:
        if q[0] == 'W':
        #    print 'let in ', q[0]
            counts[q.popleft()] += 1
        elif len(q) > 1:
            if q[1] == 'M' and abs(counts['M'] - counts['W']) == X:
                 break
            f = q.popleft()
        #    print 'next person', f, q[0]
            counts[q.popleft()] += 1
            q.appendleft(f)

        else:
            if len(q) == 1 and abs(counts['M'] - counts['W']) < X:
                counts[q.popleft()] += 1

            break

print counts['M'] + counts['W']
