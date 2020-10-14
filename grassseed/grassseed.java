import java.util.Scanner; 
import java.text.DecimalFormat;
public class grassseed{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        DecimalFormat format = new DecimalFormat("#.0000000");

        double costPMeter = in.nextDouble();
        int lawns = in.nextInt();
        double cost=0;
        for (int i = 0; i < lawns; i++){
            cost += costPMeter * (in.nextDouble() * in.nextDouble());
        }
        System.out.println(format.format(cost));
        
    }
}
