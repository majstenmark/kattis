T = int(raw_input())
for t in range(T):
    data = [int(v) for v in raw_input().split()]
    turtles = data[:-1]
    imported = 0
    last_year = 1
    for year in turtles:
        if year > last_year * 2:
            imported += year - last_year * 2
        last_year = year
    print(imported)