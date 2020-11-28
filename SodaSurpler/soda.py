E, F,C = map(int, raw_input().split())
b = E + F
drunken = 0
while b >= C:
    new_bottles = b/C
    drunken += new_bottles
    b = new_bottles + b % C
print drunken
