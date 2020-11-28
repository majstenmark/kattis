import java.util.*;
import java.io.*;

public class LIS{

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new LIS().run();
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
    private int[] findLis(int[] seq, int N){
        int[] inc = new int[N];
        int[] index = new int[N];
        for(int n =0; n < N; n++){
          inc[n] = 1;
          index[n] = -1;
        }
        for(int t = 1; t < N; t++){
          for(int b = 0; b < t; b++){
            if(seq[b] < seq[t] && inc[t] <= inc[b]){
              inc[t] = inc[b] + 1;
              index[t] = b;
            }
          }
        }
        int k = 1;
        int maxIndex = 0;
        for (int i =0; i < N; i++){
          if(inc[i] > k){
            k = inc[i];
            maxIndex = i;
          }
        }
        int i = index[maxIndex];
        int [] li = new int[k];
        li[k-1] = maxIndex;
        int p = k - 2;
        while(i != -1){
          li[p] = i;
          i = index[i];
          p -= 1;
        }
        return li;
    }

    private void run() throws Exception{
            try{
              while(true){
                int N = readInt();
                int[] vals = new int[N];
                for(int i = 0; i < N;i++){
                  vals[i] = readInt();
                }
                int [] res = findLis(vals, N);
                print(res.length);
                StringBuilder sb = new StringBuilder();
                sb.append(res[0]);
                for(int i = 1; i < res.length;i++){
                  sb.append(" " + res[i]);
                }
                print(sb.toString());
              }
            }catch(Exception e){}

        }
}
