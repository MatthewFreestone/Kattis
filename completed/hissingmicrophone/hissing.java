import java.util.*;
class hissing{
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String word	= in.next();
		System.out.println((word.contains("ss")) ? "hiss" : "no hiss");	
	}
}