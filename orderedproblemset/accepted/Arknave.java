import java.io.*;
import java.util.*;

public class Arknave {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scan.nextInt();
        }

        List<Integer> ans = new ArrayList<>();
        for (int k = 2; k <= n; k++) {
            if (n % k != 0) {
                continue;
            }

            int sectionSize = n / k;
            boolean valid = true;
            int lastMax = 0;
            int curMax = 0;
            int curMin = a[0];
            for (int i = 0; i < n; i++) {
                if (i % sectionSize == 0) {
                    lastMax = curMax;
                    curMax = 0;
                    curMin = a[i];
                }

                curMax = Math.max(curMax, a[i]);
                curMin = Math.min(curMin, a[i]);

                valid &= lastMax < curMin;
            }

            if (valid) {
                ans.add(k);
            }
        }

        if (ans.isEmpty()) {
            System.out.println(-1);
        } else {
            for (int i = 0; i < ans.size(); i++) {
                System.out.println(ans.get(i));
            }
        }
    }
}
