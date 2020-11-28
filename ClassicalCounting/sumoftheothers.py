import sys

lines = sys.stdin.readlines()
for line in lines:
    digits = map(int, line.split())
    tot = sum(digits)
    val = tot/2
    print(val)