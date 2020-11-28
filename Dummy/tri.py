def test(a, b, c):
    if a + b == c:
        return True, str(a) + '+'+str(b)

    if a - b == c:
        return True, str(a) + '-'+str(b)

    if a / b == c:
        return True, str(a) + '/'+str(b)

    if a * b == c:
        return True, str(a) + '*'+str(b)
    return False, ''

a, b, c = map(int, raw_input().split())
#eq last
last, s = test(a,b, c)
if last:
    print(s+'='+str(c))
else:

    #eq first
    _, s = test(b, c, a)
    print(str(a) + '=' +s)
