from math import pi, e

def F(r):
    return - e ** (- r**2/ (2 * sigma**2))


def prob(iR, oR):
    return (F(oR) - F(iR))/20


eye, bull, in3,out3,in2, out2 = map(float, raw_input().split())
sigma = float(raw_input())
totScore = 0
dblScore = 0
tripScore = 0


score = 0
for pie in range(1, 21):
    totScore = pie
    dblScore = 2 * pie
    tripScore = 3 * pie

    score += prob(0, eye) * 50
    score += prob(eye, bull) * 25
    score += prob(bull, in3) * totScore
    score += prob(in3, out3) * tripScore
    score += prob(out3,in2) * totScore
    score += prob(in2, out2) * dblScore
print score
