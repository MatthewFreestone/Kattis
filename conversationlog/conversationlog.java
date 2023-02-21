import java.util.*;
public class conversationlog{
   public static void main(String[] args){
      Scanner in = new Scanner(System.in);
      int msgNum = in.nextInt();
      HashMap<String, Integer> usage = new HashMap<String, Integer>();
      HashMap<String, ArrayList<String>> people = new HashMap<String, ArrayList<String>>();
      for (int i = 0; i <= msgNum; i++){
         String[] words = in.nextLine().split(" ");
         String person = words[0];
         words = Arrays.copyOfRange(words, 1, words.length);
         for (String word : words){

            if (usage.containsKey(word)){
               int newFreq = usage.get(word) + 1;
               usage.put(word, newFreq);
            }
            else{
               usage.put(word, 1);
            }
         }

      }



      HashMap<String, Integer> usageCropped = (HashMap<String,Integer>) usage.clone();
      for (Map.Entry<String, Integer> entry : usage.entrySet()){
         if (entry.getValue() == 1){
            usageCropped.remove(entry.getKey());
         }
      }
      usage = (HashMap<String,Integer>) usageCropped.clone();


      
      
      ArrayList<String> ordered = new ArrayList<String>();
      if (!usage.isEmpty()){
         //for (int i = 0; i< usage.size(); i++)
         while(!usage.isEmpty()){
            int freq = Collections.max(usage.values());
            ArrayList<String> solns = new ArrayList<String>();
            
            usageCropped = (HashMap<String,Integer>) usage.clone(); 
            for (HashMap.Entry<String, Integer> entry : usage.entrySet()){
               if (entry.getValue() == freq){

                  solns.add(entry.getKey());
                  usageCropped.remove(entry.getKey());
               }
            }
            usage = (HashMap<String,Integer>)usageCropped.clone();


            Collections.sort(solns);
            for (String s : solns){
               ordered.add(s);
            }
         }
         for (String s : ordered){
            System.out.println(s);
         }
      }
      else{
         System.out.println("ALL CLEAR");
      }
      

   }
}