
import java.util.*;
public class moneymatters
{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        

        HashMap<Integer, ArrayList<Integer>> friends = new HashMap<>();


        int n = in.nextInt();
        int m = in.nextInt();
        int[] debts = new int[n];

        for (int i = 0; i<n; i++){
            debts[i] = in.nextInt();
        }

        for (int i = 0; i<m; i++){
            int x = in.nextInt(), y=in.nextInt();

            if (!friends.containsKey(x)){
                friends.put(x, new ArrayList<Integer>());
            }
            if (!friends.containsKey(y)){
                friends.put(y, new ArrayList<Integer>());
            }

            friends.get(x).add(y);
            friends.get(y).add(x);

        }

        boolean[] visited = new boolean[n];
        for (int i=0; i<n;i++){
            if (!visited[i]){
                Stack<Integer> stack = new Stack<Integer>();
                stack.push(i);
                visited[i] = true;

                int totalDebt = 0;
                while(!stack.isEmpty()){
                    int curr = stack.pop();

                    totalDebt += debts[curr];

                    for (int x : friends.get(curr)){
                        if (!visited[x]){
                            visited[x] = true;
                            stack.push(x);
                        }
                    }
                }
                if (totalDebt != 0){
                    System.out.println("IMPOSSIBLE");
                    return;
                }
            }

        }
        System.out.println("POSSIBLE");
        
    }
}