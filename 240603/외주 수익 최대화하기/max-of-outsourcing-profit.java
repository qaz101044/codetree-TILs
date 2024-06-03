import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[] t;
    static int[] p;
    static int[] dp;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        t = new int[n];
        p = new int[n];
        dp = new int[n+1];

        for (int i=0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            t[i] = Integer.parseInt(st.nextToken());
            p[i] = Integer.parseInt(st.nextToken());
        }

        //System.out.println(Arrays.toString(t));
        //System.out.println(Arrays.toString(p));

        for (int i=0; i < n; i++) {
            if( i + t[i] <= n) {
                dp[i+t[i]] = Math.max(dp[i+t[i]], dp[i] + p[i]);
            }

            dp[i+1] = Math.max(dp[i],dp[i+1]);
        }

        System.out.println(dp[n]);
    }
}