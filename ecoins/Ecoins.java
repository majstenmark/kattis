import java.util.*;
import java.io.*;

public class Ecoins{
    BufferedReader reader;
    int INF = Integer.MAX_VALUE - 1;

    public static void main(String[] args) throws Exception{
        new Ecoins().run();
    }
    private void fail() {
        throw new IllegalArgumentException();
    }
    private void runtestcase() throws Exception{

        String[] ms = (reader.readLine()).split(" ");
        int M = Integer.parseInt(ms[0]);
        int S = Integer.parseInt(ms[1]);
        ArrayList<Coin> coins = new ArrayList<Coin>();
        int[][] dist = new int[S+1][S+1];
        for(int x = 0; x < S + 1; x++){
            for(int y = 0; y < S + 1; y++){
                dist[x][y] = INF;
            }
        }
        dist[0][0] = 0;
        int S2 = S * S;
        for(int i = 0; i < M; i++){
            String[] data = (reader.readLine()).split(" ");
            int C = Integer.parseInt(data[0]);
            int I = Integer.parseInt(data[1]);
            coins.add(new Coin(C, I));
        }
        for(int x = 0; x < S + 1; x++){
            for(int y = 0; y < S + 1; y++){
                for(Coin c: coins){
                    if(x + c.conv <= S && y + c.info <= S && dist[x][y] + 1 < dist[x + c.conv][y+ c.info]){
                        dist[x + c.conv][y+ c.info] = dist[x][y] + 1;
                    }
                }
            }
        }
        int count = INF;
        for(int x = 0; x < S + 1; x++){
            for(int y = 0; y < S + 1; y++){
            //    print(dist[x][y]);
                if(x *x + y*y == S2 && dist[x][y] < count){
                    count = dist[x][y];
                }
            }
        }

        if(count == INF){
            print("not possible");
        }
        else{
            print(count);

        }
        try{
        reader.readLine();
        }catch(Exception ex){}
    }

    private void print(String s){
        System.out.println(s);
    }

    private void print(int s){
        System.out.println(s);
    }

    private void run() throws Exception{
        reader = new BufferedReader(new InputStreamReader(System.in));
        String[] nm = (reader.readLine()).split(" ");
        int n = Integer.parseInt(nm[0]);
        for(int i = 0; i < n;i++){
            runtestcase();
        }

    }
    class Coin{
        int conv = 0;
        int info = 0;
        public Coin(int a, int b){
            conv = a;
            info = b;
        }
    }
}
