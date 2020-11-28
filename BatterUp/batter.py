N = int(raw_input())
bats = map(int, raw_input().split())
atbats = 0
score= 0
for b in bats:
    if b >= 0:
        atbats += 1
        score += b
print(score * 1.0/atbats)