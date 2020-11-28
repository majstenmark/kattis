emma = map(int, raw_input().split())
marcus = map(int, raw_input().split())
emmaLikes = 1
marcusLikes = 2
bothLikes = 3
filmTypes = [0 for _ in range(10**6)]
for film in emma[1:]:
    filmTypes[film] += emmaLikes
for film in marcus[1:]:
    filmTypes[film] += marcusLikes
segments = 0
type = 0
for filmType in filmTypes:
    if filmType != 0 and (type != filmType or filmType == bothLikes):
        segments += 1
        type = filmType

print(segments)
