import java.util.*;

class DFS_Graph{

    int vert;
    LinkedList<Integer>[] adjacent; 
    ArrayList<Integer> inNet;


    public DFS_Graph(int vert){
        this.vert = vert;
        inNet = new ArrayList<Integer>();
        adjacent = new LinkedList[vert];
        for (int i = 0; i < vert; i++){
            adjacent[i] = new LinkedList();
        }
    }

    public void addEdge(int n, int m){
        adjacent[n].add(m);
        adjacent[m].add(n);
    }


    public ArrayList<Integer> search(int v){
      Stack<Integer> stack = new Stack<Integer>(); 
      stack.push(v);
      boolean[] visited = new boolean[vert];
      visited[v] = true;
      inNet.add(v);

      while(!stack.isEmpty()){
         int curr = stack.pop();
         List<Integer> adjToCurr = adjacent[curr];
         for (int next: adjToCurr){
            if(!visited[next]){
               inNet.add(next);
               stack.push(next);
               visited[next] = true;
            }
         }

      }

        return inNet;
    }
    
    
}


class wheresmyinternet{
    public static void main(String[] args) {
		  long time = System.currentTimeMillis();
        Scanner in = new Scanner(System.in);
        int houses = in.nextInt();
        int cables = in.nextInt();
        DFS_Graph graph = new DFS_Graph(houses+1);
        for (int i = 0; i < cables; i++){
            int n = in.nextInt();
            int m = in.nextInt();
            graph.addEdge(n,m);
        }

        
        ArrayList<Integer> inNet = graph.search(1);

        ArrayList<Integer> notCon = new ArrayList<Integer>();
        if (houses > 1){
            for (int i = 1; i < houses+1; i++){
                if (!inNet.contains(i)){
                    notCon.add(i);
                }
            }
        }

        if(notCon.size() != 0){
            for (int h : notCon){
                System.out.println(h);
            }
        }
        else{
            System.out.println("Connected");
		  }
		  
		  //System.out.println("Operation took " + (System.currentTimeMillis() - time) + " ms");
		  in.close();

    }

}