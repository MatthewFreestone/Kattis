import java.util.*;
public class streetsbehind_xiaowuc1 {
  public static void main(String[] args) throws Exception {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
    while(t-- > 0) {
      int n = sc.nextInt();
      int k = sc.nextInt();
      int a = sc.nextInt();
      int b = sc.nextInt();
      System.out.println(solve(n, k, a, b));
    }
  }
  private static long solve(long n, long k, long a, long b) {
    long ret = 0;
    while(k > 0) {
      long want = (n*b - n*a) / a;
      if(want == 0) return -1;
      if(want >= k) {
        ret++;
        break;
      }
      long lhs = 1;
      long rhs = (k+want-1)/want;
      while(lhs < rhs) {
        long mid = (lhs+rhs+1)/2;
        long hypon = n + (mid-1) * want;
        long hypok = k - (mid-1) * want;
        if((hypon*b-hypon*a)/a == want) lhs = mid;
        else rhs = mid-1;
      }
      ret += lhs;
      n += lhs * want;
      k -= lhs * want;
    }
    return ret;
  }
}