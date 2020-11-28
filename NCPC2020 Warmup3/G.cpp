#include <bits/stdc++.h>
using namespace std;

int count(int c, int N){
    int s = 0;
    for(int i = 0; i<N; i++) {
        if(((1<<i)&c) != 0) s++;
    }
    return s;
}

int solve() {
    int N;
    cin >> N;
    vector<vector<int>> G(N, vector<int>(0));
    for(int i = 0; i<N; i++) {
        int no;
        cin >> no;
        for(int j = 0; j<no; j++) {
            int neigh;
            cin >> neigh;
            G[i].push_back(neigh - 1);
        }
    }
    int BEST = N;
    for(int mask = 1; mask<(1<<N); mask++) {
        int C = count(mask, N);
        if(C >= BEST) {
            continue;
        }
        vector<int> use(N, 0);
        for(int i = 0; i<N; i++) {
            if(((1<<i)&mask) != 0) {
                use[i] = 1;
                for(int j : G[i]) {
                    use[j] = 1;
                }
            }
        }
        bool ok = true;
        for(int i = 0; i<N; i++) {
            ok = ok && use[i];
        }
        if(ok) {
            BEST = C;
        }
    }
    return BEST;
}
int main() {
    cout.precision(9);
    int T;
    cin >> T;
    for(int i = 0; i<T; i++) {
        cout << solve() << endl;
    }
    return 0;
}

/*
inp = raw_input

def ni():
    return int(inp())

def nl():
    return [int(v) for v in inp().split()]

def test(mask, g):
    N = len(g)
    covered= [0]*(N+1)
    for i in range(N):
        if (1<<i)&mask:
            covered[i+1] = 1
            for ne in g[i]:
                covered[ne] = 1
    return sum(covered) == N

INF = 10**12
def solve(n, g):
    BEST = INF

    for mask in range(1, 2 ** n):
        c = bin(mask).count('1')
        if c >= BEST:
            continue
        ok = test(mask, g)
        if ok:
            BEST = c
    return BEST


t = ni()

for _ in range(t):
    n  = ni()
    g = []
    for i in range(n):
        fr = nl()
        g.append(fr[1:])
    s = solve(n, g)
    print(s)
*/
