import java.io.*;
import java.util.*;

public class caseGenerator {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        FileWriter f = new FileWriter(new File("in.in"));
        Random random = new Random();

  
        int r = 1000;//in.nextInt();
        int c = 1000;//in.nextInt();
        int pts = 50;
        f.append(r + " " + c + "\n");
  
        for (int i = 0; i < r; i++){
            String line = "";
            for (int j = 0; j < c; j++) {
                line += "1"; //random.nextInt(1);
            }
            f.append(line + "\n");
        }

        f.append(pts + "\n");
        for (int i = 0; i <pts; i++){
            String line = random.nextInt(r) + " " + random.nextInt(c);
            f.append(line + "\n");
        }
        in.close();
        f.close();
    }
}
