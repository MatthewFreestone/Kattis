import java.util.*;

public class passwordhacking
{
   public static void main (String[] args ){
      Scanner in = new Scanner(System.in);
      int len = Integer.parseInt(in.nextLine());
      ArrayList<Double> poss = new ArrayList<Double>();
      for (int i =0; i < len; i++){
         in.next(); //dumps the name
         poss.add(Double.parseDouble(in.nextLine()));
      }
      double total = 0;
      for (int i = 0; i < len; i++){
         double max = Collections.max(poss);
         total += (1+i) * max;
         poss.remove(max);
      }
      System.out.println(total);

   }
   
}