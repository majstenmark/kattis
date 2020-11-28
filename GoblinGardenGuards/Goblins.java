import java.util.*;
import java.io.*;

public class Goblins{

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new Goblins().run();
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

    private boolean dist2(int xx, int x, int yy, int y, int r2){
        int dx = (xx - x);
        int dy = (yy - y);
        return (dx * dx + dy * dy) <= r2;
      }

      private void sprinkle(int x, int y, int r){

            int startX = Math.max(0, x - r-1);
            int endX = Math.min(10001, x+ r + 1);
            int startY = Math.max(0, y - r-1);
            int endY = Math.min(10001, y + r + 1);
            int r2 = r *r;
            for(int xx = startX; xx < endX; xx++){
              for(int yy = startY; yy < endY; yy++){
                  garden[xx][yy] = garden[xx][yy] || dist2(xx, x, yy, y, r2);
              }
            }
      }


    boolean[][] garden;

    private void run() throws Exception{
            int G = readInt();
            int[][] goblins = new int[G][2];
            for(int i = 0; i < G;i++){
              int x = readInt();
              int y = readInt();
              goblins[i] = new int[]{x, y};
            }
            int M =readInt();
            int lim = 10001;
            garden = new boolean[lim][lim];
            for(int i = 0; i < M;i++){
              int x = readInt();
              int y = readInt();
              int r = readInt();
              sprinkle(x, y, r);
            }
            int count = 0;
            for(int i = 0; i < G;i++){
              int x  = goblins[i][0];
              int y  = goblins[i][1];

              if(!garden[x][y]){
                count += 1;
              }
            }
            print(count);
    }
}
/*


*/
