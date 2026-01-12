import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine().trim());
        int[] budgets = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        int max = 0;
        for (int i = 0; i < n; i++) {
            int val = Integer.parseInt(st.nextToken());
            budgets[i] = val;
            max = Math.max(max, val);
        }
        int maxBudget = Integer.parseInt(br.readLine().trim());

        // 이진탐색
        // left = 0, right = 최댓값
        int left = 0;
        int right = max;
        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            int sum = 0;
            for (int b : budgets) {
                sum += Math.min(b, mid);
            }
            if (sum <= maxBudget) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        bw.append(String.valueOf(answer));
        bw.flush();
        bw.close();
    }
}
