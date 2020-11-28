import math
N = int(raw_input())
L = math.log(N, 2)
# L days printing printers and then print last day
#Test 1
def test(days_for_printers, n):
    c = int(math.ceil(days_for_printers))
    nbr_of_printers = math.pow(2, c)
    return nbr_of_printers <= n

if test(L, N):
    print(int(L+1))
else:
    print(int(L + 2))