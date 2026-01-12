import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));        
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine().trim());
        Stack<Integer> stack = new Stack<>();

        for (int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String method = st.nextToken();
            switch (method) {
                case "push":
                    int M = Integer.parseInt(st.nextToken());
                    stack.push(M);
                    break;

                case "pop":
                    int result = -1;
                    if(!stack.empty()) result=stack.pop(); 
                    bw.write(Integer.toString(result));
                    bw.newLine();
                    break;

                case "size":
                    bw.write(Integer.toString(stack.size()));
                    bw.newLine();
                    break;

                case "empty":
                    int res = stack.empty() ? 1 : 0;
                    bw.write(String.valueOf(res));
                    bw.newLine();
                    break;

                case "top":
                    int res2 = -1;
                    if(!stack.empty()) res2 = stack.peek(); 
                    bw.write(String.valueOf(res2));
                    bw.newLine();
                    break;
            }
        }
        bw.flush();
        bw.close();
    }
}