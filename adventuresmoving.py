import sys

def fail():
    print('Impossible')
    exit()

data = sys.stdin.readlines()
D = int(data[0])
gas_stations = [(0, 0)]
if len(data) == 1 and D > 0:
    fail()

for i in range(1, len(data)):
    dist, price = map(int, data[i].split())
    gas_stations.append((dist, price))
    dist2prev = gas_stations[i][0] - gas_stations[i-1][0]
    if dist2prev > 200:
        fail()
    if dist > D:
        break

if gas_stations[1][0] > 100:
    fail()
if D - gas_stations[-1][0] > 100:
    fail()

# cheapest cost to leave the gas station with that amount of gas
INF = 10** 12
table = [[INF] * 201 for _ in range(len(gas_stations))]
table[0][100] = 0
for i in range(1, len(gas_stations)):
    dist2prev = gas_stations[i][0] - gas_stations[i-1][0]
    price = gas_stations[i][1]   
    
    for prev_litre in range(dist2prev, 201):
        for litres in range(0, 201):
            litres_now = prev_litre - dist2prev + litres
            if litres_now <= 200:
                alt_price = table[i-1][prev_litre] + litres * price
                table[i][litres_now] = min(table[i][litres_now], alt_price)
last_dist = D - gas_stations[-1][0]
print(table[-1][100+last_dist])
            

        






