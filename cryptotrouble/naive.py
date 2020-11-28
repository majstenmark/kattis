def solve(N, B):
    MOD = 10 ** 9 + 7
    B = map(int, B)
    def check(bstr, orig):   
        digs = []

        for i, ch in enumerate(bstr):
            if ch == '1':
                digs.append(orig[i])
        if digs[0] == 0 and len(digs) > 1:
            return 0
        
        res =  1 if sum(digs) % 3 == 0 else 0
        return res
        

    cnt= 0
    for ss in range(1, 2 ** len(B)):
        btmp= bin(ss)[2::]
        bstr = '0' * (N -len(btmp)) + btmp
        cnt += check(bstr, B)

        cnt %= MOD

    return cnt

if __name__ == '__main__':
    N = int(raw_input())
    B = raw_input()
    print(solve(N, B))