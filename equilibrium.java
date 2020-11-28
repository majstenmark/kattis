 
import java.util.*;
import java.io.*;
public class equilibrium {
    void solve(BufferedReader in) throws Exception {
        int N = toInt(in.readLine());
        ArrayList<Node> G = new ArrayList<Node>();
        for(int i = 0; i < N; i++){
            Node n = new Node(i);
            G.add(n);
        }
        for(int i = 0; i < N-1; i++){
            int[] uv = toInts(in.readLine());
            G.get(uv[0]).addChild(G.get(uv[1]));
            G.get(uv[1]).addChild(G.get(uv[0]));
        }
        //start with 0
        bfs(G.get(0), G);
        ArrayList<Node> out = new ArrayList<Node>();
        
        s(G.get(0), false, G, out);
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++){
            Node n = out.get(i);
            sb.append(n.id);
            if(i < N){
                sb.append(' ');
            }
        }
        System.out.println(sb.toString());


    }

    private void bfs(Node fromnode, ArrayList<Node> nodes){
        ArrayList<Node> q = new ArrayList<Node>();
        q.add(fromnode);
        fromnode.visited=true;

        ArrayList<Node> q2; 
        while(q.size()>0){
            q2 = new ArrayList<Node>();
            for(Node n: q){
                for(Node next:n.ne){
                    if(!next.visited){
                        next.visited= true;
                        n.ch.add(next);
                        q2.add(next);
                    }
                }
            }
            q = q2;
        }

    }

    private void s(Node node, boolean parent_set, ArrayList<Node> nodes, ArrayList<Node> out){
        if(node.children().size() == 0) {
            out.add(node);
            return;
        }
        int no = node.children().size();
        int breakoff = (no-1)/2;

        if(!parent_set) breakoff++;
        for(int i = 0; i<breakoff; i++)
            s(node.get(i), false,nodes,out);
        
        out.add(node);

        for(int i = breakoff; i<no; i++)
            s(node.get(i), false,nodes,out);

    }

    int toInt(String s) {return Integer.parseInt(s);}
    int[] toInts(String s) {
        String[] a = s.split(" ");
        int[] o = new int[a.length];
        for(int i = 0; i<a.length; i++) 
            o[i] = toInt(a[i]);
        return o;
    }
    public static void main(String[] args) 
    throws Exception {
        BufferedReader in = new BufferedReader
            (new InputStreamReader(System.in));
        (new equilibrium()).solve(in);
    }

    public class Node{
        ArrayList<Node> ne = new ArrayList<Node>();
        ArrayList<Node> ch = new ArrayList<Node>();
        int id;
        
        public boolean visited = false;

        public Node(int i){
            this.id = i;
        }

        public void addChild(Node n){
            ne.add(n);
        }
        public Node get(int i){
            return ch.get(i);
        }

        public ArrayList<Node> children(){
            return ch;
        }

    }
}