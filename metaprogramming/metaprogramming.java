import java.util.*;

public class metaprogramming{
   public static void main(String[] args) {
      HashMap<String, Integer> values  = new HashMap<String, Integer>();
      Scanner in = new Scanner(System.in);

      String line;
      while(in.hasNextLine()){
         line = in.nextLine();
         String[] split = line.split(" ");
         if(split[0].equals("define")){
            values.put(split[2],Integer.parseInt(split[1]));
            
         }
         else if(split[0].equals("eval")){
            if (!values.containsKey(split[1]) || !values.containsKey(split[3])){
               System.out.println("undefined");
            }
            else{
               if (split[2].equals("=")){
                  System.out.println(values.get(split[1])  == values.get(split[3]));
               }
               else if(split[2].equals("<")){
                  System.out.println(values.get(split[1]) < values.get(split[3]));
               }
               else if(split[2].equals(">")){
                  System.out.println(values.get(split[1]) > values.get(split[3]));
               }
               else{
                  System.out.println("error");
               }
            }
         }
      }  
   }
}