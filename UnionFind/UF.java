import java.util.*;
import java.io.*;

public class UF{

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new UF().run();
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

    private int find(int x){
      int y = p[x];
      while(y != x){
        p[x] = p[y];
        x = y;
        y =p[y];
      }
      return p[x];
    }
    private void union(int a, int b){
      int ap = find(a);
      int bp = find(b);
      if(ap != bp){
        if(s[ap] < s[bp]){
          s[bp] += s[ap];
          p[ap] = p[bp];
        }else{
          s[ap] += s[bp];
          p[bp] = p[ap];
        }
      }
    }

    int[] p;
    int[] s;

    private void run() throws Exception{
            int N = readInt();
            int Q = readInt();
            StringBuilder sb = new StringBuilder();
            p = new int[N+1];
            s = new int[N+1];
            for(int i = 0; i < N+1;i++){
              p[i] = i;
              s[i] = 1;
            }
            for(int i = 0; i < Q;i++){
              String op = readStr();
              int a = readInt();
              int b = readInt();
              if(op.equals("=")){
                union(a,b);
              }else{
                int ap = find(a);
                int bp = find(b);
                if(ap == bp){
                  sb.append("yes\n");
                }else{

                  sb.append("no\n");
                }
              }

        }
        System.out.print(sb.toString());
    }
}
