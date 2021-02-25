import java.io.*;
import java.util.*;

class DFS_Graph_Newest{

	int vert;
	LinkedList<Integer>[] adjacent; 



	public DFS_Graph_Newest(int vert){
      this.vert = vert;
		adjacent = new LinkedList[vert];
		for (int i = 0; i < vert; i++){
			adjacent[i] = new LinkedList();
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


class newest{
	public static void main(String[] args) throws Exception{
      long time = System.currentTimeMillis();
		Scanner in = new Scanner(System.in);
		int houses = in.nextInt();
		int cables = in.nextInt();
		DFS_Graph_Newest graph = new DFS_Graph_Newest(houses+1);
		for (int i = 0; i < cables; i++){
			int n = in.nextInt();
			int m = in.nextInt();
			graph.addEdge(n,m);
		}

      boolean[] inNet = graph.search(1);

		int notCon = 0;
		if (houses > 1){
         for (int i = 1; i < houses+1; i++){
            if(!inNet[i]){
               notCon++;
            }
         }
      }

      //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
      int x= 0;
      if(notCon != 0){
			for (int i = 1; i < houses+1; i++){
            if(!inNet[i]){
               //bw.append(i + "\n");
               x+=i;
            }
         }
         //bw.flush();
		}
		else{
			System.out.println("Connected");
      }
      
      System.out.println("Operation took " + (System.currentTimeMillis() - time) + " ms");
      in.close();

	}

}
