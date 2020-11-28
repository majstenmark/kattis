B, N, E = map(int, raw_input().split())
Sb, Sn, Se = map(int, raw_input().split())
cs = [int(v) for v in raw_input().split()]
cs.sort()
tests = [(2*Sb, (2, 0, 0)), (Sb + Sn, (1, 1, 0)), (2 *Sn, (0, 2, 0)),  (Sn + Se, (0, 1, 1)), (Sb + Se, (1, 0, 1)),  (2 *Se, (0, 0, 2))]
tests.sort()

def checkCount(cB,cN, cE):
    return cB <= B and cN <= N and cE <= E

def check(speed):
    count = (0, 0, 0)
    for kayak in cs:
        failed = True
        for strength, (a, b, c) in tests:
            newcount = a+count[0],b + count[1],c+count[2]
            if strength * kayak >= speed and checkCount(*newcount):

                count = newcount
                failed = False
                break
        if failed:
            return False
        if not failed and a == 2:
            return True
    return True

maxSpeed = cs[0] * 2 * Se + 1
minSpeed = cs[0] * 2 * Sb

while minSpeed < maxSpeed - 1: # OBS halvering!

    mid = (maxSpeed + minSpeed)/2
    if check(mid):
        minSpeed = mid
    else:

        maxSpeed = mid
print(minSpeed)
