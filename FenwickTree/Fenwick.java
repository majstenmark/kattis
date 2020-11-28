import java.util.*;
import java.io.*;

public class Frosh{
    class FenwickTree{
      int[] arr;
      public FenwickTree(int N){
        arr = new int[N+1];
      }
      public void inc(int i, int v){
        pinc(i + 1, v);
      }

      public int sum(int a){
        return psum(a);
      }

      public int sum(int a, int b){
        return psum(b) - psum(a);
      }

      private void pinc(int i, int v){

          while (i < arr.length){
            arr[i] += v;
            i += i & -i;
          }
      }
      private int psum(int i){
        int s = 0;
        while (i > 0){
          s += arr[i];
          i -= i & -i;
        }
        return s;

      }

    }

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new Frosh().run();
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
        int n = readInt();
        int cnt = 0;
        int[] a= new int[n];
        int[] b= new int[n];

        FenwickTree fen = new FenwickTree(n);
        for(int i = 0; i < n;i++){
            int x  = readInt();
            a[i] = x;
            b[i] = x;
        }
        Arrays.sort(a);
        HashMap<Integer, Integer> map= new HashMap<Integer, Integer>();
        for(int i = 0; i< n;i++){
            map.put(a[i], i);
        }
        for(int i = 0; i < n;i++){
          int index =map[b[i]];
            cnt += fen.sum(index, N-1);

            fen.inc(index, 1);
            }else{
              print(fen.sum(x));
            }
        }
    }
}
