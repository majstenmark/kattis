ZERO = '''xxxxx
x...x
x...x
x...x
x...x
x...x
xxxxx
'''
ONE = '''....x
....x
....x
....x
....x
....x
....x
'''
TWO = '''xxxxx
....x
....x
xxxxx
x....
x....
xxxxx
'''
THREE = '''xxxxx
....x
....x
xxxxx
....x
....x
xxxxx
'''
FOUR = '''x...x
x...x
x...x
xxxxx
....x
....x
....x
'''
FIVE = '''xxxxx
x....
x....
xxxxx
....x
....x
xxxxx
'''
SIX = '''xxxxx
x....
x....
xxxxx
x...x
x...x
xxxxx
'''
SEVEN = '''xxxxx
....x
....x
....x
....x
....x
....x
'''
EIGTH = '''xxxxx
x...x
x...x
xxxxx
x...x
x...x
xxxxx
'''
NINE = '''xxxxx
x...x
x...x
xxxxx
....x
....x
xxxxx
'''
ADD= '''.....
..x..
..x..
xxxxx
..x..
..x..
.....
'''

chars = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGTH, NINE]
ch2int = {}
for i, ch in enumerate(chars):
    arr = ''.join(ch)
    ch2int[arr] = i
ADD_ARR = ''.join(ADD)

def read_digits(grid):
    a, curr= 0, 0
    aset= False
    for start in range(0, len(grid[0]), 6):
        out = []
        for j in range(7):
            for i in range(start, start + 5):
                out.append(grid[j][i])
            out.append('\n')
        arr = ''.join(out)

        if arr != ADD_ARR:
            curr *= 10
            curr += ch2int[arr]
        else:
            if not aset:
                a= curr
                curr = 0
            else:
                b= curr
    return a + curr

def print_digits(res):
    out = [[] for _ in range(7)]
    s = str(res)
    for pos, ch in enumerate(s):
        i = int(ch)
        ascii = chars[i]
        for row in range(7):
            start= row * 6
            out[row].append(ascii[start: start+5])
            if pos< len(s) -1:
                out[row].append('.')
    for row in range(7):
        print(''.join(out[row]))
    


grid =[raw_input() for _ in range(7)]
res = read_digits(grid)
print_digits(res)


