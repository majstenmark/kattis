import java.util.*;

import java.util.Collections;
import java.io.*;

public class Box{

  public static void main(String[] args) throws Exception{
    new Box().run();
  }
  private void fail() {
    throw new IllegalArgumentException();
  }

  private void run() throws Exception{
    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    String[] nk = (reader.readLine()).split(" ");

    int N = Integer.parseInt(nk[0]) ;
    int K = Integer.parseInt(nk[1]) ;
    Show[] shows = new Show[N];
    for(int i= 0; i < N; i++){
      String[] data = (reader.readLine()).split(" ");
      int s = Integer.parseInt(data[0]);
      int f = Integer.parseInt(data[1]);
      shows[i] = new Show(s, f, i);
    }
    Arrays.sort(shows);
    for(int i = 0; i<N; i++) shows[i].id = i;
    int count = 0;
    TreeSet<Show> slots = new TreeSet<Show>();
    for (int i = 0; i <K; i++){
      Show troll=new Show(-1, -1, i);
      slots.add(troll);
    }
    for(Show a: shows){
      Show troll=new Show(0, a.start, N +1);
          Show latest = slots.floor(troll);
          //if(latest.end >= a.start) fail();
          //if(latest != acts[latest.id]) fail();
        //  System.out.println("Latest " + latest);
        if(latest!=null){
          slots.remove(latest);
          slots.add(a);
          if(slots.size() != K) fail();

          //System.out.println("Added " + a);
          count+= 1;
        }
      }

    System.out.println(count);
  }
  class Show implements Comparable<Show>{
    public int start, end, id;

    public Show(int s, int e, int id){
      start = s;
      end = e;
      this.id = id;
    }

    public String toString(){
        return "(" + start + ", " + end + ")";
    }

    public int compareTo(Show other){
      if(this.end != other.end) return this.end - other.end;
      return id - other.id;
    }
  }
}
