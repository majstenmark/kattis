def check(S, length):
    s = S[:length]
    for i in range(length, len(S), length):
        alt = S[i:i + length]
        s = s[-1] + s[0:length-1]
        if alt != s:
            return False
    return True

S = raw_input()
for k in range(1, len(S)+1):
    if len(S) % k == 0:
        if check(S,k):
            print(k)
            exit()