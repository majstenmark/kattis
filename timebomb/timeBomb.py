zero ='*** * * * * * * *** '
one = '  *   *   *   *   * '
two ='***   * *** *   *** '
three = '***   * ***   * *** '
four = '* * * * ***   *   * '
five = '*** *   ***   * *** '
six = '*** *   *** * * *** '
seven = '***   *   *   *   * '
eight = '*** * * *** * * *** '
nine = '*** * * ***   * *** '
digits = [zero, one, two, three, four, five, six, seven, eight, nine]
table = {}
for v, s in enumerate(digits):
    table[s] = v

def getchars(start, asc):
    s = []
    for y in range(5):
        s.append(asc[y][start: start + 4])

    va = ''.join(s)
    return va


ascii = [raw_input() + ' ' for _ in range(5)]
digit  = []
boom = False
for x in range(0, len(ascii[0]), 4):
    letter = getchars(x, ascii)
    if letter in table:
        digit.append(str(table[letter]))
    else:
        boom = True
        break
if not boom:
    value = int(''.join(digit))
    if value % 6 == 0:
        print 'BEER!!'
        exit()
print 'BOOM!!'
