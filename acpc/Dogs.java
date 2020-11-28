import java.util.*;
import java.util.*;
import java.io.*;

public class Dogs{

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new Dogs().run();
    }
    private void fail() {
        throw new IllegalArgumentException();
    }

    private void print(String s){
        System.out.println(s);
    }


    private void print(int s){
        System.out.println(s);
    }

    private int readInt() throws Exception{

        if(hasNext == 0){
          buff = (reader.readLine()).split(" ");
        }
        int n = Integer.parseInt(buff[hasNext]);
        hasNext = (hasNext + 1) % buff.length;
        return n;
    }

    private String readStr() throws Exception{

        if(hasNext == 0){
          buff = (reader.readLine()).split(" ");
        }
        String n = buff[hasNext];
        hasNext = (hasNext + 1) % buff.length;
        return n;
    }


    private void run() throws Exception{
            int N = readInt(); // dogs
            int M = readInt(); // bowls
            int nodes = N + M + 2;
            long INF = 10000000000000L;
            long [][] cap = new long[nodes][nodes];
            long [][] cost = new long[nodes][nodes];
            long [][] tij = new long[nodes][nodes];


            for(int i = 0; i < nodes; i++){
              for(int j = 0; j < nodes; j++){
                  cost[i][j] = INF;
              }
            }
            for(int i = 1; i <= N;i++){
              cap[0][i] = 1;
              cost[0][i] = 0;
            }
            for(int j = 1; j <= M;j++){
              cap[N + j][nodes-1] = 1;
              cost[N + j][nodes-1] = 0;
            }
            for(int i = 1; i <= N;i++){
              for(int j = 1; j <= M; j++){
                int t = readInt();
            //    print("tij " + tij);
                cap[i][N + j] = 1;
                tij[i][N + j] = t;
              }
            }
/*
            for(int i = 0; i < nodes; i++){
              for(int j = 0; j < nodes; j++){
                  print("" + i + "->" + j + " cap " + cap[i][j] + " cost " + cost[i][j]);
              }
            } */

            long mincost = 1000000000l;
            MinCostMaxFlow mcflow = new MinCostMaxFlow();
            for(int t = 1; t <= 200; t++){
              for(int i = 0; i < nodes;i++){
                for(int j = 0; j < nodes; j++){
                  if(t - tij[i][j] < 0){
                      cost[i][j] = INF;
                  }
                  else{
                    if(tij[i][j] > 0){

                      cost[i][j] = t - tij[i][j];
                    }else{
                      cost[i][j] = 0;

                    }
                }
              }
              }


              long [] res = mcflow.mcmf(cap, cost, 0, nodes -1);
              mincost = Math.min(mincost, res[1]);


            }
            print("" + mincost);


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
}
