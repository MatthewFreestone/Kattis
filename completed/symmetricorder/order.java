import java.util.*;

class order{
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      int n = in.nextInt();
      int setNum = 1;
      
      while (n != 0){
         LinkedList<String>  firstHalf = new LinkedList();
         LinkedList<String> secondHalf = new LinkedList();
         boolean first = true;
         for(int i = 0; i < n; i++){
            if (first){
               firstHalf.addLast(in.next());
               first = false;
            }
            else{
               secondHalf.addFirst(in.next());
               first = true;
            }

         }
         String out = "SET " + setNum + "\n";
         for (String name : firstHalf){
            out += name + "\n";
         }
         for (String name : secondHalf){
            out += name + "\n";
         }

         System.out.print(out);
         setNum++;
         n = in.nextInt();
      }
      
   }
}