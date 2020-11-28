import java.util.*;
import java.io.*;
public class G {
    class EL implements Comparable<EL> {
        int v, id;
        public EL(int v, int id) {
            this.v=v; this.id=id;
        }
        public int compareTo(EL o){
            int d = v - o.v;
            if(d != 0) return d;
            return id - o.id;
        }
    }
    boolean ok(ArrayList<EL> X, ArrayList<EL> Y, int n, int s, int d) {
        TreeSet<EL> A = new TreeSet<>(X);
        TreeSet<EL> B = new TreeSet<>(Y);

        while(A.size() > 0 && B.size() > 0 && n > 0) {
            EL eA = A.last();
            EL eB = B.last();
            if(eB.v < eA.v) {
                EL search = new EL(eA.v - d, -1);
                EL match = B.ceiling(search);
                if(match != null && match.v + eA.v <= s) {
                    B.remove(match);
                    A.remove(eA);
                    n--;
                } else {
                    A.remove(eA);
                }
            }
            else {
                EL search = new EL(eB.v - d, -1);
                EL match = A.ceiling(search);
                if(match != null && match.v + eB.v <= s) {
                    A.remove(match);
                    B.remove(eB);
                    n--;
                } else {
                    B.remove(eB);
                }
            }
        }
        return n == 0;
    }

    void solve(BufferedReader in) throws Exception {
        int[] x = toInts(in.readLine());
        int n = x[0], p = x[1], q = x[2], s = x[3];
        ArrayList<EL> X = new ArrayList<>();
        ArrayList<EL> Y = new ArrayList<>();
        for(int i = 0; i<p; i++) X.add(new EL(toInt(in.readLine()), i));
        for(int i = 0; i<q; i++) Y.add(new EL(toInt(in.readLine()), i));

        int lo = 0;
        int hi = 1000000000; //10*9
        if(!ok(X, Y, n, s, hi)){
            System.out.println(-1);
            return;
        }
        while(lo < hi) {
            int mid = (lo + hi)/2;
            if(ok(X, Y, n, s, mid)) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        System.out.println(lo);
    }
    int toInt(String s) {return Integer.parseInt(s);}
    int[] toInts(String s) {
        String[] a = s.split(" ");
        int[] o = new int[a.length];
        for(int i = 0; i<a.length; i++) o[i] = toInt(a[i]);
        return o;
    }
    void e(Object o) {
        System.err.println(o);
    }
    public static void main(String[] args) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        (new G()).solve(in);
    }
}
