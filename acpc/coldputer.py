N = int(raw_input())
deg = map(int, raw_input().split())
print len([x for x in deg if x < 0])
