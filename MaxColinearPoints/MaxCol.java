import java.util.*;
import java.io.*;

public class MaxCol{

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new MaxCol().run();
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
        int m = readInt();
        FenwickTree fen = new FenwickTree(n);
        for(int i = 0; i < m;i++){
            String op = readStr();
            int x  = readInt();
            if(op.equals("+")){
              int y  = readInt();
              fen.inc(x, y);
            }else{
              print(fen.sum(x));
            }
        }
    }
}
