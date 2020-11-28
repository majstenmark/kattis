a, b = map(int, raw_input().split())
m, sigma = map(int, raw_input().split())
xmin = max(1, sigma - m)
xmax = m - 1
R1 = a * xmin + b * (m - xmin)
R2 = a * xmax + b * (m - xmax)
print(max(R1, R2))
