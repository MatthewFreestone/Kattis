import java.io.*;
import java.util.*;

public class caseGenerator {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        FileWriter f = new FileWriter(new File("in.in"));
        Random random = new Random();

  
        int r = 1000;//in.nextInt();
        int c = 1000;//in.nextInt();
        int pts = 1000;
        f.append(r + " " + c + "\n");
  
        for (int i = 0; i < r; i++){
            String line = "";
            //int lineChar = random.nextInt(2);
            for (int j = 0; j < c; j++) {
                line += random.nextInt(2); //lineChar; 
            }
            f.append(line + "\n");
        }

        f.append(pts + "\n");
        for (int i = 0; i <pts; i++){
            String pt1 = (random.nextInt(r-1)+1) + " " + (random.nextInt(c-1)+1);
            String pt2 = (random.nextInt(r-1)+1) + " " + (random.nextInt(c-1)+1);
            f.append(pt1 + " " + pt2 + "\n");
        }
        in.close();
        f.close();
    }
}
