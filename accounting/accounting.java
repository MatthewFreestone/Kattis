import java.util.Scanner;
import java.util.HashMap;
public class accounting{
    public static void main(String[] args){
        Scanner in  = new Scanner(System.in);
        HashMap<Integer,Integer> map= new HashMap<Integer,Integer>();

        int n = in.nextInt();
        int q = in.nextInt();
        
        int def = 0;

        for (int i = 0; i < q; i++){
            String cmd = in.next();

            if (cmd.equals("SET")){
                int I = in.nextInt();
                int X = in.nextInt();

                map.put(I, X);
            }
            else if (cmd.equals("RESTART"))
            {
                map.clear();

                def = in.nextInt();

            }
            else if (cmd.equals("PRINT")){
                int I = in.nextInt();

                if(map.containsKey(I)){
                    System.out.println(map.get(I));
                }
                else{
                    System.out.println(def);
                }
            }
        }

    }
}