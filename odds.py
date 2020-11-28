inp = input
import sys

itr = (line for line in sys.stdin.read().split('\n'))
def read():
    return [int(v) for v in next(itr).replace('*', '-1').split()]


def gcd(a, b):return gcd(b, a % b) if b else a

def score(d1, d2):
    d1, d2 = max(d1, d2), min(d1, d2)
    if d1 == 2 and d2 == 1:
        return 1000
    return 100 * int(d1 == d2) + d1 * 10 + d2

def wins(p1, p2):
    score1 = score(p1[0], p1[1])
    score2 = score(p2[0], p2[1])
    return score1 > score2

def gen(s1, s2):
    if s1 != -1 and s2 != -1:
        return [(s1, s2)]
    if s1 == -1 and s2 == -1:
        return [(a, b) for a in range(1, 7) for b in range(1, 7)]
    x = max(s1, s2)
    return [(x, i) for i in range(1, 7)]

DP = {}
def test(s1, s2, r1, r2):
    if max(s1, s2, r1, r2) == -1:
        return '205/432'
    T = (s1, s2, r1, r2)
    if T in DP:
        return DP[T]
    li1 = gen(s1, s2)
    li2 = gen(r1, r2)

    w = 0
    tot = 0
    for p1 in li1:
        for p2 in li2:
            tot += 1
            w += int(wins(p1, p2))
    if w == 0:
        return '0'
    if w == tot:
        return '1'
    g = gcd(w, tot)
    w = w//g
    tot = tot//g
    DP[T] = '{}/{}'.format(w, tot)
    return DP[T]


s1, s2, r1, r2 = read()
while s1 != 0:
    
    print(test(s1, s2, r1, r2))
    s1, s2, r1, r2 = read()
