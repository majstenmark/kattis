import sys
lines = sys.stdin.readlines()
out = []

def isdigit(s):
    try:
        i = int(s)
        return True
    except:
        return False

def tens(s):
    if s == '2': return 'twenty'
    if s == '3': return 'thirty'
    if s == '4': return 'forty'
    if s == '5': return 'fifty'
    if s == '6': return 'sixty'
    if s == '7': return 'seventy'
    if s == '8': return 'eighty'
    return 'ninety'

def ones(s):
    if s == '0': return 'zero'
    if s == '1': return 'one'
    if s == '2': return 'two'
    if s == '3': return 'three'
    if s == '4': return 'four'
    if s == '5': return 'five'
    if s == '6': return 'six'
    if s == '7': return 'seven'
    if s == '8': return 'eight'
    if s == '9': return 'nine'
    if s == '10': return 'ten'
    if s == '11': return 'eleven'
    if s == '12': return 'twelve'
    if s == '13': return 'thirteen'
    if s == '14': return 'fourteen'
    if s == '15': return 'fifteen'
    if s == '16': return 'sixteen'
    if s == '17': return 'seventeen'
    if s == '18': return 'eighteen'
    if s == '19': return 'nineteen'
    return '0'
    

def toword(s):
    i = int(s)
    if i < 20:
        return ones(s)
    if i % 10 == 0:
        return tens(s[0])
    return tens(s[0]) + '-' + ones(s[1])
    

for rawline in lines:
    line = rawline.split()
    newline = []
    if isdigit(line[0]):
        word = toword(line[0])
        newline.append(word.capitalize())
    else:
        newline.append(line[0])
    for word in line[1:]:
        if isdigit(word):
            newline.append(toword(word))
        else:
            newline.append(word)
    out.append(' '.join(newline))
print('\n'.join(out))