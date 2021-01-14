import java.util.*;

class kod{
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      int n = in.nextInt();
      int k = in.nextInt();  
      int[] contests = new int[n];
      int count = 0;
      int current = 1;
      for (int i = 0; i < n; i++){
         contests[i] = in.nextInt();
      }

      int start;
      for(start = 0; start != 1; start++)

      for(int i = start; current != k; i++){
         count++;
         if(i == contests.length){
            i = 0;
         }
         if (current == contests[i]){
            current++;
         }

      }
      //count++;

      System.out.println(count);
   }
} 

// Approaches:
// Repeat the test for each starting one and find shortest (terminate after it slower than last)
// Remove non-consecurive numbers and find longest starting chain (stack two next to each other )