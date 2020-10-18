import java.util.*;
import java.util.ArrayList;

public class crosscountry{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int nodesCount = in.nextInt(); //N in problem
        int start = in.nextInt();
        int end = in.nextInt(); 

        ArrayList<HashMap<Integer, Integer>> neighbors = new ArrayList<HashMap<Integer, Integer>>();
        ArrayList<Integer> distances = new ArrayList<Integer>();

        for (int i = 0; i < nodesCount; i++){
           distances.add(-1); //fill up distances with disallowed values
        }
        PriorityQueue<Node> toEval = new PriorityQueue<>();

        for (int i = 0; i < nodesCount; i++){
            HashMap<Integer, Integer> item = new HashMap<Integer, Integer>();
            for (int j = 0; j < nodesCount; j++){
                item.put(j, in.nextInt());
            }
            neighbors.add(item);
        }

        //System.out.println(neighbors);
        toEval.add(new Node(start, 0));
        while(!toEval.isEmpty()){
           Node cur = toEval.poll();
           if (distances.get(cur.index) != -1){
              continue;
           }
           distances.set(cur.index, cur.cost);
           HashMap<Integer, Integer> distToNeighbors = neighbors.get(cur.index);
           for (int i : distToNeighbors.keySet()){
              if (distances.get(i) == -1){
                 toEval.add(new Node(i, cur.cost + distToNeighbors.get(i)));
              }
           }
        }

        System.out.println(distances.get(end));

    }
}





class Node implements Comparable<Node>{
    public int index;
    public int cost; 

    public Node(){}

    public Node(int index, int cost){
        this.index = index;
        this.cost = cost;
    }
    
    @Override 
    public int compareTo(Node n){
        return this.cost - n.cost;
    }

    @Override
    public String toString(){
        return "To " + index + " is " + cost;
    }
    


}