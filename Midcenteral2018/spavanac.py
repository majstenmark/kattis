H, M = map(int, raw_input().split())
h = (H - 1) % 24 if M < 45 else H
m = (M - 45) % 60
print '{} {}'.format(h,m)
