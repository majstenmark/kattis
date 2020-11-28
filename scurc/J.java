import java.util.*;
import java.io.*;
public class J {
    int get_id(int x) {
        if(x == -1) return R+1;
        if(x == -2) return R;
        return x;
    }
    int P, R, L;
    void solve(BufferedReader in) throws Exception {
        int[] xx = toInts(in.readLine());
        P = xx[0]; R = xx[1]; L = xx[2];
        MinCostMaxFlow net = new MinCostMaxFlow();
        int sz = R + 3;
        long[][] cap = new long[sz][sz];
        long[][] cost = new long[sz][sz];
        for(int i = 0; i<L; i++) {
            xx = toInts(in.readLine());
            int e1 = get_id(xx[0]);
            int e2 = get_id(xx[1]);
            cap[e2][e1] = 1;
            cost[e2][e1] = 1;
            cap[e1][e2] = 1;
            cost[e1][e2] = 1;
        }
        cap[R+1][R+2] = P;
        cost[R+1][R+2] = 0;
        long[] v = net.mcmf(cap, cost, R, R+2);
        long f = v[0];
        long c = v[1];
        if(f == P){
            System.out.println(c);
        }else {
            System.out.println((P - f) + " people left behind");

        }

    }
    int toInt(String s) {return Integer.parseInt(s);}
    int[] toInts(String s) {
        String[] a = s.split(" ");
        int[] o = new int[a.length];
        for(int i = 0; i<a.length; i++) o[i] = toInt(a[i]);
        return o;
    }
    void e(Object o) {
        System.err.println(o);
    }
    public static void main(String[] args) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        (new J()).solve(in);
    }
}
class MinCostMaxFlow {
    boolean found[];
    int N, dad[];
    long cap[][], flow[][], cost[][], dist[], pi[];

    static final long INF = Long.MAX_VALUE / 2 - 1;

    boolean search(int s, int t) {
        Arrays.fill(found, false);
        Arrays.fill(dist, INF);
        dist[s] = 0;

        while (s != N) {
            int best = N;
            found[s] = true;
            for (int k = 0; k < N; k++) {
                if (found[k]) continue;
                if (flow[k][s] != 0) {
                    long val = dist[s] + pi[s] - pi[k] - cost[k][s];
                    if (dist[k] > val) {
                        dist[k] = val;
                        dad[k] = s;
                    }
                }
                if (flow[s][k] < cap[s][k]) {
                    long val = dist[s] + pi[s] - pi[k] + cost[s][k];
                    if (dist[k] > val) {
                        dist[k] = val;
                        dad[k] = s;
                    }
                }

                if (dist[k] < dist[best]) best = k;
            }
            s = best;
        }
        for (int k = 0; k < N; k++)
            pi[k] = Math.min(pi[k] + dist[k], INF);
        return found[t];
    }

    long[] mcmf(long c[][], long d[][], int s, int t) {
        cap = c;
        cost = d;

        N = cap.length;
        found = new boolean[N];
        flow = new long[N][N];
        dist = new long[N+1];
        dad = new int[N];
        pi = new long[N];

        long totflow = 0, totcost = 0;
        while (search(s, t)) {
            long amt = INF;
            for (int x = t; x != s; x = dad[x])
                amt = Math.min(amt, flow[x][dad[x]] != 0 ? 
                        flow[x][dad[x]] : cap[dad[x]][x] - flow[dad[x]][x]);
            for (int x = t; x != s; x = dad[x]) {
                if (flow[x][dad[x]] != 0) {
                    flow[x][dad[x]] -= amt;
                    totcost -= amt * cost[x][dad[x]];
                } else {
                    flow[dad[x]][x] += amt;
                    totcost += amt * cost[dad[x]][x];
                }
            }
            totflow += amt;
        }

        return new long[]{ totflow, totcost };
    }
}
