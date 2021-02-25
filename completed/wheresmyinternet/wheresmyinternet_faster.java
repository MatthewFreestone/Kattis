import java.io.*;
import java.util.*;

class DFS_Graph_Faster{

	int vert;
	ArrayList<Integer>[] adjacent; 



	public DFS_Graph_Faster(int vert){
      this.vert = vert;
		adjacent = new ArrayList[vert];
		for (int i = 0; i < vert; i++){
			adjacent[i] = new ArrayList<Integer>();
		}
	}

	public void addEdge(int n, int m){
      adjacent[n].add(m);
      adjacent[m].add(n);
   }
   
	public boolean[] search(int v){
      Stack<Integer> stack = new Stack<Integer>(); 
      stack.push(v);
      boolean[] visited = new boolean[vert];
      visited[v] = true;


      while(!stack.isEmpty()){
         int curr = stack.pop();
         List<Integer> adjToCurr = adjacent[curr];
         for (int next: adjToCurr){
            if(!visited[next]){
               stack.push(next);
               visited[next] = true;
            }
         }
      }

		return visited;
	}
	
	
}


class wheresmyinternet_faster{
	public static void main(String[] args) throws Exception{
      long time = System.currentTimeMillis();
      Kattio io = new Kattio(System.in, System.out);
		int houses = io.getInt();
		int cables = io.getInt();
		DFS_Graph_Faster graph = new DFS_Graph_Faster(houses+1);
		for (int i = 0; i < cables; i++){
			int n = io.getInt();
			int m = io.getInt();
			graph.addEdge(n,m);
		}

      boolean[] inNet = graph.search(1);

      String ans = "";
		if (houses > 1){
         for (int i = 1; i < houses+1; i++){
            if(!inNet[i]){
               //notCon.add(i);
               ans += i + "\n";
            }
         }
      }
     
		if(!ans.equals("")){
         io.print(ans);
		}
		else{
			io.print("Connected");
      }
      
      //io.println("Operation took " + (System.currentTimeMillis() - time) + " ms");
      io.flush();
	}

}







class Kattio extends PrintWriter {
   public Kattio(InputStream i) {
       super(new BufferedOutputStream(System.out));
       r = new BufferedReader(new InputStreamReader(i));
   }
   public Kattio(InputStream i, OutputStream o) {
       super(new BufferedOutputStream(o));
       r = new BufferedReader(new InputStreamReader(i));
   }

   public boolean hasMoreTokens() {
       return peekToken() != null;
   }

   public int getInt() {
       return Integer.parseInt(nextToken());
   }

   public double getDouble() {
       return Double.parseDouble(nextToken());
   }

   public long getLong() {
       return Long.parseLong(nextToken());
   }

   public String getWord() {
       return nextToken();
   }



   private BufferedReader r;
   private String line;
   private StringTokenizer st;
   private String token;

   private String peekToken() {
       if (token == null)
           try {
               while (st == null || !st.hasMoreTokens()) {
                   line = r.readLine();
                   if (line == null) return null;
                   st = new StringTokenizer(line);
               }
               token = st.nextToken();
           } catch (IOException e) { }
       return token;
   }

   private String nextToken() {
       String ans = peekToken();
       token = null;
       return ans;
   }
}
