S = raw_input()
white = 0
lower = 0
upper = 0
symbols = 0
for ch in S:
    if ch == '_':
        white += 1
        continue
    if ch.islower():
        lower +=1
        continue
    if ch.isupper():
        upper += 1
        continue
    symbols += 1
tot = 1.0 * len(S)
print(white/tot)
print(lower/tot)
print(upper/tot)
print(symbols/tot)