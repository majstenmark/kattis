import sys
data = [line.strip() for line in sys.stdin]
#print(data)
cases = [data[i:i+2] for i in range(0, len(data), 2)]
for pattern, text in cases:
    #print('{} {}'.format(pattern, text))
    matches = [str(i) for i in range(len(text)) if text.startswith(pattern, i)]
    print(' '.join(matches))
