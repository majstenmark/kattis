def read(l):
    a, b = [int(v) for v in l.split()]
    return a, b

prices = [0] + [int(v) for v in raw_input().split()]
times = [read(raw_input()) for _ in range(3)]
events = []
START, END = 1, -1
for s, e in times:
    events.append((s, START))
    events.append((e, END))
events.sort()
trucks = 0
price = 0
time = events[0][0]
for e, diff in events:
    time_diff = e - time
    time = e
    price += trucks * time_diff * prices[trucks]
    trucks += diff

    #print('Event {} {}, current price {}, nbr of trucks after {}'.format(e, diff, price, trucks))

    

print(price)


    