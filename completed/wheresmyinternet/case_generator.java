import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class case_generator {
   public static void main(String[] args) throws IOException {
      Scanner in = new Scanner(System.in);
      FileWriter f = new FileWriter(new File("in.in"));
      Random random = new Random();

      // int MAX = in.nextInt();
      // int houses = random.nextInt(MAX-1) + 1; //between 1 and MAX
      // int cables = random.nextInt(MAX-1) + 1; //between 1 and MAX

      int houses = in.nextInt();
      int cables = in.nextInt();
      f.append(houses + " " + cables + "\n");

      for (int i = 0; i < cables; i++){
         int first =  random.nextInt(houses-1) + 1; //between 1 and houses
         int second = random.nextInt(houses-1) + 1; //between 1 and houses
         f.append(first + " " + second + "\n");
      }
      //in.close();
      f.close();
   }
}
