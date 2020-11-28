N = int(input())
s = list(map(int, input().split()))
gis = [s[0]]
rec = s[0]
for i in range(1, len(s)):
    if s[i] > rec:
        gis += [s[i]]
        rec = s[i]
print(len(gis))
print(' '.join(map(str, gis)))
