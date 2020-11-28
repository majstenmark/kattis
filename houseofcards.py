def count_cards(h):
    return 3 *h * (h-1) //2 + 2 * h

h = int(raw_input())
while True:
    nbr = count_cards(h)
    if nbr % 4 == 0:
        print(h)
        exit()
    h += 1
