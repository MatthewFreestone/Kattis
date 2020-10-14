import java.util.Scanner;
import java.util.ArrayList;

public class crosscountry{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int start = in.nextInt();
        int end = in.nextInt(); 

        intersection[] table = new intersection[N];
        for(int i = 0; i < N; i++){
            table[i] = new intersection(N); //gets a row
            for (int j = 0; j < N; j++){
                table[i].routeList[j] = in.nextInt();
            }
        }
        ArrayList<Integer> sptList = new ArrayList<Integer>();
        table[start].weightFromStart = 0;
        for (int i = 0; i < N; i++){
            table[i].weightFromStart = table[start].routeList[i];
        }



        

    }
}

class intersection{
    int weightFromStart = Integer.MAX_VALUE;
    int index = 0; //what intersection this is
    int[] routeList = null;
    public intersection(int N){
        routeList = new int[N];
    }
    


}