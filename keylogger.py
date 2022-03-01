import sys

itr = (line for line in sys.stdin.read().split('\n'))


sounds2keys = {'clank': 'a', 'bong': 'b', 'click': 'c', 'tap': 'd', 'poing': 'e', 'clonk': 'f', 'clack': 'g', 'ping': 'h', 'tip': 'i', 'cloing': 'j', 'tic': 'k', 'cling': 'l', 'bing': 'm', 'pong': 'n', 'clang': 'o', 'pang': 'p', 'clong': 'q', 'tac': 'r', 'boing': 's', 'boink': 't', 'cloink': 'u', 'rattle': 'v', 'clock': 'w', 'toc': 'x', 'clink': 'y', 'tuc': 'z', 'whack':' '}
shdown = 'dink'
shtup = 'thumb'
delete = 'pop'
caps = 'bump'


N = int(next(itr))
sounds = [next(itr) for _ in range(N)]
text = []
shift = False
caps = False

for s in sounds:
    if s == delete:
        if len(text) > 0:
            text.pop()
    if s == shdown or s == shdown:
        shift = not shift
    if s == caps:
        caps = not caps

    if s in sounds2keys.keys():
        if shift ^ caps:
            text.append(sounds2keys[s].upper())
        else:
            text.append(sounds2keys[s])

print(''.join(text))