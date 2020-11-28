import java.util.*;
import java.io.*;

public class MCP{
  class Point{
    int x, y;
    public Point(int x, int y){
      this.x = x;
      this.y = y;
      }
    }

  class Eq{
    int a, b, c;
    public Eq(int a, int b, int c){
      this.a = a;
      this.b =b;
      this.c =c;

    }

    public String toString(){
      return "A"+a+"B"+b+"C"+c;
    }
  }

  public int gcd(int a, int b){
    if (b == 0){
      return a;
    }
    if (a == 0 || a % b == 0){
      return b;
    }
    return gcd(b, a % b);

  }


  public Eq line(Point p1, Point p2){
    int A = (p1.y - p2.y);
    int B = (p2.x - p1.x);
    int C = (p1.x * p2.y - p2.x * p1.y);
    return new Eq(A, B, -C);
  }

  public Eq lineeq(Point p1, Point p2){
    Eq eq = line(p1, p2);
    int g = gcd(gcd(eq.a, eq.b), eq.c);
    eq.a = eq.a / g;
    eq.b = eq.b / g;
    eq.c = eq.c /g;

    if ((eq.a < 0) || (eq.a == 0 && eq.b < 0) || (eq.a == 0 &&  eq.b == 0 && eq.c < 0)){
      eq.a = -eq.a;
      eq.b = -eq.b;
      eq.c = -eq.c;
    }
    return eq;

    }



    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new MCP().run();
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
        int N = readInt();

        Point[] points = new Point[N];
        HashMap<String, Integer> eqs = new HashMap<String, Integer>();
        while(N != 0){

          for (int n = 0; n < N; n ++){
              int x  = readInt();
              int y = readInt();
              points[n] = new Point(x, y);
          }

          for (int i = 0; i < N -1; i ++){

                for (int j = i +1; j < N; j ++){
                  Eq eq = lineeq(points[i], points[j]);
                  String eq_str = eq.toString();
                  if (!eqs.containsKey(eq_str)){
                    eqs.put(eq_str, 0);
                  }
                  eqs.put(eq_str, eqs.get(eq_str) + 2);
                }
              }

              int maxCol  = 1;
              if (N == 1){
                print(1);
              }else{
                  for (int val: eqs.values()){
                    maxCol = Math.max(maxCol, val);
                  }
                //  print("Len of eqs ");
                //  print(eqs.size());
                  int mc = (int) Math.sqrt(maxCol) + 1;
                  print(mc);
              }
          N = readInt();
          points = new Point[N];
          eqs = new HashMap<String, Integer>();

    }
  }
}
