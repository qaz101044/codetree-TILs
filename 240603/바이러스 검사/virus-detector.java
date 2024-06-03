import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[] customers;
    static int num_L, num_M; // 팀장 검사 가능 수 , 팀원 검사 가능 수 

    public static void main(String[] args) throws Exception {
        // 여기에 코드를 작성해주세요.
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        customers = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i=0; i < n; i++) {
            customers[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        num_L = Integer.parseInt(st.nextToken());
        num_M = Integer.parseInt(st.nextToken());

        long min_cnt = 0; // 검사자 수의 최솟값

        for (int i=0; i < n; i++) {
            min_cnt += 1;

            min_cnt += chk_required_members(customers[i] - num_L);
        }
        
        System.out.println(min_cnt);
        
    }

    static int chk_required_members(int customers_remain) {
        if (customers_remain <= 0) {
            return 0;
        }

        if (customers_remain % num_M == 0) {
            return customers_remain / num_M;
        } else {
            return customers_remain / num_M + 1;
        }
    } 
}