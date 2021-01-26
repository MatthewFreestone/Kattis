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

      int start = findStart(contests);
      System.out.println("found start to be at " + start);

      for(int i = start; current != k+1; i++){
         count++;
         if(i == contests.length){
            i = 0;
         }
         if (contests[i] == current){
            current++;
         }

      }

      System.out.println(count);
   }

   private static int findStart(int[] comps){

      int[] lookThru = new int[comps.length*2];
      for (int i = 0; i < lookThru.length; i++){
         lookThru[i] = comps[i%comps.length];
      }

      int[] virtue = new int[comps.length];

      ArrayList<Integer> toLook = new ArrayList<Integer>();
      for(int i = 0; i < comps.length; i++){
         if (comps[i] == 1){
            toLook.add(i);
         }
      }
      
      for (int curr: toLook){
         int next = 2;
         for (int i = curr+1; i < lookThru.length && lookThru[i]!=1; i++){
            if (lookThru[i] == next){
               next++;
               virtue[curr]++;
            }
         }
      }

      int max = 0, index = 0, maxIndex = 0;
      while(index < virtue.length){
         if(virtue[index] > max){
            max = virtue[index];
            maxIndex = index;
         }
         index++;
      }
      return maxIndex;
   }
} 

// Approaches:
// Repeat the test for each starting one and find shortest (terminate after it slower than last)
// Remove non-consecurive numbers and find longest starting chain (stack two next to each other )

//Problems:
//what if we have more comps than we need?
//what if they can get to the same amount but one is faster?
//what if there is two correct answers?
