import sys
lines = sys.stdin.readlines()
def digs(line): return [int(v) for v in line.split()[1:]]

for i, line in enumerate(lines):
    digits = digs(line)
    print(f'Case {i+1}: {min(digits)} {max(digits)} {max(digits) - min(digits)}')