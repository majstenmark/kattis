def getMinOld(n):
    if n == 2:
        return '1'
    if n == 3:
        return '7'
    if n == 4:
        return '4'
    if n == 5:
        return '2'
    if n == 6:
        return '6'
    if n == 7:
        return '8'
    if n == 8:
        return '10'
    return getMin(n-7) + '8'

def getMin(n):
    digits = []
    while n > 11:
        digits.append('8')
        n -= 7
    if n == 11:
        digits.extend(['2', '6'])
    if n == 10:
        digits.extend(['2', '2'])
    if n == 9:
        digits.extend(['1', '8'])
    if n == 8:
        digits.extend(['1', '6'])

    if n == 7:
        digits.append('8')
    if n == 6:
        digits.append('6')
    if n == 5:
        digits.append('2')
    if n == 4:
        digits.append('4')
    if n == 3:
        digits.append('7')
    if n == 2:
        digits.append('1')
    digits.sort()
    res= [digits[0]]
    for digit in digits[1:]:
        if digit == '6':
            res.append('0')
        else:
            res.append(digit)
    s =  ''.join(res)
    s = s.replace('228', '200')
    return s

def getMax(n):
    if n % 2 != 0:
        return '7' + '1' * ((n-3)/2)
    else:
        return '1' * (n/2)

#T = 101
T = int(raw_input())
for t in range(T):
    N = int(raw_input())
    #print '{}: {} {}'.format(t, getMin(t), getMax(t))
    print '{} {}'.format(getMin(N), getMax(N))
