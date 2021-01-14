import java.util.Scanner;

public class freefood{
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      int n  = in.nextInt();
      int total = 0;
      int max = 0;
      boolean[] year = new boolean[365];
      for (int i = 0; i < n; i++){
         int a = in.nextInt() -1; 
         int b = in.nextInt() -1;
         for (int j = a; j <= b; j++){
            year[j] = true;
         }

      }
      for (boolean b : year){
         if (b){
            total++;
         }
      }
      System.out.println(total);
   }
}