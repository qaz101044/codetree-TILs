import java.io.*;
import java.util.*;

public class Main {

    static int n;
    static int[][] board;
    static boolean[] visited;
    static int min_value = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        board = new int[n][n];
        visited = new boolean[n];

        for (int i=0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            for (int j=0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0,0);

        System.out.println(min_value);
        
    }

    static void dfs(int idx, int depth) {

        if (depth == n / 2) {
            
            int morning = 0, night = 0;

            for (int i=0; i < n-1; i++) {
                for (int j=i+1; j < n; j++) {
                    if (visited[i] && visited[j]) {
                        morning += board[i][j];
                        morning += board[j][i];
                    }

                    else if (!visited[i] && !visited[j]) {
                        night += board[i][j];
                        night += board[j][i];
                    }
                }
            } 

            int val = Math.abs(morning - night);

            if (val == 0) {
                System.out.println(val);
                System.exit(0);
            }

            min_value = Math.min(val,min_value);
            return;
        }

        for (int i=idx; i < n; i++) {
            if(!visited[i]) {
                visited[i] = true;
                dfs(i + 1, depth + 1);
                visited[i] = false;}

            }
        }

    }