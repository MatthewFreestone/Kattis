import java.util.Scanner;

public class easiest{
   public static void main(String[] args) {
      Scanner s = new Scanner(System.in);
      int n;
      while(true) {
         n = s.nextInt();
         if(n==0){
            break;
         }
         int target = digitSum(n);

         int solution = 0;
         for (int i = 11; i < 200000; i++){
            int attempt = i*n;
            int len = digitSum(attempt);
            if (len == target){
               solution = i;
               break;
            }
         }
         System.out.println(solution);

      }
 
   }

   private static int digitSum(int i){
      char[] len = Integer.toString(i).toCharArray();

      int total = 0;
      for (char c : len){
         total += Integer.parseInt(String.valueOf(c));
      }
      return total;
     

   }
}