import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        int n = Integer.parseInt(br.readLine().trim());
        int m, res = 0;
        for (int i = 0; i < n; i++) {
            m = Integer.parseInt(br.readLine().trim());
            if (m == 0) {
                res = 0;
                // 가장 큰 값을 출력하고 제거
                if (maxHeap.peek() != null)
                    res = maxHeap.poll();
                bw.append(String.valueOf(res));
                bw.newLine();
            } else {
                maxHeap.add(m);
            }
        }
        bw.flush();
        bw.close();
    }
}
