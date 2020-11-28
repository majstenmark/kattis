import java.util.*;
import java.io.*;

public class Precomp{

    BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
    private int hasNext = 0;
    private String[] buff;

    public static void main(String[] args) throws Exception{
        new Precomp().run();
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

    private void run() throws Exception{
        int K = 1000000001;
        boolean[] primesbool = new boolean[K];
        ArrayList<Integer> primes = new ArrayList<>();
        primesbool[0] = true;
        primesbool[1] = true;
        
        for(int i = 2; i < K; i++){
            if(!primesbool[i]){
                primes.add(i);
                for(int v = 2 * i; v < K; v = v + i){
                    primesbool[v] = true;
                }
            }
        }
        print("Primesdone");
        ArrayList<Integer> ms = new ArrayList<>();
        for(int p: primes){
            ms.add(p-1);
        }
        primesbool = null;
        boolean[] states = new boolean[K];
        for(int state = 0; state < K; state ++){
            if(!states[state]){
                for(int m: ms){
                    if(state + m >= K){
                        break;
                    }
                    states[state + m] = true;

                }
            }
        }
        for(int state = 0; state < K; state ++){
            if(!states[state]){
                print(state);
            }
        }
    }


}