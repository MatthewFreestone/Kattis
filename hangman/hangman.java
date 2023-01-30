import java.util.*;
import java.util.Scanner;

public class hangman{
   public static void main(String[] args) {
      Scanner in = new Scanner(System.in);
      String word = in.next();
      ArrayList wordList = new ArrayList<Character>();
      for (char c : word.toCharArray() ){
         if(!wordList.contains(c)){
            wordList.add(c);
         }
      }

      char[] alphabet = in.next().toCharArray();
      int misses = 0;
      for (char c : alphabet){
         int index = wordList.indexOf(c);
         if (index!=-1){
            wordList.remove(index);
         }
         else{
            misses++;
         }

         if(wordList.size() == 0){
            break;
         }
         
      }
      System.out.println((misses<10) ? "WIN" : "LOSE");
   }
}