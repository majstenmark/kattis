
DEBUG = True
def debug(*s):
    p = ' '.join(map(str, s))
    if DEBUG:
        print(p)
DEBUG = True

debug('a')
b = 2
debug('b', b)
li =[1, 3, 4, 5, 6]
debug('my list', li)
