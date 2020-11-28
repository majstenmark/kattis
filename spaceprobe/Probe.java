import java.util.*;
import java.io.*;

public class Probe{
    public static void main(String[] args) throws Exception{
        new Probe().run();
    }
    private long[] deadInterval(long fb, long fe, long m, long t1, long t2){
        long start = Math.max(t1, fb - m);
        long end = Math.min(t2, fe - m);
        return new long[]{start, end};

    }

    private void run() throws Exception{

        int END = 1;
        int START = 0;
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] nkt1t2 = (reader.readLine()).split(" ");

        int N = Integer.parseInt(nkt1t2[0]);
        int K = Integer.parseInt(nkt1t2[1]);

        long T1 = Long.parseLong(nkt1t2[2]);
        long T2 = Long.parseLong(nkt1t2[3]);
        long[] measurements = new long[N];
        String[] data1 = (reader.readLine()).split(" ");

        for(int i= 0; i < N; i++){
          long m = Long.parseLong(data1[i]);
          measurements[i] = m;
        }
        long[][] deadzones = new long[K][2];

        for(int i= 0; i < K; i++){
            String[] data = (reader.readLine()).split(" ");
            long fb = Long.parseLong(data[0]);
            long fe = Long.parseLong(data[1]);
            deadzones[i][0] = fb;
            deadzones[i][1] = fe;
        }
        Event[] events = new Event[2*N*K];
        int index = 0;
        for(long m:measurements){
            for(int i = 0; i < K;i++){
                long fb = deadzones[i][0];
                long fe = deadzones[i][1];
                long[] interval = deadInterval(fb, fe, m, T1, T2);
                events[index++] = new Event(interval[0], START);
                events[index++] = new Event(interval[1], END);

            }
        }
        Arrays.sort(events);
        long deadTime = 0;
        long totDeadTime = 0;
        int counter = 0;
        for(Event e: events){
            if(e.type == START){
                if(counter == 0) deadTime = e.time;
                counter += 1;
            }
            else{
                counter -= 1;
                if(counter == 0) totDeadTime += (e.time - deadTime);
            }
        }
        long totalTime = T2 - T1;
        double prob = (totalTime - totDeadTime + 0.0)/totalTime;
        System.out.println(prob);

        }

    class Event implements Comparable<Event>{
        long time;
        int type;
        public Event(long time, int type){
            this.time = time;
            this.type = type;
        }
        public int compareTo(Event other){
            return Long.compare(time, other.time);
        }
    }
}
