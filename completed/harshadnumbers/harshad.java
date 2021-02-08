import java.util.*;
class harshad{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int i = n;
		while (true) {
			if (isHarshad(i)){
				break; 
			}
			i++;
		}
		System.out.println(i);

	}

	private static boolean isHarshad(Integer n){
		String s_num = n.toString();
		int digit_sum = 0;
		for (Character c : s_num.toCharArray()){
			digit_sum += Integer.parseInt(c.toString());
		}
		return (n%digit_sum == 0);
	}
}