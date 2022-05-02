import java.io.*;

public class TICT_3_4_UntilOne {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input = null;
        int n, k;
        int cnt = 0;

        input = br.readLine();

        n = Integer.parseInt(input.split(" ")[0]);
        k = Integer.parseInt(input.split(" ")[1]);

        while(n > 1) {
            if(n % k == 0) {
                n /= k;
            }
            else {
                n -= 1;
            }
            cnt++;
        }

        bw.write(String.valueOf(cnt));
        bw.flush();
    }
}
