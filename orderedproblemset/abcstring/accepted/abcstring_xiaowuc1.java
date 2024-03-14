import java.util.*;
public class abcstring_xiaowuc1 {
  public static void main(String[] args) throws Exception {
    Scanner sc = new Scanner(System.in);
    String s = sc.next();
    int ret = 0;
    int[] have = new int[8];
    for(int i = 0; i < s.length(); i++) {
      int val = s.charAt(i) - 'A';
      boolean found = false;
      for(int mask = 7; !found && mask >= 0; mask--) {
        if((mask&(1<<val)) != 0) continue;
        if(have[mask] > 0) {
          have[mask]--;
          int nxt = mask | (1 << val);
          if(nxt == 7) nxt = 0;
          have[nxt]++;
          found = true;
        }
      }
      if(!found) {
        ret++;
        have[1<<val]++;
      }
    }
    System.out.println(ret);
  }
}