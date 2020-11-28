

T = input()
for t in range(T):
    stack = []
    N = input()
    for n in range(N):
        ins = raw_input()
        if ins == 'PUSH':
            stack.append(set(['{}']))
        elif ins == 'DUP':
            stack.append(stack[-1])
        elif ins == 'UNION':
            top = stack.pop()
            next = stack.pop()
            un = top | next
            stack.append(un)
        elif ins == 'INTERSECT':
            top = stack.pop()
            next = stack.pop()
            i = top & next
            stack.append(i)
        elif ins == 'ADD':
            top = list(stack.pop())
            top.sort()
            next = stack[-1]
            tops = '{' + ''.join(top) + '}'
            next.add(tops)
        #print stack
        print (len(stack[-1])-1)
    print '***'
