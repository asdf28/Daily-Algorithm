import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class TICT_3_2_RuleOfBigNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String input;
        int n,m,k;
        int cnt = 0;
        int cnt_k = 0;
        ArrayList<Integer> list = new ArrayList<>();

        input = br.readLine();

        n = Integer.parseInt(input.split(" ")[0]);
        m = Integer.parseInt(input.split(" ")[1]);
        k = Integer.parseInt(input.split(" ")[2]);

        input = br.readLine();

        for(String tmp : input.split(" ")) {
            list.add(Integer.parseInt(tmp));
        }

        Collections.sort(list);

        for(int i = 0; i < m; i++) {
            if(cnt_k == k) {
                cnt_k = 0;
                cnt += list.get(n-2);
                continue;
            }
            cnt += list.get(n-1);
            cnt_k++;
        }

        bw.write(String.valueOf(cnt));

        bw.flush();
    }
}
